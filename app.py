from flask import Flask, redirect, request, render_template, url_for
from flask_mysqldb import MySQL
import yaml

app = Flask(__name__)

# Database Configuration
db = yaml.load(open('db.yaml'))
app.config['MYSQL_HOST'] = db['mysql_host']
app.config['MYSQL_USER'] = db['mysql_user']
app.config['MYSQL_PASSWORD'] = db['mysql_password']
app.config['MYSQL_DB'] = db['mysql_db']

mysql = MySQL(app)

@app.route('/')

def index():
	return render_template('index.htm')

@app.route('/comments')
def comments():
	return ''

@app.route('/users')
def users():
	return render_template('users.htm')

@app.route('/submit_post')
def submit_post():
	return render_template('submit-post.htm')

@app.route('/login')
def login():
	return render_template('login.htm')

@app.route('/signup', methods=['GET', 'POST'])

def signup():
	if request.method == 'POST':
		# Fetch Form Data
		user_signup = request.form
		user_username = user_signup['user_username']
		user_password = user_signup['user_password']
		cursor = mysql.connection.cursor()
		cursor.execute("INSERT INTO users(user_username, user_password) VALUES(%s, %s)", (user_username, user_password))
		mysql.connection.commit()
		cursor.close()
		return redirect(url_for('index'))
	return render_template('signup.htm');

if __name__ == '__main__':
	app.run(debug=True)
