from flask import Flask, render_template, request, redirect, url_for
import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")
app = Flask(__name__)

def get_db_connection():
    return psycopg2.connect(DATABASE_URL)


@app.route('/')
def index():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT cliente, servico, horario FROM agendamentos ORDER BY id DESC;')
    dados = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('index.html', agendamentos=dados)



@app.route('/agendar', methods=['POST'])
def agendar():
    cliente = request.form.get('cliente')
    servico = request.form.get('servico')
    horario = request.form.get('horario')

    if cliente and servico and horario:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute(
            'INSERT INTO agendamentos (cliente, servico, horario) VALUES (%s, %s, %s)',
            (cliente, servico, horario)
        )
        conn.commit()
        cur.close()
        conn.close()

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)