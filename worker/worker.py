from PyQt5.QtCore import QThread, pyqtSignal, QObject
from ocr.ocr_engine import OCREngine
from translator.text_translator import TextTranslator

class WorkerSignals(QObject):
    result = pyqtSignal(str, str)   # ocr_text, translated_text
    finished = pyqtSignal()

class OCRWorker(QThread):
    def __init__(self, image_path):
        super().__init__()
        self.image_path = image_path
        self.signals = WorkerSignals()
        # create engines per thread to avoid cross-thread resources
        self.ocr_engine = OCREngine()
        self.translator = TextTranslator()

    def run(self):
        try:
            ocr_text = self.ocr_engine.extract_text_from_path(self.image_path)
            translated = self.translator.translate(ocr_text)
            self.signals.result.emit(ocr_text, translated)
        except Exception as e:
            self.signals.result.emit(f"OCR error: {e}", "")
        finally:
            self.signals.finished.emit()
