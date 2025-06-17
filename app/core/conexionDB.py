
import mysql.connector
from mysql.connector import Error
import sys 
sys.path.append("C:/Users7AndresSanchez/OneDrive - Vibras/Documents/Bootcamp - Arquitectura en la nube/Git/final_proyect")
from app.utils.logger import Logger

class ConexionDB():
    def __init__(self, host, port, user, password, database):
        self.log = Logger("/app/logs/conexion.log").get_logger()
        self.config = {
            "host": "http://db-finaltech.c0hgqyu0au2e.us-east-1.rds.amazonaws.com/",
            "port": 3306,
            "user": "admin",
            "password": "",
            "database": database
        }
        self.connection = None
        self.connect()

    def connect(self):
        try:
            self.connection = mysql.connector.connect(**self.config)
            if self.connection.is_connected():
                print("✅ Conectado exitosamente a la base de datos RDS")
        except Error as e:
            print(f"❌ Error al conectar: {e}")
            self.connection = None

    def disconnect(self):
        if self.connection and self.connection.is_connected():
            self.connection.close()
            self.connection = None
            print("🔌 Desconectado de la base de datos")
        else:
            print("⚠️ No hay conexión activa para cerrar")

    def reconnect(self):
        print("♻️ Reconectando a la base de datos...")
        self.disconnect()
        self.connect()

    def is_connected(self):
        return self.connection is not None and self.connection.is_connected()

    def get_connection(self):
        return self.connection

