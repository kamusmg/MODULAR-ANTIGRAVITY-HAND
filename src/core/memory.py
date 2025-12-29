import sqlite3
import datetime
import os
import json

class Hippocampus:
    def __init__(self, db_path="nucleus_memory.db"):
        self.db_path = db_path
        self._init_db()

    def _init_db(self):
        conn = sqlite3.connect(self.db_path)
        c = conn.cursor()
        
        # Sessions: Track each time I wake up
        c.execute('''CREATE TABLE IF NOT EXISTS sessions
                     (id INTEGER PRIMARY KEY AUTOINCREMENT,
                      start_time TEXT,
                      end_time TEXT,
                      notes TEXT)''')
                      
        # Thoughts: Internal log (what I "thinking")
        c.execute('''CREATE TABLE IF NOT EXISTS thoughts
                     (id INTEGER PRIMARY KEY AUTOINCREMENT,
                      session_id INTEGER,
                      timestamp TEXT,
                      content TEXT,
                      context TEXT,
                      FOREIGN KEY(session_id) REFERENCES sessions(id))''')
                      
        # Actions: What I actually DID (clicked, typed, executed)
        c.execute('''CREATE TABLE IF NOT EXISTS actions
                     (id INTEGER PRIMARY KEY AUTOINCREMENT,
                      session_id INTEGER,
                      timestamp TEXT,
                      action_type TEXT,
                      details TEXT,
                      FOREIGN KEY(session_id) REFERENCES sessions(id))''')

        conn.commit()
        conn.close()

    def start_session(self):
        conn = sqlite3.connect(self.db_path)
        c = conn.cursor()
        start = datetime.datetime.now().isoformat()
        c.execute("INSERT INTO sessions (start_time) VALUES (?)", (start,))
        conn.commit()
        session_id = c.lastrowid
        conn.close()
        return session_id

    def remember_thought(self, session_id, content, context="general"):
        conn = sqlite3.connect(self.db_path)
        c = conn.cursor()
        ts = datetime.datetime.now().isoformat()
        c.execute("INSERT INTO thoughts (session_id, timestamp, content, context) VALUES (?, ?, ?, ?)",
                  (session_id, ts, content, context))
        conn.commit()
        conn.close()

    def remember_action(self, session_id, action_type, details):
        conn = sqlite3.connect(self.db_path)
        c = conn.cursor()
        ts = datetime.datetime.now().isoformat()
        if isinstance(details, dict):
            details = json.dumps(details)
        c.execute("INSERT INTO actions (session_id, timestamp, action_type, details) VALUES (?, ?, ?, ?)",
                  (session_id, ts, action_type, details))
        conn.commit()
        conn.close()
        
    def recall_last_thoughts(self, limit=5):
        conn = sqlite3.connect(self.db_path)
        c = conn.cursor()
        c.execute("SELECT content FROM thoughts ORDER BY id DESC LIMIT ?", (limit,))
        rows = c.fetchall()
        conn.close()
        return [r[0] for r in rows][::-1]
