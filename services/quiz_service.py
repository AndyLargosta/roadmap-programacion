from models import Pregunta, Alternativa, Progreso, Level
from app import db

def verificar_respuesta(pregunta_id: int, alternativa_id: int) -> bool:
    alternativa_elegida = Alternativa.query.get(alternativa_id)

    if alternativa_elegida.correcta:
        return True
    
    return False

