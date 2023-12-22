import sqlite3

con = sqlite3.connect('bordel.db')

cursor = con.cursor()

cursor.execute('''
                CREATE TABLE IF NOT EXISTS users(
                    id INTEGER PRIMARY KEY,
                    login TEXT NOT NULL,
                    email TEXT NOT NULL,
                    password TEXT NOT NULL
                )''')

cursor.execute('''
                CREATE TABLE IF NOT EXISTS girls(
                    id INTEGER PRIMARY KEY,
                    name TEXT NOT NULL,
                    age INTEGER NOT NULL,
                    size_boobs INTEGER NOT NULL
                )''')

cursor.execute('''
                CREATE TABLE IF NOT EXISTS administration(
                    id INTEGER PRIMARY KEY,
                    name TEXT NOT NULL,
                    login TEXT NOT NULL,
                    password TEXT NOT NULL,
                    email TEXT NOT NULL
                )''')

cursor.execute('''
                CREATE TABLE IF NOT EXISTS security(
                    id INTEGER PRIMARY KEY,
                    name TEXT NOT NULL,
                    surname TEXT NOT NULL,
                    midname TEXT NOT NULL,
                    login TEXT NOT NULL,
                    password TEXT NOT NULL,
                    email TEXT NOT NULL
                )''')