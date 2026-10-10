import psycopg2, os
from psycopg2 import extras
from dotenv import load_dotenv,find_dotenv
from App.Logger import setup_logger

class DatabaseTools:

    def __init__(self):
        self.logger = setup_logger("CAI_System", "admin_activity.log")
        # self.connection_config = {
        #     'dbname'  : 'DB_CAI',
        #     'user'    : 'postgres',
        #     'password': '1234',
        #     'host'    : 'localhost',
        #     'port'    : '5432'
        # }

        load_dotenv(find_dotenv()) # Load variables from .env file into environment

        self.connection_config = {
            'dbname'  : os.getenv('DB_NAME'),
            'user'    : os.getenv('DB_USER', 'postgres'),
            'password': os.getenv('DB_PASSWORD'),
            'host'    : os.getenv('DB_HOST', 'localhost'),
            'port'    : os.getenv('DB_PORT', '5432')
        }
    
    def get_connection(self):
        return psycopg2.connect(**self.connection_config)

    def fetch_all(self, sql, params=None):
        """
            Returns:
                List of dicts (list[RealDictCursor]):
        """
        try:
            conn = psycopg2.connect(**self.connection_config)
            with conn.cursor(cursor_factory=extras.RealDictCursor) as cur:
                cur.execute(sql, params)
                # print(cur.mogrify(sql, params).decode('utf-8'))
                return cur.fetchall()

        except Exception as e:
            self.logger.error(f"DatabaseTools().fetch_all(): {e}", exc_info=True)
            return []

        finally:
            if conn: conn.close()

    def execute_query(self, sql, params=None):
        """Equivalent to ExecuteNonQuery."""
        err = ""
        conn = None
        try:
            conn = psycopg2.connect(**self.connection_config)
            with conn.cursor() as cur:
                cur.execute(sql, params)
            conn.commit()

        except Exception as e:
            if conn:
                conn.rollback()

            err = f"Database Error: {e}"
            self.logger.error(f"DatabaseTools().execute_query(): {e}", exc_info=True)

        finally:
            if conn:
                conn.close()

        return err

    def retrieve_records(self, sql:str, params:tuple=None):
        """Returns a cursor for reading records (use with fetchone/fetchall)."""
        try:
            conn = psycopg2.connect(**self.connection_config)
            cur = conn.cursor()
            cur.execute(sql, params)
            return cur, conn

        except Exception as e:
            self.logger.error(f"DatabaseTools().retrieve_records(): {e}", exc_info=True)
            return None, None
       

        
