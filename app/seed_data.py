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

# 40 Ngành tuyển sinh chính thức của NEU với điểm chuẩn K68 và điểm dự đoán K69
MAJORS_META = [
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

# Tạo danh sách 40 ngành kèm cả Môn Đại Cương Chung và Môn Chuyên Ngành
MAJORS_40 = []
for item in MAJORS_META:
    code, name, category, quota, benchmark, predicted, desc = item
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
    
    # Kết hợp đầy đủ: Đại cương chung (15 môn) + Chuyên ngành (12-14 môn) = 27-29 môn (~130 TC)
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
