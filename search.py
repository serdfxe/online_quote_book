import sqlite3
from sqlite3 import Error
from values import *

def search(s):
    connection = sqlite3.connect(path_to_data, check_same_thread=False)
    cursor = connection.cursor()
    
    mes = set()
    message = []
    
    #поиск по name
    cursor.execute("""SELECT ID FROM cat WHERE catname LIKE '%s'""" % f'%{s}%')
    nameID_rec = cursor.fetchall()

    for i in nameID_rec:
        cursor.execute("""SELECT ID FROM deals WHERE catID = '%s'""" % i)
        for ii in cursor.fetchall():
            mes.add(ii)

    #поис по body
    cursor.execute("""SELECT ID FROM deals WHERE body LIKE '%s'""" % f'%{s}%')
    dealsID_rec = cursor.fetchall()

    mes = mes.union(dealsID_rec)
    
    for cit_id in mes:
        cursor.execute("""SELECT body, catID, ID FROM deals WHERE ID='%s'""" % cit_id)
        rec = cursor.fetchone()
        body = rec[0]
        nameID = rec[1]
        citID = rec[2]

        cursor.execute("""SELECT catname FROM cat WHERE ID = '%s'""" % nameID)
        name = cursor.fetchone()
        
        message.append({'body':body,'name':name[0], 'num':citID})

    cursor.close()
    connection.close()
    
    return str(message)
