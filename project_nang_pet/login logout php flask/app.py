from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_mysqldb import MySQL
import MySQLdb.cursors
import mysql.connector
import re

app = Flask(__name__)

app.secret_key = 'xyzsdfg'
app.config['MYSQL_HOST'] = '182.54.238.164'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'user_system'

mysql = MySQL(app)

# หน้าหลักของเว็บไซต์ #
@app.route('/')
def index():
    return render_template('index.html')

# หน้าหลักเมื่อล็อคอินเข้าระบบสำเร็จ #
@app.route('/index1')
def index1():
    return render_template('index1.html')

# หน้าสินค้า #
@app.route('/keyboard')
def keyboard():
    return render_template('keyboard.html')

# หน้าสินค้า #
@app.route('/console')
def console():
    return render_template('console.html')

# หน้าสินค้า #
@app.route('/cpu')
def cpu():
    return render_template('cpu.html')

# หน้าสินค้า #
@app.route('/Tv')
def Tv():
    return render_template('Tv.html')

# หน้าสินค้า #
@app.route('/nootebook')
def nootebook():
    return render_template('nootebook.html')

# หน้าสินค้า #
@app.route('/Apple')
def Apple():
    return render_template('Apple.html')

# หน้าสินค้า #
@app.route('/speaker_1')
def speaker_1():
    return render_template('speaker_1.html')

# หน้าสินค้า #
@app.route('/speaker_2')
def speaker_2():
    return render_template('speaker_2.html')

# หน้าสินค้า #
@app.route('/ram')
def ram():
    return render_template('ram.html')

# หน้าสินค้า #
@app.route('/mousehy')
def mousehy():
    return render_template('mousehy.html')

# หน้าสินค้า #
@app.route('/mouseoni')
def mouseoni():
    return render_template('mouseoni.html')

# หน้าสินค้า #
@app.route('/router')
def router():
    return render_template('router.html')

# หน้าแสดงรายละเอียดสินค้าที่เพิ่มสินค้าลง Database #
@app.route('/product/<string:item_id>')
def product(item_id):
    print(item_id)
    query = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    query.execute("SELECT * FROM inventory WHERE productid =  {}".format(item_id))
    result = query.fetchall()
    return render_template('product.html', item = result[0], itemname = item_id)

# หน้า Category #
@app.route('/shopping_home')
def shopping_home():
    query = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    query.execute('SELECT * FROM inventory')
    result = query.fetchall()
    print("id =", result[0])
    return render_template('shopping_home.html', products = result)

# หน้า Category สินค้าแบบแยกตามประเภทสินค้า #
@app.route('/shopping_1')
def shopping_1():
    return render_template('shopping_1.html')

# หน้า Category สินค้าแบบแยกตามประเภทสินค้า #
@app.route('/shopping_2')
def shopping_2():
    return render_template('shopping_2.html')

# หน้า Category สินค้าแบบแยกตามประเภทสินค้า #
@app.route('/shopping_3')
def shopping_3():
    return render_template('shopping_3.html')

# หน้า Category สินค้าแบบแยกตามประเภทสินค้า #
@app.route('/shopping_4')
def shopping_4():
    return render_template('shopping_4.html')

# หน้า User Profile #
@app.route('/user')
def user():
    return render_template('user.html')

# หน้า Login เข้าบัญชี #
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

# ระบบ Logout #
@app.route('/logout')
def logout():
    session.pop('loggedin', None)
    session.pop('userid', None)
    session.pop('email', None)
    return redirect(url_for('index'))

# หน้าต่างสมัครสมาชิกเว็บไซต์ #
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
        elif password == userName:
            mesage = 'Please fill out the form !'
        elif len(password) < 8:
            mesage = 'Please fill you password more than 8 letters !'
        else:
            cursor.execute('INSERT INTO user VALUES (NULL, % s, % s, % s)', (userName, email, password, ))
            mysql.connection.commit()
            mesage = 'You have successfully registered !'
    elif request.method == 'POST':
        mesage = 'Please fill out the form !'
    return render_template('register.html', mesage = mesage)

# หน้าขายสินค้าลงบนหน้าเว็บ (เก็บข้อมูลลง Database) #
@app.route('/selling', methods =['GET', 'POST'])
def seller():
    noti = ''
    if request.method == 'POST' and 'name' in request.form and 'price' in request.form and 'contact' in request.form\
    and 'img' in request.form:
        nameproduct = request.form['name']
        priceproduct = request.form['price']
        conTact = request.form['contact']
        imageproduct = request.form['img']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM inventory WHERE name = "name"' )
        product = cursor.fetchone()
        if product:
            noti = 'Product already exists !'
        elif not nameproduct or not priceproduct or not conTact or not imageproduct:
            noti = 'Please fill out the form !'
        else:
            cursor.execute('INSERT INTO inventory VALUES (NULL, % s, % s, % s, % s)', (nameproduct, priceproduct,
                                                                                           conTact, imageproduct, ))
            mysql.connection.commit()
            noti = 'You have successfully selling your product !'
    return render_template('seller.html', mesage = noti)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=False, port=8082)
