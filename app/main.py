import streamlit as st
import io
from upload import upload_image
from filters import (
    apply_ghibli_style,
    apply_sketch_style,
    apply_thermal_style,
    apply_black_and_white_style,
    apply_sepia_style,
    apply_blur
)

st.set_page_config(page_title="GenAnime", page_icon="🎨", layout="wide")
st.title("✨ Get Your Own Anime Style Way!")

st.sidebar.header("Input Source")
input_choice = st.sidebar.radio("Choose Input", ["Upload", "Camera"])

st.sidebar.header("Adjust Filters (only for Ghibli Style)")
contrast = st.sidebar.slider("Contrast", 0.5, 2.0, 1.0, 0.1)
brightness = st.sidebar.slider("Brightness", 0.5, 2.0, 1.0, 0.1)
saturation = st.sidebar.slider("Saturation", 0.0, 2.0, 1.0, 0.1)
color_balance = st.sidebar.slider("Color Balance (Warmth)", -50, 50, 0, 1)
blur_strength = st.sidebar.slider("Blur", 0, 10, 0, 1)

st.sidebar.header("Style Options")
style_choice = st.sidebar.selectbox(
    "Choose Style", ["Ghibli", "Sketch", "Thermal", "Black & White", "Sepia", "Blur"], index=0
)
generate = st.sidebar.button("Generate")

image = upload_image(input_choice)

st.subheader("Original Image")
if image:
    st.image(image, use_container_width=True)
else:
    st.write("No Image Uploaded")

st.subheader("Converted Image")
if image and generate and style_choice:
    style_functions = {
        "Ghibli": lambda img: apply_ghibli_style(img, contrast, brightness, saturation, color_balance, blur_strength),
        "Sketch": apply_sketch_style,
        "Thermal": apply_thermal_style,
        "Black & White": apply_black_and_white_style,
        "Sepia": apply_sepia_style,
        "Blur": lambda img: apply_blur(img, blur_strength)
    }
    styled_img = style_functions[style_choice](image)
    st.image(styled_img, use_container_width=True)
    buf = io.BytesIO()
    styled_img.save(buf, format="PNG")
    st.download_button("⬇️ Download Image", buf.getvalue(), "styled_output.png", "image/png")
else:
    st.write("No Conversion Applied")
