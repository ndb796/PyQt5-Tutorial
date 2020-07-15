import sqlite3

con = sqlite3.connect("./test.db")

cur = con.cursor()
cur.execute("CREATE TABLE CUSTOMER (id INTEGER PRIMARY KEY, name VARCHAR(20), age INTEGER, job VARCHAR(50));")

con.close()
