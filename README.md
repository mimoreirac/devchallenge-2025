# Carros Compartidos PUCE - Dev Challenge 2025

![Carros Compartidos PUCE](Dashboard.png)

Bienvenido al repositorio de Carros Compartidos PUCE, una app web para el agendamiento de viajes compartidos en la comunidad universitaria PUCE.

Impulsemos el transporte sostenible y ecológico!

## Descripción

Carros Compartidos PUCE es una aplicación web que permite a los estudiantes, profesores y personal de la Pontificia Universidad Católica del Ecuador (PUCE) organizar y compartir viajes en auto. La aplicación tiene como objetivo reducir el número de vehículos en el campus, disminuir la congestión del tráfico y promover un medio de transporte más sostenible y ecológico.

### Características

*   **Publicación de anuncios:** Los conductores pueden publicar anuncios de sus viajes, especificando el origen, el destino, la hora de salida y llegada, el sector y un número de contacto.
*   **Registro de usuarios:** Los usuarios pueden registrarse en la aplicación utilizando su correo electrónico de la PUCE.
*   **Autenticación de usuarios:** Los usuarios pueden iniciar sesión en la aplicación para acceder a todas las funciones.
*   **Edición de anuncios:** Los conductores pueden editar sus anuncios de viaje.
*   **Detalles del anuncio:** Los usuarios pueden ver los detalles de un anuncio de viaje, incluida la información del conductor.

## Tecnologías Utilizadas

*   **Python:** El lenguaje de programación principal utilizado en el proyecto.
*   **Django:** Un framework de desarrollo web de alto nivel para Python.
*   **SQLite:** La base de datos utilizada para el desarrollo.
*   **HTML/CSS/JavaScript:** Las tecnologías utilizadas para el frontend de la aplicación.
*   **Bootstrap:** Un framework de CSS para el diseño de la interfaz de usuario.
*   **django-allauth:** Una aplicación de Django para la autenticación de usuarios.
*   **django-widget-tweaks:** Una aplicación de Django para personalizar los widgets de los formularios.
*   **django-slippers:** Una aplicación de Django para reutilizar componentes de plantillas.
*   **django-phonenumber-field:** Una aplicación de Django para validar y mostrar números de teléfono.

## Estructura del Proyecto

```
devchallenge-2025/
├── carroscompartidos/      # La aplicación principal de Django
│   ├── migrations/         # Las migraciones de la base de datos
│   ├── templates/          # Las plantillas HTML de la aplicación
│   ├── admin.py            # La configuración del panel de administración
│   ├── apps.py             # La configuración de la aplicación
│   ├── forms.py            # Los formularios de la aplicación
│   ├── models.py           # Los modelos de la base de datos
│   ├── tests.py            # Las pruebas de la aplicación
│   ├── urls.py             # Las URLs de la aplicación
│   └── views.py            # Las vistas de la aplicación
├── devchallenge/           # El proyecto de Django
│   ├── settings.py         # La configuración del proyecto
│   ├── urls.py             # Las URLs del proyecto
│   └── ...
├── static/                 # Los archivos estáticos de la aplicación
│   └── css/
│       └── custom.css
├── .gitignore              # Los archivos y directorios ignorados por Git
├── db.sqlite3              # La base de datos de la aplicación
├── manage.py               # El script de gestión de Django
├── README.md               # La documentación del proyecto
└── requirements.txt        # Las dependencias de Python
```

## Instalación y Ejecución

Sigue estos pasos para instalar y ejecutar la aplicación en tu máquina local:

### Prerrequisitos

*   Python 3.10 o superior
*   pip (el gestor de paquetes de Python)

### Instalación del ambiente

1.  **Clona el repositorio:**

    ```bash
    git clone https://github.com/tu-usuario/devchallenge-2025.git
    cd devchallenge-2025
    ```

2.  **Crea y activa un entorno virtual:**

    ```bash
    python -m venv .venv
    .venv\Scripts\activate
    ```

3.  **Instala las dependencias:**

    ```bash
    pip install -r requirements.txt
    ```

### Ejecución de la Aplicación

1.  **Aplica las migraciones de la base de datos:**

    ```bash
    python manage.py migrate
    ```

2.  **Crea un superusuario para acceder al panel de administración:**

    ```bash
    python manage.py createsuperuser
    ```

3.  **Inicia el servidor de desarrollo:**

    ```bash
    python manage.py runserver
    ```

4.  **Abre tu navegador y visita `http://127.0.0.1:8000/` para ver la aplicación.**
