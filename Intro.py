import streamlit as st
from PIL import Image

# --------------------------------------------------
# CONFIGURACIÓN
# --------------------------------------------------

st.set_page_config(
    page_title="Aplicaciones de Inteligencia Artificial",
    page_icon="🤖",
    layout="wide"
)

# --------------------------------------------------
# ESTILOS
# --------------------------------------------------

st.markdown("""
<style>

    /* Fondo general */
    .stApp {
        background: #FFFDF5;
    }

    /* Barra lateral */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #5B2A86 0%, #7B3FB5 100%);
    }

    [data-testid="stSidebar"] h2,
    [data-testid="stSidebar"] h3,
    [data-testid="stSidebar"] p {
        color: white;
    }

    /* Título principal */
    .titulo {
        background: linear-gradient(90deg, #5B2A86, #8B4FCB);
        color: white;
        padding: 35px;
        border-radius: 25px;
        text-align: center;
        margin-bottom: 25px;
        box-shadow: 0px 8px 20px rgba(91, 42, 134, 0.20);
    }

    .titulo h1 {
        font-size: 42px;
        margin-bottom: 8px;
    }

    .titulo p {
        font-size: 18px;
        margin: 0;
    }

    /* Sección del enlace */
    .intro {
        background: #FFF1A8;
        padding: 20px 25px;
        border-radius: 18px;
        margin: 20px 0 30px 0;
        border-left: 8px solid #F2C94C;
    }

    .intro h3 {
        color: #4A206B;
        margin-bottom: 5px;
    }

    /* Tarjetas */
    .card {
        background: white;
        border-radius: 20px;
        padding: 20px;
        margin-bottom: 25px;
        min-height: 330px;
        box-shadow: 0px 5px 18px rgba(70, 40, 100, 0.12);
        border: 2px solid #EEE5F5;
        transition: 0.3s;
    }

    .card:hover {
        transform: translateY(-5px);
        box-shadow: 0px 10px 25px rgba(91, 42, 134, 0.20);
    }

    .card h3 {
        color: #5B2A86;
        font-size: 21px;
        margin-bottom: 10px;
    }

    .card p {
        color: #555555;
        font-size: 15px;
        line-height: 1.5;
    }

    /* Etiquetas */
    .tag-purple {
        display: inline-block;
        background: #E8D8F5;
        color: #5B2A86;
        padding: 5px 12px;
        border-radius: 20px;
        font-size: 12px;
        font-weight: bold;
        margin-bottom: 10px;
    }

    .tag-yellow {
        display: inline-block;
        background: #FFF1A8;
        color: #735900;
        padding: 5px 12px;
        border-radius: 20px;
        font-size: 12px;
        font-weight: bold;
        margin-bottom: 10px;
    }

    /* Botones */
    .boton {
        display: inline-block;
        background: #5B2A86;
        color: white !important;
        text-decoration: none;
        padding: 9px 18px;
        border-radius: 12px;
        font-weight: bold;
        margin-top: 8px;
    }

    .boton:hover {
        background: #F2C94C;
        color: #4A206B !important;
    }

    /* Decoraciones */
    .decoracion {
        color: #F2C94C;
        font-size: 28px;
        text-align: center;
        margin: 5px;
    }

    /* Footer */
    .footer {
        text-align: center;
        color: #7B3FB5;
        margin-top: 30px;
        padding: 20px;
        font-size: 14px;
    }

</style>
""", unsafe_allow_html=True)


# --------------------------------------------------
# BARRA LATERAL
# --------------------------------------------------

with st.sidebar:

    st.markdown("## 🤖 IA")

    st.markdown("---")

    st.markdown("### Aplicaciones con Inteligencia Artificial")

    st.write(
        "La inteligencia artificial permite mejorar la toma de decisiones "
        "con el uso de datos, automatizar tareas rutinarias y proporcionar "
        "análisis avanzados en tiempo real."
    )

    st.markdown("---")

    st.markdown("### ✨ ¿Qué encontrarás?")

    st.write("🎙️ Conversión de voz")
    st.write("👁️ Reconocimiento de imágenes")
    st.write("📊 Análisis de datos")
    st.write("📄 Análisis de documentos")
    st.write("🧠 Entrenamiento de modelos")
    st.write("🔊 Transcripción de audio")


# --------------------------------------------------
# ENCABEZADO
# --------------------------------------------------

st.markdown("""
<div class="titulo">

<h1>🤖 Aplicaciones de Inteligencia Artificial</h1>

<p>
Explora diferentes herramientas y aplicaciones prácticas de IA
</p>

</div>
""", unsafe_allow_html=True)


# --------------------------------------------------
# ENLACE PRINCIPAL
# --------------------------------------------------

url_ia = "https://sites.google.com/view/aplicacionesdeia/inicio"

st.markdown("""
<div class="intro">

<h3>✨ Explora más aplicaciones</h3>

<p>
En el siguiente enlace puedes encontrar páginas y ejercicios prácticos
relacionados con Inteligencia Artificial.
</p>

</div>
""", unsafe_allow_html=True)

st.markdown(
    f'<a class="boton" href="{url_ia}" target="_blank">🔗 Ver páginas y ejercicios</a>',
    unsafe_allow_html=True
)

st.markdown("<div class='decoracion'>◆ ◇ ◆</div>", unsafe_allow_html=True)


# --------------------------------------------------
# COLUMNAS
# --------------------------------------------------

col1, col2, col3 = st.columns(3)


# ==================================================
# COLUMNA 1
# ==================================================

with col1:

    # TARJETA 1
    st.markdown("""
    <div class="card">
    <span class="tag-yellow">🎙️ AUDIO</span>
    <h3>Conversión de texto a voz</h3>
    """, unsafe_allow_html=True)

    image = Image.open("txt_to_audio2.png")
    st.image(image, width=190)

    st.write(
        "Convierte texto escrito en voz utilizando una aplicación "
        "basada en Inteligencia Artificial."
    )

    st.markdown(
        '<a class="boton" href="https://imultimod.streamlit.app/" target="_blank">Probar aplicación →</a>',
        unsafe_allow_html=True
    )

    st.markdown("</div>", unsafe_allow_html=True)


    # TARJETA 2
    st.markdown("""
    <div class="card">
    <span class="tag-purple">👁️ VISIÓN</span>
    <h3>Reconocimiento de Objetos</h3>
    """, unsafe_allow_html=True)

    image = Image.open("txt_to_audio.png")
    st.image(image, width=200)

    st.write(
        "Observa cómo la Inteligencia Artificial puede detectar "
        "y reconocer diferentes objetos dentro de una imagen."
    )

    st.markdown(
        '<a class="boton" href="https://yolov5cmc.streamlit.app/" target="_blank">Probar YOLO →</a>',
        unsafe_allow_html=True
    )

    st.markdown("</div>", unsafe_allow_html=True)


    # TARJETA 3
    st.markdown("""
    <div class="card">
    <span class="tag-yellow">🧠 MODELOS</span>
    <h3>Entrenando Modelos</h3>
    """, unsafe_allow_html=True)

    image = Image.open("OIG5.jpg")
    st.image(image, width=200)

    st.write(
        "Conoce cómo utilizar un modelo de Inteligencia Artificial "
        "después de haberlo entrenado."
    )

    st.markdown(
        '<a class="boton" href="https://xn3pg24ztuv6fdiqon8qn3.streamlit.app/" target="_blank">Probar modelo →</a>',
        unsafe_allow_html=True
    )

    st.markdown("</div>", unsafe_allow_html=True)


# ==================================================
# COLUMNA 2
# ==================================================

with col2:

    # TARJETA 4
    st.markdown("""
    <div class="card">
    <span class="tag-purple">🗣️ VOZ</span>
    <h3>Conversión de voz a texto</h3>
    """, unsafe_allow_html=True)

    image = Image.open("OIG8.jpg")
    st.image(image, width=200)

    st.write(
        "Explora una aplicación capaz de transformar "
        "voz en texto mediante Inteligencia Artificial."
    )

    st.markdown(
        '<a class="boton" href="https://traductorw.streamlit.app/" target="_blank">Probar aplicación →</a>',
        unsafe_allow_html=True
    )

    st.markdown("</div>", unsafe_allow_html=True)


    # TARJETA 5
    st.markdown("""
    <div class="card">
    <span class="tag-yellow">📊 DATOS</span>
    <h3>Análisis de Datos</h3>
    """, unsafe_allow_html=True)

    image = Image.open("data_analisis.png")
    st.image(image, width=190)

    st.write(
        "Descubre cómo utilizar agentes de Inteligencia Artificial "
        "para analizar diferentes tipos de datos."
    )

    st.markdown(
        '<a class="boton" href="https://dataagente.streamlit.app/" target="_blank">Analizar datos →</a>',
        unsafe_allow_html=True
    )

    st.markdown("</div>", unsafe_allow_html=True)


    # TARJETA 6
    st.markdown("""
    <div class="card">
    <span class="tag-purple">📝 AUDIO / VIDEO</span>
    <h3>Transcriptor de Audio y Video</h3>
    """, unsafe_allow_html=True)

    image = Image.open("OIG3.jpg")
    st.image(image, width=200)

    st.write(
        "Realiza transcripciones automáticas de archivos "
        "de audio y video."
    )

    st.markdown(
        '<a class="boton" href="https://transcript-whisper.streamlit.app/" target="_blank">Transcribir →</a>',
        unsafe_allow_html=True
    )

    st.markdown("</div>", unsafe_allow_html=True)


# ==================================================
# COLUMNA 3
# ==================================================

with col3:

    # TARJETA 7
    st.markdown("""
    <div class="card">
    <span class="tag-yellow">📄 DOCUMENTOS</span>
    <h3>Generación en Contexto</h3>
    """, unsafe_allow_html=True)

    image = Image.open("Chat_pdf.png")
    st.image(image, width=190)

    st.write(
        "Utiliza RAG para interactuar con la información "
        "contenida dentro de un documento PDF."
    )

    st.markdown(
        '<a class="boton" href="https://chatpdf-cc.streamlit.app/" target="_blank">Probar RAG →</a>',
        unsafe_allow_html=True
    )

    st.markdown("</div>", unsafe_allow_html=True)


    # TARJETA 8
    st.markdown("""
    <div class="card">
    <span class="tag-purple">👁️ IMÁGENES</span>
    <h3>Análisis de Imagen</h3>
    """, unsafe_allow_html=True)

    image = Image.open("OIG4.jpg")
    st.image(image, width=200)

    st.write(
        "Explora la capacidad de la Inteligencia Artificial "
        "para analizar e interpretar imágenes."
    )

    st.markdown(
        '<a class="boton" href="https://vision2-gpt4o.streamlit.app/" target="_blank">Analizar imagen →</a>',
        unsafe_allow_html=True
    )

    st.markdown("</div>", unsafe_allow_html=True)


    # TARJETA 9
    st.markdown("""
    <div class="card">
    <span class="tag-yellow">⚙️ INTERACCIÓN</span>
    <h3>Sistema Ciberfísico</h3>
    """, unsafe_allow_html=True)

    image = Image.open("OIG6.jpg")
    st.image(image, width=200)

    st.write(
        "Explora la interacción entre la Inteligencia Artificial "
        "y el mundo físico."
    )

    st.markdown(
        '<a class="boton" href="https://vision2-gpt4o.streamlit.app/" target="_blank">Ver aplicación →</a>',
        unsafe_allow_html=True
    )

    st.markdown("</div>", unsafe_allow_html=True)


# --------------------------------------------------
# PIE DE PÁGINA
# --------------------------------------------------

st.markdown("""
<div class="footer">
    <div class="decoracion">◆ ◇ ◆</div>
    🤖 Explorando las posibilidades de la Inteligencia Artificial
    <br>
    <small>Aplicaciones y ejercicios prácticos</small>
</div>
""", unsafe_allow_html=True)

