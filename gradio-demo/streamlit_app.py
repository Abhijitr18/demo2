"""Streamlit port of the Gradio demo app
- Text: reverse text
- Image: grayscale / edge detect

Run locally: streamlit run streamlit_app.py
"""

from PIL import Image, ImageOps, ImageFilter
import streamlit as st


def reverse_text(text: str) -> str:
    return "" if not text else text[::-1]


def to_grayscale(img: Image.Image) -> Image.Image:
    return ImageOps.grayscale(img) if img else None


def edge_detect(img: Image.Image) -> Image.Image:
    return img.convert("L").filter(ImageFilter.FIND_EDGES) if img else None


st.set_page_config(page_title="Streamlit Demo App", layout="centered")
st.title("Streamlit Demo App ✅")

tabs = st.tabs(["Text", "Image"])

with tabs[0]:
    txt = st.text_area("Enter text to reverse")
    if st.button("Reverse text"):
        st.success(reverse_text(txt))

with tabs[1]:
    uploaded = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"]) 
    if uploaded:
        img = Image.open(uploaded)
        st.image(img, caption="Original", use_column_width=True)

        op = st.radio("Operation", ["Grayscale", "Edge detect"]) 
        if st.button("Apply"):
            out = to_grayscale(img) if op == "Grayscale" else edge_detect(img)
            st.image(out, caption="Result", use_column_width=True)

st.markdown("---\n**Note:** This repository originally contained a Gradio app (`app.py`). If you deployed the repo to Streamlit and saw a blank page, make sure your Streamlit app file is set to `streamlit_app.py` in the Streamlit deployment settings.")