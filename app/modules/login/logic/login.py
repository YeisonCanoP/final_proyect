import sys 
sys.path.append('c:/Users/yeiso/OneDrive/Escritorio/Proyecto/final_proyect')
from app.utils.logger import Logger

#Clase para manejar la logica de la vista de login 
class LogicLogin:

    def __init__(self):
        self.log = Logger("app/logs/Login.log").get_logger()
        self.url = "http://localhost:8000/cognito/login"
    
    #Funcion para iniciar con google
    def login_google(self,e):
        e.page.launch_url(self.url)

