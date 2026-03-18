from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Level(db.Model):
    __tablename__ = 'levels'

    id = db.Column(db.Integer, primary_key= True, autoincrement=True)
    titulo = db.Column(db.String(100), nullable=False)
    orden = db.Column(db.Integer, nullable=False)
    descripcion= db.Column(db.String(200))

    preguntas = db.relationship('Pregunta', backref='level', lazy=True)
    progresos = db.relationship('Progreso', backref='level', lazy=True)


class Pregunta(db.Model):
    __tablename__ = 'preguntas'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_level   = db.Column(db.Integer, db.ForeignKey('levels.id'), nullable=False)
    preguntas  = db.Column(db.String(300), nullable=False)

    alternativas = db.relationship('Alternativa', backref='pregunta', lazy=True)

class Alternativa(db.Model):
    __tablename__ = 'alternativas'

    id            = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_preguntas  = db.Column(db.Integer, db.ForeignKey('preguntas.id'), nullable=False)
    alternativas  = db.Column(db.String(200), nullable=False)
    correcta      = db.Column(db.Boolean, default=False, nullable=False)

class Estudiante(db.Model):
    __tablename__ = 'estudiante'

    id              = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre_usuario  = db.Column(db.String(100), nullable=False)
    password        = db.Column(db.String(256), nullable=False)
    email           = db.Column(db.String(100), unique=True, nullable=False)

    progresos = db.relationship('Progreso', backref='estudiante', lazy=True)

class Progreso(db.Model):
    __tablename__ = 'progreso'

    id            = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_estudiante = db.Column(db.Integer, db.ForeignKey('estudiante.id'), nullable=False)
    id_level      = db.Column(db.Integer, db.ForeignKey('levels.id'), nullable=False)
    completado    = db.Column(db.Boolean, default=False, nullable=False)
    puntaje       = db.Column(db.Integer, default=0, nullable=False)
    comodin       = db.Column(db.Integer, default=3, nullable=False)