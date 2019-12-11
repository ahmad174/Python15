# Fifteenth Day Exercise
from flask import *
import sqlite3 as sql

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
	return render_template('index.html')

@app.route('/profile', methods = ['post'])
def profile():
	name = request.form['name']
	age = request.form['age']
	address = request.form['address']
	nationality = request.form['nationality']
	
	return render_template('profile.html', name = name, age = age, address = address, nationality = nationality)
#==============================================================================
DATABASE = 'stocks.db'
@app.route('/data')
def students():
	with sql.connect(DATABASE) as con:
		cur = con.cursor()
		
	data = cur.execute('select * from stocks')
	return render_template('data.html', data = data)


if __name__ == '__main__':
	app.run()
