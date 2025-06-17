import flet as ft
import sys 
sys.path.append('c:/Users/yeiso/OneDrive/Escritorio/Proyecto/final_proyect')
from app.modules.login.interfaces.viewLogin import ViewLogin

#El nombre de la aplicacion es vizora

def main(page: ft.Page):

    view = ViewLogin(page)
    view.create_login()
    page.update()


ft.app(target=main, view=ft.WEB_BROWSER)