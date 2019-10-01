from flask import Flask, render_template,redirect
from flask_mysqldb import MySQL

app = Flask(__name__,static_folder="static")

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'mychart'

mysql = MySQL(app)

@app.route('/')
def index():
	cur = mysql.connection.cursor()
	cur.execute("SELECT *FROM chart")
	fetchdata = cur.fetchall()
	print (type(fetchdata))
	svalue = []
	pvalue  = []
	for t in fetchdata:
		pvalue.append(t[1])
		svalue.append(t[2])

	print(svalue)
	print(pvalue)
	return	render_template('index.html', svalue = svalue, pvalue=pvalue)
	cur.close()
	conn.commit()

if __name__ == "__main__":
    app.run(host='0.0.0.0')
