from models import db, Pregunta, Alternativa, Level, Progreso


def get_pregunta(level_id, ejercicio_index):
    # buscamos todas las preguntas del nivel ordenadas por id
    preguntas = Pregunta.query.filter_by(id_level=level_id).order_by(Pregunta.id).all()
    indice_real = ejercicio_index - 1

    # si el indice no existe devolvemos None
    if not preguntas or indice_real < 0 or indice_real >= len(preguntas):
        return None

    pregunta_db = preguntas[indice_real]
    alternativas = Alternativa.query.filter_by(id_preguntas=pregunta_db.id).all()

    # formateamos las alternativas para pasarlas al template
    opciones_formateadas = [
        {'id': alt.id, 'texto': alt.alternativas}
        for alt in alternativas
    ]

    return {
        'id':      pregunta_db.id,
        'texto':   pregunta_db.preguntas,
        'opciones': opciones_formateadas,
    }


def verificar_respuesta(estudiante_id, level_id, ejercicio_index, respuesta_id):
    # verificamos que el id de respuesta sea valido
    try:
        respuesta_elegida = Alternativa.query.get(int(respuesta_id))
    except (ValueError, TypeError):
        return {'aprobado': False, 'error': 'id de respuesta invalido'}

    if not respuesta_elegida:
        return {'aprobado': False, 'error': 'alternativa no encontrada'}

    es_correcta = respuesta_elegida.correcta

    if es_correcta:
        _actualizar_progreso(estudiante_id, level_id, ejercicio_index)

    # calculamos cuantos ejercicios completo el estudiante en este nivel
    progreso = Progreso.query.filter_by(
        id_estudiante=estudiante_id,
        id_level=level_id
    ).first()

    ejercicios_completados = progreso.puntaje // 25 if progreso else 0
    total_ejercicios = 4

    return {
        'aprobado':              es_correcta,
        'ejercicios_completados': ejercicios_completados,
        'total_ejercicios':       total_ejercicios,
        'nivel_completado':       progreso.completado if progreso else False,
        'level_id':               level_id,
        'ejercicio_index':        ejercicio_index,
    }


def _actualizar_progreso(estudiante_id, level_id, ejercicio_index):
    # buscamos si ya existe un registro de progreso para este estudiante y nivel
    progreso = Progreso.query.filter_by(
        id_estudiante=estudiante_id,
        id_level=level_id
    ).first()

    # si no existe lo creamos desde cero
    if not progreso:
        progreso = Progreso(
            id_estudiante=estudiante_id,
            id_level=level_id,
            completado=False,
            puntaje=0
        )
        db.session.add(progreso)

    # cada ejercicio vale 25 puntos (4 ejercicios = 100 puntos)
    puntos_por_ejercicio = 25
    puntaje_nuevo = ejercicio_index * puntos_por_ejercicio

    # solo subimos el puntaje si este ejercicio supera el progreso actual
    # esto evita que repetir ejercicios sume puntos de mas
    if puntaje_nuevo > progreso.puntaje:
        progreso.puntaje = puntaje_nuevo

    # si llego a 100 puntos el nivel queda completado
    if progreso.puntaje >= 100:
        progreso.completado = True

    db.session.commit()