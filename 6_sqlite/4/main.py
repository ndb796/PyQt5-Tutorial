import sqlite3

con = sqlite3.connect("./test.db")

cur = con.cursor()
cur.execute('SELECT * FROM CUSTOMER;')
for row in cur:
    print(row)

con.close()
