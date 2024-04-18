from pypika import Query, Table, Order
from conexao import Conexao

customers = Table('usuarios')
q = Query.from_(customers).select(customers.id, customers.usuario, customers.senha)

#USUARIOS = Table("usuarios")
#query = MSSQLQuery.from_(USUARIOS).select(usuarios.id,'usuario','senha')

try:
    db = Conexao()
    print(f"Starting the connection ...\nStatus: {db.conn.is_connected()}")
    
    cursor = db.conn.cursor()
    cursor.execute(q.get_sql())

    #db.conn.commit()
    #Para Selects
    #cursor.execute(query)
    results = cursor.fetchall() 
    print(results)

    db.conn.close()
except ConnectionError as err:
    raise f"Error during connection. Message: {err}"
