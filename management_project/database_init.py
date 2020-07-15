import sqlite3

con = sqlite3.connect("./customer.db")

cur = con.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS CUSTOMER (id INTEGER PRIMARY KEY, name VARCHAR(20), age INTEGER, job VARCHAR(50));")

customers = [
    ('홍길동', 25, '개발자'),
    ('이순신', 47, '디자이너'),
    ('아무개', 25, '변호사'),
]

cur.executemany("INSERT INTO CUSTOMER (name, age, job) VALUES (?, ?, ?);", customers)

con.commit()
con.close()
