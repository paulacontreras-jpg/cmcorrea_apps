import streamlit as st
from PIL import Image

# =========================================================
# CONFIGURACIÓN
# =========================================================

st.set_page_config(
    page_title="Aplicaciones de Inteligencia Artificial",
    page_icon="🤖",
    layout="wide"
)


# =========================================================
# CSS
# =========================================================

st.markdown("""
<style>

    /* ===== FONDO ===== */

    .stApp {
        background-color: #FFFDF5;
    }


    /* ===== SIDEBAR ===== */

    [data-testid="stSidebar"] {
        background: linear-gradient(
            180deg,
            #54257A 0%,
            #7B3FB5 100%
        );
    }

    [data-testid="stSidebar"] h2,
    [data-testid="stSidebar"] h3,
    [data-testid="stSidebar"] p {
        color: white;
    }


    /* ===== TÍTULO ===== */

    .main-title {
        background: linear-gradient(
            135deg,
            #54257A,
            #8146B5
        );

        padding: 35px 25px;

        border-radius: 25px;

        text-align: center;

        margin-bottom: 25px;

        box-shadow:
            0 8px 20px rgba(84, 37, 122, 0.20);
    }

    .main-title h1 {
        color: white;
        font-size: 40px;
        margin: 0;
    }

    .main-title p {
        color: #F8EFFF;
        font-size: 17px;
        margin-top: 10px;
    }


    /* ===== INTRO ===== */

    .intro-box {
        background-color: #FFF1A8;

        border-left: 7px solid #F2C94C;

        border-radius: 15px;

        padding: 18px 22px;

        margin-bottom: 10px;
    }

    .intro-box h3 {
        color: #54257A;
        margin: 0 0 5px 0;
    }

    .intro-box p {
        color: #5A4A00;
        margin: 0;
    }


    /* ===== BOTÓN PRINCIPAL ===== */

    .main-button {
        display: inline-block;

        background-color: #54257A;

        color: white !important;

        padding: 11px 22px;

        border-radius: 12px;

        text-decoration: none !important;

        font-weight: bold;

        margin-bottom: 20px;
    }

    .main-button:hover {
        background-color: #F2C94C;
        color: #54257A !important;
    }


    /* ===== TARJETAS ===== */

    .card-box {
        background-color: white;

        border: 2px solid #E8DDF0;

        border-radius: 20px;

        padding: 18px;

        margin-bottom: 22px;

        text-align: center;

        box-shadow:
            0 5px 15px rgba(84, 37, 122, 0.10);
    }


    /* ===== ETIQUETAS ===== */

    .purple-tag {
        display: inline-block;

        background-color: #E9D8F5;

        color: #54257A;

        padding: 5px 12px;

        border-radius: 20px;

        font-size: 12px;

        font-weight: bold;

        margin-bottom: 8px;
    }


    .yellow-tag {
        display: inline-block;

        background-color: #FFF1A8;

        color: #665000;

        padding: 5px 12px;

        border-radius: 20px;

        font-size: 12px;

        font-weight: bold;

        margin-bottom: 8px;
    }


    /* ===== TÍTULO DE TARJETA ===== */

    .card-title {
        color: #54257A;

        font-size: 20px;

        font-weight: bold;

        min-height: 55px;

        display: flex;

        align-items: center;

        justify-content: center;

        margin-bottom: 5px;
    }


    /* ===== DESCRIPCIÓN ===== */

    .card-text {
        color: #555555;

        font-size: 14px;

        line-height: 1.5;

        min-height: 65px;

        margin-top: 10px;
    }


    /* ===== DECORACIÓN ===== */

    .decoration {
        text-align: center;

        color: #F2C94C;

        font-size: 25px;

        margin: 15px 0 20px 0;
    }


    /* ===== FOOTER ===== */

    .footer {
        text-align: center;

        color: #7B3FB5;

        margin-top: 20px;

        padding: 25px;
    }

</style>
""", unsafe_allow_html=True)


# =========================================================
# SIDEBAR
# =========================================================

with st.sidebar:

    st.markdown("## 🤖 Inteligencia Artificial")

    st.markdown("---")

    st.markdown("### Aplicaciones con IA")

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


# =========================================================
# ENCABEZADO
# =========================================================

st.markdown("""
<div class="main-title">

    <h1>🤖 Aplicaciones de Inteligencia Artificial</h1>

    <p>
        Explora diferentes herramientas y aplicaciones prácticas de IA
    </p>

</div>
""", unsafe_allow_html=True)


# =========================================================
# INTRODUCCIÓN
# =========================================================

st.markdown("""
<div class="intro-box">

    <h3>✨ Explora más aplicaciones</h3>

    <p>
        En el siguiente enlace puedes encontrar páginas y ejercicios
        prácticos relacionados con Inteligencia Artificial.
    </p>

</div>
""", unsafe_allow_html=True)


url_ia = "https://sites.google.com/view/aplicacionesdeia/inicio"

st.markdown(
    f"""
    <a
        class="main-button"
        href="{url_ia}"
        target="_blank">
        🔗 Ver páginas y ejercicios
    </a>
    """,
    unsafe_allow_html=True
)


st.markdown(
    '<div class="decoration">◆ ◇ ◆</div>',
    unsafe_allow_html=True
)


# =========================================================
# COLUMNAS
# =========================================================

col1, col2, col3 = st.columns(3)


# =========================================================
# COLUMNA 1
# =========================================================

with col1:

    # TARJETA 1
    with st.container(border=True):

        st.markdown(
            '<div class="yellow-tag">🎙️ AUDIO</div>',
            unsafe_allow_html=True
        )

        st.markdown(
            '<div class="card-title">Conversión de texto a voz</div>',
            unsafe_allow_html=True
        )

        image = Image.open("txt_to_audio2.png")
        st.image(image, width=190)

        st.markdown(
            '<div class="card-text">'
            'Convierte texto escrito en voz utilizando una aplicación '
            'basada en Inteligencia Artificial.'
            '</div>',
            unsafe_allow_html=True
        )

        st.link_button(
            "Probar aplicación →",
            "https://imultimod.streamlit.app/"
        )


    # TARJETA 2
    with st.container(border=True):

        st.markdown(
            '<div class="purple-tag">👁️ VISIÓN</div>',
            unsafe_allow_html=True
        )

        st.markdown(
            '<div class="card-title">Reconocimiento de Objetos</div>',
            unsafe_allow_html=True
        )

        image = Image.open("txt_to_audio.png")
        st.image(image, width=200)

        st.markdown(
            '<div class="card-text">'
            'Observa cómo la Inteligencia Artificial puede detectar '
            'y reconocer diferentes objetos dentro de una imagen.'
            '</div>',
            unsafe_allow_html=True
        )

        st.link_button(
            "Probar YOLO →",
            "https://yolov5cmc.streamlit.app/"
        )


    # TARJETA 3
    with st.container(border=True):

        st.markdown(
            '<div class="yellow-tag">🧠 MODELOS</div>',
            unsafe_allow_html=True
        )

        st.markdown(
            '<div class="card-title">Entrenando Modelos</div>',
            unsafe_allow_html=True
        )

        image = Image.open("OIG5.jpg")
        st.image(image, width=200)

        st.markdown(
            '<div class="card-text">'
            'Conoce cómo utilizar un modelo de Inteligencia Artificial '
            'después de haberlo entrenado.'
            '</div>',
            unsafe_allow_html=True
        )

        st.link_button(
            "Probar modelo →",
            "https://xn3pg24ztuv6fdiqon8qn3.streamlit.app/"
        )


# =========================================================
# COLUMNA 2
# =========================================================

with col2:

    # TARJETA 4
    with st.container(border=True):

        st.markdown(
            '<div class="purple-tag">🗣️ VOZ</div>',
            unsafe_allow_html=True
        )

        st.markdown(
            '<div class="card-title">Conversión de voz a texto</div>',
            unsafe_allow_html=True
        )

        image = Image.open("OIG8.jpg")
        st.image(image, width=200)

        st.markdown(
            '<div class="card-text">'
            'Explora una aplicación capaz de transformar voz '
            'en texto mediante Inteligencia Artificial.'
            '</div>',
            unsafe_allow_html=True
        )

        st.link_button(
            "Probar aplicación →",
            "https://traductorw.streamlit.app/"
        )


    # TARJETA 5
    with st.container(border=True):

        st.markdown(
            '<div class="yellow-tag">📊 DATOS</div>',
            unsafe_allow_html=True
        )

        st.markdown(
            '<div class="card-title">Análisis de Datos</div>',
            unsafe_allow_html=True
        )

        image = Image.open("data_analisis.png")
        st.image(image, width=190)

        st.markdown(
            '<div class="card-text">'
            'Descubre cómo utilizar agentes de Inteligencia Artificial '
            'para analizar diferentes tipos de datos.'
            '</div>',
            unsafe_allow_html=True
        )

        st.link_button(
            "Analizar datos →",
            "https://dataagente.streamlit.app/"
        )


    # TARJETA 6
    with st.container(border=True):

        st.markdown(
            '<div class="purple-tag">📝 AUDIO / VIDEO</div>',
            unsafe_allow_html=True
        )

        st.markdown(
            '<div class="card-title">Transcriptor de Audio y Video</div>',
            unsafe_allow_html=True
        )

        image = Image.open("OIG3.jpg")
        st.image(image, width=200)

        st.markdown(
            '<div class="card-text">'
            'Realiza transcripciones automáticas de archivos '
            'de audio y video.'
            '</div>',
            unsafe_allow_html=True
        )

        st.link_button(
            "Transcribir →",
            "https://transcript-whisper.streamlit.app/"
        )


# =========================================================
# COLUMNA 3
# =========================================================

with col3:

    # TARJETA 7
    with st.container(border=True):

        st.markdown(
            '<div class="yellow-tag">📄 DOCUMENTOS</div>',
            unsafe_allow_html=True
        )

        st.markdown(
            '<div class="card-title">Generación en Contexto</div>',
            unsafe_allow_html=True
        )

        image = Image.open("Chat_pdf.png")
        st.image(image, width=190)

        st.markdown(
            '<div class="card-text">'
            'Utiliza RAG para interactuar con la información '
            'contenida dentro de un documento PDF.'
            '</div>',
            unsafe_allow_html=True
        )

        st.link_button(
            "Probar RAG →",
            "https://chatpdf-cc.streamlit.app/"
        )


    # TARJETA 8
    with st.container(border=True):

        st.markdown(
            '<div class="purple-tag">👁️ IMÁGENES</div>',
            unsafe_allow_html=True
        )

        st.markdown(
            '<div class="card-title">Análisis de Imagen</div>',
            unsafe_allow_html=True
        )

        image = Image.open("OIG4.jpg")
        st.image(image, width=200)

        st.markdown(
            '<div class="card-text">'
            'Explora la capacidad de la Inteligencia Artificial '
            'para analizar e interpretar imágenes.'
            '</div>',
            unsafe_allow_html=True
        )

        st.link_button(
            "Analizar imagen →",
            "https://vision2-gpt4o.streamlit.app/"
        )


    # TARJETA 9
    with st.container(border=True):

        st.markdown(
            '<div class="yellow-tag">⚙️ INTERACCIÓN</div>',
            unsafe_allow_html=True
        )

        st.markdown(
            '<div class="card-title">Sistema Ciberfísico</div>',
            unsafe_allow_html=True
        )

        image = Image.open("OIG6.jpg")
        st.image(image, width=200)

        st.markdown(
            '<div class="card-text">'
            'Explora la interacción entre la Inteligencia Artificial '
            'y el mundo físico.'
            '</div>',
            unsafe_allow_html=True
        )

        st.link_button(
            "Ver aplicación →",
            "https://vision2-gpt4o.streamlit.app/"
        )


# =========================================================
# FOOTER
# =========================================================

st.markdown("""
<div class="footer">

    <div class="decoration">
        ◆ ◇ ◆
    </div>

    🤖 Explorando las posibilidades de la Inteligencia Artificial

    <br><br>

    <small>
        Aplicaciones y ejercicios prácticos
    </small>

</div>
""", unsafe_allow_html=True)
