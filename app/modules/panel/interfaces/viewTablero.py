import asyncio
import sys
import flet as ft
sys.path.append('c:/Users/yeiso/OneDrive/Escritorio/Proyecto/final_proyect')
from app.utils.logger import Logger
from app.core.login import LogicLogin

#Clase para manejar la construccion de la vista de tablero
class ViewTablero:
    def __init__(self, page):
        self.page = page
        self.log = Logger("app/logs/viewTablero.log").get_logger()
    

    def create_tablero(self):
        try:
            container = ft.Container(
                content=ft.Column(
                    [
                        ft.Text("Tablero de Control", style=ft.TextStyle(size=24, weight=ft.FontWeight.BOLD)),
                        ft.Text("Bienvenido al tablero de control. Aquí podrás ver las estadísticas y datos relevantes."),
                        # Aquí puedes agregar más widgets según sea necesario
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                ),
                padding=20,
                bgcolor=ft.Colors.WHITE,
                border_radius=10,
            )
            return ft.View(
                "/tablero",
                [
                    container,
                    ft.TextButton("Volver", on_click=lambda e: asyncio.run(LogicLogin().logout(e)))
                ],
                padding=20,
                bgcolor=ft.Colors.LIGHT_BLUE_50,
            )

        except Exception as ex:
            self.log.error(f"Error creating tablero view: {ex}")
            raise ex