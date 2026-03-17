from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from models import db

def create_app():
    app = Flask(__name__)

    # configuraciones
    app.config['SECRET_KEY'] = 'hackaton_codepro_2026'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///roadmap.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    # registro de blueprints
    from routes.auth import auth
    from routes.roadmap import roadmap
    from routes.quiz import quiz

    app.register_blueprint(auth)
    app.register_blueprint(roadmap)
    app.register_blueprint(quiz)

    with app.app_context():
        db.create_all()

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)