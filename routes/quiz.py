# esto evita que app.py falle al importar los blueprint mientras los archivos estan vacios
from flask import Blueprint

quiz = Blueprint("quiz", __name__)