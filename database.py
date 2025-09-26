import sqlite3

connect = sqlite3.connect ('database.db')
connect.execute("PRAGMA foreign_keys = ON;")
cursor = connect.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS tournaments (
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                name VARCHAR(50) NOT NULL,
                format VARCHAR(50),
                created_by varchar(50)
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS players (
                osu_id INTEGER NOT NULL PRIMARY KEY,
                discord_id VARCHAR(50),
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
               )
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS player_registrations (
                player_id INTEGER NOT NULL,
                tournament_id INTEGER NOT NULL,
                status VARCHAR(20) DEFAULT 'pending',
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
               
                FOREIGN KEY (tournament_id) REFERENCES tournaments (id),
                FOREIGN KEY (player_id) REFERENCES players (osu_id),
                PRIMARY KEY (tournament_id, player_id)
                )
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS teams (
                tournament_id INTEGER NOT NULL,
                team_name VARCHAR(50) NOT NULL,
                created_by varchar(50),
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

                FOREIGN KEY (tournament_id) REFERENCES tournaments (id),
                PRIMARY KEY (tournament_id, team_name)
                )
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS team_members (
                tournament_id INTEGER NOT NULL,
                team_name VARCHAR(50) NOT NULL,
                player_id INTEGER NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                role varchar(20) DEFAULT 'member',

                PRIMARY KEY (tournament_id, team_name, player_id),
                FOREIGN KEY (player_id) REFERENCES players (osu_id),
                CONSTRAINT fk_teams FOREIGN KEY (tournament_id, team_name) REFERENCES teams (tournament_id, team_name)
                )
''')

cursor.execute('''
            CREATE TRIGGER trigger_players_updated_at
            AFTER UPDATE ON players
            FOR EACH ROW            
            WHEN NEW.updated_at = OLD.updated_at
            BEGIN
                UPDATE players
                SET updated_at = CURRENT_TIMESTAMP
                WHERE rowid = OLD.rowid;
            END;             
''')

cursor.execute('''
            CREATE TRIGGER trigger_player_registrations_updated_at
            AFTER UPDATE ON player_registrations
            FOR EACH ROW
            WHEN NEW.updated_at = OLD.updated_at
            BEGIN
                UPDATE player_registrations
                SET updated_at = CURRENT_TIMESTAMP
                WHERE rowid = OLD.rowid;
            END;             
''')

cursor.execute('''
            CREATE TRIGGER trigger_teams_updated_at
            AFTER UPDATE ON teams
            FOR EACH ROW
            WHEN NEW.updated_at = OLD.updated_at
            BEGIN
                UPDATE teams
                SET updated_at = CURRENT_TIMESTAMP
                WHERE rowid = OLD.rowid;
            END;             
''')

cursor.execute('''
            CREATE TRIGGER trigger_team_members_updated_at
            AFTER UPDATE ON team_members
            FOR EACH ROW
            WHEN NEW.updated_at = OLD.updated_at
            BEGIN
                UPDATE team_members
                SET updated_at = CURRENT_TIMESTAMP
                WHERE rowid = OLD.rowid;
            END;             
''')

connect.commit()

connect.close()

print("Database created.")
