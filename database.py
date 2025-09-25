import sqlite3

connect = sqlite3.connect ('tournaments.db')

cursor = connect.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS tournaments (
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               name TEXT NOT NULL,
               format TEXT NOT NULL,
               created_at TEXT NOT NULL
               )
               ''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS player_registrations (
               player_id INTEGER PRIMARY KEY AUTOINCREMENT,
               tournament_id INTEGER,
               registered_at TEXT NOT NULL,
               status TEXT NOT NULL,
               screening_status TEXT NOT NULL,
               FOREIGN KEY (tournament_id) REFERENCES tournaments (id)
               )
''')

connect.commit()

connect.close()

print("Database "'tournaments.db'" created.")
