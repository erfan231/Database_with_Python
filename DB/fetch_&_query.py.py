import sqlite3

#all rows
conn = sqlite3.connect('database.db')

def sql_fetch(conn):
	cursorobj = conn.cursor()

	cursorobj.execute('SELECT * FROM employees') #selects all the data
	rows = cursorobj.fetchall()

	for row in rows:
		print(row)

sql_fetch(conn)

def sql_query(conn):
	cursorobj = conn.cursor()
	cursorobj.execute('SELECT name FROM employees WHERE position == "Software engineer"') #query
	rows = cursorobj.fetchall()
	print(rows)
	print('These the people who is a software engineer')
	for row in rows:
		print(f'\t {row}')


#(conn)
sql_query(conn)
