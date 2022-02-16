from flask import Flask, jsonify, request, render_template, make_response
import json
import random
from values import *
from search import *
from add_logindb import *
from check_db import *
import sys

chars = '+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'

app = Flask(__name__)
    
@app.route('/search/<string:s>', methods=['GET', 'POST'])
def search_handler(s):
    print('searching. . .')
    if request.method == 'GET':
        print('searching. . .')
        message = {'info':search(s)}
        response = jsonify(message)
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
    if request.method == 'POST':
        print(request.get_json())
        return 'Sucesss', 200

@app.route('/log/setcookie', methods = ['POST'])
def setcookie_log():
   if request.method == 'POST':
       req = request
       name = req.form['login']
       password = req.form['password']
       resp = make_response(render_template('perep.html'))
       if check_login(name, password):
           print('TRUUUUUUE')
           resp.set_cookie('name', value=name)
       return resp

@app.route('/reg/setcookie', methods = ['POST'])
def setcookie_reg():
   if request.method == 'POST':
       req = request
       name = req.form['login']
       password = req.form['password']
       resp = make_response(render_template('perep.html'))
       if add_login(name, password):
            resp.set_cookie('name', value=name)
       else:
           resp = 'Логин занят'
       return resp

@app.route('/<string:s>')
def prime(s):
    if s!='account':
        if s in html:
            return render_template(html[s])
        return render_template('perep.html')
    if request.cookies.get('name')!=None:
        name = request.cookies.get('name')
        return render_template(html[s], name=name)
    return render_template(html['login'])

@app.route('/')
def empty():
    return render_template('perep.html')

@app.route('/stop/stop')
def stop():
    sys.exit()

app.debug = True
app.run('0.0.0.0', port=80)
