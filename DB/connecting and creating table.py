import sqlite3

def sql_connection():

	conn = sqlite3.connect("database.db")
	return conn

def sql_table(con):

	cursorobj = conn.cursor()

	cursorobj.execute("CREATE TABLE IF NOT EXISTS employees(id integer PRIMARY KEY,name text, position text)")
	conn.commit() # push the code

	cursorobj.execute('INSERT INTO employees VALUES(3,"Erfan","Software engineer")')
	conn.commit()

#insert data into the table



conn = sql_connection()
sql_table(conn)


#fetch all the data
def sql_fetch(conn):
	cursorobj = conn.cursor()

	cursorobj.execute('SELECT * FROM employees')
	rows = cursorobj.fetchall()

	for row in rows:
		print(row)

sql_fetch(conn)
