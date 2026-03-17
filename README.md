# Pingui Code 🐧

**Pingui Code** es una plataforma de aprendizaje interactiva, inspirada en Duolingo, diseñada para dominar conceptos de **Python** a través de cuestionarios dinámicos y divertidos.

---

## ✨ Características Principales

- **Aprendizaje Progresivo:** Cuestionarios organizados por niveles de dificultad dentro de un Roadmap interactivo.
- **Sistema de Usuarios Inteligente:** Inicio de sesión simplificado. Si el usuario no existe, el sistema crea un nuevo perfil automáticamente al ingresar por primera vez.
- **Sistema de Comodines:** Para ayudar en el aprendizaje, cada usuario cuenta con **3 comodines por nivel** que permiten eliminar una de las opciones incorrectas en las preguntas más difíciles.
- **Persistencia de Datos:** Seguimiento del progreso, puntajes y niveles completados mediante SQLAlchemy y SQLite.

---

## 🛠️ Tecnologías Utilizadas

| Capa | Tecnología |
|------|------------|
| Backend | Flask (Python) |
| Base de Datos | SQLite + SQLAlchemy |
| Frontend | HTML, CSS (Tailwind) y JavaScript |

---

## 🚀 Instalación y Configuración

Sigue estos pasos para ejecutar el proyecto en tu entorno local.

### 1. Clonar el repositorio

```bash
git clone https://github.com/AndyLargosta/roadmap-programacion
cd pingui-code
```

### 2. Crear y activar el entorno virtual

Es fundamental usar un entorno virtual para mantener las dependencias aisladas.

**En Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**En Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Instalar dependencias

Con el entorno virtual activo, instalá los paquetes necesarios:

```bash
pip install -r requirements.txt
```

### 4. Poblar la base de datos (Seed)

Para cargar los niveles, las preguntas y las alternativas iniciales, ejecutá el script de semillas. **Este paso es obligatorio** para ver contenido en la aplicación:

```bash
python seed.py
```

### 5. Ejecutar la aplicación

Iniciá el servidor de Flask:

```bash
python app.py
```

La aplicación estará disponible en tu navegador en:

```
http://127.0.0.1:5000
```