import streamlit as st
from PIL import Image, ImageDraw
import requests
import io

st.set_page_config(page_title="Détection Roboflow", layout="wide")

st.title("🧪 Détection encre ferrogallique – Roboflow (HTTP API)")

API_KEY = st.secrets["ROBOFLOW_API_KEY"]
MODEL_ID = "encre-ferrogallique-2-wy9md/2"

uploaded_file = st.file_uploader("Choisir une image :", type=["jpg","jpeg","png"])

# --- Slider de confiance au-dessus des images ---
confidence_threshold = st.slider("Seuil de confiance", 0.0, 1.0, 0.5, 0.01)

if uploaded_file:
    image = Image.open(uploaded_file).convert("RGB")
    width, height = image.size

    # Convert to bytes
    buffered = io.BytesIO()
    image.save(buffered, format="JPEG")
    img_bytes = buffered.getvalue()

    # --- API HTTP Roboflow ---
    url = f"https://detect.roboflow.com/{MODEL_ID}?api_key={API_KEY}"
    response = requests.post(url, files={"file": img_bytes})
    result = response.json()

    # --- Annotate image ---
    annotated = image.copy()
    draw = ImageDraw.Draw(annotated)

    # Filtrer les prédictions selon le seuil de confiance
    for pred in result.get("predictions", []):
        if pred["confidence"] < confidence_threshold:
            continue

        x0 = pred["x"] - pred["width"]/2
        y0 = pred["y"] - pred["height"]/2
        x1 = pred["x"] + pred["width"]/2
        y1 = pred["y"] + pred["height"]/2

        draw.rectangle([x0, y0, x1, y1], outline="red", width=4)
        draw.text((x0, y0 - 10), f"{pred['confidence']:.2f}", fill="green")

    # --- Display side-by-side ---
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Image originale")
        st.image(image)

    with col2:
        st.subheader("Image annotée")
        st.image(annotated)
