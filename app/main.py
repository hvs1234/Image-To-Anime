import streamlit as st
import io
from upload import upload_image
from filters import apply_ghibli_style

st.set_page_config(page_title="Ghibli Image Generator", layout="wide")
st.title("✨ Get Your Own Anime Style Way!")

st.sidebar.header("Adjust Filters")
contrast = st.sidebar.slider("Contrast", 0.5, 2.0, 1.0, 0.1)
brightness = st.sidebar.slider("Brightness", 0.5, 2.0, 1.0, 0.1)
saturation = st.sidebar.slider("Saturation", 0.0, 2.0, 1.0, 0.1)
color_balance = st.sidebar.slider("Color Balance (Warmth)", -50, 50, 0, 1)
blur_strength = st.sidebar.slider("Blur", 0, 10, 0, 1)

image = upload_image()
generate = st.sidebar.button("Generate")

st.subheader("Original Image")
if image:
    st.image(image, use_container_width=True)
else:
    st.write("No Image Uploaded")

st.subheader("Ghibli Styled Image")
if image and generate:
    styled_img = apply_ghibli_style(
        image, contrast, brightness, saturation, color_balance, blur_strength
    )
    st.image(styled_img, use_container_width=True)
    buf = io.BytesIO()
    styled_img.save(buf, format="PNG")
    st.download_button(
        "⬇️ Download Styled Image", buf.getvalue(), "ghibli_style.png", "image/png"
    )
else:
    st.write("No Ghibli Converted")
