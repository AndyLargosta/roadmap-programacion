from flask import Blueprint, render_template, request
from services.quiz_service import obtener_pregunta_y_respuestas, verificar_respuesta

quiz = Blueprint("quiz", __name__)

@quiz.route('/pregunta/<int:pregunta_id>', methods=['GET'])
def cargar_pregunta(pregunta_id):
    pregunta_data = obtener_pregunta_y_respuestas(pregunta_id)

    if not pregunta_data:
        return "Pregunta no encontrada", 404
    
    return render_template('quiz.html', pregunta=pregunta_data)
