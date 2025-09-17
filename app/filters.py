from PIL import Image, ImageEnhance, ImageFilter
import torch
import torchvision.transforms as T

device = "cuda" if torch.cuda.is_available() else "cpu"
model = torch.hub.load(
    "bryandlee/animegan2-pytorch:main", 
    "generator", 
    pretrained="face_paint_512_v2"
)
model.to(device).eval()

transform = T.Compose([
    T.Resize((512, 512)),
    T.ToTensor(),
    T.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5)),
])
to_pil = T.ToPILImage()

def apply_ghibli_style(image, contrast, brightness, saturation, color_balance, blur_strength):
    img = image.convert("RGB")
    img = ImageEnhance.Contrast(img).enhance(contrast)
    img = ImageEnhance.Brightness(img).enhance(brightness)
    img = ImageEnhance.Color(img).enhance(saturation)
    if blur_strength > 0:
        img = img.filter(ImageFilter.GaussianBlur(blur_strength))

    x = transform(img).unsqueeze(0).to(device)
    with torch.no_grad():
        out = model(x)[0].cpu() * 0.5 + 0.5
    styled_img = to_pil(out)
    return styled_img

def apply_sketch_style(image):
    import cv2
    import numpy as np
    img = image.convert("RGB")
    cv_img = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2GRAY)
    inv = 255 - cv_img
    blur = cv2.GaussianBlur(inv, (21, 21), 0)
    sketch = cv2.divide(cv_img, 255 - blur, scale=256)
    return Image.fromarray(sketch)
