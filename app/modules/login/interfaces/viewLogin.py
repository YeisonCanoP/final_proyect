import flet as ft
import sys
sys.path.append('c:/Users/yeiso/OneDrive/Escritorio/Proyecto/final_proyect')
from app.utils.logger import Logger


#Clase para menjar al creacion del login en flet Vizora 
class ViewLogin:
    
    #Construcot de la clase }
    def __init__(self, page: ft.Page):
        """
        Constructor de la clase ViewLogin.
        Inicializa la página y establece el título.
        """

        self.log = Logger("/app/logs/viewLogin.log").get_logger()
        self.page = page
        self.page.title = "Vizora-Login"
    
    #Funcion para crear el login
    def create_login(self):
        self.log.info("Creating login view")
        container = ft.Container(
            bgcolor=ft.colors.RED,
            expand=True,
        )

        self.page.add(
            container
        )
        self.page.update()