#!/usr/bin/python3
import MySQLdb

def create_database():
    try:
        MyDB = MySQLdb.connect(
            host="localhost",
            user="root",
            passwd="@Abdo.01283908329abdo",
        )

        cursor = MyDB.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store ")
        MyDB.commit()
        
        print("Database 'alx_book_store' created successfully!")
        
    except MySQLdb.Error as e:
        print(f"Error: {e}")
        
    finally:
        cursor.close()
        MyDB.close()
        
if __name__ == "__main__":
    create_database()
