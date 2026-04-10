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
    cur.execute("SELECT id, cliente, servico, horario FROM agendamentos ORDER BY horario ASC")
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


@app.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar(id):
    conn = get_db_connection()
    cur = conn.cursor()

    if request.method == 'POST':
        novo_cliente = request.form['cliente']
        novo_servico = request.form['servico']
        novo_horario = request.form['horario']

        cur.execute("""
            UPDATE agendamentos 
            SET cliente = %s, servico = %s, horario = %s 
            WHERE id = %s
        """, (novo_cliente, novo_servico, novo_horario, id))
        
        conn.commit()
        cur.close()
        conn.close()
        return redirect(url_for('index'))

    cur.execute("SELECT id, cliente, servico, horario FROM agendamentos WHERE id = %s", (id,))
    agendamento = cur.fetchone()
    cur.close()
    conn.close()

    return render_template('editar.html', agendamento=agendamento)

if __name__ == '__main__':
    app.run(debug=True)