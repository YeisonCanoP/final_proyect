
#Clase para manejar la session del usuario en flet
class SessionManager:

    #Funcion para guardar usuario en la session de flet
    @staticmethod
    def set_user(page, email: str, name: str):
        try:
            page.session.set("email", email)
            page.session.set("name", name)
        except Exception as ex:
            raise Exception(f"Error al guardar el usuario en la session: {ex}")

    #Funcion para obtener el usuario de la session de flet
    @staticmethod
    def get_user(page):
        try:
            email = page.session.get("email") or "Desconocido"
            name = page.session.get("name") or "Usuario"
            return email, name
        except Exception as ex:
            raise Exception(f"Error al obtener el usuario de la session: {ex}")
        
    #Funcion para eliminar el usuario de la session de flet
    @staticmethod
    def clear_user(page):
        page.session.clear()
