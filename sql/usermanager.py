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
    _c.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER AUTO_INCREMENT, pass VARCHAR(200), uname VARCHAR(200), group INTEGER)')

def loadUsers():
    _c.execute('SELECT * FROM users')
    ret = _c.fetchone()

def getUserData():
    _c.execute('SELECT id, uname, group FROM users')
    return _c.fetchall()

def getUserData(uname):
    _c.execute('SELECT id, uname, group FROM users WHERE uname = "?"', uname)
    return _c.fetchone()

def addUser(uname, upass, group):
    group = int(group)
    hpass = hashpass(upass)
    vals = [uname, hpass, group]
    _c.execute('INSERT INTO users (uname, pass, group) VALUES (?, ?, ?)', vals)
    return "User added"

def updateUserGroup(uname, group):
    group = int(group)
    vals = [uname, group]
    _c.execute('UPDATE user SET group = ? WHERE uname = ?', vals)
    return "Set user " + uname + " to group " + group

def updateUserPass(uname, upass):
    hpass = hashpass(upass)
    vals = [uname, hpass]
    _c.execute('UPDATE user SET pass = ? WHERE uname = ?', vals)
    return "Password updated"

def resetUserPass(uname):
    upass = genpass()
    hpass = hashpass(upass)
    vals = [uname, hpass]
    _c.execute('UPDATE user SET pass = ? WHERE uname = ?', vals)
    return upass

def verif(uname, upass):
    hpass = hashpass(upass)
    _c.execute('SELECT pass FROM users WHERE uname = "?"', uname)
    retpass = _c.fetchone()
    return retpass == hpass

def hashpass(upass):
    m = hashlib.sha256()
    m.update(upass)
    return m.hexdigest()

def genpass():
    upass = ''
    for i in range(10):
        upass += random.choice(string.ascii_letters)
    return upass