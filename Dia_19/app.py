from flask import Flask,make_response,jsonify,request
from bd import Carros
from conexao import Conexao

app = Flask('Carro')
app.config['JSON_SORT_KEYS'] = False

@app.route('/carros',methods=['GET'])
def get_carros():
    db = Conexao()
    cursor = db.conn.cursor()
    cursor.execute("select * from Carros")
    meus_carros = cursor.fetchall()
    print(meus_carros)
    return make_response(
        jsonify(meus_carros) 
    ) 

@app.route('/carros',methods=['POST'])
def create_carros():
    carro = request.json
    db = Conexao()
    cursor = db.conn.cursor()
    cursor.execute(f"insert into carros (marca,modelo,ano) values ('{carro['marca']}','{carro['modelo']}',{carro['ano']})")
    db.conn.commit()
    return make_response(
        jsonify(carro) 
    ) 

app.run()


