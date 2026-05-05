
import os
import psycopg2
from psycopg2.extras import RealDictCursor

# Получаем URL из переменных окружения (в Vercel ты добавишь его в настройках проекта)
DATABASE_URL = os.environ.get("DATABASE_URL")

def get_db_connection():
    return psycopg2.connect(DATABASE_URL)

def init_db():
    conn = get_db_connection()
    cur = conn.cursor()
    # Создаем таблицу игроков, если её нет
    cur.execute('''
        CREATE TABLE IF NOT EXISTS players (
            user_id BIGINT PRIMARY KEY,
            username TEXT,
            balance INTEGER DEFAULT 1000,
            status TEXT DEFAULT 'alive'
        )
    ''')
    conn.commit()
    cur.close()
    conn.close()

def add_player(user_id, username):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO players (user_id, username) VALUES (%s, %s) ON CONFLICT (user_id) DO NOTHING",
        (user_id, username)
    )
    conn.commit()
    cur.close()
    conn.close()
