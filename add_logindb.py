import sqlite3
from sqlite3 import Error
from values import *

def add_login(name, password):
    connection = sqlite3.connect(path_to_login, check_same_thread=False)
    cursor = connection.cursor()
    cursor.execute("""SELECT userid FROM users WHERE name='%s'""" % name)
    if cursor.fetchall()==[]:
        cursor.execute('''SELECT userid FROM users''')
        lastid = cursor.fetchall()[-1][0]+1
        cursor.execute("""INSERT INTO users(userid, name, password) VALUES(?,?,?);""", (lastid, name, password))
        connection.commit()
        cursor.close()
        connection.close()
        return True
    cursor.close()
    connection.close()
    return False

    
