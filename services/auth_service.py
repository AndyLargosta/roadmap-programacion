from models import db, Estudiante
from werkzeug.security import generate_password_hash, check_password_hash

def check_or_create_user(email, password):
    """
    Busca un usuario por email. Si existe, verifica la contraseña.
    Si no existe, intenta crear uno nuevo (Registro automático).
    """
    # Busca si el estudiante ya existe
    user = Estudiante.query.filter_by(email=email).first()
    
    if user:
        # Verifica si la contraseña coincide con el hash almacenado
        if check_password_hash(user.password, password):
            return user, False
        return None, False  # Contraseña incorrecta
    
    # Si no existe, intenta crear un nuevo registro
    try:
        hashed_password = generate_password_hash(password)
        new_user = Estudiante(
            email=email, 
            password=hashed_password,
            nombre_usuario=email.split('@')[0]
        )
        
        db.session.add(new_user)
        db.session.commit()
        return new_user, True
        
    except Exception as e:
        # En caso de error (DB bloqueada, error de conexión, etc.)
        # Deshacemos cualquier cambio pendiente en la sesión
        db.session.rollback()
        # imprimir el error en consola para debugging
        print(f"Error crítico en el registro: {e}")
        return None, False

def email_exists(email):
    #Verifica la existencia del email para el aviso dinámico en el frontend.
    return Estudiante.query.filter_by(email=email).first() is not None
