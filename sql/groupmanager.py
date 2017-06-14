import sqlite3

_conn = None
_c = None

def init(conn):
    c = conn.cursor()
    _conn = conn
    _c = c
    _c.execute('CREATE TABLE IF NOT EXISTS group (id INTEGER AUTO_INCREMENT, name VARCHAR(200))')
    _c.execute('CREATE TABLE IF NOT EXISTS perm (id INTEGER AUTO_INCREMENT, group INTEGER, permname VARCHAR(200), permvalue VARCHAR(200))')

def createGroup(gname):
    _c.execute('INSERT INTO group (name) VALUES (?)', gname)
    return "Group created"

def getAllGroups():
    _c.execute('SELECT * FROM group')
    return _c.fetchall()

def getGroupData(gid):
    _c.execute('SELECT * FROM group WHERE id = ?', gid)
    return _c.fetchone()

def setPerm(gid, permname, permvalue):
    vals = [gid, permname]
    _c.execute('SELECT * FROM perm WHERE group = ? AND permname = ?', vals)
    if _c.fetchone():
        vals = [permvalue, permname, gid]
        _c.execute('UPDATE perm SET permvalue = ? WHERE permname = ? AND group = ?', vals)
    else:
        vals = [gid, permname, permvalue]
        _c.execute('INSERT INTO perm (group, permname, permvalue) VALUES (?, ?, ?)', vals)
    return "Updated group permission"

def delPerm(permid):
    _c.execute('DELETE FROM perm WHERE permid = ?', permid)
    return "Deleted permission"