# -*- coding: utf-8 -*-
import sqlite3

class UsersModel():
    def __init__(self, connection):
        self.connection = connection
        
    def init_table(self):
        cursor = self.connection.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS users 
                            (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                             username VARCHAR(50),
                             name VARCHAR(50),
                             surname VARCHAR(50),
                             status VARCHAR(50),
                             password_hash VARCHAR(250),
                             photo_url VARCHAR(500))''')
        cursor.close()
        self.connection.commit()
     
    def insert(self, username, name, surname, password_hash):
        cursor = self.connection.cursor()
        status = ''
        photo_url = 'data:image/png;base64,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'
        cursor.execute('''INSERT INTO users 
                          (username, name, surname, status, password_hash, photo_url) 
                          VALUES (?,?,?,?,?,?)''', (username, name, surname, status, password_hash, photo_url))
        cursor.close()
        self.connection.commit()     
       
    def update_status(self, status, user_id):
        cursor = self.connection.cursor()
        cursor.execute('''UPDATE users 
                          SET status = ? 
                          WHERE id = ?''', (status, user_id,))
        cursor.close()
        self.connection.commit()
        
    def update_photo(self, url, user_id):
        cursor = self.connection.cursor()
        cursor.execute('''UPDATE users 
                          SET photo_url = ? 
                          WHERE id = ?''', (url, user_id,))
        cursor.close()
        self.connection.commit()        
        
    def exists(self, username, password_hash):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM users WHERE username = ? AND password_hash = ?", (username, password_hash))
        row = cursor.fetchone()
        return (True, row[0]) if row else (False,)
    
    def password_check(self, username):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM users WHERE username = ?", (username, ))
        row = cursor.fetchone()
        return row[5]
    
    def get(self, user_id):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM users WHERE id = ?", (str(user_id),))
        row = cursor.fetchone()
        return row
    
    def get_all(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM users")
        rows = cursor.fetchall()
        return rows    