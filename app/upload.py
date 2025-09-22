import streamlit as st
from PIL import Image

def upload_image(input_choice):
    if input_choice == "Upload":
        uploaded_file = st.file_uploader("Upload Image", type=["jpg", "jpeg", "png","webp","heic"])
        if uploaded_file:
            return Image.open(uploaded_file)
    elif input_choice == "Camera":
        camera_file = st.camera_input("Take a Picture")
        if camera_file:
            return Image.open(camera_file)
    return None
