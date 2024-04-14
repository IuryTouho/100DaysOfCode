from conexao import Conexao


query = "select * from usuarios"
try:
    db = Conexao()
    print(f"Starting the connection ...\nStatus: {db.conn.is_connected()}")

    cursor = db.conn.cursor()
    cursor.execute(query)
    results = cursor.fetchall()

    print(results)

    db.conn.close()
except ConnectionError as err:
    raise f"Error during connection. Message: {err}"