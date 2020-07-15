import sqlite3

con = sqlite3.connect("./test.db")

deleted_id = 1
cur = con.cursor()
cur.execute("DELETE FROM CUSTOMER WHERE id = ?;", (deleted_id, ))

con.commit()
con.close()
