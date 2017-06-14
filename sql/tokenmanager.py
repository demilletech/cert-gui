import sqlite3

import usermanager

_conn = None
_c = None

def init(conn):
    c = conn.cursor()
    _conn = conn
    _c = c
    _c.execute('CREATE TABLE IF NOT EXISTS token (id INTEGER AUTO_INCREMENT, userid INTEGER, token VARCHAR(200), valid BOOLEAN DEFAULT TRUE)')

def createToken(uid):
    token = usermanager.hashpass(usermanager.genpass())
    vals = [uid, token]
    _c.execute('INSERT INTO token (userid, token) VALUES (?, ?)', vals)
    return token

def getUserToken(uid):
    _c.execute('SELECT * FROM token WHERE userid = ?', uid)
    return _c.fetchall()

def invalidateToken(tid):
    _c.execute('UPDATE token SET valid = FALSE WHERE id = ?', tid)
    return "Token invalidated"

def getGroupData(gid):
    _c.execute('SELECT * FROM group WHERE id = ?', gid)
    return _c.fetchone()