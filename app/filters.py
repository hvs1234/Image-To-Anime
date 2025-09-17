from PIL import Image, ImageEnhance, ImageFilter
import numpy as np
import cv2


def apply_ghibli_style(
    image, contrast, brightness, saturation, color_balance, blur_strength
):
    img = image.convert("RGB")
    img = ImageEnhance.Contrast(img).enhance(contrast)
    img = ImageEnhance.Brightness(img).enhance(brightness)
    cv_img = np.array(img)
    cv_img = cv2.cvtColor(cv_img, cv2.COLOR_RGB2HSV).astype("float32")
    cv_img[..., 1] *= saturation
    cv_img[..., 1] = np.clip(cv_img[..., 1], 0, 255)
    cv_img = cv2.cvtColor(cv_img.astype("uint8"), cv2.COLOR_HSV2RGB)
    if color_balance != 0:
        b, g, r = cv2.split(cv_img)
        if color_balance > 0:
            r = np.clip(r + color_balance, 0, 255)
        else:
            b = np.clip(b + abs(color_balance), 0, 255)
        cv_img = cv2.merge([b, g, r])
    img = Image.fromarray(cv_img)
    if blur_strength > 0:
        img = img.filter(ImageFilter.GaussianBlur(blur_strength))
    return img
