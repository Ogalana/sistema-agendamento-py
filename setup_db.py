import psycopg2
import os
from dotenv import load_dotenv
from pathlib import Path

# Força a busca pelo .env na pasta onde o script está
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

DB_URL = os.getenv("DATABASE_URL")

# --- BLOCO DE DIAGNÓSTICO (Sem caracteres especiais) ---
print("--- Verificacao de Ambiente ---")
if os.path.exists('.env'):
    print("[OK] Arquivo .env encontrado na pasta.")
else:
    print("[ERRO] Arquivo .env NAO encontrado nesta pasta!")

if DB_URL:
    # Mostra apenas o início para conferência
    print(f"[OK] Variavel carregada: {DB_URL[:20]}...") 
else:
    print("[ERRO] A variavel DATABASE_URL esta vazia ou nao foi lida!")
print("-------------------------------\n")

def setup():
    if not DB_URL:
        return

    conn = None
    try:
        print("Tentando conectar ao Supabase...")
        conn = psycopg2.connect(DB_URL)
        cursor = conn.cursor()

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS agendamentos (
                id SERIAL PRIMARY KEY,
                cliente TEXT NOT NULL,
                servico TEXT NOT NULL,
                horario TIMESTAMP NOT NULL
            );
        ''')

        conn.commit()
        print("SUCESSO: Tabela criada no Supabase!")
        
    except Exception as e:
        # Usamos repr(e) para evitar caracteres especiais na mensagem de erro
        print(f"ERRO de Conexao: {repr(e)}")
    finally:
        if conn:
            conn.close()

if __name__ == "__main__":
    setup()