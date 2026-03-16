from models import Pregunta, Alternativa, Progreso, Level
from app import db

def verificar_respuesta(pregunta_id: int, respuesta: str) -> bool:
    alternativas_obj = Alternativa.query.filter_by(id_preguntas=pregunta_id).all()
    
    for obj en alternativas_obj:
        if obj.correcta == True:
            respuesta_correcta = obj.alternativas
            break
    
    if respuesta_correcta == respuesta:
        return True
    
    return False


def obtener_pregunta_y_respuestas(pregunta_id):
    # almacenamos en la variable pregunta, el texto que se encuentra
    # en la DB, bajo el campo preguntas
    pregunta = Pregunta.query.get(pregunta_id).preguntas
    # creamos un objeto que contiene todas las alternativas con id_preguntas=pregunta_id
    alternativas_encontradas_obj = Alternativa.query.filter_by(id_preguntas=pregunta_id).all()
    # creamos una lista iterando sobre el obj, para extraer solo el texto
    lista_alternativas = []
    for item in alternativas_encontradas_obj:
        lista_alternativas.append(item.alternativas)
    
    return [pregunta, lista_alternativas]