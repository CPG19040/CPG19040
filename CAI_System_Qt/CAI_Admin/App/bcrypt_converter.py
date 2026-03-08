import bcrypt
import psycopg2

# 1. Database Connection Details
DB_CONFIG = {
    "dbname": "DB_CAI",
    "user": "postgres",
    "password": "1234",
    "host": "localhost",
    "port": "5432"
}

def insert_staff_member():
    # 2. Hash the password '1234' using bcrypt 5.0.0
    plain_password = "1234"
    # Convert string to bytes for bcrypt
    password_bytes = plain_password.encode('utf-8')
    # Generate salt and hash (rounds=12 is standard)
    hashed_password = bcrypt.hashpw(password_bytes, bcrypt.gensalt(12))
    # Decode to string to store in PostgreSQL TEXT/VARCHAR column
    storage_hash = hashed_password.decode('utf-8')

    try:
        # 3. Connect to PostgreSQL
        conn = psycopg2.connect(**DB_CONFIG)
        cur = conn.cursor()

        # 4. Define the Insert Query
        # We omit user_id because it defaults to gen_random_uuid()
        insert_query = """
        INSERT INTO cai.tbl_staff_info (
            firstname, middlename, lastname, username, 
            password, position, recovery_question, answer, no
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);
        """
        
        data_to_insert = (
            'Christopher', 'Pilar', 'Gabriel', 'chip1994', 
            storage_hash, 'Admin', 'First Pet?', 'Buddy', None
        )

        # 5. Execute and Commit
        cur.execute(insert_query, data_to_insert)
        conn.commit()
        print("Successfully inserted new staff member with hashed password.")

    except Exception as e:
        print(f"Database error: {e}")
    finally:
        if conn:
            cur.close()
            conn.close()

if __name__ == "__main__":
    insert_staff_member()
