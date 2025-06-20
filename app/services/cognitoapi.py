from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse
from authlib.integrations.starlette_client import OAuth
from starlette.middleware.sessions import SessionMiddleware
from starlette.responses import HTMLResponse
import os
import sys
sys.path.append('c:/Users/yeiso/OneDrive/Escritorio/Proyecto/final_proyect')
from app.core.secretManager import SecretManager

app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key=os.urandom(24))
oauth = OAuth()

oauth.register(
    name='cognito',
    client_id="362d15nphvpgclqek3ucumef1f",
    client_secret="b0p3n194u5ah7su7iclfdulffss5eiiejlniuaj9ed6t2a61vf3",
    server_metadata_url="https://cognito-idp.us-east-1.amazonaws.com/us-east-1_valpTt49s/.well-known/openid-configuration",
    client_kwargs={
        'scope': 'openid email phone'
    }
)

# 🔐 Paso 1: Redirigir a Cognito 
@app.get("/cognito/login")
async def login(request: Request):
    redirect_uri = "http://localhost:8000/cognito/callback"
    return await oauth.cognito.authorize_redirect(request,redirect_uri)

# ✅ Paso 2: Recibir token y redirigir al Flet Frontend
@app.get("/cognito/callback")
async def callback(request: Request):
    token = await oauth.cognito.authorize_access_token(request)
    user = token.get("userinfo")

    if not user:
        return RedirectResponse("http://localhost:52928/#/error")

    # Puedes extraer más datos si quieres
    email = user.get("email")
    name = user.get("name")

    # Redirigir al frontend Flet pasando datos por query params
    redirect_url = f"http://localhost:52928/#/tablero?email={email}&name={name}"
    return RedirectResponse(redirect_url)