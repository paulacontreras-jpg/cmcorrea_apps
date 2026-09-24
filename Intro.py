import streamlit as st
import base64

# ==================================================
# CONFIGURACIÓN
# ==================================================

st.set_page_config(
    page_title="Aplicaciones de Inteligencia Artificial",
    page_icon="🤖",
    layout="wide"
)


# ==================================================
# FUNCIONES
# ==================================================

def imagen_base64(ruta):
    with open(ruta, "rb") as archivo:
        return base64.b64encode(archivo.read()).decode()


def tarjeta(titulo, etiqueta, imagen, descripcion, url, color="purple"):

    img_base64 = imagen_base64(imagen)

    if color == "yellow":
        tag_class = "tag-yellow"
    else:
        tag_class = "tag-purple"

    st.markdown(f"""
    <div class="card">

        <span class="{tag_class}">{etiqueta}</span>

        <h3>{titulo}</h3>

        <img 
            src="data:image/png;base64,{img_base64}" 
            class="card-image"
        >

        <p>{descripcion}</p>

        <a 
            class="boton" 
            href="{url}" 
            target="_blank"
        >
            Probar aplicación →
        </a>

    </div>
    """, unsafe_allow_html=True)


# ==================================================
# CSS
# ==================================================

st.markdown("""
<style>

    /* ---------------------------------------------
       FONDO GENERAL
    --------------------------------------------- */

    .stApp {
        background: #FFFDF5;
    }


    /* ---------------------------------------------
       BARRA LATERAL
    --------------------------------------------- */

    [data-testid="stSidebar"] {
        background: linear-gradient(
            180deg,
            #5B2A86 0%,
            #7B3FB5 100%
        );
    }

    [data-testid="stSidebar"] h2,
    [data-testid="stSidebar"] h3,
    [data-testid="stSidebar"] p {
        color: white;
    }

    [data-testid="stSidebar"] hr {
        border-color: rgba(255,255,255,0.3);
    }


    /* ---------------------------------------------
       TÍTULO PRINCIPAL
    --------------------------------------------- */

    .titulo {
        background: linear-gradient(
            90deg,
            #5B2A86,
            #8B4FCB
        );

        color: white;

        padding: 35px;

        border-radius: 25px;

        text-align: center;

        margin-bottom: 25px;

        box-shadow:
            0px 8px 20px
            rgba(91, 42, 134, 0.20);
    }

    .titulo h1 {
        font-size: 42px;
        margin: 0 0 8px 0;
    }

    .titulo p {
        font-size: 18px;
        margin: 0;
    }


    /* ---------------------------------------------
       CAJA DE INTRODUCCIÓN
    --------------------------------------------- */

    .intro {
        background: #FFF1A8;

        padding: 20px 25px;

        border-radius: 18px;

        margin: 20px 0 15px 0;

        border-left: 8px solid #F2C94C;
    }

    .intro h3 {
        color: #4A206B;
        margin: 0 0 5px 0;
    }

    .intro p {
        color: #5A4A00;
        margin: 0;
    }


    /* ---------------------------------------------
       DECORACIÓN
    --------------------------------------------- */

    .decoracion {
        color: #F2C94C;

        font-size: 26px;

        text-align: center;

        margin: 18px 0;
    }


    /* ---------------------------------------------
       TARJETAS
    --------------------------------------------- */

    .card {

        background: white;

        border-radius: 20px;

        padding: 20px;

        margin-bottom: 25px;

        height: 430px;

        box-sizing: border-box;

        box-shadow:
            0px 5px 18px
            rgba(70, 40, 100, 0.12);

        border: 2px solid #EEE5F5;

        text-align: center;

        transition: all 0.25s ease;
    }


    .card:hover {

        transform: translateY(-5px);

        box-shadow:
            0px 10px 25px
            rgba(91, 42, 134, 0.20);

        border-color: #D8C0EA;
    }


    /* ---------------------------------------------
       ETIQUETAS
    --------------------------------------------- */

    .tag-purple {

        display: inline-block;

        background: #E8D8F5;

        color: #5B2A86;

        padding: 5px 12px;

        border-radius: 20px;

        font-size: 12px;

        font-weight: bold;

        margin-bottom: 7px;
    }


    .tag-yellow {

        display: inline-block;

        background: #FFF1A8;

        color: #735900;

        padding: 5px 12px;

        border-radius: 20px;

        font-size: 12px;

        font-weight: bold;

        margin-bottom: 7px;
    }


    /* ---------------------------------------------
       TÍTULO DE TARJETA
    --------------------------------------------- */

    .card h3 {

        color: #5B2A86;

        font-size: 20px;

        margin: 6px 0 10px 0;

        min-height: 48px;

        display: flex;

        align-items: center;

        justify-content: center;
    }


    /* ---------------------------------------------
       IMÁGENES
    --------------------------------------------- */

    .card-image {

        width: 190px;

        height: 145px;

        object-fit: contain;

        display: block;

        margin: 5px auto 15px auto;

        border-radius: 12px;
    }


    /* ---------------------------------------------
       DESCRIPCIÓN
    --------------------------------------------- */

    .card p {

        color: #555555;

        font-size: 14px;

        line-height: 1.45;

        min-height: 65px;

        margin: 5px 0 10px 0;
    }


    /* ---------------------------------------------
       BOTONES
    --------------------------------------------- */

    .boton {

        display: inline-block;

        background: #5B2A86;

        color: white !important;

        text-decoration: none;

        padding: 9px 18px;

        border-radius: 12px;

        font-weight: bold;

        margin-top: 5px;

        transition: all 0.2s ease;
    }


    .boton:hover {

        background: #F2C94C;

        color: #4A206B !important;

        text-decoration: none;
    }


    /* ---------------------------------------------
       BOTÓN PRINCIPAL
    --------------------------------------------- */

    .boton-principal {

        display: inline-block;

        background: #5B2A86;

        color: white !important;

        text-decoration: none;

        padding: 12px 24px;

        border-radius: 14px;

        font-weight: bold;

        font-size: 16px;

        transition: all 0.2s ease;
    }


    .boton-principal:hover {

        background: #F2C94C;

        color: #4A206B !important;

        text-decoration: none;
    }


    /* ---------------------------------------------
       FOOTER
    --------------------------------------------- */

    .footer {

        text-align: center;

        color: #7B3FB5;

        margin-top: 25px;

        padding: 20px;

        font-size: 14px;
    }


    /* ---------------------------------------------
       ESPACIADO ENTRE COLUMNAS
    --------------------------------------------- */

    [data-testid="column"] {
        padding: 0 8px;
    }

</style>
""", unsafe_allow_html=True)


# ==================================================
# BARRA LATERAL
# ==================================================

with st.sidebar:

    st.markdown("## 🤖 IA")

    st.markdown("---")

    st.markdown("### Aplicaciones con Inteligencia Artificial")

    st.write(
        "La inteligencia artificial permite mejorar la toma de "
        "decisiones con el uso de datos, automatizar tareas "
        "rutinarias y proporcionar análisis avanzados en tiempo real."
    )

    st.markdown("---")

    st.markdown("### ✨ ¿Qué encontrarás?")

    st.write("🎙️ Conversión de voz")
    st.write("👁️ Reconocimiento de imágenes")
    st.write("📊 Análisis de datos")
    st.write("📄 Análisis de documentos")
    st.write("🧠 Entrenamiento de modelos")
    st.write("🔊 Transcripción de audio")


# ==================================================
# ENCABEZADO
# ==================================================

st.markdown("""
<div class="titulo">

    <h1>🤖 Aplicaciones de Inteligencia Artificial</h1>

    <p>
        Explora diferentes herramientas y aplicaciones prácticas de IA
    </p>

</div>
""", unsafe_allow_html=True)


# ==================================================
# INTRODUCCIÓN
# ==================================================

url_ia = "https://sites.google.com/view/aplicacionesdeia/inicio"

st.markdown("""
<div class="intro">

    <h3>✨ Explora más aplicaciones</h3>

    <p>
        En el siguiente enlace puedes encontrar páginas y ejercicios
        prácticos relacionados con Inteligencia Artificial.
    </p>

</div>
""", unsafe_allow_html=True)

st.markdown(
    f"""
    <a 
        class="boton-principal"
        href="{url_ia}"
        target="_blank"
    >
        🔗 Ver páginas y ejercicios
    </a>
    """,
    unsafe_allow_html=True
)

st.markdown(
    "<div class='decoracion'>◆ ◇ ◆</div>",
    unsafe_allow_html=True
)


# ==================================================
# COLUMNAS
# ==================================================

col1, col2, col3 = st.columns(3)


# ==================================================
# COLUMNA 1
# ==================================================

with col1:

    tarjeta(
        titulo="Conversión de texto a voz",
        etiqueta="🎙️ AUDIO",
        imagen="txt_to_audio2.png",
        descripcion=(
            "Convierte texto escrito en voz utilizando "
            "una aplicación basada en Inteligencia Artificial."
        ),
        url="https://imultimod.streamlit.app/",
        color="yellow"
    )


    tarjeta(
        titulo="Reconocimiento de Objetos",
        etiqueta="👁️ VISIÓN",
        imagen="txt_to_audio.png",
        descripcion=(
            "Observa cómo la Inteligencia Artificial puede "
            "detectar y reconocer diferentes objetos dentro de una imagen."
        ),
        url="https://yolov5cmc.streamlit.app/",
        color="purple"
    )


    tarjeta(
        titulo="Entrenando Modelos",
        etiqueta="🧠 MODELOS",
        imagen="OIG5.jpg",
        descripcion=(
            "Conoce cómo utilizar un modelo de Inteligencia "
            "Artificial después de haberlo entrenado."
        ),
        url="https://xn3pg24ztuv6fdiqon8qn3.streamlit.app/",
        color="yellow"
    )


# ==================================================
# COLUMNA 2
# ==================================================

with col2:

    tarjeta(
        titulo="Conversión de voz a texto",
        etiqueta="🗣️ VOZ",
        imagen="OIG8.jpg",
        descripcion=(
            "Explora una aplicación capaz de transformar "
            "voz en texto mediante Inteligencia Artificial."
        ),
        url="https://traductorw.streamlit.app/",
        color="purple"
    )


    tarjeta(
        titulo="Análisis de Datos",
        etiqueta="📊 DATOS",
        imagen="data_analisis.png",
        descripcion=(
            "Descubre cómo utilizar agentes de Inteligencia "
            "Artificial para analizar diferentes tipos de datos."
        ),
        url="https://dataagente.streamlit.app/",
        color="yellow"
    )


    tarjeta(
        titulo="Transcriptor de Audio y Video",
        etiqueta="📝 AUDIO / VIDEO",
        imagen="OIG3.jpg",
        descripcion=(
            "Realiza transcripciones automáticas de archivos "
            "de audio y video."
        ),
        url="https://transcript-whisper.streamlit.app/",
        color="purple"
    )


# ==================================================
# COLUMNA 3
# ==================================================

with col3:

    tarjeta(
        titulo="Generación en Contexto",
        etiqueta="📄 DOCUMENTOS",
        imagen="Chat_pdf.png",
        descripcion=(
            "Utiliza RAG para interactuar con la información "
            "contenida dentro de un documento PDF."
        ),
        url="https://chatpdf-cc.streamlit.app/",
        color="yellow"
    )


    tarjeta(
        titulo="Análisis de Imagen",
        etiqueta="👁️ IMÁGENES",
        imagen="OIG4.jpg",
        descripcion=(
            "Explora la capacidad de la Inteligencia Artificial "
            "para analizar e interpretar imágenes."
        ),
        url="https://vision2-gpt4o.streamlit.app/",
        color="purple"
    )


    tarjeta(
        titulo="Sistema Ciberfísico",
        etiqueta="⚙️ INTERACCIÓN",
        imagen="OIG6.jpg",
        descripcion=(
            "Explora la interacción entre la Inteligencia "
            "Artificial y el mundo físico."
        ),
        url="https://vision2-gpt4o.streamlit.app/",
        color="yellow"
    )


# ==================================================
# FOOTER
# ==================================================

st.markdown("""
<div class="footer">

    <div class="decoracion">
        ◆ ◇ ◆
    </div>

    🤖 Explorando las posibilidades de la Inteligencia Artificial

    <br>

    <small>
        Aplicaciones y ejercicios prácticos
    </small>

</div>
""", unsafe_allow_html=True)
