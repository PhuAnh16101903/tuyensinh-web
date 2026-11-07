import json
from sqlalchemy import text
from app.database import engine

print("Loading all_88_crawled_curricula.json...")
with open("all_88_crawled_curricula.json", encoding="utf-8") as f:
    data = json.load(f)

print(f"Loaded curricula for {len(data)} majors.")

total_inserted = 0

with engine.begin() as conn:
    print("Clearing old subjects in database...")
    conn.execute(text("DELETE FROM subjects"))
    
    # Reset SQLite autoincrement sequence if exists
    try:
        conn.execute(text("DELETE FROM sqlite_sequence WHERE name='subjects'"))
    except Exception:
        pass

    for m_id_str, m_info in data.items():
        m_id = int(m_id_str)
        subs = m_info["subjects"]
        for s in subs:
            conn.execute(text("""
                INSERT INTO subjects (code, name, credits, semester, subject_type, description, major_id)
                VALUES (:code, :name, :credits, :semester, :subject_type, :description, :major_id)
            """), {
                "code": s["code"],
                "name": s["name"],
                "credits": s["credits"],
                "semester": s["semester"],
                "subject_type": s["subject_type"],
                "description": s["description"],
                "major_id": m_id
            })
            total_inserted += 1

print(f"Successfully inserted {total_inserted} authentic NEU subjects into admission_system.db!")
