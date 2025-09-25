import sqlite3

connect = sqlite3.connect ('database.db')

cursor = connect.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS tournaments (
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               name VARCHAR(50) NOT NULL,
               created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
               )
               ''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS player_registrations (
               osu_id INTEGER PRIMARY KEY AUTOINCREMENT,
               tournament_id INTEGER,
               registered_at TIMESTAMP NOT NULL,
               status VARCHAR(20) NOT NULL,
               FOREIGN KEY (tournament_id) REFERENCES tournaments (id)
               )
''')

connect.commit()

connect.close()

print("Database created.")
