import sys 
sys.path.append('c:/Users/yeiso/OneDrive/Escritorio/Proyecto/final_proyect')
from app.utils.logger import Logger
import httpx

#Clase para manejar la logica de la vista de login 
class LogicLogin:

    def __init__(self):
        self.log = Logger("app/logs/Login.log").get_logger()
        self.url = "http://localhost:8000/cognito/login"
        self.urlCierre = "http://localhost:8000/cognito/logout"
    
    #Funcion para iniciar con google
    def login_google(self,e):
        e.page.launch_url(self.url)
    
    #Funcion para cerrar sesion
    async def logout(self, e):
        async with httpx.AsyncClient() as client:
            response = await client.get(self.urlCierre)
            if response.status_code == 200:
                e.page.go("/")
            else:
                self.log.error(f"Error al cerrar sesión: {response.text}")

