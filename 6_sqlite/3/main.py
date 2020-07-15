import sqlite3

con = sqlite3.connect("./test.db")

customers = ('John Doe', 25, 'Programmer')
cur = con.cursor()
cur.execute("INSERT INTO CUSTOMER (name, age, job) VALUES (?, ?, ?);", customers)

con.commit()
con.close()
