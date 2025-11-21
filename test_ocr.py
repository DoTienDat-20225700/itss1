import pytesseract
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
from ocr.ocr_engine import OcrEngine


ocr = OcrEngine(lang="jpn")
print(ocr.run_ocr("samples/download.png"))
