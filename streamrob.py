import streamlit as st
from PIL import Image, ImageDraw, ImageFont
import numpy as np

st.set_page_config(page_title="Détection Roboflow", layout="wide")
st.title("🧪 Détection avec Roboflow et seuil de confiance")

# --- Choix du modèle ---
models = [
    "encre-ferrogallique-2-wy9md-instant-1",
    "encre-ferrogallique-2-wy9md/1",
    "encre-ferrogallique-2-wy9md/5",
    "encre-ferrogallique-2-wy9md/3",
    "encre-ferrogallique-2-wy9md/2",
]
selected_model = st.selectbox("Choisir le modèle Roboflow :", models)

# --- Upload de l'image ---
uploaded_file = st.file_uploader("Choisir une image :", type=["jpg","jpeg","png"])
if uploaded_file:
    image = Image.open(uploaded_file).convert("RGB")
    width, height = image.size

    # --- Slider pour seuil de confiance ---
    confidence_threshold = st.slider("Seuil de confiance", 0.0, 1.0, 0.5, 0.01)

    # --- Exemple prédictions Roboflow pour cette image ---
    # Ici tu devrais remplacer par l'appel API Roboflow pour `selected_model`
    result = {
        "predictions": [
            {"x": 0.3, "y": 0.2, "width": 0.2, "height": 0.1, "confidence": 0.85},
            {"x": 0.6, "y": 0.5, "width": 0.15, "height": 0.15, "confidence": 0.6},
            {"x": 0.5, "y": 0.7, "width": 0.1, "height": 0.1, "confidence": 0.3},
        ]
    }

    annotated = image.copy()
    draw = ImageDraw.Draw(annotated)
    font = ImageFont.load_default()

    # --- Dessiner les boxes en tenant compte de la taille de l'image ---
    for pred in result["predictions"]:
        conf = pred["confidence"]
        if conf < confidence_threshold:
            continue
        x0 = int((pred["x"] - pred["width"]/2) * width)
        y0 = int((pred["y"] - pred["height"]/2) * height)
        x1 = int((pred["x"] + pred["width"]/2) * width)
        y1 = int((pred["y"] + pred["height"]/2) * height)
        draw.rectangle([x0, y0, x1, y1], outline="red", width=3)
        draw.text((x0, y0 - 10), f"{conf:.2f}", fill="green", font=font)

    # --- Affichage côte à côte ---
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Image originale")
        st.image(image)
    with col2:
        st.subheader("Image annotée")
        st.image(annotated)
