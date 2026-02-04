# TITULO DEL PROYECTO
ForLiveRunning | Domina tu Ruta

"La naturaleza te llama, ForLive te guía."

ForLiveRunning es una aplicación web de mapas diseñada para corredores de trail y aventureros. Combina una estética inmersiva "Dark Mode" con funcionalidades de seguridad críticas, visualización topográfica y una experiencia de usuario optimizada para situaciones de movimiento.

# CÓMO CORRER EL PROYECTO

Este proyecto consta de un frontend estático (HTML/JS) y un backend ligero en Python (Flask) para simular la persistencia de datos.

 - # Prerrequisitos

-   Python 3.x instalado.

-   Navegador web moderno.

# Pasos para instalarlo

- # Clonar o descargar el repositorio.
-   Instalar dependencias del Backend:
-   Abre tu terminal en la carpeta del proyecto y ejecuta:

    -   pip install flask flask-cors


-   Iniciar el Servidor:
-   Ejecuta el archivo principal de la aplicación:

    -   python main.py


-   Deberías ver un mensaje indicando que el servidor corre en http://localhost:5000.

# STACK TECNOLOGÓGICO

-   Frontend:

    -   HTML5 & JavaScript (ES6+): Lógica del cliente y estructura semántica.

    -   Tailwind CSS (vía CDN): Estilizado utilitario rápido, diseño responsivo y animaciones personalizadas.

    -   Leaflet.js: Renderizado de mapas interactivos y gestión de marcadores.

    -   Phosphor Icons: Iconografía vectorial limpia y universal.

-   Backend:

    -   Python & Flask: API RESTful simple para manejar solicitudes POST asíncronas.

    -   Flask-CORS: Manejo de seguridad para permitir peticiones entre el frontend local y el servidor.

# JUSTIFICACIÓN DE DISEÑO

El diseño de la interfaz se centró en dos pilares: Aventurera y Segura.
- Estética "Dark Adventure":
    -   Se utilizó una paleta de colores oscuros (Slate-900) para reducir la fatiga visual y ahorrar batería en dispositivos móviles durante rutas largas.

    -   El color de acento Naranja Seguridad (#f97316) se usó exclusivamente para acciones críticas (CTA, Guardar, Ubicación actual) asegurando un contraste alto y visibilidad inmediata.

- Ergonomía Móvil (Thumb Zone):

    -   Los controles de zoom y navegación se movieron a la parte inferior de la pantalla, facilitando el uso con una sola mano (el pulgar) mientras se corre.

    -   En dispositivos móviles, la vista se adapta a un sistema de pestañas (Tabs) para maximizar el área visible del mapa.

# CREDITOS A LA IA

Este código fue co-creado con Gemini Canvas.
- Prompt principal utilizado para la generación:
    -   "Crea una Landing Page HTML para una app de mapas llamada [ForLiveRunning]. Debe tener un 'Hero' con una imagen de fondo de un mapa estilizado o topográfico, un título grande, y un botón CTA prominente que diga 'Explorar Mapa'. Usa Tailwind CSS. El diseño debe inspirar aventura/seguridad..."
