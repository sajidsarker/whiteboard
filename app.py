from flask import Flask, redirect, request, render_template, url_for, session
from flask_mysqldb import MySQL
import os
import yaml

app = Flask(__name__)

# Database Configuration
db = yaml.load(open('db.yaml'))
app.config['MYSQL_HOST'] = db['mysql_host']
app.config['MYSQL_USER'] = db['mysql_user']
app.config['MYSQL_PASSWORD'] = db['mysql_password']
app.config['MYSQL_DB'] = db['mysql_db']
app.config['SECRET_KEY'] = os.urandom(24)

mysql = MySQL(app)

@app.route('/')
def index():
	return render_template('index.htm')

@app.route('/comments')
def comments():
	return render_template('comments.htm')

@app.route('/u')
def u():
	cursor = mysql.connection.cursor()
	output = cursor.execute('SELECT * FROM users')
	if output > 0:
		users = cursor.fetchall()
		return render_template('users.htm', users=users)
	return render_template('users.htm')

@app.route('/submit_post')
def submit_post():
	return render_template('submit-post.htm')

@app.route('/login', methods=['GET', 'POST'])
def login():
	if 'username' in session:
		return redirect(url_for('index'))

	if request.method == 'POST':
		# Fetch Form Data
		user_login = request.form
		user_username = user_login['user_username']
		user_password = user_login['user_password']
		cursor = mysql.connection.cursor()
		cursor.execute('SELECT * FROM users WHERE user_username="' + user_username + '" and user_password="' + user_password + '"')
		authentication = cursor.fetchone()
		cursor.close()
		if authentication is None:
			return 'Username or Password is invalid.'
		else:
			session['logged_in'] = True
			session['username'] = user_username
			return redirect(url_for('index'))
	return render_template('login.htm')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
	if 'username' in session:
		return redirect(url_for('index'))

	if request.method == 'POST':
		# Fetch Form Data
		user_signup = request.form
		user_username = user_signup['user_username']
		user_password = user_signup['user_password']
		cursor = mysql.connection.cursor()
		cursor.execute('SELECT * FROM users WHERE user_username="' + user_username + '"')
		authentication = cursor.fetchone()
		if authentication is None:
			cursor.execute("INSERT INTO users(user_username, user_password) VALUES(%s, %s)", (user_username, user_password))
			mysql.connection.commit()
			cursor.close()
			session['logged_in'] = True
			session['username'] = user_username
			return redirect(url_for('index'))
		else:
			cursor.close()
			return 'Username already exists.'
	return render_template('signup.htm');

@app.route('/u/profile')
def profile():
	return render_template('profile.htm')

@app.route('/logout')
def logout():
	session['logged_in'] = False
	session.pop('username', None)
	return redirect(url_for('index'))

if __name__ == '__main__':
	app.run(debug=True)
