import sqlite3

import usermanager

def init():
    load_user_db()

def load_user_db():
    conn = sqlite3.connect('users.db')
    usermanager.init(conn)