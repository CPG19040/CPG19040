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
        self.loc = ""

    def _get_connection(self):
        """Helper to create and return a connection."""
        return psycopg2.connect(**self.connection_config)

    def set_database(self, s):
        self.loc = s

    def get_database(self):
        return self.loc

    def fetch_all(self, sql):
        try:
            with self._get_connection() as conn:
                with conn.cursor(cursor_factory=extras.RealDictCursor) as cur:
                    cur.execute(sql)
                    return cur.fetchall()
        except Exception as e:
            print(f"Database Error: {e}")
            return []

    def execute_query(self, sql, params=None):
        """Equivalent to ExecuteNonQuery."""
        try:
            print(sql.__str__())
            with self._get_connection() as conn:
                with conn.cursor() as cur:
                    cur.execute(sql, params)
                conn.commit()
        except Exception as e:
            print(f"Database Error: {e}")

    def retrieve_records(self, sql):
        try:
            conn = self._get_connection()
            cur = conn.cursor()
            cur.execute(sql)
            return cur
        except Exception as e:
            print(f"Database Error: {e}")
            return None

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
            with self._get_connection() as conn:
                with conn.cursor() as cur:
                    cur.execute(sql, (psycopg2.Binary(img_bytes),))
                conn.commit()
        except Exception as e:
            print(f"Database Error: {e}")