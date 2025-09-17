✨ Ghibli & Sketch Image Generator

A dynamic Streamlit application that transforms your images into Ghibli-inspired art or pencil sketch style. Upload any image, choose your preferred style, adjust filters, and generate a beautifully stylized output that you can download instantly.

🛠 Features

🖼 Upload Images – Accepts JPG, JPEG, PNG formats.

🎨 Ghibli Style – Apply soft, dreamy, and colorful filters inspired by Studio Ghibli.

✏️ Sketch Style – Convert any image into a realistic pencil sketch.

⚡ Dynamic Filters – Adjust contrast, brightness, saturation, warmth, and blur.

🔄 Real-time Preview – See original and converted images before download.

⬇️ Download – Save your stylized image in PNG format instantly.

🖥 Interactive UI – Style selection appears dynamically after image upload.

🚀 How to Use

Clone the repository:

git clone https://github.com/yourusername/ghibli-sketch-generator.git
cd ghibli-sketch-generator


Install dependencies:

pip install -r requirements.txt


Run the Streamlit app:

streamlit run main.py


Upload your image using the sidebar.

Select Ghibli Style or Sketch Style.

Adjust filters (if Ghibli is selected).

Click Generate to see the converted image.

Download your result using the Download button.

🗂 Project Structure
ghibli-sketch-generator/
│
├─ main.py              # Streamlit UI
├─ filters.py           # Ghibli & Sketch style functions
├─ upload.py            # File upload handling
├─ requirements.txt     # Project dependencies
└─ README.md

⚙ Dependencies

Streamlit

Pillow

OpenCV

NumPy

PyTorch

💡 Notes

The Ghibli style uses a combination of filters and a lightweight GAN model for stylization.

The Sketch style is generated using OpenCV pencil sketch techniques.

The project is modular, with separate files for upload, filters, and main UI logic.

Works on both CPU and GPU.