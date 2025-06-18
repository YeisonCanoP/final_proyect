import flet as ft
import sys 
sys.path.append('c:/Users/yeiso/OneDrive/Escritorio/Proyecto/final_proyect')
from app.modules.login.interfaces.viewLogin import ViewLogin
from app.modules.login.build.responsi import ResponsiLogin

#El nombre de la aplicacion es vizora

def main(page: ft.Page):    
    page.expand = True
    view = ViewLogin(page)

    def page_resize(e):
        height = page.height
        print(f"Height: {height}")
        responsi = ResponsiLogin(view)
        responsi.update_height(height)


    page.on_resized = page_resize
    view.create_login()
    page_resize(None)
    page.update()

ft.app(target=main,view=ft.WEB_BROWSER,assets_dir="app/assets")