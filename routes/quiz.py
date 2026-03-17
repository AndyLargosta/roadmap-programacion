from flask import Blueprint, render_template, request, session, redirect, url_for
# Asegúrate de importar tu servicio donde manejes la lógica de base de datos
from services import quiz_service

quiz = Blueprint('quiz', __name__)

@quiz.route('/quiz/<int:level_id>/ejercicio/<int:ejercicio_id>', methods=['GET', 'POST'])
def ejercicio_view(level_id, ejercicio_id):
    # Simulamos el ID del estudiante (igual que en tu roadmap.py)
    estudiante_id = session.get('user_id')

    # Opcional: Si por alguna razón no hay sesión, abortamos para que no explote
    if not estudiante_id:
        return redirect(url_for('auth.login'))

    # --- SI EL USUARIO ENTRA A VER LA PREGUNTA ---
    if request.method == 'GET':
        # Le pedimos al servicio que busque la pregunta correspondiente
        pregunta = quiz_service.get_pregunta(level_id, ejercicio_id)
        
        # Si por alguna razón no existe, lo devolvemos al roadmap
        if not pregunta:
            return redirect(url_for('roadmap.roadmap_view'))
            
        return render_template('quiz.html', 
                               pregunta=pregunta, 
                               level_id=level_id, 
                               ejercicio_id=ejercicio_id)

    # --- SI EL USUARIO ENVÍA SU RESPUESTA ---
    elif request.method == 'POST':
        # Capturamos la opción que seleccionó en el formulario
        respuesta_usuario = request.form.get('respuesta')
        
        # Evaluamos la respuesta (esto debería guardar el progreso en DB si aprueba)
        resultado = quiz_service.verificar_respuesta(estudiante_id, level_id, ejercicio_id, respuesta_usuario)

        # Renderizamos la pantalla de éxito/error pasándole el resultado
        return render_template('resultado.html', resultado=resultado)