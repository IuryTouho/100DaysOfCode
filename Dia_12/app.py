from conexao import Conexao
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,String, Integer
from sqlalchemy.orm import sessionmaker

engine = create_engine("mysql+pymysql://root:Iury@localhost:3306/teste")
conn = engine.connect()
Base = declarative_base
Session = sessionmaker(bind=engine)
session = Session()

#response = conn.execute("select * from usuarios")

print(engine)

class Usuarios(Base):
    _tablename_ = "usuarios"

    id = Column(String, primary_key=True)
    usuario = Column(String, nullable=True)
    senha = Column(String, nullable=True)

data = session.query(Usuarios).all()
print(data)

"""
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

"""