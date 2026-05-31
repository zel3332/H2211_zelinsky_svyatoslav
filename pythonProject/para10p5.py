import sqlite3

connection = sqlite3.connect("itstep_DB.sil3", 5)
cur = connection.cursor()
cur.execute("INSERT INTO first_table (name) VALUES ('Anna');")
cur.execute("INSERT INTO first_table (name) VALUES ('John');")
connection.commit()
cur.execute("SELECT rowid, name FROM first_table;")
connection.commit()
res = cur.fetchall()
print(res)
connection.close()

