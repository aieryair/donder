import sqlite3

def connect_db():
    return sqlite3.connect('database.db')

def create_tournament(name, format):
    connect = connect_db();
    cursor = connect.cursor();
    cursor.execute('SELECT * FROM tournaments')
    tournaments = cursor.fetchall()
    connect.close()
    print(f"Tournament '{name}' created.")