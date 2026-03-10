import psycopg2
from psycopg2 import extras
from datetime import datetime

class DatabaseTools:
    def __init__(self):
        self.connection_config = {
            'dbname': 'DB_CAI',
            'user': 'postgres',
            'password': '1234',
            'host': 'localhost',
            'port': '5432'
        }
        self.conn = psycopg2.connect(**self.connection_config)

    def fetch_all(self, sql, params=None):
        """Equivalent to ExecuteReader, returns list of dicts."""
        try:
            with self.conn as conn:
                with conn.cursor(cursor_factory=extras.RealDictCursor) as cur:
                    cur.execute(sql, params)
                    return cur.fetchall()
        except Exception as e:
            print(f"Database Error: {e}")
            return []

    def execute_query(self, sql, params=None):
        """Equivalent to ExecuteNonQuery."""
        try:
            with self.conn.cursor() as cur:
                cur.execute(sql, params)
            self.conn.commit()
        except Exception as e:
            print(f"Database Error: {e}")

    def retrieve_records(self, sql, params=None):
        """Returns a cursor for reading records (use with fetchone/fetchall)."""
        try:
            cur = self.conn.cursor()
            cur.execute(sql, params)
            return cur
        except Exception as e:
            print(f"Database Error: {e}")
            return None

    def close_connection(self):
        if self.conn:
            self.conn.close()

    def stud_activity_log(self, student_id, action):
        """Logs student activity using parameterized queries (SQL Injection safe)."""
        now = datetime.now()
        date_str = now.strftime("%d/%m/%Y")
        time_str = now.strftime("%I:%M %p")

        sql = """INSERT INTO tbl_StudentLog (StudentNo, Action, LogDate, LogTime) 
                 VALUES (%s, %s, %s, %s)"""
        
        self.execute_query(sql, (student_id, action, date_str, time_str))

    def save_image(self, sql, img_bytes):
        """Saves binary data (bytearray) to the database."""
        try:
            with self.conn.cursor() as cur:
                cur.execute(sql, (psycopg2.Binary(img_bytes),))
            self.conn.commit()
        except Exception as e:
            print(f"Database Error: {e}")