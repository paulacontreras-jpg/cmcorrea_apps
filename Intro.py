import base64
from pathlib import Path

import streamlit as st

# --------------------------------------------------
# CONFIGURACIÓN
# --------------------------------------------------

st.set_page_config(
    page_title="Aplicaciones de Inteligencia Artificial",
    page_icon="🤖",
    layout="wide"
)

COLUMNAS_POR_FILA = 3
URL_IA = "https://sites.google.com/view/aplicacionesdeia/inicio"

# --------------------------------------------------
# DATOS: EDITA AQUÍ TUS TARJETAS
# --------------------------------------------------
# color: "yellow" o "purple"
# imagen: nombre del archivo (o None para mostrar un emoji)
# emoji: se usa solo si no hay imagen

APLICACIONES = [
    {
        "tag": "🎙️ AUDIO", "color": "yellow",
        "titulo": "Conversión de texto a voz",
        "imagen": "talk.jfif", "emoji": "🎙️",
        "descripcion": "Convierte texto escrito en voz utilizando una aplicación basada en Inteligencia Artificial.",
        "url": "https://interfazmultimodal1-paula.streamlit.app/",
        "boton": "Probar aplicación →",
    },
    {
        "tag": "🌟 CHAT", "color": "purple",
        "titulo": "INTRO: Mi mood de hoy",
        "imagen": "mood.jfif", "emoji": "🌟",
        "descripcion": "Un espacio interactivo para compartir mi estado de ánimo, explorar emociones y descubrir qué tan relatable es mi mood del día.",
        "url": "https://introstrelit.streamlit.app/",
        "boton": "Probar aplicación →",
    },
    {
        "tag": "🧠 CÁMARA", "color": "yellow",
        "titulo": "RECONOCIMIENTO ÓPTICO DE CARACTERES",
        "imagen": "charc.jfif", "emoji": "🧠",
        "descripcion": "Convierte imágenes en texto de forma rápida y sencilla. Sube o toma una fotografía de un documento, texto o imagen y el sistema reconocerá automáticamente las palabras que contiene.",
        "url": "https://4di4tgzegjkvtdx98nnspw.streamlit.app/",
        "boton": "Probar modelo →",
    },
    {
        "tag": "🎙️ CHAT", "color": "yellow",
        "titulo": "Detective de sentimientos",
        "imagen": "feeling.jfif", "emoji": "🔎",
        "descripcion": "¿Quieres saber cómo te sientes? Este detective encontrará todos tus sentimientos.",
        "url": "https://sentimenta-kkcpxrndzcrh4vzxjuoyik.streamlit.app/",
        "boton": "Probar aplicación →",
    },
    {
        "tag": "🗣️ VOZ", "color": "purple",
        "titulo": "Traductor",
        "imagen": "traductor.jfif", "emoji": "🗣️",
        "descripcion": "Una herramienta interactiva para traducir lo que dices. Presiona el botón, habla cuando escuches la señal y selecciona el idioma que necesitas.",
        "url": "https://traductorr5d9v9t32kchhniyxnsdos.streamlit.app/",
        "boton": "Probar aplicación →",
    },
    {
        "tag": "🧠 CÁMARA", "color": "yellow",
        "titulo": "LumiTranslate",
        "imagen": "translate.jfif", "emoji": "🌍",
        "descripcion": "Convierte imágenes en texto y traduce su contenido a diferentes idiomas con ayuda de la inteligencia artificial.",
        "url": "https://ocr-audio-wvhaldww4dn4zze8kltksm.streamlit.app/",
        "boton": "Probar aplicación →",
    },
    {
        "tag": "📝 CHAT", "color": "purple",
        "titulo": "WordCloud: Laboratorio de Palabras",
        "imagen": "cloud.jfif", "emoji": "☁️",
        "descripcion": "Explora un texto, identifica las palabras más frecuentes y conviértelas en una nube visual. Personaliza colores, formas y filtros para descubrir los patrones principales de cualquier contenido.",
        "url": "https://wordcloud-8xcyhnovzzx3urhzjdvxcf.streamlit.app/",
        "boton": "Probar aplicación →",
    },
    {
        "tag": "🧠 CÁMARA", "color": "yellow",
        "titulo": "VisionScan: Detección Inteligente de Objetos",
        "imagen": "vision.jfif", "emoji": "👁️",
        "descripcion": "Utiliza visión artificial para identificar objetos en imágenes capturadas con la cámara y visualizar sus resultados en tiempo real.",
        "url": "https://yolov5-bhfvwptkqgplobjtsjr8xj.streamlit.app/",
        "boton": "Probar aplicación →",
    },
    {
        "tag": "👁️ CHAT", "color": "purple",
        "titulo": "TextDetective: Buscador de Pistas",
        "imagen": "detec.jfif", "emoji": "📄",
        "descripcion": "Analiza documentos y encuentra la pista más relacionada con tu pregunta mediante TF-IDF y similitud de textos.",
        "url": "https://questanswer-qnpwbc5jnzurzcdjfnrzzp.streamlit.app/",
        "boton": "Probar aplicación →",
    },
    {
        "tag": "⚙️ INTERACCIÓN", "color": "yellow",
        "titulo": "AI Lab — Explorando la Inteligencia Artificial",
        "imagen": "scientist.jfif", "emoji": "🔬",
        "descripcion": "Un laboratorio interactivo donde puedes explorar aplicaciones de IA para texto, voz, imágenes, datos y mucho más.",
        "url": "https://tm59m47cvqpdasyxtsnmy3pk.streamlit.app/",
        "boton": "Probar aplicación →",
    },

    # ---------- 8 TARJETAS NUEVAS PARA EDITAR ----------
    {
        "tag": "✏️ EDITAR", "color": "purple",
        "titulo": "EDITAR: Título 11",
        "imagen": None, "emoji": "✨",
        "descripcion": "EDITAR: escribe aquí la descripción de la aplicación.",
        "url": "https://",
        "boton": "Probar aplicación →",
    },
    {
        "tag": "✏️ EDITAR", "color": "yellow",
        "titulo": "EDITAR: Título 12",
        "imagen": None, "emoji": "✨",
        "descripcion": "EDITAR: escribe aquí la descripción de la aplicación.",
        "url": "https://",
        "boton": "Probar aplicación →",
    },
    {
        "tag": "✏️ EDITAR", "color": "purple",
        "titulo": "EDITAR: Título 13",
        "imagen": None, "emoji": "✨",
        "descripcion": "EDITAR: escribe aquí la descripción de la aplicación.",
        "url": "https://",
        "boton": "Probar aplicación →",
    },
    {
        "tag": "✏️ EDITAR", "color": "yellow",
        "titulo": "EDITAR: Título 14",
        "imagen": None, "emoji": "✨",
        "descripcion": "EDITAR: escribe aquí la descripción de la aplicación.",
        "url": "https://",
        "boton": "Probar aplicación →",
    },
    {
        "tag": "✏️ EDITAR", "color": "purple",
        "titulo": "EDITAR: Título 15",
        "imagen": None, "emoji": "✨",
        "descripcion": "EDITAR: escribe aquí la descripción de la aplicación.",
        "url": "https://",
        "boton": "Probar aplicación →",
    },
    {
        "tag": "✏️ EDITAR", "color": "yellow",
        "titulo": "EDITAR: Título 16",
        "imagen": None, "emoji": "✨",
        "descripcion": "EDITAR: escribe aquí la descripción de la aplicación.",
        "url": "https://",
        "boton": "Probar aplicación →",
    },
    {
        "tag": "✏️ EDITAR", "color": "purple",
        "titulo": "EDITAR: Título 17",
        "imagen": None, "emoji": "✨",
        "descripcion": "EDITAR: escribe aquí la descripción de la aplicación.",
        "url": "https://",
        "boton": "Probar aplicación →",
    },
    {
        "tag": "✏️ EDITAR", "color": "yellow",
        "titulo": "EDITAR: Título 18",
        "imagen": None, "emoji": "✨",
        "descripcion": "EDITAR: escribe aquí la descripción de la aplicación.",
        "url": "https://",
        "boton": "Probar aplicación →",
    },
]

# --------------------------------------------------
# ESTILOS
# --------------------------------------------------

st.markdown("""
<style>
    .stApp { background: #FFFDF5; }

    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #5B2A86 0%, #7B3FB5 100%);
    }
    [data-testid="stSidebar"] h2,
    [data-testid="stSidebar"] h3,
    [data-testid="stSidebar"] p { color: white; }

    .titulo {
        background: linear-gradient(90deg, #5B2A86, #8B4FCB);
        color: white; padding: 35px; border-radius: 25px;
        text-align: center; margin-bottom: 25px;
        box-shadow: 0px 8px 20px rgba(91, 42, 134, 0.20);
    }
    .titulo h1 { font-size: 42px; margin-bottom: 8px; }
    .titulo p  { font-size: 18px; margin: 0; }

    .intro {
        background: #FFF1A8; padding: 20px 25px; border-radius: 18px;
        margin: 20px 0 15px 0; border-left: 8px solid #F2C94C;
    }
    .intro h3 { color: #4A206B; margin-bottom: 5px; }

    .card {
        background: white; border-radius: 20px; padding: 20px;
        margin-bottom: 25px; min-height: 420px;
        box-shadow: 0px 5px 18px rgba(70, 40, 100, 0.12);
        border: 2px solid #EEE5F5; transition: 0.3s;
        display: flex; flex-direction: column; align-items: flex-start;
    }
    .card:hover {
        transform: translateY(-5px);
        box-shadow: 0px 10px 25px rgba(91, 42, 134, 0.20);
    }
    .card h3 { color: #5B2A86; font-size: 21px; margin-bottom: 10px; }
    .card p  { color: #555; font-size: 15px; line-height: 1.5; flex-grow: 1; }
    .card img { width: 200px; max-width: 100%; border-radius: 12px; margin: 5px 0 12px 0; }
    .card .emoji-img { font-size: 70px; text-align: center; width: 100%; margin: 10px 0 15px 0; }

    .tag-purple, .tag-yellow {
        display: inline-block; padding: 5px 12px; border-radius: 20px;
        font-size: 12px; font-weight: bold; margin-bottom: 10px;
    }
    .tag-purple { background: #E8D8F5; color: #5B2A86; }
    .tag-yellow { background: #FFF1A8; color: #735900; }

    .boton {
        display: inline-block; background: #5B2A86; color: white !important;
        text-decoration: none; padding: 9px 18px; border-radius: 12px;
        font-weight: bold; margin-top: 8px;
    }
    .boton:hover { background: #F2C94C; color: #4A206B !important; }

    .decoracion { color: #F2C94C; font-size: 28px; text-align: center; margin: 5px; }
    .footer { text-align: center; color: #7B3FB5; margin-top: 30px; padding: 20px; font-size: 14px; }
</style>
""", unsafe_allow_html=True)


# --------------------------------------------------
# FUNCIONES
# --------------------------------------------------

@st.cache_data
def imagen_a_base64(ruta: str):
    """Convierte una imagen local a base64 para incrustarla en el HTML."""
    archivo = Path(ruta)
    if not archivo.exists():
        return None
    return base64.b64encode(archivo.read_bytes()).decode()


def crear_tarjeta(app: dict) -> str:
    """Devuelve el HTML completo de una tarjeta."""
    datos = imagen_a_base64(app["imagen"]) if app.get("imagen") else None

    if datos:
        imagen_html = f'<img src="data:image/jpeg;base64,{datos}">'
    else:
        imagen_html = f'<div class="emoji-img">{app.get("emoji", "✨")}</div>'

    return f"""
    <div class="card">
        <span class="tag-{app['color']}">{app['tag']}</span>
        <h3>{app['titulo']}</h3>
        {imagen_html}
        <p>{app['descripcion']}</p>
        <a class="boton" href="{app['url']}" target="_blank">{app['boton']}</a>
    </div>
    """


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
    st.write("📄 Análisis de documentos")
    st.write("🔊 Transcripción de audio")


# --------------------------------------------------
# ENCABEZADO Y ENLACE PRINCIPAL
# --------------------------------------------------

st.markdown("""
<div class="titulo">
    <h1>🤖 Aplicaciones de Inteligencia Artificial</h1>
    <p>Explora diferentes herramientas y aplicaciones prácticas de IA</p>
</div>

<div class="intro">
    <h3>✨ Explora más aplicaciones</h3>
    <p>En el siguiente enlace puedes encontrar páginas y ejercicios prácticos
    relacionados con Inteligencia Artificial.</p>
</div>
""", unsafe_allow_html=True)

st.markdown(
    f'<a class="boton" href="{URL_IA}" target="_blank">🔗 Ver páginas y ejercicios</a>',
    unsafe_allow_html=True
)
st.markdown("<div class='decoracion'>◆ ◇ ◆</div>", unsafe_allow_html=True)


# --------------------------------------------------
# TARJETAS (en filas de 3)
# --------------------------------------------------

for i in range(0, len(APLICACIONES), COLUMNAS_POR_FILA):
    fila = APLICACIONES[i:i + COLUMNAS_POR_FILA]
    columnas = st.columns(COLUMNAS_POR_FILA)
    for columna, app in zip(columnas, fila):
        with columna:
            st.markdown(crear_tarjeta(app), unsafe_allow_html=True)


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
