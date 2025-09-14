import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

# Debug: print loaded DB_HOST value
print('DB_HOST:', os.getenv('DB_HOST'))

def get_connection():
    mycon = mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME"),
        port=int(os.getenv("DB_PORT", 3306))
    )
    return mycon

def setup_database(cursor):
    cursor.execute("CREATE DATABASE IF NOT EXISTS railway")
    cursor.execute("USE railway")

    # Railway table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS railway(
            ticket_id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            phno VARCHAR(15) NOT NULL,
            age INT CHECK (age > 0 AND age < 120),
            gender ENUM('MALE','FEMALE','NOT SPECIFIED') NOT NULL,
            from_f VARCHAR(100) NOT NULL,
            to_t VARCHAR(100) NOT NULL,
            date_d DATE NOT NULL,
            CONSTRAINT uq_ticket UNIQUE (phno, date_d, from_f, to_t)
        )
    """)

    # User Accounts table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS user_accounts(
            user_id INT AUTO_INCREMENT PRIMARY KEY,
            fname VARCHAR(100) NOT NULL,
            lname VARCHAR(100) NOT NULL,
            user_name VARCHAR(100) NOT NULL UNIQUE,
            password VARCHAR(255) NOT NULL,
            phno VARCHAR(15) UNIQUE,
            gender ENUM('MALE','FEMALE','NOT SPECIFIED'),
            dob DATE,
            age INT CHECK (age > 0 AND age < 120)
        )
    """)

