from worker.worker import Worker
from ocr.ocr_engine import OcrEngine
from translator.text_translator import TextTranslator
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def done(ocr_text, translated_text):
    print("OCR:", ocr_text)
    print("TRANS:", translated_text)

ocr = OcrEngine()
trans = TextTranslator()

w = Worker(ocr, trans, "samples/download.png")
w.finished.connect(done)
w.start()
w.wait()
