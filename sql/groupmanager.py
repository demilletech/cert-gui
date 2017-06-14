import sqlite3
import hashlib
import random
import string

_conn = None
_c = None

def init(conn):
    c = conn.cursor()
    _conn = conn
    _c = c
    _c.execute('CREATE TABLE IF NOT EXISTS group (id INTEGER AUTO_INCREMENT, name VARCHAR(200))')