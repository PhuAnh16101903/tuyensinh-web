import sqlite3
import os

DB_PATH = r"C:\Users\Admin\.gemini\antigravity\scratch\Lập trình web\admission_system.db"

# Toàn bộ 88 ngành / chương trình đào tạo chính thức của NEU từ bảng điểm chuẩn chính thức
NEU_ALL_88_MAJORS = [
    (1, "7480202", "An toàn thông tin", "Công nghệ & Phân tích số", 70, 26.00, 26.15, "Đào tạo kỹ sư an toàn thông tin, bảo mật mạng, điều tra số và ứng cứu sự cố không gian mạng."),
    (2, "7340204", "Bảo hiểm", "Kinh tế & Quản lý", 85, 25.35, 25.40, "Nghiên cứu và ứng dụng định phí bảo hiểm, quản trị rủi ro tài chính và doanh nghiệp bảo hiểm."),
    (3, "7340116", "Bất động sản", "Kinh tế & Quản lý", 95, 25.36, 25.45, "Định giá bất động sản, đầu tư phát triển dự án địa ốc và kinh doanh tài sản số."),
    (4, "EP20", "Công nghệ Logistics và quản trị chuỗi cung ứng", "Chương trình Tiên tiến & Quốc tế (EP/POHE/CLC)", 85, 27.39, 27.55, "Chương trình đào tạo bằng tiếng Anh chuyên sâu về tự động hóa logistics và chuỗi cung ứng toàn cầu."),
    (5, "EP19", "Công nghệ Marketing", "Chương trình Tiên tiến & Quốc tế (EP/POHE/CLC)", 85, 26.68, 26.85, "Đào tạo MarTech, phân tích hành vi khách hàng bằng AI và tiếp thị kỹ thuật số chuẩn quốc tế."),
    (6, "EP26", "Công nghệ môi trường và phát triển bền vững", "Chương trình Tiên tiến & Quốc tế (EP/POHE/CLC)", 70, 23.48, 23.55, "Kinh tế tuần hoàn, quản trị môi trường doanh nghiệp và thị trường tín chỉ carbon."),
    (7, "7340205", "Công nghệ tài chính", "Công nghệ & Phân tích số", 110, 27.52, 27.70, "Ngành học mũi nhọn tích hợp tài chính số, ví điện tử, ngân hàng số và ứng dụng Blockchain."),
    (8, "EP09", "Công nghệ tài chính và Ngân hàng số", "Chương trình Tiên tiến & Quốc tế (EP/POHE/CLC)", 85, 26.86, 27.05, "Chương trình tiếng Anh tích hợp giải pháp ngân hàng mở, thanh toán số và an ninh tài chính."),
    (9, "7480201", "Công nghệ thông tin", "Công nghệ & Phân tích số", 165, 25.68, 25.85, "Đào tạo kỹ sư phần mềm, phát triển ứng dụng di động, hệ thống đám mây và web full-stack."),
    (10, "7480104", "Hệ thống thông tin", "Công nghệ & Phân tích số", 95, 27.09, 27.20, "Thiết kế kiến trúc hệ thống công nghệ, quản trị cơ sở dữ liệu lớn và an toàn thông tin doanh nghiệp."),
    (11, "7340405", "Hệ thống thông tin quản lý", "Công nghệ & Phân tích số", 125, 28.01, 28.15, "Cầu nối chiến lược giữa công nghệ và vận hành doanh nghiệp: triển khai ERP, CRM, phân tích nghiệp vụ BA."),
    (12, "7340301", "Kế toán", "Kinh tế & Quản lý", 220, 27.30, 27.35, "Kế toán tài chính, kế toán quản trị, chuẩn mực báo cáo tài chính quốc tế IFRS."),
    (13, "TT1", "Các chương trình: Kế toán; Kế hoạch tài chính; Quản trị kinh doanh", "Chương trình Tiên tiến & Quốc tế (EP/POHE/CLC)", 140, 25.25, 25.30, "Chương trình tiên tiến học bằng tiếng Anh liên kết các đại học hàng đầu thế giới."),
    (14, "EP04", "Kế toán tích hợp chứng chỉ quốc tế (ICAEW CFAB)", "Chương trình Tiên tiến & Quốc tế (EP/POHE/CLC)", 85, 26.62, 26.75, "Đào tạo kế toán kiểm toán theo chuẩn nghề nghiệp Anh quốc ICAEW CFAB."),
    (15, "EP15", "Khoa học dữ liệu", "Chương trình Tiên tiến & Quốc tế (EP/POHE/CLC)", 85, 26.52, 26.70, "Khai phá dữ liệu lớn Big Data, học máy Machine Learning và trực quan hóa dữ liệu kinh doanh bằng tiếng Anh."),
    (16, "7480101", "Khoa học máy tính", "Công nghệ & Phân tích số", 120, 26.19, 26.35, "Cơ sở khoa học tính toán, thuật toán tối ưu, bảo mật và phát triển hệ thống thông minh."),
    (17, "7340401", "Khoa học quản lý", "Kinh tế & Quản lý", 105, 26.30, 26.35, "Khoa học ra quyết định quản lý, chính sách công nghệ, quản trị sở hữu trí tuệ và đổi mới sáng tạo."),
    (18, "EP02", "Khoa học tính toán trong tài chính và bảo hiểm", "Chương trình Tiên tiến & Quốc tế (EP/POHE/CLC)", 70, 26.44, 26.55, "Định phí bảo hiểm (Actuary), phân tích định lượng tài chính và mô hình hóa rủi ro thị trường."),
    (19, "EP01", "Khởi nghiệp và phát triển kinh doanh (BBAE)", "Chương trình Tiên tiến & Quốc tế (EP/POHE/CLC)", 85, 25.22, 25.30, "Cử nhân Quản trị kinh doanh định hướng Khởi nghiệp và đổi mới sáng tạo chuẩn quốc tế."),
    (20, "7340302", "Kiểm toán", "Kinh tế & Quản lý", 165, 28.84, 28.90, "Ngành đào tạo kiểm toán viên uy tín bậc nhất, tích hợp chứng chỉ nghề nghiệp ACCA và CPA."),
    (21, "EP21", "Kiểm toán nội bộ", "Chương trình Tiên tiến & Quốc tế (EP/POHE/CLC)", 70, 26.39, 26.50, "Chuyên sâu về quản trị rủi ro, kiểm soát nội bộ và quản trị công ty theo thông lệ quốc tế."),
    (22, "EP12", "Kiểm toán tích hợp chứng chỉ quốc tế (ICAEW CFAB)", "Chương trình Tiên tiến & Quốc tế (EP/POHE/CLC)", 85, 28.25, 28.35, "Đào tạo kiểm toán viên quốc tế đạt chứng chỉ nghề nghiệp ICAEW Anh quốc."),
    (23, "7620114", "Kinh doanh nông nghiệp", "Kinh tế & Quản lý", 70, 24.75, 24.80, "Chuỗi giá trị nông nghiệp công nghệ cao, xúc tiến thương mại nông sản xuất khẩu quốc tế."),
    (24, "7340120", "Kinh doanh quốc tế", "Kinh tế & Quản lý", 180, 28.50, 28.55, "Giao thương toàn cầu, ngoại thương, tập đoàn đa quốc gia và đàm phán hợp đồng quốc tế."),
    (25, "CLC3", "Các chương trình: Tài chính doanh nghiệp; Marketing số; Quản trị Marketing; Quản trị kinh doanh quốc tế; Kinh tế quốc tế; Logistics và quản lý chuỗi cung ứng; Thương mại điện tử; Kiểm toán tích hợp chứng chỉ ACCA", "Chương trình Tiên tiến & Quốc tế (EP/POHE/CLC)", 165, 25.89, 26.00, "Chương trình chất lượng cao đào tạo chuẩn quốc tế đa chuyên ngành mũi nhọn."),
    (26, "EP05", "Kinh doanh số (E-BDB)", "Chương trình Tiên tiến & Quốc tế (EP/POHE/CLC)", 85, 26.84, 27.00, "Mô hình kinh doanh nền tảng số, kinh tế số và khởi nghiệp công nghệ toàn cầu."),
    (27, "7340121", "Kinh doanh thương mại", "Kinh tế & Quản lý", 140, 27.94, 28.00, "Quản trị bán lẻ hiện đại, phân phối hàng hóa, xúc tiến thương mại dịch vụ và xuất nhập khẩu."),
    (28, "7310104", "Kinh tế đầu tư", "Kinh tế & Quản lý", 150, 27.56, 27.60, "Thẩm định dự án đầu tư công - tư, quản lý quỹ mạo hiểm và danh mục đầu tư tài chính."),
    (29, "CLC2", "Các chương trình: Kinh tế đầu tư; Quản trị nhân lực; Quản trị kinh doanh; Quan hệ công chúng", "Chương trình Tiên tiến & Quốc tế (EP/POHE/CLC)", 140, 24.83, 24.95, "Đào tạo chất lượng cao 4 nhóm ngành quản trị, đầu tư và truyền thông."),
    (30, "7310101P1", "Kinh tế học", "Kinh tế & Quản lý", 110, 26.64, 26.70, "Nền tảng tư duy kinh tế học hiện đại, tư vấn chính sách vĩ mô và vi mô."),
    (31, "EP13", "Kinh tế học tài chính (FE)", "Chương trình Tiên tiến & Quốc tế (EP/POHE/CLC)", 70, 25.89, 26.00, "Phân tích kinh tế vĩ mô cho thị trường tài chính, chính sách tiền tệ và định chế tài chính."),
    (32, "7620115", "Kinh tế nông nghiệp", "Kinh tế & Quản lý", 70, 24.59, 24.65, "Kinh tế phát triển nông nghiệp, kinh tế tuần hoàn và tài chính nông thôn."),
    (33, "7310105", "Kinh tế phát triển", "Kinh tế & Quản lý", 95, 26.79, 26.85, "Hoạch định phát triển kinh tế vùng, chính sách giảm nghèo bền vững và phát triển bao trùm."),
    (34, "CLC1", "Các chương trình: Kinh tế phát triển; Ngân hàng; Công nghệ thông tin và chuyển đổi số; Bảo hiểm tích hợp chứng chỉ ANZIIF", "Chương trình Tiên tiến & Quốc tế (EP/POHE/CLC)", 140, 25.28, 25.40, "Chương trình chất lượng cao kết hợp công nghệ chuyển đổi số và tài chính ngân hàng."),
    (35, "7310106", "Kinh tế quốc tế", "Kinh tế & Quản lý", 125, 28.30, 28.35, "Phân tích thương mại quốc tế, dòng vốn đầu tư trực tiếp FDI và hội nhập kinh tế toàn cầu."),
    (36, "EP22", "Kinh tế quốc tế (EP)", "Chương trình Tiên tiến & Quốc tế (EP/POHE/CLC)", 85, 27.20, 27.30, "Chương trình tiếng Anh đào tạo chuyên sâu về kinh tế thương mại và tài chính toàn cầu."),
    (37, "EP23", "Kinh tế số", "Chương trình Tiên tiến & Quốc tế (EP/POHE/CLC)", 85, 26.51, 26.70, "Tác động của AI và dữ liệu lớn lên cấu trúc nền kinh tế và các mô hình thị trường số."),
    (38, "7850102", "Kinh tế tài nguyên thiên nhiên", "Kinh tế & Quản lý", 70, 24.38, 24.45, "Kinh tế năng lượng xanh, quản lý tài nguyên nước, khoáng sản và định giá hệ sinh thái."),
    (39, "7310101P2", "Kinh tế và quản lý đô thị", "Kinh tế & Quản lý", 85, 25.90, 26.00, "Quy hoạch kinh tế đô thị thông minh Smart City, đầu tư hạ tầng và phát triển nhà ở."),
    (40, "7310101P3", "Kinh tế và quản lý nguồn nhân lực", "Kinh tế & Quản lý", 95, 27.07, 27.15, "Phân tích thị trường lao động, kinh tế nhân khẩu học và chính sách việc làm quốc gia."),
    (41, "EP24", "Kinh tế Y tế", "Chương trình Tiên tiến & Quốc tế (EP/POHE/CLC)", 70, 24.42, 24.50, "Quản lý bệnh viện, bảo hiểm y tế, kinh tế dược phẩm và chính sách chăm sóc sức khỏe."),
    (42, "EP17", "Kỹ thuật phần mềm", "Chương trình Tiên tiến & Quốc tế (EP/POHE/CLC)", 85, 25.00, 25.20, "Kiến trúc phần mềm doanh nghiệp, DevOps, kiểm thử và quản lý dự án Agile/Scrum."),
    (43, "7510605", "Logistics và Quản lý chuỗi cung ứng", "Kinh tế & Quản lý", 150, 28.53, 28.65, "Tối ưu hóa vận tải đa phương thức, kho bãi thông minh và chuỗi cung ứng toàn cầu."),
    (44, "EP14", "Logistics và Quản lý chuỗi cung ứng tích hợp chứng chỉ quốc tế (LSIC)", "Chương trình Tiên tiến & Quốc tế (EP/POHE/CLC)", 85, 27.87, 28.00, "Đào tạo Logistics chuẩn quốc tế tích hợp chứng chỉ nghề nghiệp FIATA và LSIC."),
    (45, "7380101", "Luật", "Luật & Ngoại ngữ - Xã hội", 110, 25.52, 25.60, "Hệ thống pháp luật quốc gia, tố tụng dân sự, hình sự và tư vấn giải quyết tranh chấp."),
    (46, "POHE4", "Luật kinh doanh", "Chương trình Tiên tiến & Quốc tế (EP/POHE/CLC)", 70, 25.68, 25.75, "Chương trình cử nhân định hướng ứng dụng thực chiến pháp lý cho doanh nghiệp và tập đoàn."),
    (47, "7380107", "Luật kinh tế", "Luật & Ngoại ngữ - Xã hội", 140, 26.62, 26.70, "Pháp luật doanh nghiệp, hợp đồng thương mại, trọng tài quốc tế và bảo hộ sở hữu trí tuệ."),
    (48, "7380109", "Luật thương mại quốc tế", "Luật & Ngoại ngữ - Xã hội", 85, 26.38, 26.45, "Quy chế thương mại WTO, tranh chấp thương mại xuyên biên giới và các hiệp định FTA."),
    (49, "7340115", "Marketing", "Kinh tế & Quản lý", 195, 27.99, 28.05, "Chiến lược định vị sản phẩm, Digital Marketing, nghiên cứu thị trường và quản trị thương hiệu."),
    (50, "7220201", "Ngôn ngữ Anh", "Luật & Ngoại ngữ - Xã hội", 165, 26.46, 26.55, "Tiếng Anh thương mại cao cấp C1, biên phiên dịch kinh tế ngoại giao và truyền thông quốc tế."),
    (51, "EP03", "Phân tích dữ liệu kinh tế (EDA)", "Chương trình Tiên tiến & Quốc tế (EP/POHE/CLC)", 85, 27.24, 27.40, "Khai phá dữ liệu lớn bằng ngôn ngữ R/Python, mô hình hóa kinh tế định lượng bằng tiếng Anh."),
    (52, "EP06", "Phân tích kinh doanh (BA)", "Chương trình Tiên tiến & Quốc tế (EP/POHE/CLC)", 95, 27.40, 27.55, "Business Analytics: Phân tích nghiệp vụ, tối ưu hóa quy trình doanh nghiệp dựa trên dữ liệu."),
    (53, "EP25", "Phát triển quốc tế", "Chương trình Tiên tiến & Quốc tế (EP/POHE/CLC)", 70, 24.68, 24.75, "Chính sách viện trợ quốc tế, các tổ chức phi chính phủ NGO và phát triển bền vững toàn cầu."),
    (54, "7320108", "Quan hệ công chúng", "Luật & Ngoại ngữ - Xã hội", 110, 27.58, 27.65, "Truyền thông đa phương tiện, xử lý khủng hoảng dư luận và tổ chức sự kiện chuyên nghiệp."),
    (55, "7340408", "Quan hệ lao động", "Kinh tế & Quản lý", 70, 25.52, 25.60, "Thỏa ước lao động tập thể, đối thoại xã hội, giải quyết tranh chấp lao động và công đoàn."),
    (56, "7340403", "Quản lý công", "Kinh tế & Quản lý", 85, 25.37, 25.45, "Quản trị khu vực công, tài chính công, cải cách hành chính và đổi mới dịch vụ công ích."),
    (57, "EPMP", "Quản lý công và Chính sách (E-PMP)", "Chương trình Tiên tiến & Quốc tế (EP/POHE/CLC)", 70, 24.05, 24.15, "Chương trình tiếng Anh về phân tích và hoạch định chính sách công chuẩn quốc tế."),
    (58, "7850103", "Quản lý đất đai", "Kinh tế & Quản lý", 85, 24.75, 24.80, "Hệ thống thông tin địa lý GIS, định giá đất, quy hoạch sử dụng đất và chính sách bất động sản."),
    (59, "7340409", "Quản lý dự án", "Kinh tế & Quản lý", 110, 26.67, 26.75, "Lập kế hoạch, quản trị tiến độ, chi phí, rủi ro dự án theo chuẩn quốc tế PMP/PRINCE2."),
    (60, "7850101", "Quản lý tài nguyên và môi trường", "Kinh tế & Quản lý", 70, 24.20, 24.25, "Đánh giá tác động môi trường ĐTM, quản lý chất thải và chính sách bảo vệ tài nguyên sinh thái."),
    (61, "POHE6", "Quản lý thị trường", "Chương trình Tiên tiến & Quốc tế (EP/POHE/CLC)", 70, 24.89, 24.95, "Chương trình ứng dụng thực hành thanh tra kiểm tra thương mại, bảo vệ quyền lợi người tiêu dùng."),
    (62, "EP08", "Quản trị chất lượng và Đổi mới (E-MQI)", "Chương trình Tiên tiến & Quốc tế (EP/POHE/CLC)", 70, 25.12, 25.20, "Quản trị chất lượng toàn diện TQM, Lean Six Sigma và hệ thống quản lý chuẩn ISO."),
    (63, "EP27", "Quản trị công nghiệp sáng tạo", "Chương trình Tiên tiến & Quốc tế (EP/POHE/CLC)", 70, 24.08, 24.15, "Quản lý sản phẩm nghệ thuật, công nghiệp giải trí số, truyền thông và bản quyền tác phẩm."),
    (64, "7810103", "Quản trị dịch vụ du lịch và lữ hành", "Kinh tế & Quản lý", 105, 25.79, 25.85, "Thiết kế sản phẩm du lịch thông minh, điều hành mạng lưới tour quốc tế và hướng dẫn lữ hành."),
    (65, "EP07", "Quản trị điều hành thông minh (E-SOM)", "Chương trình Tiên tiến & Quốc tế (EP/POHE/CLC)", 85, 25.80, 25.95, "Quản trị vận hành số, tự động hóa quy trình nghiệp vụ RPA và ra quyết định thông minh."),
    (66, "EP18", "Quản trị giải trí và sự kiện", "Chương trình Tiên tiến & Quốc tế (EP/POHE/CLC)", 85, 25.89, 26.00, "Tổ chức sự kiện âm nhạc, thể thao, lễ hội quốc tế và quản trị cơ sở giải trí văn hóa."),
    (67, "7810201", "Quản trị khách sạn", "Kinh tế & Quản lý", 110, 26.08, 26.15, "Vận hành chuỗi khách sạn và resort 5 sao quốc tế, quản trị buồng phòng và ẩm thực cao cấp."),
    (68, "POHE1", "Quản trị khách sạn (POHE)", "Chương trình Tiên tiến & Quốc tế (EP/POHE/CLC)", 85, 25.05, 25.15, "Chương trình cử nhân định hướng nghề nghiệp thực hành chuyên sâu tại các tập đoàn khách sạn."),
    (69, "EP11", "Quản trị khách sạn quốc tế (IHME)", "Chương trình Tiên tiến & Quốc tế (EP/POHE/CLC)", 70, 24.93, 25.05, "Đào tạo nhà quản lý khách sạn quốc tế với môi trường thực tập nước ngoài chuyên nghiệp."),
    (70, "7340101", "Quản trị kinh doanh", "Kinh tế & Quản lý", 275, 26.85, 26.95, "Tư duy chiến lược tổng thể, quản trị vận hành tổ chức, lãnh đạo và phát triển doanh nghiệp."),
    (71, "EBBA", "Quản trị kinh doanh (E-BBA)", "Chương trình Tiên tiến & Quốc tế (EP/POHE/CLC)", 110, 25.74, 25.85, "Chương trình Cử nhân Quản trị kinh doanh bằng tiếng Anh đạt kiểm định chất lượng quốc tế ACBSP."),
    (72, "POHE5", "Quản trị kinh doanh thương mại", "Chương trình Tiên tiến & Quốc tế (EP/POHE/CLC)", 85, 26.64, 26.75, "Đào tạo thực hành chuyên sâu về quản trị chuỗi cửa hàng, kênh phân phối và thương mại hiện đại."),
    (73, "POHE2", "Quản trị lữ hành", "Chương trình Tiên tiến & Quốc tế (EP/POHE/CLC)", 70, 24.77, 24.85, "Đào tạo ứng dụng điều hành tour du lịch lữ hành quốc tế, kết nối thực tế doanh nghiệp lữ hành."),
    (74, "7340404", "Quản trị nhân lực", "Kinh tế & Quản lý", 120, 27.25, 27.30, "Thu hút và phát triển nhân tài, chế độ lương thưởng C&B, xây dựng văn hóa doanh nghiệp số."),
    (75, "EP28", "Quản trị nhân lực quốc tế", "Chương trình Tiên tiến & Quốc tế (EP/POHE/CLC)", 70, 25.75, 25.85, "Quản lý nguồn nhân lực đa quốc gia, chính sách nhân sự toàn cầu và đàm phán quốc tế."),
    (76, "EP29", "Quản trị rủi ro định lượng", "Chương trình Tiên tiến & Quốc tế (EP/POHE/CLC)", 70, 26.15, 26.25, "Định lượng rủi ro tín dụng, rủi ro thị trường và rủi ro hoạt động trong định chế tài chính."),
    (77, "TT2", "Các chương trình: Tài chính; Kinh doanh quốc tế", "Chương trình Tiên tiến & Quốc tế (EP/POHE/CLC)", 140, 26.00, 26.10, "Chương trình tiên tiến học bằng tiếng Anh liên kết với các trường đại học danh tiếng tại Mỹ."),
    (78, "7340201", "Tài chính – Ngân hàng", "Kinh tế & Quản lý", 250, 27.43, 27.50, "Thị trường tài chính, chứng khoán, quản trị ngân hàng thương mại và thẩm định tín dụng."),
    (79, "EP10", "Tài chính và Đầu tư (BFI)", "Chương trình Tiên tiến & Quốc tế (EP/POHE/CLC)", 85, 26.76, 26.90, "Quản lý danh mục đầu tư, ngân hàng đầu tư và thị trường vốn quốc tế giảng dạy bằng tiếng Anh."),
    (80, "POHE7", "Thẩm định giá", "Chương trình Tiên tiến & Quốc tế (EP/POHE/CLC)", 70, 24.96, 25.05, "Thực hành chuyên sâu về định giá tài sản, thẩm định giá doanh nghiệp và tài sản vô hình."),
    (81, "EP31", "Thẩm định giá/Ngành TC-NH", "Chương trình Tiên tiến & Quốc tế (EP/POHE/CLC)", 70, 24.10, 24.20, "Thẩm định giá tài sản đảm bảo trong hoạt động tín dụng của các ngân hàng thương mại."),
    (82, "7310107", "Thống kê kinh tế", "Kinh tế & Quản lý", 85, 27.29, 27.35, "Kinh tế lượng, phân tích chuỗi thời gian, dự báo kinh tế vĩ mô và khảo sát điều tra thị trường."),
    (83, "EP32", "Thống kê và Trí tuệ kinh doanh", "Chương trình Tiên tiến & Quốc tế (EP/POHE/CLC)", 85, 25.54, 25.70, "Business Intelligence: Ứng dụng thống kê hiện đại và khai phá dữ liệu xây dựng dashboard trực quan."),
    (84, "7340122", "Thương mại điện tử", "Kinh tế & Quản lý", 140, 28.62, 28.75, "Vận hành sàn giao dịch trực tuyến, tiếp thị đa kênh Omnichannel, thanh toán số và logistics TMĐT."),
    (85, "7310108", "Toán kinh tế", "Công nghệ & Phân tích số", 85, 27.22, 27.30, "Toán tài chính, giải thuật tối ưu hóa, lý thuyết trò chơi và quản trị rủi ro định lượng."),
    (86, "EP30", "Toán ứng dụng", "Chương trình Tiên tiến & Quốc tế (EP/POHE/CLC)", 70, 25.60, 25.75, "Giải thuật tính toán khoa học, mô phỏng tài chính và tối ưu hóa hệ thống bằng tiếng Anh."),
    (87, "EP16", "Trí tuệ nhân tạo", "Công nghệ & Phân tích số", 95, 25.64, 25.85, "Học sâu Deep Learning, xử lý ngôn ngữ tự nhiên NLP, thị giác máy tính và ứng dụng AI kinh tế."),
    (88, "POHE3", "Truyền thông Marketing", "Chương trình Tiên tiến & Quốc tế (EP/POHE/CLC)", 85, 27.39, 27.50, "Sáng tạo nội dung truyền thông tích hợp IMC, quản lý agency và chiến dịch truyền thông đa nền tảng."),
]

def migrate():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Thêm cột predicted_score nếu chưa có
    cursor.execute("PRAGMA table_info(majors)")
    cols = [c[1] for c in cursor.fetchall()]
    if "predicted_score" not in cols:
        cursor.execute("ALTER TABLE majors ADD COLUMN predicted_score FLOAT DEFAULT 0.0")
        conn.commit()

    print(f"Bắt đầu đồng bộ chính xác {len(NEU_ALL_88_MAJORS)} ngành/chương trình đào tạo NEU...")

    # Đổi mã tạm để tránh xung đột UNIQUE
    cursor.execute("UPDATE majors SET code = 'OLD_' || id || '_' || code")
    conn.commit()

    for item in NEU_ALL_88_MAJORS:
        id_val, code, name, cat, quota, bench, pred, desc = item
        cursor.execute("SELECT id FROM majors WHERE id = ?", (id_val,))
        if cursor.fetchone():
            cursor.execute("""
                UPDATE majors
                SET code = ?, name = ?, category = ?, quota = ?, benchmark_score = ?, predicted_score = ?, description = ?
                WHERE id = ?
            """, (code, name, cat, quota, bench, pred, desc, id_val))
        else:
            cursor.execute("""
                INSERT INTO majors (id, code, name, category, quota, benchmark_score, predicted_score, description)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """, (id_val, code, name, cat, quota, bench, pred, desc))

    # Xóa các id cũ thừa nếu có id > 88
    cursor.execute("DELETE FROM majors WHERE id > 88")
    conn.commit()

    cursor.execute("SELECT count(*), min(benchmark_score), max(benchmark_score), min(predicted_score), max(predicted_score) FROM majors")
    cnt, min_b, max_b, min_p, max_p = cursor.fetchone()
    print(f"✅ ĐỒNG BỘ THÀNH CÔNG: Tổng số {cnt} ngành/chương trình NEU!")
    print(f"📊 Điểm chuẩn K68 (Gốc): {min_b} -> {max_b} | Dự đoán K69: {min_p} -> {max_p}")
    conn.close()

if __name__ == "__main__":
    migrate()
