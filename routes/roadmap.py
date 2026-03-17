from flask import Blueprint, render_template, session, redirect, url_for
from services import roadmap_service


roadmap = Blueprint('roadmap', __name__)

# patron zigzag: A = izq a centro, B = centro a der, C = der a izq
# 6 niveles, todos tienen conector porque el ultimo conecta al nodo final
CONN_TYPES = ['A', 'B', 'C', 'A', 'B', 'C']


def _agregar_conectores(levels):
    # agrega el tipo de conector a cada nivel segun su posicion en el zigzag
    for i, level in enumerate(levels):
        level['conn_type'] = CONN_TYPES[i] if i < len(CONN_TYPES) else None
    return levels


@roadmap.route('/roadmap')
def roadmap_view():
    # si el usuario no inicio sesion lo mandamos al login
    if 'user_id' not in session:
        return redirect(url_for('auth.login'))

    # user_id es el nombre que guarda auth.py en la sesion
    estudiante_id = session.get('user_id')

    # pedimos el progreso del estudiante al service
    levels = roadmap_service.get_progreso(estudiante_id)

    # agregamos el tipo de conector a cada nivel para el zigzag
    levels = _agregar_conectores(levels)

    return render_template('roadmap.html', levels=levels)