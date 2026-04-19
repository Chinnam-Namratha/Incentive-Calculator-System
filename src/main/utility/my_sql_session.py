from __future__ import annotations
import mysql.connector
from mysql.connector import Error
from resources.dev import config

def get_mysql_connection():
    try:
        connection = mysql.connector.connect(
            host=config.host,
            user=config.user,
            password=config.password,
            database=config.database,
            port=3306  # Explicitly add port (default is 3306)
        )
        print("MySQL connection successful!")
        return connection
    except Error as e:
        print("MySQL Connection Error: {}".format(e))  # Python 3.6-style string format
        return None

# Test the connection
if __name__ == "__main__":
    conn = get_mysql_connection()
    if conn:
        conn.close()  # Always close the connection