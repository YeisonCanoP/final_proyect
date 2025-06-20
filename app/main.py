import flet as ft
import sys
from urllib.parse import urlparse, parse_qs
sys.path.append('c:/Users/yeiso/OneDrive/Escritorio/Proyecto/final_proyect')
from app.modules.login.interfaces.viewLogin import ViewLogin
from app.modules.panel.interfaces.viewTablero import ViewTablero
from app.modules.login.build.responsi import ResponsiLogin

#El nombre de la aplicacion es vizora

def main(page: ft.Page):
    page.fonts = {
        "NotoSans": "fonts/NotoSans/NotoSans-VariableFont_wdth,wght.ttf",
        "Poppins": "fonts/Poppins/Poppins-Regular.ttf.ttf",
        "PoppinsBold": "fonts/Poppins/Poppins-Bold.ttf",
        }
    page.theme = ft.Theme(
        font_family="Poppins",
        )
    page.padding = 0
    page.expand = True
    view = ViewLogin(page)
    tablero = ViewTablero(page)

    def aplicar_respondi():
        height = page.height
        responsi = ResponsiLogin(view)
        responsi.update_height(height)

    def page_resize(e):
        if page.route == "/":
            aplicar_respondi()
    
    def route_change(e):
        page.views.clear()

        if page.route.startswith("/tablero"):
            parsed = urlparse(page.route)
            query_params = parse_qs(parsed.query)
            email = query_params.get("email", [""])[0]
            name = query_params.get("name", [""])[0]

            page.views.append(
                tablero.create_tablero()
            )
            page.update()
        
        elif page.route == "/":
            page.views.append(
                view.create_login()
            )
            page.update()
            aplicar_respondi()


    page.on_route_change = route_change
    page.on_resized = page_resize
    page.go(page.route)
    page.update()

ft.app(target=main,view=ft.WEB_BROWSER,assets_dir="app/assets")