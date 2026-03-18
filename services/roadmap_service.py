from models import db, Level, Progreso


# cuantas preguntas tiene cada nivel
PREGUNTAS_POR_NIVEL = 4

# comodines que tiene cada estudiante al inicio
COMODINES_INICIALES = 3


def _calcular_ejercicios(puntaje):
    # convierte el puntaje del nivel en una lista de True/False
    # ejemplo: puntaje 50 con 4 preguntas = [True, True, False, False]
    if puntaje <= 0:
        return [False] * PREGUNTAS_POR_NIVEL

    # cada pregunta vale 100 / 4 = 25 puntos
    puntos_por_pregunta = 100 // PREGUNTAS_POR_NIVEL
    completadas = min(puntaje // puntos_por_pregunta, PREGUNTAS_POR_NIVEL)

    return [i < completadas for i in range(PREGUNTAS_POR_NIVEL)]


def _calcular_estado(i, completado, niveles_db, estudiante_id):
    # decide si un nivel esta bloqueado, disponible o completado
    if completado:
        return 'completado'

    # el primer nivel siempre esta disponible
    if i == 0:
        return 'disponible'

    # los demas dependen de si el nivel anterior fue completado
    nivel_anterior = niveles_db[i - 1]
    progreso_anterior = Progreso.query.filter_by(
        id_estudiante=estudiante_id,
        id_level=nivel_anterior.id
    ).first()

    anterior_completado = progreso_anterior.completado if progreso_anterior else False

    return 'disponible' if anterior_completado else 'bloqueado'


def get_progreso(estudiante_id):
    # devuelve la lista de niveles con el progreso del estudiante
    niveles_db = Level.query.order_by(Level.orden).all()

    resultado = []

    for i, nivel in enumerate(niveles_db):
        # buscamos el progreso del estudiante en este nivel
        progreso = Progreso.query.filter_by(
            id_estudiante=estudiante_id,
            id_level=nivel.id
        ).first()

        # si no hay registro de progreso el nivel no fue tocado todavia
        completado  = progreso.completado if progreso else False
        puntaje     = progreso.puntaje    if progreso else 0

        estado      = _calcular_estado(i, completado, niveles_db, estudiante_id)
        ejercicios  = _calcular_ejercicios(puntaje)
        completados = sum(ejercicios)

        resultado.append({
            'id':          nivel.id,
            'titulo':      nivel.titulo,
            'estado':      estado,
            'puntaje':     puntaje,
            'ejercicios':  ejercicios,
            'completados': completados,
            'total':       PREGUNTAS_POR_NIVEL,
            'conn_type':   None,
        })

    return resultado


def get_comodines(estudiante_id):
    # buscamos el primer registro de progreso del estudiante para leer sus comodines
    progreso = Progreso.query.filter_by(id_estudiante=estudiante_id).first()

    # si no tiene ningun progreso todavia tiene los comodines iniciales
    if not progreso:
        return COMODINES_INICIALES

    return progreso.comodin


def usar_comodin(estudiante_id):
    # buscamos todos los registros de progreso del estudiante
    progresos = Progreso.query.filter_by(id_estudiante=estudiante_id).all()

    if not progresos:
        # si no tiene progresos creamos uno en el primer nivel para guardar los comodines
        primer_nivel = Level.query.order_by(Level.orden).first()
        if not primer_nivel:
            return {'ok': False, 'mensaje': 'no hay niveles disponibles'}

        nuevo = Progreso(
            id_estudiante=estudiante_id,
            id_level=primer_nivel.id,
            completado=False,
            puntaje=0,
            comodin=COMODINES_INICIALES
        )
        db.session.add(nuevo)
        db.session.commit()
        progresos = [nuevo]

    # leemos cuantos comodines quedan del primer registro
    comodines_restantes = progresos[0].comodin

    if comodines_restantes <= 0:
        return {'ok': False, 'comodines': 0, 'mensaje': 'no quedan comodines'}

    # descontamos un comodin en todos los registros del estudiante
    # para mantener consistencia entre niveles
    nuevos_comodines = comodines_restantes - 1
    for p in progresos:
        p.comodin = nuevos_comodines

    db.session.commit()

    return {'ok': True, 'comodines': nuevos_comodines}