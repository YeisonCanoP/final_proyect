import flet as ft
import sys
sys.path.append('c:/Users/yeiso/OneDrive/Escritorio/Proyecto/final_proyect')
from app.utils.logger import Logger
from app.utils.builder import Builder


#Clase para menjar al creacion del login en flet Vizora 
class ViewLogin:
    
    #Construcot de la clase }
    def __init__(self, page: ft.Page):
        """
        Constructor de la clase ViewLogin.
        Inicializa la página y establece el título.
        """
        self.imagen_fondo = "https://techwebgato.s3.us-east-1.amazonaws.com/imagenes/fondo_login.webp"
        self.log = Logger("/app/logs/viewLogin.log").get_logger()
        self.colorLetra = "#0D0630"
        self.page = page
        self.builder = Builder()
    
    #Funcion  para crear el container de fondo
#Funcion para crear el fondo del login
    def crear_fondo(self):
        fondo = ft.ResponsiveRow(
            expand=True,
            controls=[
            # Container o imagen de fondo
            ft.Container(
                width=float("inf"),
                height=float("inf"),
                expand=True,
                content=ft.Image(
                    src=self.imagen_fondo,
                    expand=True,
                    fit=ft.ImageFit.FILL,
                ),
            ),
            ]
        )
        return fondo

    #Funcion para crear el encabezado del contianer de login
    def create_encabezado(self):
        encabezado = ft.ResponsiveRow(
            expand=True,
            alignment=ft.MainAxisAlignment.CENTER,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                #Container del encabezado
                ft.Container(
                    expand=True,
                    alignment=ft.alignment.bottom_center,
                    content=ft.Text(
                        "Bienvenido a Vizora",
                        style=ft.TextStyle(
                            size=35,
                            color=self.colorLetra,
                            letter_spacing=2,
                            weight=ft.FontWeight.W_900,
                        )
                    )
                ),
            ]
        )

        return encabezado
    
    #Funcion para crear el cuerpo, donde va estar los texfields y etc
    def create_cuerpo(self):
        cuerpo = ft.ResponsiveRow(
            expand=True,
            alignment=ft.MainAxisAlignment.CENTER,
            controls=[
                ft.Column(
                    expand=True,
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    spacing=0,
                    col ={"xs":9,"sm":7.5,"md":7.5,"lg":6,"xl":5.5,"xxl":4.5},
                    controls=[
                        #Container del texfield de usuario
                        ft.Container(
                            expand=10,
                            alignment=ft.alignment.center,
                            content=self.builder.create_textfield(
                                password=False,
                                hint_text="Ingrese su correo",
                                prefix_icon=ft.Icons.PERSON
                            ),
                        ),
                        #Container del texfield de contraseña
                        ft.Container(
                            expand=10,
                            alignment=ft.alignment.top_center,
                            content=self.builder.create_textfield(
                                password=True,
                                hint_text="Ingrese su contraseña",
                                prefix_icon=ft.Icons.LOCK
                            ),
                        ),
                        #Container del boton de login
                        ft.Container(
                            expand=5,
                            bgcolor=ft.Colors.RED,
                            content=self.builder.create_button(
                                bgcolor=self.colorLetra,
                                text="Iniciar Sesión",
                                tooltip="Iniciar sesión",
                                on_click=None, # Aquí puedes agregar la función que maneja el clic
                            )
                        ),
                    ]
                )
            ]
        )

        return cuerpo

    #Funcion para crear lo que tendra dentro el container, estara divido en encabezado, cuerpo y pie
    def create_contenido(self):
        container = ft.Column(
            expand=True,
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                #Container de encabezado
                ft.Container(
                    expand=3,
                    alignment=ft.alignment.center,
                    content=self.create_encabezado()
                ),
                #Container del cuerpo
                ft.Container(
                    expand=11,
                    bgcolor=ft.Colors.BLUE,
                    content=self.create_cuerpo()
                ),
                #Container del pie
                ft.Container(
                    expand=5,
                    alignment=ft.alignment.center,
                    bgcolor=ft.Colors.GREEN,
                )
            ]
        )
        return container

    #Funcion para crear el container que va tener el login y todo la informacion del login
    def create_container(self):
        container = ft.ResponsiveRow(
            expand=True,
            alignment=ft.MainAxisAlignment.CENTER,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                #Columnna que va tener el container del login con los otros dos contenedore para hacer espacio
                ft.Column(
                    expand=True,
                    alignment=ft.MainAxisAlignment.CENTER,
                    col ={"xs":9,"sm":7.5,"md":7.5,"lg":6,"xl":5.5,"xxl":4.5},
                    controls=[
                        ft.Container(
                            expand=3,
                            alignment=ft.alignment.center,
                        ),
                        ft.Stack(
                            alignment=ft.alignment.center,
                            expand=11,
                            controls=[
                                ft.Container(
                                    alignment=ft.alignment.center,
                                    gradient=ft.LinearGradient(
                                        begin=ft.alignment.bottom_left,
                                        end=ft.alignment.top_right,
                                        colors=["#FF6B81","#FF8CD1","#8C7BFF","#8A7FD9",]
                                    ),
                                    opacity=0.4,
                                    border_radius=25,
                                ),
                                self.create_contenido()
                            ]
                        ),
                        ft.Container(
                            expand=3,
                            alignment=ft.alignment.center,
                        )
                    ]
                ),
            ]
        )
    
        return container

    #Funcion para crear el login
    def create_login(self):
        self.log.info("Creating login view")

        fondo_contenido=ft.Stack(
            expand=True,
            alignment=ft.alignment.center,
            controls=[
                # Fondo del login
                self.crear_fondo(),
                ft.Container(
                    bgcolor=ft.Colors.TRANSPARENT,
                    expand=True,
                    alignment=ft.alignment.center,
                    content=self.create_container()
                )
            ]
        )


        self.page.add(
            fondo_contenido
        )
        self.page.fonts = {
            "NotoSans": "fonts/NotoSans/NotoSans-VariableFont_wdth,wght.ttf",
        }
        self.page.theme = ft.Theme(
            font_family="NotoSans"
        )
        self.page.padding = 0
        self.page.expand = True
        self.page.update()