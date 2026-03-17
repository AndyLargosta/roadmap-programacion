from flask import Blueprint, render_template, request, redirect, url_for, session, jsonify
from services.auth_service import check_or_create_user, email_exists

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if 'user_id' in session:
        return redirect(url_for('roadmap.index')) 

    error = None
    email = ''

    if request.method == 'POST':
        email = request.form.get('email', '').strip().lower()
        password = request.form.get('password', '')

        if not email or not password:
            error = 'Por favor completá todos los campos.'
            return render_template('login.html', error=error, email=email)

        user, is_new = check_or_create_user(email, password)

        if user is None:
            error = 'Contraseña incorrecta.'
            return render_template('login.html', error=error, email=email)

        session['user_id'] = user.id
        session['user_email'] = user.email
        session['is_new'] = is_new
        session['nombre_usuario'] = user.email.split('@')[0]
        return redirect(url_for('roadmap.index'))

    return render_template('login.html', error=error, email=email)

@auth.route('/check-email', methods=['POST'])
def check_email():
    data = request.get_json(silent=True) or {}
    email = data.get('email', '').strip().lower()

    if not email:
        return jsonify({'exists': False, 'error': 'Email requerido'}), 400

    exists = email_exists(email)
    return jsonify({'exists': exists})

@auth.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('auth.login'))