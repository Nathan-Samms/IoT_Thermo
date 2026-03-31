import os

from flask import Flask
from settings import AUTH_ENV_VAR

app = Flask(__name__, template_folder = "templates", static_folder = "static")

def auth_ok(req):
    token = os.getenv(AUTH_ENV_VAR)
    if not token:
        return True
    
    