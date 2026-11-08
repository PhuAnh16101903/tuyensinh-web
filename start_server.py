import sys
import os
import socket
import uvicorn

def is_port_in_use(port: int) -> bool:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(0.5)
        return s.connect_ex(('127.0.0.1', port)) == 0

if __name__ == "__main__":
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    
    env_port = os.environ.get("PORT")
    if env_port:
        port = int(env_port)
    elif not is_port_in_use(8000):
        port = 8000
    else:
        port = 8001
        
    print("=" * 60)
    print(f"[*] HE THONG TUYEN SINH NEU 2026 - KHOA 69")
    print(f"[*] Truy cap he thong tai: http://127.0.0.1:{port}")
    if port != 8000:
        print(f"[*] Luu y: Cong 8000 dang duoc su dung boi du an khac (EduMind AI), he thong tu dong chuyen sang cong {port} de tranh xung dot!")
    print("=" * 60)
    
    uvicorn.run("main:app", host="127.0.0.1", port=port, log_level="info")
