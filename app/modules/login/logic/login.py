import sys 
sys.path.append('c:/Users/yeiso/OneDrive/Escritorio/Proyecto/final_proyect')
from app.utils.logger import Logger

#Clase para manejar la logica de la vista de login 
class LogicLogin:

    def __init__(self):
        self.log = Logger("app/logs/Login.log").get_logger()

    
    #Funcion para validar el login
    def validate_login(self):
        