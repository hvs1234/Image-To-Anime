from PIL import Image, ImageEnhance, ImageFilter
import torch
import torchvision.transforms as T
import cv2
import numpy as np

device = "cuda" if torch.cuda.is_available() else "cpu"
model = torch.hub.load(
    "bryandlee/animegan2-pytorch:main", 
    "generator",    
    pretrained="face_paint_512_v2"
)
model.to(device).eval()

to_tensor = T.ToTensor()
to_pil = T.ToPILImage()

def apply_ghibli_style(image, contrast, brightness, saturation, color_balance, blur_strength):
    orig_size = image.size
    img = image.convert("RGB")
    img = ImageEnhance.Contrast(img).enhance(contrast)
    img = ImageEnhance.Brightness(img).enhance(brightness)
    img = ImageEnhance.Color(img).enhance(saturation)
    if blur_strength > 0:
        img = img.filter(ImageFilter.GaussianBlur(blur_strength))
    resize = T.Resize(512)
    x = to_tensor(resize(img)).unsqueeze(0).to(device)
    x = (x - 0.5) / 0.5 
    with torch.no_grad():
        out = model(x)[0].cpu()
    out = (out * 0.5 + 0.5).clamp(0, 1)
    styled_img = to_pil(out)
    styled_img = styled_img.resize(orig_size, Image.Resampling.LANCZOS)
    return styled_img

def apply_sketch_style(image):
    img = image.convert("RGB")
    cv_img = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2GRAY)
    inv = 255 - cv_img
    blur = cv2.GaussianBlur(inv, (21, 21), 0)
    sketch = cv2.divide(cv_img, 255 - blur, scale=256)
    return Image.fromarray(sketch)
    
def apply_thermal_style(image):
    img = image.convert("RGB")
    cv_img = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
    gray = cv2.cvtColor(cv_img, cv2.COLOR_BGR2GRAY)
    thermal = cv2.applyColorMap(gray, cv2.COLORMAP_JET)
    return Image.fromarray(cv2.cvtColor(thermal, cv2.COLOR_BGR2RGB))

def apply_black_and_white_style(image):
    img = image.convert("RGB")
    gray = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2GRAY)
    bw_img = Image.fromarray(gray)
    return bw_img

def apply_sepia_style(image):
    img = image.convert("RGB")
    cv_img = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
    sepia_filter = np.array([[0.393, 0.769, 0.189],
                             [0.349, 0.686, 0.168],
                             [0.272, 0.534, 0.131]])
    sepia_img = cv2.transform(cv_img, sepia_filter)
    sepia_img = np.clip(sepia_img, 0, 255).astype(np.uint8)
    return Image.fromarray(cv2.cvtColor(sepia_img, cv2.COLOR_BGR2RGB))

def apply_blur(image, blur_strength):
    if blur_strength > 0:
        return image.filter(ImageFilter.GaussianBlur(blur_strength))
    return image