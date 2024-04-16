from conexao import Conexao


query = "insert into usuarios (id,usuario,senha) values (2,'iury','123456') "
try:
    db = Conexao()
    print(f"Starting the connection ...\nStatus: {db.conn.is_connected()}")

    cursor = db.conn.cursor()
    cursor.execute(query)

    db.conn.commit()
    #Para Selects
    #cursor.execute(query)
    #results = cursor.fetchall()
    #print(results)

    db.conn.close()
except ConnectionError as err:
    raise f"Error during connection. Message: {err}"