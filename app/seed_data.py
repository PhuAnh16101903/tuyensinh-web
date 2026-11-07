# Danh mục các môn học đại cương chung (15 môn, đủ kỳ 1-4, áp dụng cho tất cả 40 ngành)
COMMON_GENERAL_SUBJECTS = [
    ("GEN101", "Triết học Mác - Lênin", 3, 1, "Đại cương chung", "Thế giới quan và phương pháp luận duy vật biện chứng, quy luật phát triển tự nhiên và xã hội."),
    ("GEN102", "Tiếng Anh Đại cương 1", 3, 1, "Đại cương chung", "Rèn luyện 4 kỹ năng nghe, nói, đọc, viết tiếng Anh giao tiếp chuẩn quốc tế."),
    ("GEN103", "Pháp luật Đại cương", 2, 1, "Đại cương chung", "Hệ thống pháp luật Việt Nam, nhà nước pháp quyền, quyền và nghĩa vụ công dân."),
    ("GEN104", "Tin học Đại cương & Kỹ năng số", 3, 1, "Đại cương chung", "Tin học ứng dụng văn phòng nâng cao, an toàn thông tin số và tư duy thuật toán."),
    ("GEN105", "Toán cao cấp cho các ngành ứng dụng", 3, 1, "Đại cương chung", "Phép tính vi phân, tích phân hàm một biến và nhiều biến ứng dụng thực tế."),
    ("GEN201", "Kinh tế Chính trị Mác - Lênin", 2, 2, "Đại cương chung", "Hàng hóa, tiền tệ, giá trị thặng dư và quy luật kinh tế thị trường định hướng XHCN."),
    ("GEN202", "Tiếng Anh Đại cương 2", 3, 2, "Đại cương chung", "Nâng cao kỹ năng tiếng Anh học thuật, ngữ pháp nâng cao và kỹ năng thuyết trình."),
    ("GEN203", "Kỹ năng mềm & Làm việc nhóm", 2, 2, "Đại cương chung", "Tư duy phản biện, giải quyết xung đột, kỹ năng lãnh đạo và làm việc nhóm hiệu quả."),
    ("GEN204", "Đại số tuyến tính & Hình học giải tích", 3, 2, "Đại cương chung", "Không gian vector, ma trận, định thức, hệ phương trình tuyến tính và phép biến đổi."),
    ("GEN205", "Xác suất & Thống kê ứng dụng", 3, 2, "Đại cương chung", "Lý thuyết xác suất, biến ngẫu nhiên, ước lượng thống kê và kiểm định giả thuyết."),
    ("GEN301", "Chủ nghĩa Xã hội Khoa học", 2, 3, "Đại cương chung", "Sứ mệnh lịch sử giai cấp công nhân, dân chủ xã hội chủ nghĩa và chính sách dân tộc."),
    ("GEN302", "Tư tưởng Hồ Chí Minh", 2, 3, "Đại cương chung", "Quan điểm toàn diện của Chủ tịch Hồ Chí Minh về độc lập dân tộc gắn liền với CNXH."),
    ("GEN303", "Tiếng Anh Chuyên ngành Bậc 1", 3, 3, "Đại cương chung", "Thuật ngữ chuyên môn ngành, đọc hiểu tài liệu học thuật và viết tóm tắt học thuật."),
    ("GEN401", "Lịch sử Đảng Cộng sản Việt Nam", 2, 4, "Đại cương chung", "Quá trình thành lập, các mốc son lãnh đạo cách mạng và đường lối đổi mới của Đảng."),
    ("GEN402", "Phương pháp Nghiên cứu Khoa học", 3, 4, "Đại cương chung", "Thiết kế nghiên cứu, thu thập dữ liệu, phân tích định lượng/định tính và viết báo cáo.")
]

# Danh mục môn cơ sở và chuyên ngành đặc trưng cho từng ngành
MAJOR_SPECIFIC_SUBJECTS = {
    # --- KHỐI CÔNG NGHỆ & KỸ THUẬT ---
    "7480201": [ # CNTT
        ("IT101", "Nhập môn Lập trình Python", 3, 1, "Cơ sở ngành", "Cú pháp căn bản Python, hàm, hướng đối tượng cơ bản và thư viện chuẩn."),
        ("IT102", "Cơ sở dữ liệu & SQL", 3, 2, "Cơ sở ngành", "Mô hình ERD, chuẩn hóa dữ liệu, thiết kế CSDL quan hệ với PostgreSQL."),
        ("IT201", "Cấu trúc dữ liệu & Giải thuật", 4, 3, "Cơ sở ngành", "Danh sách liên kết, ngăn xếp, hàng đợi, cây nhị phân, thuật toán sắp xếp và tìm kiếm."),
        ("IT202", "Lập trình Hướng đối tượng C++", 3, 3, "Cơ sở ngành", "Tính đóng gói, kế thừa, đa hình, trừu tượng và mẫu thiết kế Design Patterns."),
        ("IT301", "Phát triển Ứng dụng Web Fullstack", 4, 4, "Chuyên ngành", "Xây dựng RESTful API với Python FastAPI và giao diện Single Page App hiện đại."),
        ("IT302", "Công nghệ Phần mềm & Agile/Scrum", 3, 4, "Chuyên ngành", "Vòng đời phần mềm, tài liệu đặc tả SRS, mô hình UML và quản trị dự án Scrum."),
        ("IT401", "Điện toán Đám mây & DevOps", 3, 5, "Chuyên ngành", "Đóng gói Docker containers, quy trình CI/CD và kiến trúc Microservices."),
        ("IT402", "Khóa luận Tốt nghiệp CNTT", 10, 8, "Khóa luận tốt nghiệp", "Nghiên cứu ứng dụng công nghệ hoặc phát triển sản phẩm phần mềm hoàn chỉnh.")
    ],
    "7480101": [ # Khoa học máy tính
        ("CS101", "Toán rời rạc & Giải thuật ứng dụng", 3, 1, "Cơ sở ngành", "Lý thuyết đồ thị, tổ hợp, logic mệnh đề và đại số Boole."),
        ("CS201", "Lý thuyết Tính toán & Ôtômat", 3, 3, "Cơ sở ngành", "Mô hình máy Turing, ngữ pháp phi ngữ cảnh và độ phức tạp tính toán."),
        ("CS301", "Thuật toán Nâng cao", 4, 4, "Chuyên ngành", "Quy hoạch động nâng cao, luồng cực đại và hình học tính toán."),
        ("CS302", "Thị giác Máy tính (Computer Vision)", 3, 5, "Chuyên ngành", "Xử lý ảnh số, mạng tích chập CNN, nhận diện vật thể và khuôn mặt."),
        ("CS401", "Xử lý Ngôn ngữ Tự nhiên (NLP)", 4, 6, "Chuyên ngành", "Mô hình Transformer, Word2Vec, trích xuất thực thể và tóm tắt văn bản.")
    ],
    "7480103": [ # Kỹ thuật phần mềm
        ("SE101", "Quy trình Phát triển Phần mềm", 3, 2, "Cơ sở ngành", "Mô hình thác nước, Agile, Scrum, Kanban và quản trị phiên bản Git."),
        ("SE201", "Kiến trúc & Thiết kế Phần mềm", 4, 3, "Chuyên ngành", "Clean Architecture, Domain-Driven Design (DDD) và Design Patterns."),
        ("SE301", "Kiểm thử & Đảm bảo Chất lượng (QA/QC)", 3, 4, "Chuyên ngành", "Kiểm thử tự động Selenium, PyTest, kiểm thử tải và bảo mật phần mềm."),
        ("SE302", "Lập trình Ứng dụng Di động Flutter/React Native", 4, 5, "Chuyên ngành", "Phát triển ứng dụng Android/iOS đa nền tảng kết nối API.")
    ],
    "7480202": [ # An toàn thông tin
        ("SEC101", "Nhập môn Mật mã học", 3, 2, "Cơ sở ngành", "Mật mã khóa đối xứng AES, khóa công khai RSA, hàm băm SHA và chữ ký số."),
        ("SEC201", "An toàn Mạng & Tường lửa", 3, 3, "Chuyên ngành", "Phân tích gói tin Wireshark, hệ thống IDS/IPS, VPN và mạng an toàn."),
        ("SEC301", "Kiểm thử Xâm nhập (Penetration Testing)", 4, 5, "Chuyên ngành", "Khai thác lỗ hổng OWASP Top 10, công cụ Metasploit, Burp Suite."),
        ("SEC302", "Điều tra Số & Ứng cứu Sự cố (Digital Forensics)", 3, 6, "Chuyên ngành", "Thu thập chứng cứ số, phân tích nhật ký log và khôi phục dữ liệu.")
    ],
    "7480107": [ # AI
        ("AI101", "Đại số Tuyến tính & Tối ưu hóa cho AI", 3, 1, "Cơ sở ngành", "Ma trận, vector, tích phân tối ưu gradient descent."),
        ("AI201", "Học sâu & Mạng nơ-ron (Deep Learning)", 4, 4, "Chuyên ngành", "Framework PyTorch, kiến trúc MLP, CNN, RNN và Attention mechanism."),
        ("AI301", "Mô hình Ngôn ngữ Lớn (LLMs & Generative AI)", 4, 6, "Chuyên ngành", "Prompt engineering, kỹ thuật RAG, Fine-tuning mô hình ngôn ngữ Llama."),
        ("AI302", "Học tăng cường & Robot thông minh", 3, 7, "Chuyên ngành", "Q-Learning, Policy Gradient và thuật toán điều khiển tự trị.")
    ],
    "7480108": [ # Data Science
        ("DS101", "Xác suất Thống kê cho Dữ liệu lớn", 3, 1, "Cơ sở ngành", "Phân phối xác suất, ước lượng tham số, kiểm định A/B testing."),
        ("DS201", "Khai phá & Tiền xử lý Dữ liệu", 3, 3, "Chuyên ngành", "Thư viện Pandas, NumPy, xử lý dữ liệu khuyết, Feature Engineering."),
        ("DS301", "Hạ tầng Dữ liệu lớn (Big Data)", 4, 5, "Chuyên ngành", "Apache Spark, Hadoop, Kafka và xây dựng Data Warehouse."),
        ("DS302", "Trực quan hóa Dữ liệu Kinh doanh (BI)", 3, 6, "Chuyên ngành", "Tableau, Power BI, thiết kế Dashboard thông minh hỗ trợ ra quyết định.")
    ],
    "7480204": [ # Mạng máy tính
        ("NET101", "Giao thức Mạng TCP/IP", 3, 2, "Cơ sở ngành", "Mô hình OSI, định tuyến RIP/OSPF/BGP, chuyển mạch phân đoạn VLAN."),
        ("NET201", "Lập trình Hệ thống Mạng", 3, 3, "Chuyên ngành", "Socket programming, WebSocket và truyền thông thời gian thực."),
        ("NET301", "Mạng Không dây & IoT", 3, 5, "Chuyên ngành", "Giao thức MQTT, cảm biến Zigbee, LoRa và vi điều khiển ESP32."),
        ("NET302", "Quản trị Hệ thống Linux Server", 3, 6, "Chuyên ngành", "Cấu hình Nginx, DNS BIND, DHCP, sao lưu và giám sát Zabbix.")
    ],
    "7480104": [ # HTTT
        ("IS101", "Phân tích & Thiết kế Hệ thống Thông tin", 3, 2, "Cơ sở ngành", "Sơ đồ dòng dữ liệu DFD, biểu đồ Use Case UML, thiết kế CSDL."),
        ("IS201", "Hệ thống Hoạch định Tài nguyên (ERP)", 3, 4, "Chuyên ngành", "Triển khai phần mềm quản trị Odoo/SAP, tích hợp quy trình doanh nghiệp."),
        ("IS301", "Quản trị Dự án Chuyển đổi số", 3, 5, "Chuyên ngành", "Chiến lược số hóa, quản lý thay đổi và đánh giá rủi ro công nghệ.")
    ],
    "7520216": [ # Tự động hóa
        ("AUT101", "Lý thuyết Điều khiển Tự động", 3, 2, "Cơ sở ngành", "Hàm truyền, quỹ đạo nghiệm số, biểu đồ Bode, bộ điều khiển PID."),
        ("AUT201", "Lập trình PLC & Mạng Công nghiệp", 4, 3, "Chuyên ngành", "PLC Siemens S7-1200, ngôn ngữ LAD/FBD, truyền thông Profinet."),
        ("AUT301", "Hệ thống Giám sát SCADA & HMI", 3, 5, "Chuyên ngành", "Thiết kế giao diện WinCC, thu thập dữ liệu và cảnh báo sự cố công nghiệp."),
        ("AUT302", "Cánh tay Robot Công nghiệp", 3, 6, "Chuyên ngành", "Động học Robot KUKA/ABB, lập trình quỹ đạo gắp đặt tự động.")
    ],
    "7520114": [ # Cơ điện tử
        ("MEC101", "Cơ sở Thiết kế Máy & CAD/CAM", 3, 2, "Cơ sở ngành", "Tính toán chi tiết máy, vẽ kỹ thuật SolidWorks và gia công CNC."),
        ("MEC201", "Cảm biến & Cơ cấu Chấp hành", 3, 3, "Chuyên ngành", "Động cơ bước, động cơ servo, xi lanh khí nén và thủy lực."),
        ("MEC301", "Hệ thống Nhúng Điều khiển", 4, 5, "Chuyên ngành", "Lập trình STM32/ARM, xử lý ngắt, PWM và giao tiếp SPI/I2C.")
    ],
    "7520130": [ # Ô tô
        ("OTO101", "Kết cấu Ô tô Hiện đại", 3, 2, "Cơ sở ngành", "Nguyên lý động cơ đốt trong, hệ thống treo, phanh ABS, lái điện EPS."),
        ("OTO201", "Điện - Điện tử Ô tô & Mạng CAN Bus", 3, 4, "Chuyên ngành", "Hệ thống phun xăng điện tử EFI, chẩn đoán lỗi OBD-II, mạng CAN."),
        ("OTO301", "Công nghệ Xe điện EV & Pin Lithium", 4, 5, "Chuyên ngành", "Động cơ xoay chiều ba pha, quản lý bộ pin BMS và trạm sạc điện."),
        ("OTO302", "Hệ thống Hỗ trợ Lái xe Nâng cao (ADAS)", 3, 6, "Chuyên ngành", "Cảm biến Radar, Camera nhận diện làn đường, phanh khẩn cấp tự động.")
    ],
    "7520207": [ # Điện tử viễn thông
        ("ECE101", "Mạch Điện tử Tương tự & Số", 3, 2, "Cơ sở ngành", "Transistor, Op-Amp, cổng logic, mạch vi xử lý và FPGA."),
        ("ECE201", "Xử lý Tín hiệu Số (DSP)", 3, 3, "Chuyên ngành", "Biến đổi Fourier nhanh FFT, bộ lọc số IIR/FIR."),
        ("ECE301", "Kỹ thuật Thông tin Vô tuyến & 5G", 3, 5, "Chuyên ngành", "Điều chế số QAM, công nghệ MIMO, ăng-ten mảng và mạng di động 5G.")
    ],
    "7520215": [ # Vi mạch bán dẫn
        ("SEMI101", "Vật lý Bán dẫn & Thiết bị Siêu vi", 3, 2, "Cơ sở ngành", "Vùng năng lượng, hạt tải điện, cấu trúc bóng bán dẫn FinFET."),
        ("SEMI201", "Thiết kế Mạch số với Verilog/VHDL", 4, 3, "Chuyên ngành", "Mô tả phần cứng RTL, mô phỏng ModelSim, tổng hợp mạch logic."),
        ("SEMI301", "Thiết kế Vi mạch Tích hợp VLSI", 4, 5, "Chuyên ngành", "Bố trí layout chip, kiểm tra quy tắc hình học DRC/LVS và Tape-out."),
        ("SEMI302", "Quy trình Chế tạo Bán dẫn Cleanroom", 3, 6, "Chuyên ngành", "Quang khắc Lithography, lắng đọng hơi CVD, khắc ăn mòn Etching.")
    ],
    "7580201": [ # Kỹ thuật xây dựng
        ("CIV101", "Sức bền Vật liệu & Cơ học Kết cấu", 4, 2, "Cơ sở ngành", "Biểu đồ nội lực mô men, lực cắt, ứng suất và chuyển vị kết cấu."),
        ("CIV201", "Kết cấu Bê tông Cốt thép", 4, 3, "Chuyên ngành", "Tính toán dầm, cột, móng, sàn theo tiêu chuẩn TCVN 5574."),
        ("CIV301", "Mô hình Thông tin Công trình (BIM Revit)", 3, 5, "Chuyên ngành", "Thiết kế 3D Revit kết cấu, phát hiện va chạm Navisworks."),
        ("CIV302", "Quản lý Dự án & Dự toán Xây dựng", 3, 6, "Chuyên ngành", "Bóc tách khối lượng, lập bảng dự toán chi phí và tiến độ thi công.")
    ],

    # --- KHỐI KINH TẾ & QUẢN LÝ ---
    "7340101": [ # Quản trị kinh doanh
        ("BA101", "Nguyên lý Quản trị học", 3, 1, "Cơ sở ngành", "Chức năng hoạch định, tổ chức bộ máy, phong cách lãnh đạo, kiểm tra."),
        ("BA201", "Quản trị Chiến lược Doanh nghiệp", 3, 3, "Chuyên ngành", "Mô hình 5 áp lực Porter, ma trận SWOT, định vị lợi thế cạnh tranh."),
        ("BA301", "Khởi sự Doanh nghiệp & Đổi mới sáng tạo", 3, 5, "Chuyên ngành", "Xây dựng mô hình kinh doanh Canvas, gọi vốn đầu tư thiên thần."),
        ("BA302", "Quản trị Rủi ro & Khủng hoảng Doanh nghiệp", 3, 6, "Chuyên ngành", "Nhận diện rủi ro tài chính, vận hành và phương án ứng phó.")
    ],
    "7340115": [ # Marketing
        ("MKT101", "Marketing Căn bản", 3, 1, "Cơ sở ngành", "Nghiên cứu thị trường, hành vi khách hàng, phối thức Marketing-Mix 4P/7P."),
        ("MKT201", "Digital Marketing & SEO/SEM", 3, 3, "Chuyên ngành", "Tối ưu hóa công cụ tìm kiếm, quảng cáo Google Ads, Meta Ads."),
        ("MKT301", "Quản trị Thương hiệu (Brand Management)", 3, 4, "Chuyên ngành", "Định vị thương hiệu, đo lường tài sản thương hiệu, chiến dịch lan tỏa."),
        ("MKT302", "Sáng tạo Nội dung & Tiếp thị Đa kênh", 3, 5, "Chuyên ngành", "Content marketing, kịch bản video ngắn TikTok, Omnichannel marketing.")
    ],
    "7340120": [ # Kinh doanh quốc tế
        ("IB101", "Môi trường Kinh doanh Toàn cầu", 3, 2, "Cơ sở ngành", "Xu hướng toàn cầu hóa, các hiệp định thương mại tự do CPTPP, EVFTA."),
        ("IB201", "Thanh toán & Tín dụng Quốc tế", 3, 3, "Chuyên ngành", "Phương thức tín dụng chứng từ L/C, nhờ thu D/A, D/P, chuyển tiền T/T."),
        ("IB301", "Đàm phán & Hợp đồng Ngoại thương", 3, 5, "Chuyên ngành", "Điều kiện Incoterms 2020, soạn thảo hợp đồng xuất nhập khẩu quốc tế.")
    ],
    "7340201": [ # Tài chính ngân hàng
        ("FIN101", "Thị trường Tài chính & Định chế", 3, 2, "Cơ sở ngành", "Thị trường tiền tệ, trái phiếu, cổ phiếu và chính sách ngân hàng trung ương."),
        ("FIN201", "Phân tích & Đầu tư Chứng khoán", 3, 3, "Chuyên ngành", "Phân tích cơ bản định giá cổ phiếu, phân tích kỹ thuật biểu đồ nến."),
        ("FIN301", "Nghiệp vụ Ngân hàng Thương mại", 3, 4, "Chuyên ngành", "Thẩm định tín dụng khách hàng doanh nghiệp, quản trị rủi ro nợ xấu."),
        ("FIN302", "Công nghệ Tài chính (Fintech) & Ngân hàng số", 3, 6, "Chuyên ngành", "Ví điện tử, công nghệ Blockchain, thanh toán Open Banking API.")
    ],
    "7340301": [ # Kế toán
        ("ACC101", "Nguyên lý Kế toán", 3, 1, "Cơ sở ngành", "Ghi chép chứng từ kế toán, định khoản kép nợ/có, lập bảng cân đối kế toán."),
        ("ACC201", "Kế toán Tài chính Doanh nghiệp 1 & 2", 4, 3, "Chuyên ngành", "Kế toán doanh thu, tài sản cố định, vốn chủ sở hữu theo chuẩn VAS/IFRS."),
        ("ACC301", "Kế toán Quản trị & Phân tích Chi phí", 3, 4, "Chuyên ngành", "Phân tích điểm hòa vốn, dự toán ngân sách và định giá sản phẩm.")
    ],
    "7340302": [ # Kiểm toán
        ("AUD101", "Kiểm toán Căn bản", 3, 2, "Cơ sở ngành", "Bằng chứng kiểm toán, tính trọng yếu và đánh giá rủi ro kiểm toán."),
        ("AUD201", "Kiểm toán Báo cáo Tài chính", 4, 4, "Chuyên ngành", "Thủ tục kiểm tra chi tiết số dư, kiểm tra tuân thủ và lập biên bản kiểm toán."),
        ("AUD301", "Hệ thống Kiểm soát Nội bộ", 3, 5, "Chuyên ngành", "Khuôn khổ COSO, nhận diện gian lận và kiểm tra tính tuân thủ quy trình.")
    ],
    "7340122": [ # TMĐT
        ("EC101", "Tổng quan Thương mại Điện tử", 3, 1, "Cơ sở ngành", "Các mô hình B2B, B2C, D2C, kinh tế nền tảng số và mạng xã hội."),
        ("EC201", "Cổng Thanh toán & Bảo mật TMĐT", 3, 3, "Chuyên ngành", "Tích hợp VNPay, Momo, Stripe, tiêu chuẩn an toàn bảo mật PCI-DSS."),
        ("EC301", "Vận hành Sàn TMĐT & Livestream Bán hàng", 3, 4, "Chuyên ngành", "Thuật toán hiển thị Shopee, TikTok Shop, quản lý kho đa kênh."),
        ("EC302", "Phân tích Dữ liệu Khách hàng TMĐT", 3, 5, "Chuyên ngành", "Google Analytics 4, tỷ lệ chuyển đổi CRO, hành trình mua sắm.")
    ],
    "7510605": [ # Logistics
        ("LOG101", "Tổng quan Chuỗi Cung ứng (SCM)", 3, 2, "Cơ sở ngành", "Mô hình SCOR, tích hợp dòng sản phẩm, dòng tiền và thông tin."),
        ("LOG201", "Quản trị Kho bãi & Trung tâm Phân phối", 3, 3, "Chuyên ngành", "Phần mềm WMS, thiết kế bố trí kho hàng, quản trị tồn kho JIT."),
        ("LOG301", "Giao nhận Vận tải Đa phương thức Quốc tế", 3, 4, "Chuyên ngành", "Vận đơn Bill of Lading, dịch vụ Freight Forwarder, thủ tục hải quan."),
        ("LOG302", "Thu mua & Quản lý Nhà cung ứng (Procurement)", 3, 5, "Chuyên ngành", "Chiến lược đấu thầu thu mua, đàm phán hợp đồng cung ứng bền vững.")
    ],
    "7340404": [ # Quản trị nhân lực
        ("HR101", "Quản trị Nguồn Nhân lực Căn bản", 3, 1, "Cơ sở ngành", "Hoạch định nhân sự, phân tích công việc, bản mô tả công việc JD."),
        ("HR201", "Đào tạo & Phát triển Nhân tài", 3, 3, "Chuyên ngành", "Quy trình đào tạo ADDIE, xây dựng khung năng lực nhân viên."),
        ("HR301", "Tiền lương & Đãi ngộ (C&B)", 3, 4, "Chuyên ngành", "Xây dựng thang bảng lương, chính sách thưởng, bảo hiểm xã hội và thuế.")
    ],
    "7380107": [ # Luật kinh tế
        ("LAW101", "Pháp luật Doanh nghiệp", 3, 2, "Cơ sở ngành", "Thủ tục thành lập, giải thể công ty cổ phần, TNHH, quyền lợi cổ đông."),
        ("LAW201", "Pháp luật Hợp đồng Thương mại", 3, 3, "Chuyên ngành", "Soạn thảo hợp đồng, điều khoản miễn trừ, xử lý vi phạm hợp đồng."),
        ("LAW301", "Giải quyết Tranh chấp Kinh doanh Thương mại", 3, 5, "Chuyên ngành", "Trọng tài thương mại VIAC, thủ tục tố tụng tòa án kinh tế.")
    ],
    "7310106": [ # Kinh tế đối ngoại
        ("EXT101", "Lý thuyết Kinh tế Quốc tế", 3, 2, "Cơ sở ngành", "Lợi thế so sánh, thuế quan, hạn ngạch và cán cân thanh toán quốc gia."),
        ("EXT201", "Đầu tư Trực tiếp Nước ngoài (FDI)", 3, 3, "Chuyên ngành", "Chính sách thu hút FDI, tập đoàn đa quốc gia và chuyển giá quốc tế."),
        ("EXT301", "Thị trường Hàng hóa & Phái sinh Quốc tế", 3, 5, "Chuyên ngành", "Giao dịch hợp đồng tương lai, hợp đồng quyền chọn hàng hóa.")
    ],
    "7810103": [ # Du lịch
        ("TOU101", "Tài nguyên & Địa lý Du lịch Việt Nam", 3, 1, "Cơ sở ngành", "Di sản văn hóa UNESCO, danh lam thắng cảnh và tuyến điểm du lịch."),
        ("TOU201", "Thiết kế & Định giá Sản phẩm Tour", 3, 3, "Chuyên ngành", "Lập lịch trình tour, tính giá vốn và chiến lược định giá bán tour."),
        ("TOU301", "Nghiệp vụ Hướng dẫn & Điều hành Tour", 3, 4, "Chuyên ngành", "Thuyết minh tuyến điểm, tâm lý du khách, xử lý tình huống khẩn cấp.")
    ],
    "7810201": [ # Khách sạn
        ("HOT101", "Tổng quan Ngành Khách sạn & Resort", 3, 1, "Cơ sở ngành", "Cơ cấu tổ chức khách sạn, tiêu chuẩn xếp hạng sao quốc tế."),
        ("HOT201", "Quản trị Tiền sảnh (Front Office)", 3, 3, "Chuyên ngành", "Quy trình check-in/out, phần mềm quản lý phòng Opera PMS."),
        ("HOT301", "Quản trị Ẩm thực & Yến tiệc (F&B)", 3, 4, "Chuyên ngành", "Nghiệp vụ bàn, quầy bar, tổ chức hội nghị và tiệc cưới chuyên nghiệp.")
    ],

    # --- KHỐI NGOẠI NGỮ & XÃ HỘI ---
    "7220201": [ # Ngôn ngữ Anh
        ("EN101", "Ngữ âm & Âm vị học tiếng Anh", 3, 1, "Cơ sở ngành", "Bảng phiên âm quốc tế IPA, trọng âm từ, nối âm và ngữ điệu câu."),
        ("EN201", "Viết Luận Học thuật (Academic Writing)", 4, 3, "Chuyên ngành", "Tư duy phản biện, cấu trúc bài luận học thuật, trích dẫn chuẩn APA."),
        ("EN301", "Biên - Phiên dịch Chuyên ngành Kinh tế", 4, 4, "Chuyên ngành", "Dịch thuật hợp đồng thương mại, báo cáo tài chính thường niên."),
        ("EN302", "Tiếng Anh Thương mại & Đàm phán Quốc tế", 3, 5, "Chuyên ngành", "Soạn email công vụ, thuyết trình dự án và đàm phán bằng tiếng Anh.")
    ],
    "7220204": [ # Ngôn ngữ Trung
        ("CN101", "Ngữ âm & Chữ Hán Căn bản", 3, 1, "Cơ sở ngành", "Quy tắc phát âm Pinyin, cấu tạo bộ thủ chữ Hán, ngữ pháp căn bản."),
        ("CN201", "Tiếng Trung Thương mại & Thư tín", 3, 3, "Chuyên ngành", "Giao dịch đàm phán thương mại, hợp đồng xuất nhập khẩu đối tác Trung."),
        ("CN301", "Biên dịch & Phiên dịch Hán - Việt", 4, 5, "Chuyên ngành", "Dịch thuật tin tức kinh tế, phiên dịch hội nghị và đàm phán.")
    ],
    "7220209": [ # Ngôn ngữ Nhật
        ("JP101", "Nhập môn Tiếng Nhật & Chữ Hán Kanji", 4, 1, "Cơ sở ngành", "Bảng chữ cái Hiragana, Katakana, quy tắc viết 500 chữ Kanji cơ bản."),
        ("JP201", "Tiếng Nhật Doanh nghiệp & Kính ngữ", 3, 3, "Chuyên ngành", "Văn hóa giao tiếp công sở Nhật, kính ngữ Sonkeigo, khiêm nhường ngữ."),
        ("JP301", "Dịch thuật Công nghệ IT Comtor", 4, 5, "Chuyên ngành", "Thuật ngữ ngành phần mềm, dịch tài liệu thiết kế đặc tả kỹ thuật.")
    ],
    "7220210": [ # Ngôn ngữ Hàn
        ("KR101", "Chữ viết Hangeul & Ngữ pháp Căn bản", 3, 1, "Cơ sở ngành", "Quy tắc biến âm, cấu trúc câu tiếng Hàn, giao tiếp hàng ngày."),
        ("KR201", "Tiếng Hàn Thương mại Doanh nghiệp", 3, 3, "Chuyên ngành", "Văn hóa doanh nghiệp Hàn Quốc, email trao đổi đối tác tập đoàn."),
        ("KR301", "Biên phiên dịch Hàn - Việt Chuyên sâu", 4, 5, "Chuyên ngành", "Dịch đuổi hội thoại, dịch thuật tài liệu kinh tế và văn hóa.")
    ],
    "7320108": [ # Quan hệ công chúng PR
        ("PR101", "Nhập môn Quan hệ Công chúng (PR)", 3, 1, "Cơ sở ngành", "Bản chất truyền thông đại chúng, phân biệt PR và quảng cáo."),
        ("PR201", "Quản trị Khủng hoảng Truyền thông", 3, 3, "Chuyên ngành", "Kỹ thuật phản hồi dư luận, tổ chức họp báo, dập tắt tin đồn xấu."),
        ("PR301", "Lập kế hoạch & Tổ chức Sự kiện (Event)", 4, 4, "Chuyên ngành", "Viết kịch bản proposal sự kiện, điều phối âm thanh ánh sáng thực tế.")
    ],
    "7320101": [ # Báo chí truyền thông
        ("JOU101", "Kỹ năng Phỏng vấn & Viết tin Báo chí", 3, 1, "Cơ sở ngành", "Cấu trúc tháp ngược, kỹ thuật khai thác nguồn tin và viết bài phóng sự."),
        ("JOU201", "Sản xuất Chương trình Podcast & Video", 4, 3, "Chuyên ngành", "Thu âm phòng thu, dựng phim Premiere/Capcut, biên tập kịch bản hình."),
        ("JOU301", "Báo chí Dữ liệu (Data Journalism)", 3, 5, "Chuyên ngành", "Trực quan hóa số liệu Infographic, phân tích dữ liệu điều tra báo chí.")
    ],
    "7210403": [ # Thiết kế đồ họa
        ("DES101", "Nguyên lý Thị giác & Nghệ thuật Chữ (Typography)", 3, 1, "Cơ sở ngành", "Bố cục thị giác, bánh xe màu sắc, tâm lý học tiếp nhận hình ảnh."),
        ("DES201", "Thiết kế Bộ Nhận diện Thương hiệu", 4, 3, "Chuyên ngành", "Thiết kế logo, cẩm nang thương hiệu Brand Guideline trên Illustrator."),
        ("DES301", "Thiết kế Giao diện UI/UX trên Figma", 3, 4, "Chuyên ngành", "Nghiên cứu người dùng, Wireframe, Prototype và hệ thống Design System.")
    ],
    "7310401": [ # Tâm lý học
        ("PSY101", "Tâm lý học Đại cương", 3, 1, "Cơ sở ngành", "Bản chất ý thức, cảm xúc, động cơ hành vi và sự hình thành nhân cách."),
        ("PSY201", "Kỹ năng Tham vấn & Trị liệu Tâm lý", 3, 3, "Chuyên ngành", "Lắng nghe chủ động, kỹ thuật thấu cảm, đạo đức nghề nghiệp tham vấn."),
        ("PSY301", "Tâm lý học Tổ chức & Nhân sự", 3, 4, "Chuyên ngành", "Động lực làm việc của nhân viên, giải tỏa căng thẳng stress công sở.")
    ],

    # --- KHỐI Y DƯỢC, SINH HỌC & KIẾN TRÚC ---
    "7720101": [ # Y khoa
        ("MED101", "Giải phẫu học Người Toàn diện", 4, 1, "Cơ sở ngành", "Cấu tạo hệ xương khớp, hệ tuần hoàn, hô hấp và thần kinh trung ương."),
        ("MED201", "Sinh lý Bệnh & Miễn dịch học Lâm sàng", 4, 3, "Cơ sở ngành", "Cơ chế sinh bệnh, phản ứng viêm, kháng thể và đáp ứng miễn dịch."),
        ("MED301", "Bệnh học Nội khoa & Thực tập Bệnh viện", 5, 5, "Chuyên ngành", "Thăm khám lâm sàng tại giường bệnh, phân tích kết quả cận lâm sàng."),
        ("MED302", "Bệnh học Ngoại khoa & Phẫu thuật Thực hành", 5, 6, "Chuyên ngành", "Nguyên tắc vô khuẩn phòng mổ, kỹ thuật khâu vết thương, phẫu thuật cơ bản.")
    ],
    "7720201": [ # Dược học
        ("PHA101", "Hóa Dược học 1 & 2", 4, 2, "Cơ sở ngành", "Cấu trúc hóa học của dược chất, mối liên quan cấu trúc và hoạt tính."),
        ("PHA201", "Công nghệ Bào chế & Sinh Dược học", 4, 4, "Chuyên ngành", "Quy trình dập viên nén, sản xuất dung dịch siro, thuốc tiêm vô trùng."),
        ("PHA301", "Dược lý & Dược Lâm sàng", 4, 5, "Chuyên ngành", "Cơ chế tác dụng thuốc, tương tác thuốc, hướng dẫn sử dụng thuốc an toàn.")
    ],
    "7720301": [ # Điều dưỡng
        ("NUR101", "Kỹ thuật Điều dưỡng Cơ bản", 3, 2, "Cơ sở ngành", "Đo dấu hiệu sinh tồn mạch nhiệt áp, tiêm truyền, băng bó và thay băng."),
        ("NUR201", "Chăm sóc Bệnh nhân Hồi sức Cấp cứu", 4, 4, "Chuyên ngành", "Cấp cứu ngừng tuần hoàn CPR, hỗ trợ thở máy, theo dõi máy Monitor."),
        ("NUR301", "Điều dưỡng Ngoại khoa & Chăm sóc Sau mổ", 3, 5, "Chuyên ngành", "Chăm sóc dẫn lưu, phục hồi chức năng sau mổ và chống loét tì đè.")
    ],
    "7420201": [ # Công nghệ sinh học
        ("BIO101", "Sinh học Phân tử & Tế bào", 3, 1, "Cơ sở ngành", "Cấu trúc axit nucleic DNA/RNA, phiên mã, dịch mã và điều hòa gen."),
        ("BIO201", "Kỹ thuật Di truyền & Công nghệ Gen", 4, 3, "Chuyên ngành", "Phản ứng PCR, điện di gel, nhân dòng plasmid và chỉnh sửa gen CRISPR."),
        ("BIO301", "Công nghệ Vi sinh & Lên men Công nghiệp", 3, 4, "Chuyên ngành", "Nuôi cấy vi sinh vật quy mô lớn, sản xuất enzym, chế phẩm sinh học.")
    ],
    "7580101": [ # Kiến trúc
        ("ARC101", "Cơ sở Tạo hình & Vẽ Mỹ thuật Không gian", 4, 1, "Cơ sở ngành", "Quy luật phối cảnh 1-2 điểm tụ, dựng hình khối, đánh bóng kiến trúc."),
        ("ARC201", "Nguyên lý Thiết kế Kiến trúc Nhà ở", 3, 3, "Chuyên ngành", "Quy hoạch không gian sống, chiếu sáng tự nhiên và thông gió vi khí hậu."),
        ("ARC301", "Đồ án Kiến trúc Công trình Công cộng", 5, 5, "Chuyên ngành", "Thiết kế tổ hợp trường học, bảo tàng, trung tâm văn hóa cộng đồng.")
    ]
}

# Toàn bộ 88 ngành & chương trình đào tạo chính thức của Đại học Kinh tế Quốc dân (NEU)
NEU_ALL_88_MAJORS = [
    # Image 1 (1 - 18)
    (1, "7480202", "An toàn thông tin", "Công nghệ & Phân tích số", 70, 26.00, 26.15, "Đào tạo kỹ sư an toàn thông tin, bảo mật mạng, điều tra số và ứng cứu sự cố không gian mạng."),
    (2, "7340204", "Bảo hiểm", "Kinh tế & Quản lý", 60, 25.35, 25.40, "Nghiên cứu và ứng dụng định phí bảo hiểm, quản trị rủi ro tài chính và doanh nghiệp bảo hiểm."),
    (3, "7340116", "Bất động sản", "Kinh tế & Quản lý", 70, 25.36, 25.45, "Định giá bất động sản, đầu tư phát triển dự án địa ốc và kinh doanh tài sản số."),
    (4, "EP20", "Công nghệ Logistics và quản trị chuỗi cung ứng", "Chương trình Tiên tiến & Quốc tế (EP/POHE/CLC)", 60, 27.39, 27.55, "Chương trình đào tạo bằng tiếng Anh chuyên sâu về tự động hóa logistics và chuỗi cung ứng toàn cầu."),
    (5, "EP19", "Công nghệ Marketing", "Chương trình Tiên tiến & Quốc tế (EP/POHE/CLC)", 60, 26.68, 26.85, "Đào tạo MarTech, phân tích hành vi khách hàng bằng AI và tiếp thị kỹ thuật số chuẩn quốc tế."),
    (6, "EP26", "Công nghệ môi trường và phát triển bền vững", "Chương trình Tiên tiến & Quốc tế (EP/POHE/CLC)", 50, 23.48, 23.55, "Kinh tế tuần hoàn, quản trị môi trường doanh nghiệp và thị trường tín chỉ carbon."),
    (7, "7340205", "Công nghệ tài chính", "Công nghệ & Phân tích số", 80, 27.52, 27.70, "Ngành học mũi nhọn tích hợp tài chính số, ví điện tử, ngân hàng số và ứng dụng Blockchain."),
    (8, "EP09", "Công nghệ tài chính và Ngân hàng số", "Chương trình Tiên tiến & Quốc tế (EP/POHE/CLC)", 60, 26.86, 27.05, "Chương trình tiếng Anh tích hợp giải pháp ngân hàng mở, thanh toán số và an ninh tài chính."),
    (9, "7480201", "Công nghệ thông tin", "Công nghệ & Phân tích số", 120, 25.68, 25.85, "Đào tạo kỹ sư phần mềm, phát triển ứng dụng di động, hệ thống đám mây và web full-stack."),
    (10, "7480104", "Hệ thống thông tin", "Công nghệ & Phân tích số", 70, 27.09, 27.20, "Thiết kế kiến trúc hệ thống công nghệ, quản trị cơ sở dữ liệu lớn và an toàn thông tin doanh nghiệp."),
    (11, "7340405", "Hệ thống thông tin quản lý", "Công nghệ & Phân tích số", 90, 28.01, 28.15, "Cầu nối chiến lược giữa công nghệ và vận hành doanh nghiệp: triển khai ERP, CRM, phân tích nghiệp vụ BA."),
    (12, "7340301", "Kế toán", "Kinh tế & Quản lý", 160, 27.30, 27.35, "Kế toán tài chính, kế toán quản trị, chuẩn mực báo cáo tài chính quốc tế IFRS."),
    (13, "TT1", "Các chương trình: Kế toán; Kế hoạch tài chính; Quản trị kinh doanh", "Chương trình Tiên tiến & Quốc tế (EP/POHE/CLC)", 100, 25.25, 25.30, "Chương trình tiên tiến học bằng tiếng Anh liên kết các đại học hàng đầu thế giới."),
    (14, "EP04", "Kế toán tích hợp chứng chỉ quốc tế (ICAEW CFAB)", "Chương trình Tiên tiến & Quốc tế (EP/POHE/CLC)", 60, 26.62, 26.75, "Đào tạo kế toán kiểm toán theo chuẩn nghề nghiệp Anh quốc ICAEW CFAB."),
    (15, "EP15", "Khoa học dữ liệu", "Chương trình Tiên tiến & Quốc tế (EP/POHE/CLC)", 60, 26.52, 26.70, "Khai phá dữ liệu lớn Big Data, học máy Machine Learning và trực quan hóa dữ liệu kinh doanh bằng tiếng Anh."),
    (16, "7480101", "Khoa học máy tính", "Công nghệ & Phân tích số", 85, 26.19, 26.35, "Cơ sở khoa học tính toán, thuật toán tối ưu, bảo mật và phát triển hệ thống thông minh."),
    (17, "7340401", "Khoa học quản lý", "Kinh tế & Quản lý", 75, 26.30, 26.35, "Khoa học ra quyết định quản lý, chính sách công nghệ, quản trị sở hữu trí tuệ và đổi mới sáng tạo."),
    (18, "EP02", "Khoa học tính toán trong tài chính và bảo hiểm", "Chương trình Tiên tiến & Quốc tế (EP/POHE/CLC)", 50, 26.44, 26.55, "Định phí bảo hiểm (Actuary), phân tích định lượng tài chính và mô hình hóa rủi ro thị trường."),

    # Image 2 (19 - 65)
    (19, "EP01", "Khởi nghiệp và phát triển kinh doanh (BBAE)", "Chương trình Tiên tiến & Quốc tế (EP/POHE/CLC)", 60, 25.22, 25.30, "Cử nhân Quản trị kinh doanh định hướng Khởi nghiệp và đổi mới sáng tạo chuẩn quốc tế."),
    (20, "7340302", "Kiểm toán", "Kinh tế & Quản lý", 120, 28.84, 28.90, "Ngành đào tạo kiểm toán viên uy tín bậc nhất, tích hợp chứng chỉ nghề nghiệp ACCA và CPA."),
    (21, "EP21", "Kiểm toán nội bộ", "Chương trình Tiên tiến & Quốc tế (EP/POHE/CLC)", 50, 26.39, 26.50, "Chuyên sâu về quản trị rủi ro, kiểm soát nội bộ và quản trị công ty theo thông lệ quốc tế."),
    (22, "EP12", "Kiểm toán tích hợp chứng chỉ quốc tế (ICAEW CFAB)", "Chương trình Tiên tiến & Quốc tế (EP/POHE/CLC)", 60, 28.25, 28.35, "Đào tạo kiểm toán viên quốc tế đạt chứng chỉ nghề nghiệp ICAEW Anh quốc."),
    (23, "7620114", "Kinh doanh nông nghiệp", "Kinh tế & Quản lý", 50, 24.75, 24.80, "Chuỗi giá trị nông nghiệp công nghệ cao, xúc tiến thương mại nông sản xuất khẩu quốc tế."),
    (24, "7340120", "Kinh doanh quốc tế", "Kinh tế & Quản lý", 130, 28.50, 28.55, "Giao thương toàn cầu, ngoại thương, tập đoàn đa quốc gia và đàm phán hợp đồng quốc tế."),
    (25, "CLC3", "Các chương trình: Tài chính doanh nghiệp; Marketing số; Quản trị Marketing; Quản trị kinh doanh quốc tế; Kinh tế quốc tế; Logistics và quản lý chuỗi cung ứng; Thương mại điện tử; Kiểm toán tích hợp chứng chỉ ACCA", "Chương trình Tiên tiến & Quốc tế (EP/POHE/CLC)", 120, 25.89, 26.00, "Chương trình chất lượng cao đào tạo chuẩn quốc tế đa chuyên ngành mũi nhọn."),
    (26, "EP05", "Kinh doanh số (E-BDB)", "Chương trình Tiên tiến & Quốc tế (EP/POHE/CLC)", 60, 26.84, 27.00, "Mô hình kinh doanh nền tảng số, kinh tế số và khởi nghiệp công nghệ toàn cầu."),
    (27, "7340121", "Kinh doanh thương mại", "Kinh tế & Quản lý", 100, 27.94, 28.00, "Quản trị bán lẻ hiện đại, phân phối hàng hóa, xúc tiến thương mại dịch vụ và xuất nhập khẩu."),
    (28, "7310104", "Kinh tế đầu tư", "Kinh tế & Quản lý", 110, 27.56, 27.60, "Thẩm định dự án đầu tư công - tư, quản lý quỹ mạo hiểm và danh mục đầu tư tài chính."),
    (29, "CLC2", "Các chương trình: Kinh tế đầu tư; Quản trị nhân lực; Quản trị kinh doanh; Quan hệ công chúng", "Chương trình Tiên tiến & Quốc tế (EP/POHE/CLC)", 100, 24.83, 24.95, "Đào tạo chất lượng cao 4 nhóm ngành quản trị, đầu tư và truyền thông."),
    (30, "7310101P1", "Kinh tế học", "Kinh tế & Quản lý", 80, 26.64, 26.70, "Nền tảng tư duy kinh tế học hiện đại, tư vấn chính sách vĩ mô và vi mô."),
    (31, "EP13", "Kinh tế học tài chính (FE)", "Chương trình Tiên tiến & Quốc tế (EP/POHE/CLC)", 50, 25.89, 26.00, "Phân tích kinh tế vĩ mô cho thị trường tài chính, chính sách tiền tệ và định chế tài chính."),
    (32, "7620115", "Kinh tế nông nghiệp", "Kinh tế & Quản lý", 50, 24.59, 24.65, "Kinh tế phát triển nông nghiệp, kinh tế tuần hoàn và tài chính nông thôn."),
    (33, "7310105", "Kinh tế phát triển", "Kinh tế & Quản lý", 70, 26.79, 26.85, "Hoạch định phát triển kinh tế vùng, chính sách giảm nghèo bền vững và phát triển bao trùm."),
    (34, "CLC1", "Các chương trình: Kinh tế phát triển; Ngân hàng; Công nghệ thông tin và chuyển đổi số; Bảo hiểm tích hợp chứng chỉ ANZIIF", "Chương trình Tiên tiến & Quốc tế (EP/POHE/CLC)", 100, 25.28, 25.40, "Chương trình chất lượng cao kết hợp công nghệ chuyển đổi số và tài chính ngân hàng."),
    (35, "7310106", "Kinh tế quốc tế", "Kinh tế & Quản lý", 90, 28.30, 28.35, "Phân tích thương mại quốc tế, dòng vốn đầu tư trực tiếp FDI và hội nhập kinh tế toàn cầu."),
    (36, "EP22", "Kinh tế quốc tế (EP)", "Chương trình Tiên tiến & Quốc tế (EP/POHE/CLC)", 60, 27.20, 27.30, "Chương trình tiếng Anh đào tạo chuyên sâu về kinh tế thương mại và tài chính toàn cầu."),
    (37, "EP23", "Kinh tế số", "Chương trình Tiên tiến & Quốc tế (EP/POHE/CLC)", 60, 26.51, 26.70, "Tác động của AI và dữ liệu lớn lên cấu trúc nền kinh tế và các mô hình thị trường số."),
    (38, "7850102", "Kinh tế tài nguyên thiên nhiên", "Kinh tế & Quản lý", 50, 24.38, 24.45, "Kinh tế năng lượng xanh, quản lý tài nguyên nước, khoáng sản và định giá hệ sinh thái."),
    (39, "7310101P2", "Kinh tế và quản lý đô thị", "Kinh tế & Quản lý", 60, 25.90, 26.00, "Quy hoạch kinh tế đô thị thông minh Smart City, đầu tư hạ tầng và phát triển nhà ở."),
    (40, "7310101P3", "Kinh tế và quản lý nguồn nhân lực", "Kinh tế & Quản lý", 70, 27.07, 27.15, "Phân tích thị trường lao động, kinh tế nhân khẩu học và chính sách việc làm quốc gia."),
    (41, "EP24", "Kinh tế Y tế", "Chương trình Tiên tiến & Quốc tế (EP/POHE/CLC)", 50, 24.42, 24.50, "Quản lý bệnh viện, bảo hiểm y tế, kinh tế dược phẩm và chính sách chăm sóc sức khỏe."),
    (42, "EP17", "Kỹ thuật phần mềm", "Chương trình Tiên tiến & Quốc tế (EP/POHE/CLC)", 60, 25.00, 25.20, "Kiến trúc phần mềm doanh nghiệp, DevOps, kiểm thử và quản lý dự án Agile/Scrum."),
    (43, "7510605", "Logistics và Quản lý chuỗi cung ứng", "Kinh tế & Quản lý", 110, 28.53, 28.65, "Tối ưu hóa vận tải đa phương thức, kho bãi thông minh và chuỗi cung ứng toàn cầu."),
    (44, "EP14", "Logistics và Quản lý chuỗi cung ứng tích hợp chứng chỉ quốc tế (LSIC)", "Chương trình Tiên tiến & Quốc tế (EP/POHE/CLC)", 60, 27.87, 28.00, "Đào tạo Logistics chuẩn quốc tế tích hợp chứng chỉ nghề nghiệp FIATA và LSIC."),
    (45, "7380101", "Luật", "Luật & Ngoại ngữ - Xã hội", 80, 25.52, 25.60, "Hệ thống pháp luật quốc gia, tố tụng dân sự, hình sự và tư vấn giải quyết tranh chấp."),
    (46, "POHE4", "Luật kinh doanh", "Chương trình Tiên tiến & Quốc tế (EP/POHE/CLC)", 50, 25.68, 25.75, "Chương trình cử nhân định hướng ứng dụng thực chiến pháp lý cho doanh nghiệp và tập đoàn."),
    (47, "7380107", "Luật kinh tế", "Luật & Ngoại ngữ - Xã hội", 100, 26.62, 26.70, "Pháp luật doanh nghiệp, hợp đồng thương mại, trọng tài quốc tế và bảo hộ sở hữu trí tuệ."),
    (48, "7380109", "Luật thương mại quốc tế", "Luật & Ngoại ngữ - Xã hội", 60, 26.38, 26.45, "Quy chế thương mại WTO, tranh chấp thương mại xuyên biên giới và các hiệp định FTA."),
    (49, "7340115", "Marketing", "Kinh tế & Quản lý", 140, 27.99, 28.05, "Chiến lược định vị sản phẩm, Digital Marketing, nghiên cứu thị trường và quản trị thương hiệu."),
    (50, "7220201", "Ngôn ngữ Anh", "Luật & Ngoại ngữ - Xã hội", 120, 26.46, 26.55, "Tiếng Anh thương mại cao cấp C1, biên phiên dịch kinh tế ngoại giao và truyền thông quốc tế."),
    (51, "EP03", "Phân tích dữ liệu kinh tế (EDA)", "Chương trình Tiên tiến & Quốc tế (EP/POHE/CLC)", 60, 27.24, 27.40, "Khai phá dữ liệu lớn bằng ngôn ngữ R/Python, mô hình hóa kinh tế định lượng bằng tiếng Anh."),
    (52, "EP06", "Phân tích kinh doanh (BA)", "Chương trình Tiên tiến & Quốc tế (EP/POHE/CLC)", 70, 27.40, 27.55, "Business Analytics: Phân tích nghiệp vụ, tối ưu hóa quy trình doanh nghiệp dựa trên dữ liệu."),
    (53, "EP25", "Phát triển quốc tế", "Chương trình Tiên tiến & Quốc tế (EP/POHE/CLC)", 50, 24.68, 24.75, "Chính sách viện trợ quốc tế, các tổ chức phi chính phủ NGO và phát triển bền vững toàn cầu."),
    (54, "7320108", "Quan hệ công chúng", "Luật & Ngoại ngữ - Xã hội", 80, 27.58, 27.65, "Truyền thông đa phương tiện, xử lý khủng hoảng dư luận và tổ chức sự kiện chuyên nghiệp."),
    (55, "7340408", "Quan hệ lao động", "Kinh tế & Quản lý", 50, 25.52, 25.60, "Thỏa ước lao động tập thể, đối thoại xã hội, giải quyết tranh chấp lao động và công đoàn."),
    (56, "7340403", "Quản lý công", "Kinh tế & Quản lý", 60, 25.37, 25.45, "Quản trị khu vực công, tài chính công, cải cách hành chính và đổi mới dịch vụ công ích."),
    (57, "EPMP", "Quản lý công và Chính sách (E-PMP)", "Chương trình Tiên tiến & Quốc tế (EP/POHE/CLC)", 50, 24.05, 24.15, "Chương trình tiếng Anh về phân tích và hoạch định chính sách công chuẩn quốc tế."),
    (58, "7850103", "Quản lý đất đai", "Kinh tế & Quản lý", 60, 24.75, 24.80, "Hệ thống thông tin địa lý GIS, định giá đất, quy hoạch sử dụng đất và chính sách bất động sản."),
    (59, "7340409", "Quản lý dự án", "Kinh tế & Quản lý", 80, 26.67, 26.75, "Lập kế hoạch, quản trị tiến độ, chi phí, rủi ro dự án theo chuẩn quốc tế PMP/PRINCE2."),
    (60, "7850101", "Quản lý tài nguyên và môi trường", "Kinh tế & Quản lý", 50, 24.20, 24.25, "Đánh giá tác động môi trường ĐTM, quản lý chất thải và chính sách bảo vệ tài nguyên sinh thái."),
    (61, "POHE6", "Quản lý thị trường", "Chương trình Tiên tiến & Quốc tế (EP/POHE/CLC)", 50, 24.89, 24.95, "Chương trình ứng dụng thực hành thanh tra kiểm tra thương mại, bảo vệ quyền lợi người tiêu dùng."),
    (62, "EP08", "Quản trị chất lượng và Đổi mới (E-MQI)", "Chương trình Tiên tiến & Quốc tế (EP/POHE/CLC)", 50, 25.12, 25.20, "Quản trị chất lượng toàn diện TQM, Lean Six Sigma và hệ thống quản lý chuẩn ISO."),
    (63, "EP27", "Quản trị công nghiệp sáng tạo", "Chương trình Tiên tiến & Quốc tế (EP/POHE/CLC)", 50, 24.08, 24.15, "Quản lý sản phẩm nghệ thuật, công nghiệp giải trí số, truyền thông và bản quyền tác phẩm."),
    (64, "7810103", "Quản trị dịch vụ du lịch và lữ hành", "Kinh tế & Quản lý", 75, 25.79, 25.85, "Thiết kế sản phẩm du lịch thông minh, điều hành mạng lưới tour quốc tế và hướng dẫn lữ hành."),
    (65, "EP07", "Quản trị điều hành thông minh (E-SOM)", "Chương trình Tiên tiến & Quốc tế (EP/POHE/CLC)", 60, 25.80, 25.95, "Quản trị vận hành số, tự động hóa quy trình nghiệp vụ RPA và ra quyết định thông minh."),

    # Image 3 (66 - 88)
    (66, "EP18", "Quản trị giải trí và sự kiện", "Chương trình Tiên tiến & Quốc tế (EP/POHE/CLC)", 60, 25.89, 26.00, "Tổ chức sự kiện âm nhạc, thể thao, lễ hội quốc tế và quản trị cơ sở giải trí văn hóa."),
    (67, "7810201", "Quản trị khách sạn", "Kinh tế & Quản lý", 80, 26.08, 26.15, "Vận hành chuỗi khách sạn và resort 5 sao quốc tế, quản trị buồng phòng và ẩm thực cao cấp."),
    (68, "POHE1", "Quản trị khách sạn (POHE)", "Chương trình Tiên tiến & Quốc tế (EP/POHE/CLC)", 60, 25.05, 25.15, "Chương trình cử nhân định hướng nghề nghiệp thực hành chuyên sâu tại các tập đoàn khách sạn."),
    (69, "EP11", "Quản trị khách sạn quốc tế (IHME)", "Chương trình Tiên tiến & Quốc tế (EP/POHE/CLC)", 50, 24.93, 25.05, "Đào tạo nhà quản lý khách sạn quốc tế với môi trường thực tập nước ngoài chuyên nghiệp."),
    (70, "7340101", "Quản trị kinh doanh", "Kinh tế & Quản lý", 200, 26.85, 26.95, "Tư duy chiến lược tổng thể, quản trị vận hành tổ chức, lãnh đạo và phát triển doanh nghiệp."),
    (71, "EBBA", "Quản trị kinh doanh (E-BBA)", "Chương trình Tiên tiến & Quốc tế (EP/POHE/CLC)", 80, 25.74, 25.85, "Chương trình Cử nhân Quản trị kinh doanh bằng tiếng Anh đạt kiểm định chất lượng quốc tế ACBSP."),
    (72, "POHE5", "Quản trị kinh doanh thương mại", "Chương trình Tiên tiến & Quốc tế (EP/POHE/CLC)", 60, 26.64, 26.75, "Đào tạo thực hành chuyên sâu về quản trị chuỗi cửa hàng, kênh phân phối và thương mại hiện đại."),
    (73, "POHE2", "Quản trị lữ hành", "Chương trình Tiên tiến & Quốc tế (EP/POHE/CLC)", 50, 24.77, 24.85, "Đào tạo ứng dụng điều hành tour du lịch lữ hành quốc tế, kết nối thực tế doanh nghiệp lữ hành."),
    (74, "7340404", "Quản trị nhân lực", "Kinh tế & Quản lý", 85, 27.25, 27.30, "Thu hút và phát triển nhân tài, chế độ lương thưởng C&B, xây dựng văn hóa doanh nghiệp số."),
    (75, "EP28", "Quản trị nhân lực quốc tế", "Chương trình Tiên tiến & Quốc tế (EP/POHE/CLC)", 50, 25.75, 25.85, "Quản lý nguồn nhân lực đa quốc gia, chính sách nhân sự toàn cầu và đàm phán quốc tế."),
    (76, "EP29", "Quản trị rủi ro định lượng", "Chương trình Tiên tiến & Quốc tế (EP/POHE/CLC)", 50, 26.15, 26.25, "Định lượng rủi ro tín dụng, rủi ro thị trường và rủi ro hoạt động trong định chế tài chính."),
    (77, "TT2", "Các chương trình: Tài chính; Kinh doanh quốc tế", "Chương trình Tiên tiến & Quốc tế (EP/POHE/CLC)", 100, 26.00, 26.10, "Chương trình tiên tiến học bằng tiếng Anh liên kết với các trường đại học danh tiếng tại Mỹ."),
    (78, "7340201", "Tài chính – Ngân hàng", "Kinh tế & Quản lý", 180, 27.43, 27.50, "Thị trường tài chính, chứng khoán, quản trị ngân hàng thương mại và thẩm định tín dụng."),
    (79, "EP10", "Tài chính và Đầu tư (BFI)", "Chương trình Tiên tiến & Quốc tế (EP/POHE/CLC)", 60, 26.76, 26.90, "Quản lý danh mục đầu tư, ngân hàng đầu tư và thị trường vốn quốc tế giảng dạy bằng tiếng Anh."),
    (80, "POHE7", "Thẩm định giá", "Chương trình Tiên tiến & Quốc tế (EP/POHE/CLC)", 50, 24.96, 25.05, "Thực hành chuyên sâu về định giá tài sản, thẩm định giá doanh nghiệp và tài sản vô hình."),
    (81, "EP31", "Thẩm định giá/Ngành TC-NH", "Chương trình Tiên tiến & Quốc tế (EP/POHE/CLC)", 50, 24.10, 24.20, "Thẩm định giá tài sản đảm bảo trong hoạt động tín dụng của các ngân hàng thương mại."),
    (82, "7310107", "Thống kê kinh tế", "Kinh tế & Quản lý", 60, 27.29, 27.35, "Kinh tế lượng, phân tích chuỗi thời gian, dự báo kinh tế vĩ mô và khảo sát điều tra thị trường."),
    (83, "EP32", "Thống kê và Trí tuệ kinh doanh", "Chương trình Tiên tiến & Quốc tế (EP/POHE/CLC)", 60, 25.54, 25.70, "Business Intelligence: Ứng dụng thống kê hiện đại và khai phá dữ liệu xây dựng dashboard trực quan."),
    (84, "7340122", "Thương mại điện tử", "Kinh tế & Quản lý", 100, 28.62, 28.75, "Vận hành sàn giao dịch trực tuyến, tiếp thị đa kênh Omnichannel, thanh toán số và logistics TMĐT."),
    (85, "7310108", "Toán kinh tế", "Công nghệ & Phân tích số", 60, 27.22, 27.30, "Toán tài chính, giải thuật tối ưu hóa, lý thuyết trò chơi và quản trị rủi ro định lượng."),
    (86, "EP30", "Toán ứng dụng", "Chương trình Tiên tiến & Quốc tế (EP/POHE/CLC)", 50, 25.60, 25.75, "Giải thuật tính toán khoa học, mô phỏng tài chính và tối ưu hóa hệ thống bằng tiếng Anh."),
    (87, "EP16", "Trí tuệ nhân tạo", "Công nghệ & Phân tích số", 70, 25.64, 25.85, "Học sâu Deep Learning, xử lý ngôn ngữ tự nhiên NLP, thị giác máy tính và ứng dụng AI kinh tế."),
    (88, "POHE3", "Truyền thông Marketing", "Chương trình Tiên tiến & Quốc tế (EP/POHE/CLC)", 60, 27.39, 27.50, "Sáng tạo nội dung truyền thông tích hợp IMC, quản lý agency và chiến dịch truyền thông đa nền tảng.")
]

MAJORS_40 = []
for item in NEU_ALL_88_MAJORS:
    id_val, code, name, category, quota, benchmark, predicted, desc = item
    specific = MAJOR_SPECIFIC_SUBJECTS.get(code, [
        (f"SPE-{code[-3:]}-31", f"Cơ sở chuyên ngành {name} 1", 3, 3, "Cơ sở ngành", f"Kiến thức nền tảng và phương pháp luận chuyên ngành {name}."),
        (f"SPE-{code[-3:]}-32", f"Cơ sở chuyên ngành {name} 2", 3, 3, "Cơ sở ngành", f"Mô hình hóa và các công cụ thực nghiệm trong {name}."),
        (f"SPE-{code[-3:]}-41", f"Lý thuyết chuyên sâu {name}", 3, 4, "Cơ sở ngành", f"Phân tích chuyên sâu các mô hình lý thuyết của {name}."),
        (f"SPE-{code[-3:]}-42", f"Ứng dụng chuyển đổi số trong {name}", 3, 4, "Cơ sở ngành", f"Áp dụng công nghệ số, dữ liệu và tự động hóa trong {name}."),
        (f"SPE-{code[-3:]}-51", f"Chuyên đề nâng cao ngành {name}", 4, 5, "Chuyên ngành", f"Ứng dụng thực hành chuyên sâu và giải quyết vấn đề trong {name}."),
        (f"SPE-{code[-3:]}-52", f"Quản trị dự án & Thực chiến {name}", 3, 5, "Chuyên ngành", f"Kỹ năng lập kế hoạch, triển khai dự án thực tế ngành {name}."),
        (f"SPE-{code[-3:]}-61", f"Hệ thống thông tin & Phân tích chuyên sâu {name}", 3, 6, "Chuyên ngành", f"Kỹ thuật phân tích, mô phỏng và tối ưu giải pháp {name}."),
        (f"SPE-{code[-3:]}-62", f"Đồ án thực hành chuyên ngành {name}", 3, 6, "Chuyên ngành", f"Xây dựng đề án / sản phẩm hoàn chỉnh theo nhóm."),
        (f"SPE-{code[-3:]}-71", f"Khởi nghiệp đổi mới sáng tạo ngành {name}", 3, 7, "Chuyên ngành", f"Tư duy khởi nghiệp, lập kế hoạch kinh doanh và sở hữu trí tuệ."),
        (f"SPE-{code[-3:]}-72", f"Thực tập doanh nghiệp (OJT) ngành {name}", 4, 7, "Chuyên ngành", f"Trải nghiệm môi trường làm việc thực tế và cọ xát nghiệp vụ {name}."),
        (f"SPE-{code[-3:]}-81", f"Chuyên đề tốt nghiệp định hướng nghề nghiệp", 4, 8, "Chuyên ngành", f"Phân tích giải pháp thực tiễn trước khi tốt nghiệp."),
        (f"SPE-{code[-3:]}-82", f"Khóa luận / Đồ án tốt nghiệp ngành {name}", 10, 8, "Khóa luận tốt nghiệp", f"Đồ án tốt nghiệp tổng hợp kiến thức toàn khóa học {name}.")
    ])
    full_subjects = list(COMMON_GENERAL_SUBJECTS) + specific
    MAJORS_40.append({
        "code": code,
        "name": name,
        "category": category,
        "quota": quota,
        "benchmark_score": benchmark,
        "predicted_score": predicted,
        "description": desc,
        "subjects": full_subjects
    })
