import sqlite3
import random
from config import DATABASE

def problem_generator_lvl1(): 
    first = random.randint(0, 999)
    second = random.randint(0, 999)
    saying = (str(first), '+', str(second), '=', '?')
    answer = first + second
    return saying, answer

class DB_Manager:
    def __init__(self, database):
        self.database = database
        
    def create_tables(self):
        conn = sqlite3.connect(self.database)
        with conn:
            conn.execute('''CREATE TABLE IF NOT EXISTS score (
                        user_id INTEGER PRIMARY KEY,
                        user_name TEXT
                        points INTEGER
                        )''') 

            conn.commit()

    def __executemany(self, sql, data):
        conn = sqlite3.connect(self.database)
        with conn:
            conn.executemany(sql, data)
            conn.commit()
    
    def __select_data(self, sql, data = tuple()):
        conn = sqlite3.connect(self.database)
        with conn:
            cur = conn.cursor()
            cur.execute(sql, data)
            return cur.fetchall()
            
