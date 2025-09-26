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

def edit_tournament(tournament_id, name=None, format=None):
    connect = connect_db();
    cursor = connect.cursor();
    if name: 
        cursor.execute('''
        UPDATE tournaments SET name = ? WHERE id = ?
                       ''', (name, tournament_id))
    
    if format: 
        cursor.execute('''
        UPDATE tournaments SET format = ? WHERE id = ?
                       ''', (format, tournament_id))
    connect.commit()
    connect.close()
    print (f"Tournament {name} (ID: {tournament_id}) updated.") 

def delete_tournament(tournament_id):
    connect = connect_db()
    cursor = connect.cursor()
    cursor.execute('''
    DELETE FROM tournaments WHERE id = ?
                   ''', (tournament_id))
    connect.commit()
    connect.close()
    print(f"Tournament {name} (ID {tournament_id}) deleted.")