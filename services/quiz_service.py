from models import db, Pregunta, Alternativa, Level

def get_pregunta(level_id, ejercicio_index):
    preguntas = Pregunta.query.filter_by(id_level=level_id).order_by(Pregunta.id).all()
    indice_real = ejercicio_index - 1
    
    if not preguntas or indice_real < 0 or indice_real >= len(preguntas):
        return None
        
    pregunta_db = preguntas[indice_real]
    alternativas = Alternativa.query.filter_by(id_preguntas=pregunta_db.id).all()
    opciones_formateadas = []
    for alt in alternativas:
        opciones_formateadas.append({
            "id": alt.id, 
            "texto": alt.alternativas
        })
        
    return {
        "id": pregunta_db.id,
        "texto": pregunta_db.preguntas,
        "opciones": opciones_formateadas
    }

def verificar_respuesta(estudiante_id, level_id, ejercicio_index, respuesta_id):

    try:
        respuesta_elegida = Alternativa.query.get(int(respuesta_id))
    except (ValueError, TypeError):
        return {"aprobado": False, "error": "ID de respuesta inválido"}

    if not respuesta_elegida:
        return {"aprobado": False, "error": "Alternativa no encontrada"}

    es_correcta = respuesta_elegida.correcta

    if es_correcta:
        pass

    return {"aprobado": es_correcta}