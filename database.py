import streamlit as st
import sqlite3
import hashlib

def hash_password(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()

def create_user_table():
    conn = sqlite3.connect("users.db")
    c = conn.cursor()

    c.execute("""
    CREATE TABLE IF NOT EXISTS users(
        username TEXT PRIMARY KEY,
        password TEXT
    )
    """)

    conn.commit()
    conn.close()


def add_user(username, password):
    conn = sqlite3.connect("users.db")
    c = conn.cursor()

    try:
        c.execute(
            "INSERT INTO users VALUES (?,?)",
            (username, hash_password(password))
        )
        conn.commit()
        return True
    except:
        return False
    finally:
        conn.close()


def login_user(username, password):
    conn = sqlite3.connect("users.db")
    c = conn.cursor()

    c.execute(
        "SELECT * FROM users WHERE username=? AND password=?",
        (username, hash_password(password))
    )

    data = c.fetchone()
    conn.close()

    return data is not None


# -------------------------
# HEALTH DATA
# -------------------------
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


# -------------------------
# PROFILE
# -------------------------
def create_profile_table():
    conn = sqlite3.connect("users.db")
    c = conn.cursor()

    c.execute("""
    CREATE TABLE IF NOT EXISTS profile(
        username TEXT,
        age INTEGER,
        height REAL,
        weight REAL,
        goal TEXT,
        target_weight REAL
    )
    """)

    conn.commit()
    conn.close()


def save_profile(username, age, height, weight, goal, target_weight):
    conn = sqlite3.connect("users.db")
    c = conn.cursor()

    c.execute("DELETE FROM profile WHERE username=?", (username,))

    c.execute(
        "INSERT INTO profile VALUES (?,?,?,?,?,?)",
        (username, age, height, weight, goal, target_weight)
    )

    conn.commit()
    conn.close()


def get_profile(username):
    conn = sqlite3.connect("users.db")
    c = conn.cursor()

    c.execute(
        "SELECT age, height, weight, goal, target_weight FROM profile WHERE username=?",
        (username,)
    )

    data = c.fetchone()
    conn.close()
    return data


# -------------------------
# HABIT TRACKER
# -------------------------
def create_habit_table():
    conn = sqlite3.connect("users.db")
    c = conn.cursor()

    c.execute("""
    CREATE TABLE IF NOT EXISTS habits(
        username TEXT,
        date TEXT,
        water REAL,
        sleep REAL,
        steps INTEGER
    )
    """)

    conn.commit()
    conn.close()


def save_habit(username, date, water, sleep, steps):
    conn = sqlite3.connect("users.db")
    c = conn.cursor()

    c.execute(
        "INSERT INTO habits VALUES (?,?,?,?,?)",
        (username, date, water, sleep, steps)
    )

    conn.commit()
    conn.close()


def get_habits(username):
    conn = sqlite3.connect("users.db")
    c = conn.cursor()

    c.execute(
        "SELECT date, water, sleep, steps FROM habits WHERE username=?",
        (username,)
    )

    data = c.fetchall()
    conn.close()
    return data