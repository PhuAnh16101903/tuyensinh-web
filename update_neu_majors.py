import sqlite3
import os

DB_PATH = r"C:\Users\Admin\.gemini\antigravity\scratch\Lập trình web\admission_system.db"

# Official 40 NEU Majors data with real K68 benchmark scores and predicted K69 scores
NEU_OFFICIAL_MAJORS = [
    ("7340302", "Kiểm toán", "Kinh tế & Quản lý", 120, 28.84, 28.90, "Ngành đào tạo kiểm toán viên chuyên nghiệp hàng đầu Việt Nam, tích hợp chứng chỉ ACCA và CPA quốc tế."),
    ("7340122", "Thương mại điện tử", "Kinh tế & Quản lý", 100, 28.62, 28.75, "Đào tạo chuyên gia kinh doanh trực tuyến, tiếp thị đa kênh Omnichannel, sàn TMĐT toàn cầu và thanh toán số."),
    ("7510605", "Logistics và Quản lý chuỗi cung ứng", "Kinh tế & Quản lý", 110, 28.53, 28.65, "Tối ưu hóa dòng chảy hàng hóa quốc tế, kho bãi thông minh, vận tải đa phương thức và chuỗi cung ứng xanh."),
    ("7340120", "Kinh doanh quốc tế", "Kinh tế & Quản lý", 130, 28.50, 28.55, "Giao thương quốc tế, đàm phán ngoại thương, quản trị tập đoàn đa quốc gia và chính sách xuất nhập khẩu."),
    ("7310106", "Kinh tế quốc tế", "Kinh tế & Quản lý", 90, 28.30, 28.35, "Phân tích kinh tế vĩ mô toàn cầu, dòng vốn FDI, chính sách thương mại và hội nhập kinh tế quốc tế sâu rộng."),
    ("7320108", "Quan hệ công chúng (PR)", "Ngoại ngữ & Xã hội", 80, 28.18, 28.25, "Xây dựng chiến lược truyền thông thương hiệu, quản trị quan hệ báo chí, xử trị khủng hoảng và tổ chức sự kiện đỉnh cao."),
    ("7340409", "Quản lý chuỗi cung ứng", "Kinh tế & Quản lý", 80, 28.10, 28.15, "Hoạch định nhu cầu, mua sắm chiến lược, quản lý nhà cung cấp và chuỗi cung ứng số toàn diện."),
    ("7340405", "Hệ thống thông tin quản lý", "Công nghệ & Kỹ thuật", 90, 28.01, 28.10, "Cầu nối chiến lược giữa công nghệ và điều hành doanh nghiệp: Triển khai ERP, CRM, phân tích nghiệp vụ BA."),
    ("7340115", "Marketing", "Kinh tế & Quản lý", 140, 27.99, 28.05, "Chiến lược tiếp thị sản phẩm, Digital Marketing, nghiên cứu hành vi người tiêu dùng và quản trị giá trị thương hiệu."),
    ("7340121", "Kinh doanh thương mại", "Kinh tế & Quản lý", 100, 27.94, 28.00, "Phát triển mạng lưới bán lẻ hiện đại, phân phối hàng hóa, thương mại dịch vụ và quản trị kênh bán lẻ."),
    ("7340124", "Kinh doanh số (Digital Business)", "Kinh tế & Quản lý", 70, 27.90, 28.05, "Mô hình kinh doanh trên nền tảng số, khởi nghiệp công nghệ, phân tích dữ liệu khách hàng số và tự động hóa kinh doanh."),
    ("7310104", "Kinh tế đầu tư", "Kinh tế & Quản lý", 110, 27.56, 27.60, "Thẩm định dự án đầu tư công và tư, quản lý danh mục đầu tư tài chính, quỹ mạo hiểm và đầu tư công nghệ."),
    ("7340205", "Công nghệ tài chính (Fintech)", "Công nghệ & Kỹ thuật", 75, 27.52, 27.65, "Ứng dụng AI, Blockchain, Big Data trong tài chính, ngân hàng số, ví điện tử và cổng thanh toán trung gian."),
    ("7380107", "Luật kinh tế", "Kinh tế & Quản lý", 100, 27.45, 27.50, "Tư vấn pháp lý doanh nghiệp, hợp đồng thương mại quốc tế, giải quyết tranh chấp trọng tài và sở hữu trí tuệ."),
    ("7340201", "Tài chính - Ngân hàng", "Kinh tế & Quản lý", 180, 27.43, 27.45, "Thị trường tài chính, chứng khoán, ngân hàng thương mại, định giá doanh nghiệp và quản trị rủi ro tài chính."),
    ("7340101", "Quản trị kinh doanh", "Kinh tế & Quản lý", 220, 27.40, 27.45, "Đào tạo nhà quản trị tương lai với tư duy chiến lược, kỹ năng điều hành tổ chức và khởi nghiệp đổi mới sáng tạo."),
    ("7340206", "Ngân hàng số & Tài chính công nghệ", "Kinh tế & Quản lý", 60, 27.35, 27.50, "Chuyển đổi số ngân hàng, thanh toán không tiền mặt, tín dụng trực tuyến và quản lý rủi ro an ninh tài chính."),
    ("7340301", "Kế toán", "Kinh tế & Quản lý", 160, 27.30, 27.35, "Hạch toán kế toán tài chính, kế toán quản trị, chuẩn mực kế toán quốc tế IFRS và ứng dụng phần mềm kế toán số."),
    ("7310107", "Thống kê kinh tế", "Kinh tế & Quản lý", 60, 27.29, 27.30, "Mô hình hóa kinh tế lượng, điều tra khảo sát xã hội học, phân tích xu hướng thị trường và dự báo kinh tế vĩ mô."),
    ("7340404", "Quản trị nhân lực", "Kinh tế & Quản lý", 85, 27.25, 27.30, "Thu hút và giữ chân nhân tài, xây dựng văn hóa doanh nghiệp, lương thưởng đãi ngộ C&B và chiến lược nhân sự số."),
    ("7310108", "Toán kinh tế", "Công nghệ & Kỹ thuật", 60, 27.22, 27.25, "Toán tài chính, giải thuật tối ưu hóa, quản trị rủi ro định lượng và mô hình hóa chính sách kinh tế."),
    ("7310101", "Kinh tế học (Kinh tế & Quản lý)", "Kinh tế & Quản lý", 90, 27.20, 27.25, "Nền tảng kinh tế học hiện đại, tư vấn chính sách công, phân tích thị trường cạnh tranh và phát triển kinh tế vùng."),
    ("7310105", "Kinh tế phát triển", "Kinh tế & Quản lý", 70, 27.20, 27.20, "Quy hoạch phát triển kinh tế xã hội, giảm nghèo bền vững, kinh tế tuần hoàn và tài chính khí hậu."),
    ("7340412", "Quản trị điều hành thông minh", "Kinh tế & Quản lý", 60, 27.20, 27.30, "Vận hành doanh nghiệp bằng dữ liệu, tự động hóa quy trình nghiệp vụ RPA và ra quyết định thời gian thực."),
    ("7480107", "Trí tuệ nhân tạo (AI)", "Công nghệ & Kỹ thuật", 70, 27.15, 27.30, "Chuyên sâu về học máy (Machine Learning), xử lý ngôn ngữ tự nhiên, Generative AI và ứng dụng AI kinh tế."),
    ("7220201", "Ngôn ngữ Anh", "Ngoại ngữ & Xã hội", 120, 27.10, 27.15, "Tiếng Anh thương mại cao cấp, biên phiên dịch kinh tế đối ngoại và giao tiếp đa văn hóa quốc tế."),
    ("7480104", "Hệ thống thông tin", "Công nghệ & Kỹ thuật", 65, 27.09, 27.15, "Thiết kế kiến trúc hệ thống, an toàn cơ sở dữ liệu lớn và giải pháp chuyển đổi số cho cơ quan, tổ chức."),
    ("7340401", "Khoa học quản lý", "Kinh tế & Quản lý", 75, 26.95, 27.00, "Khoa học ra quyết định quản lý, chính sách công nghệ, quản trị sở hữu trí tuệ và quản lý đổi mới sáng tạo."),
    ("7810201", "Quản trị khách sạn", "Kinh tế & Quản lý", 80, 26.90, 26.95, "Quản trị resort, khách sạn tiêu chuẩn quốc tế 5 sao, quản trị dịch vụ lưu trú và ẩm thực cao cấp."),
    ("7460108", "Khoa học dữ liệu trong kinh tế & kinh doanh", "Công nghệ & Kỹ thuật", 80, 26.85, 27.00, "Phân tích dữ liệu lớn, trực quan hóa số liệu BI, dự báo hành vi khách hàng và tối ưu hóa quyết định kinh doanh."),
    ("7380101", "Luật", "Kinh tế & Quản lý", 80, 26.80, 26.85, "Hệ thống pháp luật quốc gia, luật dân sự, luật hình sự, luật tố tụng và kỹ năng tranh tụng tại tòa."),
    ("7810103", "Quản trị dịch vụ du lịch & lữ hành", "Kinh tế & Quản lý", 75, 26.80, 26.80, "Thiết kế sản phẩm du lịch thông minh, điều hành lữ hành quốc tế, du lịch sinh thái và phát triển điểm đến."),
    ("7480101", "Khoa học máy tính", "Công nghệ & Kỹ thuật", 85, 26.75, 26.85, "Cơ sở khoa học tính toán, thuật toán tối ưu, bảo mật mật mã học và phát triển phần mềm lõi thông minh."),
    ("7340116", "Bất động sản", "Kinh tế & Quản lý", 70, 26.50, 26.50, "Định giá bất động sản, đầu tư phát triển dự án địa ốc, quản lý vận hành tòa nhà và môi giới bất động sản chuyên nghiệp."),
    ("7480103", "Kỹ thuật phần mềm", "Công nghệ & Kỹ thuật", 80, 26.25, 26.35, "Quy trình thiết kế phần mềm doanh nghiệp, DevOps, kiểm thử tự động và kiến trúc Microservices hiện đại."),
    ("7480202", "An toàn thông tin", "Công nghệ & Kỹ thuật", 65, 25.80, 25.90, "Bảo vệ hạ tầng số trọng yếu, phòng thủ tấn công mạng, an ninh dữ liệu tài chính và điều tra tội phạm mạng."),
    ("7850103", "Quản lý đất đai", "Kinh tế & Quản lý", 60, 25.80, 25.80, "Hệ thống thông tin địa lý GIS, quy hoạch sử dụng đất đai, thị trường quyền sử dụng đất và chính sách bồi thường tái định cư."),
    ("7480201", "Công nghệ thông tin", "Công nghệ & Kỹ thuật", 110, 25.68, 25.85, "Kỹ sư phát triển phần mềm ứng dụng, web full-stack, di động và quản trị cơ sở hạ tầng mạng doanh nghiệp."),
    ("7340204", "Bảo hiểm", "Kinh tế & Quản lý", 60, 25.35, 25.40, "Bảo hiểm nhân thọ, bảo hiểm phi nhân thọ, tính toán định phí bảo hiểm (Actuary) và quản trị quỹ hưu trí."),
    ("7310109", "Kinh tế nông nghiệp & PTNT", "Kinh tế & Quản lý", 55, 25.10, 25.15, "Kinh doanh nông sản xuất khẩu, chuỗi giá trị nông nghiệp công nghệ cao và kinh tế xanh bền vững.")
]

def migrate():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Check if predicted_score column exists in majors table
    cursor.execute("PRAGMA table_info(majors)")
    columns = [c[1] for c in cursor.fetchall()]
    if "predicted_score" not in columns:
        print("Adding column predicted_score to majors table...")
        cursor.execute("ALTER TABLE majors ADD COLUMN predicted_score FLOAT DEFAULT 0.0")
        conn.commit()

    print("Temporarily renaming codes to avoid UNIQUE collision during migration...")
    cursor.execute("UPDATE majors SET code = 'OLD_' || id || '_' || code")
    conn.commit()

    print("Updating 40 official NEU majors...")
    for idx, (code, name, category, quota, benchmark, predicted, desc) in enumerate(NEU_OFFICIAL_MAJORS, 1):
        cursor.execute("SELECT id FROM majors WHERE id = ?", (idx,))
        row = cursor.fetchone()
        if row:
            cursor.execute("""
                UPDATE majors
                SET code = ?, name = ?, category = ?, quota = ?, benchmark_score = ?, predicted_score = ?, description = ?
                WHERE id = ?
            """, (code, name, category, quota, benchmark, predicted, desc, idx))
        else:
            cursor.execute("""
                INSERT INTO majors (id, code, name, category, quota, benchmark_score, predicted_score, description)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """, (idx, code, name, category, quota, benchmark, predicted, desc))
    
    conn.commit()
    print("Migration completed successfully!")

    # Verify
    cursor.execute("SELECT count(*), min(benchmark_score), max(benchmark_score), min(predicted_score), max(predicted_score) FROM majors")
    cnt, min_b, max_b, min_p, max_p = cursor.fetchone()
    print(f"Total Majors: {cnt} | K68 Benchmark: {min_b} -> {max_b} | K69 Predicted: {min_p} -> {max_p}")
    conn.close()

if __name__ == "__main__":
    migrate()
