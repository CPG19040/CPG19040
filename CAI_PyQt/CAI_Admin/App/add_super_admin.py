import os, bcrypt, psycopg2

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
    plain_password = "admin123"
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
        
        script_dir = os.path.dirname(os.path.abspath(__file__))
        image_path = os.path.join(script_dir, "..", "Images", "admin.png")
        binaryImage = None

        with open(image_path, 'rb') as file:
            binaryImage = file.read()

        # 4. Define the Insert Query
        # We omit user_id because it defaults to gen_random_uuid()
        insert_query = """
            INSERT INTO cai.tbl_staff_info (
                school_id,
                firstname,
                lastname,
                username, 
                password, 
                positionid,
                profile_pic
            ) 
            VALUES (
                to_char(CURRENT_DATE, 'YYYY') || '-' || lpad(nextval('cai.staff_id_seq')::text, 4, '0') || '-STA',
                %s, %s, %s, %s, %s, %s
            );
        """
        data_to_insert = ('Admin', 'User', 'chip1994', storage_hash, '1', 
                          psycopg2.Binary(binaryImage) if binaryImage else None)

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
