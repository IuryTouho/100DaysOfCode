import mysql.connector as mysql_connector
class Conexao:
    def __init__(self):
        #Variaveis privadas
        self._host = "localhost"
        self._username = "root"
        self._passwd = "Iury"
        self._database = "teste"
        self.conn = self._connecting()

    def _connecting(self):
        return mysql_connector.connect(
            host=self._host,
            username=self._username,  
            password=self._passwd,
            database=self._database
        )