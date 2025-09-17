import streamlit as st
from PIL import Image


def upload_image():
    uploaded_file = st.sidebar.file_uploader(
        "Upload an image", type=["jpg", "jpeg", "png"]
    )
    if uploaded_file:
        return Image.open(uploaded_file)
    return None
