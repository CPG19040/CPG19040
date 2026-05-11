import psycopg2
from psycopg2 import extras

class DatabaseTools:
    def __init__(self):
        self.connection_config = {
            'dbname': 'DB_CAI',
            'user': 'postgres',
            'password': '1234',
            'host': 'localhost',
            'port': '5432'
        }
    
    def get_connection(self):
        return psycopg2.connect(**self.connection_config)

    def fetch_all(self, sql, params=None):
        """Equivalent to ExecuteReader, returns list of dicts."""
        try:
            conn = psycopg2.connect(**self.connection_config)
            with conn.cursor(cursor_factory=extras.RealDictCursor) as cur:
                cur.execute(sql, params)
                # print(cur.mogrify(sql, params).decode('utf-8'))
                return cur.fetchall()

        except Exception as e:
            print(f"Database Error: {e}")
            return []

        finally:
            conn.close()

    def execute_query(self, sql, params=None):
        """Equivalent to ExecuteNonQuery."""
        try:
            conn = psycopg2.connect(**self.connection_config)
            with conn.cursor() as cur:
                cur.execute(sql, params)
            conn.commit()

        except Exception as e:
            print(f"Database Error: {e}")

        finally:
            conn.close()

    def retrieve_records(self, sql:str, params:tuple=None):
        """Returns a cursor for reading records (use with fetchone/fetchall)."""
        try:
            conn = psycopg2.connect(**self.connection_config)
            cur = conn.cursor()
            cur.execute(sql, params)
            return cur, conn

        except Exception as e:
            print(f"Database Error: {e}")
            return None, None

        
