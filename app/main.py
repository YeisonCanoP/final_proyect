import flet as ft
import sys
sys.path.append('c:/Users/yeiso/OneDrive/Escritorio/Proyecto/final_proyect')
from app.utils.pageconfi import PageConfig
from app.utils.logger import Logger
from app.modules.login.interfaces.viewLogin import ViewLogin
from app.modules.panel.interfaces.viewTablero import ViewTablero
from app.modules.login.build.responsi import ResponsiLogin
from app.routers.fletFrontend import FletFrontendRouter


log = Logger("app/logs/main.log").get_logger()
#El nombre de la aplicacion es vizora
def main(page: ft.Page):
    #Inicializacion la configuracion de la pagina
    PageConfig.configure(page)
    #Instancia de las vistas
    view = ViewLogin(page)
    tablero = ViewTablero(page)

    def aplicar_respondiHome():
        height = page.height
        responsi = ResponsiLogin(view)
        responsi.update_height(height)

    def page_resize(e):
        if page.route == "/":
            aplicar_respondiHome()
    
    def route_change(e):
        router = FletFrontendRouter(page, view, tablero)
        router.handle()


    page.on_route_change = route_change
    page.on_resized = page_resize
    page.go(page.route)
    page.update()

ft.app(target=main,view=ft.WEB_BROWSER,assets_dir="app/assets",port=52928)