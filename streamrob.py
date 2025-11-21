from PIL import Image, ImageDraw, ImageFont
import streamlit as st
import requests
import io

st.set_page_config(page_title="Détection Roboflow", layout="wide")
st.title("🧪 Détection avec barre de confiance")

# --- Upload ---
uploaded_file = st.file_uploader("Choisir une image :", type=["jpg","jpeg","png"])
if uploaded_file:
    image = Image.open(uploaded_file).convert("RGB")

    # Convert to bytes
    buffered = io.BytesIO()
    image.save(buffered, format="JPEG")
    img_bytes = buffered.getvalue()

    # --- Fake result pour exemple ---
    # Remplacer par votre appel API Roboflow
    result = {
        "predictions": [
            {"x": 150, "y": 100, "width": 100, "height": 50, "confidence": 0.85},
            {"x": 300, "y": 200, "width": 80, "height": 80, "confidence": 0.6}
        ]
    }

    # --- Annotate image ---
    annotated = image.copy()
    draw = ImageDraw.Draw(annotated)
    font = ImageFont.load_default()

    for pred in result["predictions"]:
        x0 = pred["x"] - pred["width"]/2
        y0 = pred["y"] - pred["height"]/2
        x1 = pred["x"] + pred["width"]/2
        y1 = pred["y"] + pred["height"]/2
        conf = pred["confidence"]

        # Boîte de détection
        draw.rectangle([x0, y0, x1, y1], outline="red", width=3)

        # Barre de confiance en haut de la boîte
        bar_height = 5
        bar_width = (x1 - x0) * conf  # proportionnelle à la confiance
        draw.rectangle([x0, y0 - bar_height, x0 + bar_width, y0], fill="green")

        # Valeur de confiance
        draw.text((x0, y0 - bar_height - 10), f"{conf:.2f}", fill="green", font=font)

    # --- Affichage côté à côte ---
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Image originale")
        st.image(image)
    with col2:
        st.subheader("Image annotée")
        st.image(annotated)
