from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re

app = Flask(__name__)

app.secret_key = 'xyzsdfg'

app.config['MYSQL_HOST'] = '182.54.238.164'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'user_system'

mysql = MySQL(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/shopping_home')
def shopping_home():
    return render_template('shopping_home.html')

@app.route('/home')
def index1():
    return render_template('index1.html')

@app.route('/user')
def user():
    return render_template('user.html')

@app.route('/login', methods =['GET', 'POST'])
def login():
    mesage = ''
    if request.method == 'POST' and 'email' in request.form and 'password' in request.form:
        email = request.form['email']
        password = request.form['password']
        print(email, password)
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM user WHERE email = % s AND password = % s', (email, password, ))
        user = cursor.fetchone()
        if user:
            session['loggedin'] = True
            session['userid'] = user['userid']
            session['name'] = user['name']
            session['email'] = user['email']
            mesage = 'Logged in successfully !'
            return render_template('user.html', mesage = mesage)
        else:
            mesage = 'Please enter correct email / password !'
    return render_template('login.html', mesage = mesage)

@app.route('/logout')
def logout():
    session.pop('loggedin', None)
    session.pop('userid', None)
    session.pop('email', None)
    return redirect(url_for('index'))

@app.route('/register', methods =['GET', 'POST'])
def register():
    mesage = ''
    if request.method == 'POST' and 'name' in request.form and 'password' in request.form and 'email' in request.form :
        userName = request.form['name']
        password = request.form['password']
        email = request.form['email']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM user WHERE email = % s', (email, ))
        account = cursor.fetchone()
        if account:
            mesage = 'Account already exists !'
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            mesage = 'Invalid email address !'
        elif not userName or not password or not email:
            mesage = 'Please fill out the form !'
        else:
            cursor.execute('INSERT INTO user VALUES (NULL, % s, % s, % s)', (userName, email, password, ))
            mysql.connection.commit()
            mesage = 'You have successfully registered !'
    elif request.method == 'POST':
        mesage = 'Please fill out the form !'
    return render_template('register.html', mesage = mesage)

@app.route('/selling', methods =['GET', 'POST'])
def seller():
    mesage = ''
    if request.method == 'POST' and 'name' in request.form and 'price' in request.form and 'contact' in request.form\
    and 'img' in request.form:
        proDuctid = request.form['productid']
        nameproduct = request.form['productname']
        priceproduct = request.form['price']
        conTact = request.form['contact']
        imageproduct = request.form['img-url']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM inventory', )
        product = cursor.fetchone()
        if product:
            mesage = 'Product already exists !'
        elif not nameproduct or not priceproduct or not conTact or not imageproduct:
            mesage = 'Please fill out the form !'
        else:
            cursor.execute('INSERT INTO inventory VALUES (NOT NULL, % s, % s, % s, % s)', (proDuctid, nameproduct, priceproduct,
                                                                                           conTact, imageproduct, ))
            mysql.connection.commit()
            mesage = 'You have successfully selling your product !'
    elif request.method == 'POST':
        mesage = 'Please fill out the form !'
    return render_template('seller.html', mesage = mesage)

# @app.route('/test', methods = ['GET'])
# def test():
#     query = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
#     query.execute("SELECT * FROM inventory")
#     result = query.fetchall()
#     return render_template('test.html', mesage = result)

if __name__ == "__main__":
    app.run()
