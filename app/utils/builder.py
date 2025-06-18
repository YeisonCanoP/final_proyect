import flet as ft
import sys
sys.path.append('c:/Users/yeiso/OneDrive/Escritorio/Proyecto/final_proyect')
from app.utils.logger import Logger

#Builder para crear elementos ahorrar tiempo y codigo
class Builder:

    def __init__(self):
        self.log = Logger("app/logs/builder.log").get_logger()
        self.colorLetra = "#0D0630"
        self.fondo = "#f5f5f5"

    #Funcion para crear un tooltip
    def create_tooltip(self, text:str) -> ft.Tooltip:
        tooltip = ft.Tooltip(
            message=text,
            bgcolor=self.colorLetra,
            text_style=ft.TextStyle(
                color=ft.Colors.WHITE,
                size=11,
                weight=ft.FontWeight.W_500
            ),
        )

        return tooltip

    #Funcion para crear un texfield
    def create_textfield(self,password:bool,hint_text:str,prefix_icon:ft.Icon) -> ft.TextField:
        texfield = ft.TextField(
            autofocus=True,
            bgcolor=self.fondo,
            border_color=ft.Colors.TRANSPARENT,
            border_radius=15,
            password=password,
            can_reveal_password=password,
            color=self.colorLetra,
            content_padding=ft.padding.all(8),
            hint_text=hint_text,
            hint_style=ft.TextStyle(
                color=ft.Colors.GREY_400,
                size=14,
                weight=ft.FontWeight.W_500
            ),
            prefix_icon=prefix_icon,
        )

        return texfield
    
    #Funcion para crear un boton
    def create_button(self,bgcolor:str,text:str,tooltip:str,on_click:None,radius:int=20,col = None) -> ft.ElevatedButton:
        boton=ft.ElevatedButton(
            text=text,
            expand=True,
            bgcolor=bgcolor,
            style=ft.ButtonStyle(
                color=ft.Colors.WHITE,
                padding=ft.padding.only(top=6, bottom=6, left=10, right=10),
                shape=ft.RoundedRectangleBorder(radius=radius),
                text_style=ft.TextStyle(
                    color="white",
                    size=25,
                    weight=ft.FontWeight.W_500,
                    letter_spacing=1.5,
                ),
            ),
            on_click=on_click,
        )

        return boton