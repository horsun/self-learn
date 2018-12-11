import psycopg2

conn = psycopg2.connect(host="127.0.0.1", port=5432, user='horsun', password='123456',database = 'exampledb')
cur = conn.cursor()
cur.execute("SELECT * ")
rows = cur.fetchall()
print(rows)
