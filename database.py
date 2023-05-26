import mysql.connector
import sqlite3
import os

class db:

    def __init__(self):
       conn = self.dbcon()
        
    def dbcon(self):
        conn = sqlite3.connect("software.db")
        return conn

    def user(self,conn):
        res = []
        cursor = conn.cursor()
        query = "SELECT username FROM user"
        cursor.execute(query)
        results = cursor.fetchall()
        for result in results:
            print(result[0])
            res.append(result[0])
        user1 = input("Enter the username: ")
        while user1 not in res:
            user1 = input("Username not found. Re-enter username: ")
        sql = "SELECT host, port, username, password, path FROM user WHERE username = ?"
        cursor.execute(sql, (user1,))
        result = cursor.fetchone()
        return result  

    def select(self,conn):
        os.system('cls')
        cursor = conn.cursor()
        query = "SELECT name FROM software"
        cursor.execute(query)
        results = cursor.fetchall()
        for result in results:
            print(result[0])
        cursor.close()
        conn.close()

        folder_path = r"C:\Users\LENOVO\Desktop\teast"

        for filename in os.listdir(folder_path):
            files = os.listdir(folder_path)

        name = input("\n \n Enter the name of the file from the above list: ")
        while True:
            if name in files:
                return name
            name = input("\n \n File not found. Please re-enter: ")      