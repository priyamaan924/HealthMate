import sqlite3
def create_user_table():

    conn = sqlite3.connect("users.db")
    c = conn.cursor()

    c.execute("""
    CREATE TABLE IF NOT EXISTS users(
        username TEXT,
        password TEXT
    )
    """)

    conn.commit()
    conn.close()


def add_user(username, password):

    conn = sqlite3.connect("users.db")
    c = conn.cursor()

    c.execute("INSERT INTO users VALUES (?,?)",(username,password))

    conn.commit()
    conn.close()


def login_user(username, password):

    conn = sqlite3.connect("users.db")
    c = conn.cursor()

    c.execute(
        "SELECT * FROM users WHERE username=? AND password=?",
        (username,password)
    )

    data = c.fetchall()

    conn.close()

    return data


def create_health_table():

    conn = sqlite3.connect("users.db")
    c = conn.cursor()

    c.execute("""
    CREATE TABLE IF NOT EXISTS health_history(
        username TEXT,
        date TEXT,
        weight REAL,
        bmi REAL,
        health_score INTEGER,
        calories INTEGER
    )
    """)

    conn.commit()
    conn.close()


def save_health_data(username, date, weight, bmi, health_score, calories):

    conn = sqlite3.connect("users.db")
    c = conn.cursor()

    c.execute(
        "INSERT INTO health_history VALUES (?,?,?,?,?,?)",
        (username, date, weight, bmi, health_score, calories)
    )

    conn.commit()
    conn.close()


def get_health_data(username):

    conn = sqlite3.connect("users.db")
    c = conn.cursor()

    c.execute(
        "SELECT date, weight, bmi, health_score, calories FROM health_history WHERE username=?",
        (username,)
    )

    data = c.fetchall()

    conn.close()

    return data



def create_profile_table():

    conn = sqlite3.connect("users.db")
    c = conn.cursor()

    c.execute("""
    CREATE TABLE IF NOT EXISTS profile(
        username TEXT,
        age INTEGER,
        height REAL,
        weight REAL,
        goal TEXT
    )
    """)

    conn.commit()
    conn.close()


def save_profile(username, age, height, weight, goal):

    conn = sqlite3.connect("users.db")
    c = conn.cursor()

    c.execute("DELETE FROM profile WHERE username=?", (username,))

    c.execute(
        "INSERT INTO profile VALUES (?,?,?,?,?)",
        (username, age, height, weight, goal)
    )

    conn.commit()
    conn.close()


def get_profile(username):

    conn = sqlite3.connect("users.db")
    c = conn.cursor()

    c.execute(
        "SELECT age, height, weight, goal FROM profile WHERE username=?",
        (username,)
    )

    data = c.fetchone()

    conn.close()

    return data


def add_sample_data():
    
    conn = sqlite3.connect("users.db")
    c = conn.cursor()

    c.execute(
        "INSERT INTO health_history VALUES (?,?,?,?,?,?)",
        ("testuser","2026-03-10",70,25,70,2200)
    )

    c.execute(
        "INSERT INTO health_history VALUES (?,?,?,?,?,?)",
        ("testuser","2026-03-12",68,24,80,2100)
    )

    conn.commit()
    conn.close()