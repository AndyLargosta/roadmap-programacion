from models import db, Pregunta, Alternativa, Level, Progreso

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

def actualizar_progreso(pregunta_id: int, estudiante_id: int)
    
    # 1. Obtener la pregunta y su level
    pregunta = Pregunta.query.get_or_404(pregunta_id)
    level = pregunta.level

    # 2. Buscar o crear el progreso
    progreso = Progreso.query.filter_by(
        id_estudiante=estudiante_id,
        id_level=level.id
    ).first()

    if not progreso:
        progreso = Progreso(
            id_estudiante=estudiante_id,
            id_level=level.id,
            completado=False,
            puntaje=0
        )
        db.session.add(progreso)

    # 3. Incrementar puntaje (siempre correcto si llega aquí)
    progreso.puntaje += 1

    # 4. Verificar si el level se completó
    total_preguntas = Pregunta.query.filter_by(id_level=level.id).count()
    if progreso.puntaje >= total_preguntas:
        progreso.completado = True

    db.session.commit()
    return progreso

### asegurarse de que tambien suba a la DB level una vez que todas las preguntas esten completas
