import sqlite3

def create_database():
    conn = sqlite3.connect('my_database.db')

    cursor = conn.cursor()

    cursor.execute('''CREATE TABLE users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL,
        password TEXT NOT NULL,
        age INTEGER NOT NULL
    )''')

    conn.commit()
    conn.close()

try:
    create_database()
except:
    True



def add_elemet( email,password,age):
    conn = sqlite3.connect('my_database.db')
    c = conn.cursor()
    c.execute("INSERT INTO users ( username, password,age) VALUES ( ?, ?,?)", ( email, password,age))
    conn.commit()
    conn.close()


def view_all():
    conn = sqlite3.connect('my_database.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM users")
    rows = cursor.fetchall()
    
    conn.close()
    return rows


def check_exist(email,password):
    conn = sqlite3.connect("my_database.db")
    cursor = conn.cursor()

    select_query = "SELECT * FROM users WHERE username = ? and password = ?"
    cursor.execute(select_query, (email,password))
    row= cursor.fetchone()
    if row is not None:
        return row
    else:
        False
    conn.close()




