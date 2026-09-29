```python
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

.stApp {
    background: #FFFDF7;
}

.block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
}

/* ================================
   SIDEBAR
================================ */

[data-testid="stSidebar"] {
    background: linear-gradient(
        180deg,
        #51247A 0%,
        #7139A3 55%,
        #8B4FCB 100%
    );
}

[data-testid="stSidebar"] h2,
[data-testid="stSidebar"] h3,
[data-testid="stSidebar"] p,
[data-testid="stSidebar"] span {
    color: white;
}

/* ================================
   TÍTULO
================================ */

.titulo {
    background: linear-gradient(
        135deg,
        #542580 0%,
        #7540A5 55%,
        #8D51C9 100%
    );

    color: white;
    padding: 38px 35px;
    border-radius: 28px;
    text-align: center;
    margin-bottom: 25px;

    box-shadow:
        0 12px 30px rgba(91, 42, 134, 0.18);

    position: relative;
    overflow: hidden;
}

.titulo::after {
    content: "✦";
    position: absolute;
    right: 35px;
    top: 18px;
    font-size: 40px;
    color: #F9D95C;
    opacity: 0.8;
}

.titulo h1 {
    font-size: 40px;
    margin: 0 0 10px 0;
    font-weight: 800;
}

.titulo p {
    font-size: 17px;
    margin: 0;
    opacity: 0.95;
}

/* ================================
   INTRO
================================ */

.intro {
    background: linear-gradient(
        135deg,
        #FFF6C7,
        #FFF0A0
    );

    padding: 20px 25px;
    border-radius: 20px;
    margin: 20px 0 15px 0;

    border-left: 7px solid #F2C94C;

    box-shadow:
        0 5px 15px rgba(180, 145, 30, 0.10);
}

.intro h3 {
    color: #4A206B;
    margin: 0 0 6px 0;
    font-size: 21px;
}

.intro p {
    color: #5F511B;
    margin: 0;
    font-size: 15px;
    line-height: 1.5;
}

/* ================================
   DECORACIÓN
================================ */

.decoracion {
    color: #E6B72D;
    font-size: 22px;
    text-align: center;
    margin: 18px 0;
    letter-spacing: 8px;
}

/* ================================
   TARJETAS
================================ */

.tarjeta {
    background: white;
    border: 1px solid #E9DDF2;
    border-radius: 22px;

    padding: 18px;
    margin-bottom: 25px;

    box-shadow:
        0 6px 20px rgba(70, 40, 100, 0.10);

    transition: all 0.25s ease;

    min-height: 480px;

    display: flex;
    flex-direction: column;
}

.tarjeta:hover {
    transform: translateY(-6px);

    box-shadow:
        0 14px 30px rgba(91, 42, 134, 0.18);

    border-color: #D8C4E8;
}

/* Etiquetas */

.tag-purple {
    display: inline-block;

    background: #E9D9F7;
    color: #5B2A86;

    padding: 6px 12px;
    border-radius: 30px;

    font-size: 11px;
    font-weight: 800;

    letter-spacing: 0.4px;

    margin-bottom: 10px;
}

.tag-yellow {
    display: inline-block;

    background: #FFF0A3;
    color: #705600;

    padding: 6px 12px;
    border-radius: 30px;

    font-size: 11px;
    font-weight: 800;

    letter-spacing: 0.4px;

    margin-bottom: 10px;
}

/* Título tarjeta */

.card-title {
    color: #542580;

    font-size: 20px;
    font-weight: 750;

    line-height: 1.25;

    min-height: 52px;

    margin-bottom: 10px;
}

/* Imagen */

.imagen-card {
    background: #FAF7FC;

    border-radius: 16px;

    padding: 8px;

    margin-bottom: 12px;

    text-align: center;

    border: 1px solid #EEE5F5;
}

.imagen-card img {
    max-height: 165px;
    width: auto;

    border-radius: 12px;
}

/* Descripción */

.card-description {
    color: #555555;

    font-size: 14px;

    line-height: 1.55;

    min-height: 95px;

    margin-bottom: 10px;
}

/* Botón */

.boton-card {
    display: inline-block;

    background: #5B2A86;
    color: white !important;

    text-decoration: none;

    padding: 10px 17px;

    border-radius: 12px;

    font-size: 13px;
    font-weight: 700;

    transition: all 0.25s ease;
}

.boton-card:hover {
    background: #F2C94C;
    color: #4A206B !important;

    transform: translateY(-2px);

    box-shadow:
        0 6px 15px rgba(242, 201, 76, 0.30);
}

/* ================================
   FOOTER
================================ */

.footer {
    text-align: center;

    color: #76519A;

    margin-top: 35px;
    padding: 25px;

    font-size: 14px;
}

.footer small {
    color: #9A83B0;
}

/* ================================
   RESPONSIVE
================================ */

@media (max-width: 900px) {

    .titulo h1 {
        font-size: 32px;
    }

    .titulo {
        padding: 30px 20px;
    }

}

</style>
""", unsafe_allow_html=True)


# --------------------------------------------------
# FUNCIÓN PARA CREAR TARJETAS
# --------------------------------------------------

def tarjeta(tag, tipo, titulo, imagen, descripcion, url):

    if tipo == "yellow":
        tag_class = "tag-yellow"
    else:
        tag_class = "tag-purple"

    st.markdown(
        f"""
        <div class="tarjeta">

            <span class="{tag_class}">
                {tag}
            </span>

            <div class="card-title">
                {titulo}
            </div>

            <div class="imagen-card">
        """,
        unsafe_allow_html=True
    )

    # Imagen
    image = Image.open(imagen)

    st.image(
        image,
        use_container_width=True
    )

    st.markdown(
        f"""
            </div>

            <div class="card-description">
                {descripcion}
            </div>

            <a
                class="boton-card"
                href="{url}"
                target="_blank"
            >
                Probar aplicación →
            </a>

        </div>
        """,
        unsafe_allow_html=True
    )


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
        Explora herramientas y proyectos interactivos
        creados con Inteligencia Artificial
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
        Encuentra páginas, experimentos y ejercicios prácticos
        relacionados con Inteligencia Artificial.
    </p>

</div>
""", unsafe_allow_html=True)

st.markdown(
    f"""
    <a
        class="boton-card"
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


# --------------------------------------------------
# COLUMNAS
# --------------------------------------------------

col1, col2, col3 = st.columns(3, gap="large")


# ==================================================
# COLUMNA 1
# ==================================================

with col1:

    tarjeta(
        "🎙️ AUDIO",
        "yellow",
        "Conversión de texto a voz",
        "txt_to_audio2.png",
        "Convierte texto escrito en voz utilizando una aplicación basada en Inteligencia Artificial.",
        "https://interfazmultimodal1-paula.streamlit.app/"
    )

    tarjeta(
        "🌟 CHAT",
        "purple",
        "INTRO: Mi mood de hoy",
        "txt_to_audio.png",
        "Un espacio interactivo para compartir mi estado de ánimo, explorar emociones y descubrir qué tan relatable es mi mood del día.",
        "https://introstrelit.streamlit.app/"
    )

    tarjeta(
        "🧠 CÁMARA",
        "yellow",
        "Reconocimiento Óptico de Caracteres",
        "OIG5.jpg",
        "Convierte imágenes en texto de forma rápida y sencilla. Sube o toma una fotografía y el sistema reconocerá automáticamente las palabras que contiene.",
        "https://4di4tgzegjkvtdx98nnspw.streamlit.app/"
    )


# ==================================================
# COLUMNA 2
# ==================================================

with col2:

    tarjeta(
        "🗣️ VOZ",
        "purple",
        "Traductor",
        "OIG8.jpg",
        "Una herramienta interactiva para traducir lo que dices. Presiona el botón, habla cuando escuches la señal y selecciona el idioma que necesitas.",
        "https://traductorr5d9v9t32kchhniyxnsdos.streamlit.app/"
    )

    tarjeta(
        "🧠 CÁMARA",
        "yellow",
        "LumiTranslate",
        "data_analisis.png",
        "Convierte imágenes en texto y traduce su contenido a diferentes idiomas con ayuda de la inteligencia artificial.",
        "https://ocr-audio-wvhaldww4dn4zze8kltksm.streamlit.app/"
    )

    tarjeta(
        "📝 CHAT",
        "purple",
        "WordCloud: Laboratorio de Palabras",
        "OIG3.jpg",
        "Explora un texto, identifica las palabras más frecuentes y conviértelas en una nube visual. Personaliza colores, formas y filtros para descubrir patrones.",
        "https://wordcloud-8xcyhnovzzx3urhzjdvxcf.streamlit.app/"
    )


# ==================================================
# COLUMNA 3
# ==================================================

with col3:

    tarjeta(
        "🧠 CÁMARA",
        "yellow",
        "VisionScan: Detección Inteligente de Objetos",
        "Chat_pdf.png",
        "Utiliza visión artificial para identificar objetos en imágenes capturadas con la cámara y visualizar sus resultados en tiempo real.",
        "https://yolov5-bhfvwptkqgplobjtsjr8xj.streamlit.app/"
    )

    tarjeta(
        "👁️ CHAT",
        "purple",
        "TextDetective: Buscador de Pistas",
        "OIG4.jpg",
        "Analiza documentos y encuentra la pista más relacionada con tu pregunta mediante TF-IDF y similitud de textos.",
        "https://questanswer-qnpwbc5jnzurzcdjfnrzzp.streamlit.app/"
    )

    tarjeta(
        "⚙️ INTERACCIÓN",
        "yellow",
        "AI Lab — Explorando la Inteligencia Artificial",
        "OIG6.jpg",
        "Un laboratorio interactivo donde puedes explorar aplicaciones de IA para texto, voz, imágenes, datos y mucho más.",
        "https://tm59m47cvqpdasyxtsnmy3pk.streamlit.app/"
    )


# --------------------------------------------------
# FOOTER
# --------------------------------------------------

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
```
