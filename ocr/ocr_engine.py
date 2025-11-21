import pytesseract
from PIL import Image
import cv2
import os
from datetime import datetime

# fallback to easyocr if pytesseract not producing expected results
try:
    import easyocr
    _HAS_EASYOCR = True
except Exception:
    _HAS_EASYOCR = False

class OCREngine:
    def __init__(self, tesseract_lang="jpn"):
        # tesseract_lang e.g. "eng", "jpn", "vie"
        self.lang = tesseract_lang

    def extract_text_from_path(self, path):
        # open with PIL then use pytesseract
        try:
            img = Image.open(path)
            text = pytesseract.image_to_string(img, lang=self.lang)
            text = text.strip()
            if text:
                return text
        except Exception:
            pass

        # fallback to easyocr if installed
        if _HAS_EASYOCR:
            reader = easyocr.Reader([self.lang[:2] if len(self.lang)>=2 else 'en'], gpu=False)
            # easyocr expects cv2 image (numpy array)
            img_cv = cv2.imread(path)
            if img_cv is None:
                return ""
            results = reader.readtext(img_cv, detail=0)
            return "\n".join(results)

        return ""

    def save_temp_image(self, cv_img):
        """cv_img: numpy array (BGR). save to samples/ with timestamp."""
        os.makedirs("samples", exist_ok=True)
        fname = f"samples/crop_{int(datetime.now().timestamp()*1000)}.png"
        # cv2.imwrite expects BGR
        cv2.imwrite(fname, cv_img)
        return fname
