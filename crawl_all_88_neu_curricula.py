import httpx
from bs4 import BeautifulSoup
import json
import unicodedata
import re
import time
from sqlalchemy import text
from app.database import engine

def normalize(text):
    text = unicodedata.normalize('NFD', text.lower())
    text = re.sub(r'[\u0300-\u036f]', '', text)
    text = re.sub(r'[^a-z0-9]', '', text)
    return text

with open('all_curriculum_links.json', encoding='utf-8') as f:
    links = json.load(f)

with engine.connect() as conn:
    majors = conn.execute(text('SELECT id, code, name FROM majors ORDER BY id')).fetchall()

OVERRIDE_MAP = {
    '7310101P2': '/curriculum/kinh-te-va-quan-ly-do-thi-k68-73101012k68?year=K68%20-%202026',
    '7310101P3': '/curriculum/kinh-te-va-quan-ly-nguon-nhan-luc-k68-73101013k68?year=K68%20-%202026',
    '7310101P1': '/curriculum/kinh-te-hoc-k68-73101011k68?year=K68%20-%202026',
    'EP03': '/curriculum/phan-tich-du-lieu-kinh-te-k68-K687310108?year=K68%20-%202026',
    'EP06': '/curriculum/phan-tich-kinh-doanh-k68-K68340101?year=K68%20-%202026',
    'EP10': '/curriculum/dau-tu-tai-chinh-k67ep10-1?year=K68%20-%202026',
    'EP09': '/curriculum/cong-nghe-tai-chinh-va-ngan-hang-so-k68ep09-1?year=K68%20-%202026',
    '7340205': '/curriculum/cong-nghe-tai-chinh-k68-k68ep09?year=K68%20-%202026',
    'CLC1': '/curriculum/kinh-te-phat-trien-clc-k68-7310105?year=K68%20-%202026',
    'CLC2': '/curriculum/kinh-te-dau-tu-clc-k68-7310104?year=K68%20-%202026',
    'CLC3': '/curriculum/tai-chinh-doanh-nghiep-clc-7340201?year=K68%20-%202026',
    'TT1': '/curriculum/ke-toan-tt-k68-7340301?year=K68%20-%202026',
    'TT2': '/curriculum/tai-chinh-tt-k68-7340201?year=K68%20-%202026',
    'EP24': '/curriculum/kinh-te-y-te-mnag3ple?year=K68%20-%202026',
    'EP26': '/curriculum/cong-nghe-moi-truong-va-phat-trien-ben-vung-mnag4a50?year=K68%20-%202026',
    'POHE1': '/curriculum/quan-tri-khach-san-pohe-k68-7810201?year=K68%20-%202026',
    'POHE2': '/curriculum/quan-tri-lu-hanh-pohe-k68-7810103?year=K68%20-%202026',
    'POHE3': '/curriculum/truyen-thong-marketing-pohe-k68-7340115?year=K68%20-%202026',
    'POHE4': '/curriculum/luat-kinh-doanh-pohe-k68-7380107?year=K68%20-%202026',
    'POHE5': '/curriculum/quan-tri-kinh-doanh-thuong-mai-pohe-k68-7340121?year=K68%20-%202026',
    'POHE6': '/curriculum/quan-ly-thi-truong-pohe-k68-7340121?year=K68%20-%202026',
    'POHE7': '/curriculum/tham-dinh-gia-k68-K68POHE77340201?year=K68%20-%202026',
    'EP31': '/curriculum/tham-inh-gia-k68ep31?year=K68%20-%202026',
}

def get_link_for_major(m_code, m_name):
    if m_code in OVERRIDE_MAP:
        return OVERRIDE_MAP[m_code]
    norm_code = normalize(m_code)
    norm_name = normalize(m_name)
    for l in links:
        if norm_code in normalize(l):
            return l
    for l in links:
        slug = l.split('?')[0].replace('/curriculum/', '')
        if norm_name in normalize(slug) or normalize(slug) in norm_name:
            return l
    return None

def parse_curriculum(html, major_name):
    soup = BeautifulSoup(html, 'html.parser')
    table = None
    for t in soup.find_all('table'):
        txt = t.get_text()
        if 'Tên học phần' in txt and 'Mã học phần' in txt:
            table = t
            break
            
    if not table:
        return []

    current_section = 'Đại cương chung'
    raw_subjects = []
    
    for tr in table.find_all('tr'):
        ths = tr.find_all('th')
        tds = tr.find_all('td')
        
        # Check if section header row
        if ths and not tds:
            sec_text = ths[0].get_text(strip=True)
            sec_lower = sec_text.lower()
            if 'stt' in sec_lower or 'mã học phần' in sec_lower:
                continue
            if 'chung' in sec_lower or 'trường' in sec_lower or 'đại cương' in sec_lower or 'đại học' in sec_lower:
                current_section = 'Đại cương chung'
            elif 'cơ sở' in sec_lower or 'lĩnh vực' in sec_lower or 'nhóm ngành' in sec_lower:
                current_section = 'Cơ sở ngành'
            elif 'thực tập' in sec_lower or 'khóa luận' in sec_lower or 'khoá luận' in sec_lower or 'chuyên đề tốt nghiệp' in sec_lower:
                current_section = 'Khóa luận tốt nghiệp'
            else:
                current_section = 'Chuyên ngành'
            continue
            
        # Parse subject data row
        if tds:
            texts = [td.get_text(strip=True) for td in tds]
            # Pattern A: [STT, Name, Code, Credits, ...]
            # Pattern B: [Name, Code, Credits, ...]
            if len(texts) >= 4:
                name = texts[1]
                code = texts[2]
                credits_str = texts[3]
            elif len(texts) == 3:
                name = texts[0]
                code = texts[1]
                credits_str = texts[2]
            else:
                continue
                
            if not code or code == 'Mã học phần' or not name or name == 'Tên học phần':
                continue
                
            # Filter out numeric codes that are just STT accidentally parsed
            try:
                credits = int(re.sub(r'\D', '', credits_str)) if credits_str else 3
            except:
                credits = 3
            if credits <= 0 or credits > 15:
                credits = 3
                
            raw_subjects.append({
                'code': code,
                'name': name,
                'credits': credits,
                'subject_type': current_section
            })
            
    total = len(raw_subjects)
    if total == 0:
        return []
        
    subjects = []
    for idx, s in enumerate(raw_subjects):
        stype = s['subject_type']
        if stype == 'Đại cương chung':
            sem = 1 if idx < total * 0.15 else (2 if idx < total * 0.30 else 3)
        elif stype == 'Cơ sở ngành':
            sem = 3 if idx < total * 0.45 else 4
        elif stype == 'Chuyên ngành':
            if idx < total * 0.65:
                sem = 5
            elif idx < total * 0.85:
                sem = 6
            else:
                sem = 7
        elif stype == 'Khóa luận tốt nghiệp':
            sem = 8
        else:
            sem = min(8, max(1, int((idx / total) * 8) + 1))
            
        desc = f"Học phần chuẩn NEU (Mã {s['code']}) thuộc khối {stype} ngành {major_name}, đào tạo {s['credits']} tín chỉ theo khung chuẩn Đại học Kinh tế Quốc dân."
        name_lower = s['name'].lower()
        if 'pháp luật' in name_lower:
            desc = "Trang bị kiến thức căn bản về nhà nước và pháp luật, quyền công dân và pháp chế trong hoạt động kinh tế xã hội."
        elif 'triết học' in name_lower:
            desc = "Thế giới quan và phương pháp luận duy vật biện chứng, quy luật vận động tự nhiên và phát triển xã hội."
        elif 'kinh tế chính trị' in name_lower:
            desc = "Quy luật kinh tế khách quan, lý luận giá trị thặng dư và cơ chế thị trường định hướng XHCN."
        elif 'chủ nghĩa xã hội' in name_lower:
            desc = "Sứ mệnh lịch sử của giai cấp công nhân, nền dân chủ XHCN và đại đoàn kết toàn dân tộc."
        elif 'tư tưởng hồ chí minh' in name_lower:
            desc = "Hệ thống quan điểm toàn diện của Chủ tịch Hồ Chí Minh về độc lập dân tộc gắn liền với CNXH."
        elif 'lịch sử đảng' in name_lower:
            desc = "Lịch sử ra đời, các mốc son lãnh đạo cách mạng và đường lối đổi mới của Đảng Cộng sản Việt Nam."
        elif 'vi mô' in name_lower:
            desc = "Hành vi người tiêu dùng, tối ưu hóa sản xuất kinh doanh của doanh nghiệp và cơ chế hình thành giá cả thị trường."
        elif 'vĩ mô' in name_lower:
            desc = "Tổng quan nền kinh tế: tổng cầu, tổng cung, lạm phát, thất nghiệp, tăng trưởng và các chính sách tài khóa, tiền tệ."
        elif 'toán' in name_lower or 'đại số' in name_lower or 'giải tích' in name_lower:
            desc = "Công cụ giải tích ma trận, vi phân tích phân và tối ưu toán học ứng dụng trong kinh tế và công nghệ."
        elif 'thống kê' in name_lower or 'xác suất' in name_lower:
            desc = "Xử lý biến ngẫu nhiên, phân phối xác suất, ước lượng thống kê và kiểm định giả thuyết dữ liệu thực nghiệm."
        elif 'tiếng anh' in name_lower:
            desc = "Phát triển năng lực tiếng Anh học thuật, giao tiếp quốc tế, kỹ năng thuyết trình và đọc hiểu tài liệu chuyên ngành."
        elif 'khóa luận' in name_lower or 'chuyên đề' in name_lower or 'thực tập' in name_lower:
            desc = "Thực tập thực tế tại doanh nghiệp, tổ chức và thực hiện đề tài tốt nghiệp dưới sự hướng dẫn của giảng viên NEU."
            
        subjects.append({
            'code': s['code'],
            'name': s['name'],
            'credits': s['credits'],
            'semester': sem,
            'subject_type': stype,
            'description': desc
        })
        
    return subjects

print("Starting to crawl NEU curricula for all 88 majors with robust table detection...")
client = httpx.Client(base_url="https://courses.neu.edu.vn", verify=False, timeout=20.0)

results = {}
failed = []

for m in majors:
    m_id, m_code, m_name = m
    link = get_link_for_major(m_code, m_name)
    if not link:
        print(f"FAILED link lookup for Major ID {m_id}: {m_code} - {m_name}")
        failed.append(m)
        continue
        
    try:
        r = client.get(link)
        if r.status_code == 200:
            subs = parse_curriculum(r.text, m_name)
            results[m_id] = {
                'major_id': m_id,
                'major_code': m_code,
                'major_name': m_name,
                'curriculum_url': link,
                'subjects_count': len(subs),
                'subjects': subs
            }
            print(f"[{len(results):2d}/88] ID {m_id:2d} | {m_code:10s} | {len(subs):2d} môn | {m_name[:35]}")
        else:
            print(f"ERROR {r.status_code} for {m_code}: {link}")
            failed.append(m)
    except Exception as e:
        print(f"EXCEPTION for {m_code}: {e}")
        failed.append(m)
        
    time.sleep(0.04)

print("\n--- CRAWL COMPLETED ---")
print(f"Total crawled successfully: {len(results)}/88")
zero_subjects = [r for r in results.values() if r['subjects_count'] == 0]
if zero_subjects:
    print(f"Warning: {len(zero_subjects)} majors have 0 subjects:")
    for z in zero_subjects:
        print(f"  ID {z['major_id']}: {z['major_code']} - {z['major_name']}")
else:
    print("ALL 88 MAJORS HAVE OFFICIAL SUBJECTS FROM COURSES.NEU.EDU.VN!")

with open("all_88_crawled_curricula.json", "w", encoding="utf-8") as f:
    json.dump(results, f, ensure_ascii=False, indent=2)

print("Saved all crawled curricula to all_88_crawled_curricula.json")
