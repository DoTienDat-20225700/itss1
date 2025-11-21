import pytesseract
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
from PyQt5.QtWidgets import QApplication
from ui.main_window import MainWindow
import sys
import os

if __name__ == "__main__":
    os.makedirs("samples", exist_ok=True)
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())
