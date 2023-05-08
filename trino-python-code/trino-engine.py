import trino
conn = trino.dbapi.connect(
    host='localhost',
    port=9091,
    user='eliar'
)

# Execute a cross-database query
cur = conn.cursor()
cur.execute("""
        SELECT * FROM postgresql1.dwh.machinedim
        UNION ALL
        SELECT * FROM postgresql2.dwh.machinedim
    """)
rows = cur.fetchall()
for row in rows:
    print(row)