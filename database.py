import psycopg2

def save_to_db(data):
    try:
        # Yahan password check karein!
        conn = psycopg2.connect(
            dbname="resume_db",
            user="postgres",
            password="Ayu@020705", # <-- Apna asli password yahan likhein
            host="localhost",
            port="5432"
        )
        cur = conn.cursor()
        
        cur.execute(
            "INSERT INTO parsed_resumes (email, skills) VALUES (%s, %s)",
            (data['email'], data['skills'])
        )
        
        conn.commit()
        cur.close()
        conn.close()
        print("Data saved successfully!")
    except Exception as e:
        print(f"Database error: {e}")