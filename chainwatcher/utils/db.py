import sys
import os
import time
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import sqlite3
import os
import time

DB_PATH = "chainwatcher.db"

def init_db():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS block_data (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            block_number INTEGER,
            timestamp INTEGER,
            latency REAL,
            success BOOLEAN
        )
    ''')
    conn.commit()
    conn.close()

def insert_block_data(block_number, timestamp, latency, success):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('''
        INSERT INTO block_data (block_number, timestamp, latency, success)
        VALUES (?, ?, ?, ?)
    ''', (block_number, timestamp, latency, success))
    conn.commit()
    conn.close()

def save_block_data(block_number, latency, success=True):
    timestamp = int(time.time())
    insert_block_data(block_number, timestamp, latency, success)
