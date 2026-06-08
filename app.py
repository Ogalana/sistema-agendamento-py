from flask import Flask, render_template, request, redirect, url_for
import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")
app = Flask(__name__)

def get_db_connection():
    return psycopg2.connect(DATABASE_URL)

TABELA_PRECOS = {
    'Corte de Cabelo': 40.00,
    'Barba': 30.00,
    'Sobrancelha': 15.00,
    'Coloração': 70.00
}

@app.route('/')
def index():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("""
        SELECT id, cliente, servico, horario, valor 
        FROM agendamentos 
        WHERE status = 'Agendado' 
        ORDER BY horario ASC
    """)
    dados = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('index.html', agendamentos=dados)



@app.route('/agendar', methods=['POST'])
def agendar():
    cliente = request.form.get('cliente')
    servico = request.form.get('servico')
    horario = request.form.get('horario')

    valor = TABELA_PRECOS.get(servico, 0.00)

    if cliente and servico and horario:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute(
            'INSERT INTO agendamentos (cliente, servico, horario, valor) VALUES (%s, %s, %s, %s)',
            (cliente, servico, horario, valor)
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
        
        novo_valor = TABELA_PRECOS.get(novo_servico, 0.00)
        
        cur.execute("""
            UPDATE agendamentos 
            SET cliente = %s, servico = %s, horario = %s, valor = %s
            WHERE id = %s
        """, (novo_cliente, novo_servico, novo_horario, novo_valor, id))
        
        conn.commit()
        cur.close()
        conn.close()
        return redirect(url_for('index'))

    cur.execute("SELECT id, cliente, servico, horario FROM agendamentos WHERE id = %s", (id,))
    agendamento = cur.fetchone()
    cur.close()
    conn.close()

    return render_template('editar.html', agendamento=agendamento)



@app.route('/cancelar/<int:id>')
def cancelar(id):
    conn = get_db_connection()
    cur = conn.cursor()
    
    cur.execute("UPDATE agendamentos SET status = 'Cancelado' WHERE id = %s", (id,))

    conn.commit()
    cur.close()
    conn.close()
    
    return redirect(url_for('index'))


@app.route('/pagar/<int:id>')
def pagar(id):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT id, cliente, servico, valor FROM agendamentos WHERE id = %s", (id,))
    agendamento = cur.fetchone()
    cur.close()
    conn.close()
    return render_template('checkout.html', agendamento=agendamento)

@app.route('/processar_pagamento', methods=['POST'])
def processar_pagamento():
    id_agendamento = request.form.get('id')
    forma_pagamento = request.form.get('forma_pagamento')
    
    conn = get_db_connection()
    cur = conn.cursor()
    # Atualiza o status para 'Concluído' e grava como o cliente pagou
    cur.execute("""
        UPDATE agendamentos 
        SET status = 'Concluído', forma_pagamento = %s 
        WHERE id = %s
    """, (forma_pagamento, id_agendamento))
    conn.commit()
    cur.close()
    conn.close()
    return redirect(url_for('index'))


@app.route('/historico')
def historico():
    conn = get_db_connection()
    cur = conn.cursor()
    
    cur.execute("""
        SELECT cliente, servico, horario, valor, status, forma_pagamento 
        FROM agendamentos 
        WHERE status IN ('Concluído', 'Cancelado')
        ORDER BY horario DESC
    """)
    dados_historico = cur.fetchall()
 
    cur.execute("SELECT SUM(valor) FROM agendamentos WHERE status = 'Concluído'")
    total_faturado = cur.fetchone()[0] or 0.00
    
    cur.close()
    conn.close()
    return render_template('historico.html', historico=dados_historico, total=total_faturado)

if __name__ == '__main__':
    app.run(debug=True)