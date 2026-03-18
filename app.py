from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, redirect, url_for
from models import db
import socket

def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = 'hackaton_codepro_2026'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///roadmap.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    from routes.auth import auth
    from routes.roadmap import roadmap
    from routes.quiz import quiz

    app.register_blueprint(auth)
    app.register_blueprint(roadmap)
    app.register_blueprint(quiz)

    @app.route('/')
    def index():
        return redirect(url_for('auth.login'))

    with app.app_context():
        db.create_all()

    return app


if __name__ == '__main__':
    host_name = socket.gethostname()
    ip = socket.gethostbyname(host_name)  
    app = create_app()
    app.run(host=ip, debug=True)