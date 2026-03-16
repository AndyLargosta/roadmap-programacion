from app import create_app
from models import db, Level, Pregunta, Alternativa

def seed():
    app = create_app()

    with app.app_context():

        # Limpia datos anteriores para no duplicar
        Alternativa.query.delete()
        Pregunta.query.delete()
        Level.query.delete()
        db.session.commit()

        # Crea los niveles
        niveles = [
            Level(titulo="Variables", orden=1, descripcion="Declara y usa variables en Python"),
            Level(titulo="Condicionales", orden=2, descripcion="Toma decisiones con if, elif y else"),
            Level(titulo="Bucles", orden=3, descripcion="Repite acciones con for y while"),
            Level(titulo="Funciones", orden=4, descripcion="Crea y usa funciones en Python"),
            Level(titulo="Listas", orden=5, descripcion="Crea y usa listas en Python"),
            Level(titulo="POO", orden=6, descripcion="Programación orientada a objetos"),
        ]

        db.session.add_all(niveles)
        db.session.commit()

        contenido = [

        # NIVEL 1: Variables
        {
            "level": niveles[0],
            "preguntas": [
                {
                    "texto": "¿Qué valor tendrá x si x = 10 + 5?",
                    "alternativas": [
                        ("15", True),
                        ("x+5", False),
                        ("10", False),
                        ("5", False),
                    ]
                },
                {
                    "texto": "¿Como se convierte la variable x = '42' a entero?",
                    "alternativas": [
                        ("int(x)", True),
                        ("integer(x)", False),
                        ("x.toInt()", False),
                        ("convert(x)", False),
                    ]
                },
                {
                    "texto": "¿Qué palabra reservada se usa para imprimir por consola?",
                    "alternativas": [
                        ("print()", True),
                        ("integer()", False),
                        ("def()", False),
                        ("imprimir()", False),
                    ]
                },{
                    "texto": "¿Para qué sirve input?",
                    "alternativas": [
                        ("Para solicitar datos", True),
                        ("Para asignar listas", False),
                        ("Para definir un tipo de datos", False),
                        ("Para sumar variables", False),
                    ]
                },
            ]
        },

        # NIVEL 2: Condicionales
        {
            "level": niveles[1],
            "preguntas": [
                {
                    "texto": "¿Qué palabra se usa para iniciar una condición en Python?",
                    "alternativas": [
                        ("if", True),
                        ("when", False),
                        ("cond", False),
                        ("case", False),
                    ]
                },
                {
                    "texto": "¿Qué palabra se usa para una segunda condición?",
                    "alternativas": [
                        ("elif", True),
                        ("else if", False),
                        ("elseif", False),
                        ("other", False),
                    ]
                },
                {
                    "texto": "¿Qué bloque se ejecuta si ninguna condición se cumple?",
                    "alternativas": [
                        ("else", True),
                        ("elif", False),
                        ("if", False),
                        ("default", False),
                    ]
                },
                {
                    "texto": "¿Qué operador se usa para comparar igualdad?",
                    "alternativas": [
                        ("==", True),
                        ("=", False),
                        ("!=", False),
                        (":=", False),
                    ]
                },
            ]
        },

        # NIVEL 3: Bucles 
        {
            "level": niveles[2],
            "preguntas": [
                {
                    "texto": "¿Qué bucle se usa para recorrer una lista?",
                    "alternativas": [
                        ("for", True),
                        ("while", False),
                        ("loop", False),
                        ("repeat", False),
                    ]
                },
                {
                    "texto": "¿Qué bucle se ejecuta mientras una condición sea verdadera?",
                    "alternativas": [
                        ("while", True),
                        ("for", False),
                        ("loop", False),
                        ("until", False),
                    ]
                },
                {
                    "texto": "¿Qué palabra detiene un bucle?",
                    "alternativas": [
                        ("break", True),
                        ("stop", False),
                        ("exit", False),
                        ("end", False),
                    ]
                },
                {
                    "texto": "¿Qué palabra salta a la siguiente iteración?",
                    "alternativas": [
                        ("continue", True),
                        ("break", False),
                        ("next", False),
                        ("pass", False),
                    ]
                },
            ]
        },

        # NIVEL 4: Funciones 
        {
            "level": niveles[3],
            "preguntas": [
                {
                    "texto": "¿Qué palabra se usa para definir una función?",
                    "alternativas": [
                        ("def", True),
                        ("function", False),
                        ("func", False),
                        ("define", False),
                    ]
                },
                {
                    "texto": "¿Qué palabra devuelve un valor en una función?",
                    "alternativas": [
                        ("return", True),
                        ("give", False),
                        ("send", False),
                        ("output", False),
                    ]
                },
                {
                    "texto": "¿Cómo se llama la información que recibe una función?",
                    "alternativas": [
                        ("parametros", True),
                        ("variables", False),
                        ("datos", False),
                        ("argumentos", False),
                    ]
                },
                {
                    "texto": "¿Cómo se llama ejecutar una función?",
                    "alternativas": [
                        ("llamar la funcion", True),
                        ("crear la funcion", False),
                        ("definir la funcion", False),
                        ("compilar", False),
                    ]
                },
            ]
        },

        # ■■ NIVEL 5: Listas ■■
        {
            "level": niveles[4],
            "preguntas": [
                {
                    "texto": "¿Cómo se define una lista en Python?",
                    "alternativas": [
                        ("[]", True),
                        ("()", False),
                        ("{}", False),
                        ("<>", False),
                    ]
                },
                {
                    "texto": "¿Qué método agrega un elemento a una lista?",
                    "alternativas": [
                        ("append()", True),
                        ("add()", False),
                        ("push()", False),
                        ("insertar()", False),
                    ]
                },
                {
                    "texto": "¿Qué función devuelve el tamaño de una lista?",
                    "alternativas": [
                        ("len()", True),
                        ("size()", False),
                        ("count()", False),
                        ("length()", False),
                    ]
                },
                {
                    "texto": "¿Qué método elimina el último elemento?",
                    "alternativas": [
                        ("pop()", True),
                        ("remove()", False),
                        ("delete()", False),
                        ("clear()", False),
                    ]
                },
            ]
        },

        # ■■ NIVEL 6: POO ■■
        {
            "level": niveles[5],
            "preguntas": [
                {
                    "texto": "¿Qué palabra se usa para definir una clase en Python?",
                    "alternativas": [
                        ("class", True),
                        ("def", False),
                        ("object", False),
                        ("create", False),
                    ]
                },
                {
                    "texto": "¿Qué es un objeto en programación orientada a objetos?",
                    "alternativas": [
                        ("una instancia de una clase", True),
                        ("una variable simple", False),
                        ("una lista", False),
                        ("una funcion", False),
                    ]
                },
                {
                    "texto": "¿Qué método se ejecuta automáticamente al crear un objeto?",
                    "alternativas": [
                        ("__init__", True),
                        ("start()", False),
                        ("create()", False),
                        ("build()", False),
                    ]
                },
                {
                    "texto": "¿Qué significa herencia en programación?",
                    "alternativas": [
                        ("una clase puede heredar atributos y metodos de otra", True),
                        ("copiar variables entre funciones", False),
                        ("repetir codigo", False),
                        ("crear listas", False),
                    ]
                },
            ]
        },

        ]

        # Inserta datos
        for nivel_data in contenido:
            for p in nivel_data["preguntas"]:
                pregunta = Pregunta(
                    id_level=nivel_data["level"].id,
                    preguntas=p["texto"]
                )

                db.session.add(pregunta)
                db.session.flush()

                for texto, correcta in p["alternativas"]:
                    db.session.add(Alternativa(
                        id_preguntas=pregunta.id,
                        alternativas=texto,
                        correcta=correcta
                    ))

        db.session.commit()

        print("Base de datos cargada correctamente.")
        print(f"Niveles: {Level.query.count()}")
        print(f"Preguntas: {Pregunta.query.count()}")
        print(f"Alternativas: {Alternativa.query.count()}")

if __name__ == '__main__':
    seed()