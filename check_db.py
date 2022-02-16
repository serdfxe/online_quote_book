import sqlite3
from sqlite3 import Error
from values import *

def check_login(name, password):
    connection = sqlite3.connect(path_to_login, check_same_thread=False)
    cursor = connection.cursor()
    
    cursor.execute("""SELECT password FROM users WHERE name = '%s'""" % name)
    pas = cursor.fetchone()[0]
    
    cursor.close()
    connection.close()
    
    return pas == password
