
import flet as ft
import sys
sys.path.append('c:/Users/yeiso/OneDrive/Escritorio/Proyecto/final_proyect')
from app.utils.logger import Logger


#Clase para mannejar la creacion de funcines que se van ampoder eutilar en otro lado
class Utils:

    def __init__(self):
        self.log = Logger("app/logs/utils.log").get_logger()
        self.colorLetra = "#0D0630"
        self.fondo = "#f5f5f5"
    
    #Funcion para crear un hover 
    def on_hover(self,e,scale:int = 1.1) -> None:
        button = e.control

        if e.data == "true":
            button.scale = scale
        else:
            button.scale = 1.0
        
        button.update()



