import sqlite3
import random
import queue

c = None
conn = None

dbName = "notes.db"

def create_table():
    conn = sqlite3.connect(dbName)
    c = conn.cursor()

    c.execute('''CREATE TABLE IF NOT EXISTS notes
                (id PRIMARY KEY,thread, content , channel )''')
    conn.commit()
    conn.close()


def delete_note(id):
    conn = sqlite3.connect(dbName)
    c = conn.cursor()
    c.execute("DELETE FROM notes WHERE id =?",(id,))  
    
    conn.commit()
    conn.close()



def get_notes(thread):
    conn = sqlite3.connect(dbName)
    c = conn.cursor()

    c.execute("SELECT * FROM notes WHERE  thread = ?",(thread,))
    res = c.fetchall()    
    l = []
    for t in res:
        l.append(dict(zip(["id", "thread", "content", "channel"], t)))

    return l

  
    
def add_note(thread, channel, content):
    conn = sqlite3.connect(dbName)
    c = conn.cursor()
    c.execute("INSERT INTO notes VALUES (?, ?, ?, ?)", (str(random.randint(0,9999999999)),str(thread), str(channel), str(content) ))
    conn.commit()
    conn.close()





