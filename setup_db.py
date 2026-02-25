import sqlite3

conn = sqlite3.connect('database.db')

cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS agendamentos (
                    ID INTEGER PRIMARY KEY AUTOINCREMENT,
                    Cliente TEXT,
                    Servico TEXT,
                    HORARIO TEXT
                )''')

conn.commit()
conn.close()