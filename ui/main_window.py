from PyQt5.QtWidgets import (
    QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout,
    QTextEdit, QGroupBox
)
from PyQt5.QtCore import Qt, QRect
from PyQt5.QtGui import QPixmap, QGuiApplication, QImage
import cv2
import numpy as np

from ui.screen_cropper import ScreenCropper


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Screen OCR Tool")
        self.setStyleSheet("""
            QWidget { background: #f4f4f4; }
            QPushButton {
                background: #e0e0e0;
                padding: 6px;
                border-radius: 4px;
            }
            QPushButton:hover { background: #d5d5d5; }
            QGroupBox {
                border: 1px solid #ccc;
                border-radius: 6px;
                margin-top: 10px;
                padding: 10px;
                font-weight: bold;
            }
        """)

        # ================= TOP BUTTON =================
        self.btn_capture = QPushButton("Capture Screen")

        # ================= SETTINGS (LEFT SIDE) =================
        self.settings_box = QGroupBox("Settings")
        self.settings_label = QLabel("Settings Panel (coming soon)")
        self.settings_label.setAlignment(Qt.AlignLeft)

        left_layout = QVBoxLayout()
        left_layout.addWidget(self.settings_box)
        self.settings_box.setLayout(QVBoxLayout())
        self.settings_box.layout().addWidget(self.settings_label)

        # ================= MERGED PREVIEW (RIGHT SIDE) =================
        self.image_label = QLabel("Captured / Preview Area")
        self.image_label.setAlignment(Qt.AlignCenter)
        self.image_label.setStyleSheet("""
            background: #fff;
            border: 2px dashed #aaa;
        """)
        self.image_label.setFixedHeight(300)

        # ================= OCR OUTPUT =================
        self.ocr_output = QTextEdit()
        self.ocr_output.setPlaceholderText("OCR Result will show here...")
        self.ocr_output.setStyleSheet("""
            background: #fff;
            border: 1px solid #aaa;
            font-size: 14px;
            padding: 8px;
        """)

        right_layout = QVBoxLayout()
        right_layout.addWidget(self.image_label)
        right_layout.addWidget(self.ocr_output)

        # ================= MAIN SPLIT LAYOUT =================
        split_layout = QHBoxLayout()
        split_layout.addLayout(left_layout, 1)   # left side smaller
        split_layout.addLayout(right_layout, 2)  # right side bigger

        # ================= ROOT LAYOUT =================
        main_layout = QVBoxLayout()
        main_layout.addWidget(self.btn_capture)
        main_layout.addLayout(split_layout)

        self.setLayout(main_layout)

        # Events
        self.btn_capture.clicked.connect(self.start_screen_capture)

    # -------------------------------------------------------
    def start_screen_capture(self):
        self.cropper = ScreenCropper()
        self.cropper.crop_finished.connect(self.handle_crop)
        self.cropper.show()

    # -------------------------------------------------------
    def handle_crop(self, rect: QRect):
        screen = QGuiApplication.primaryScreen()
        screenshot = screen.grabWindow(0)

        cropped_pixmap = screenshot.copy(rect)

        # show in preview
        self.image_label.setPixmap(
            cropped_pixmap.scaled(
                self.image_label.width(),
                self.image_label.height(),
                Qt.KeepAspectRatio,
                Qt.SmoothTransformation
            )
        )

        # convert to opencv
        self.cv_img = self.qpixmap_to_cv(cropped_pixmap)

    # -------------------------------------------------------
    def qpixmap_to_cv(self, pixmap: QPixmap):
        qimg = pixmap.toImage().convertToFormat(QImage.Format.Format_RGB888)
        w, h = qimg.width(), qimg.height()

        ptr = qimg.bits()
        ptr.setsize(h * w * 3)

        arr = np.frombuffer(ptr, np.uint8).reshape((h, w, 3))
        return cv2.cvtColor(arr, cv2.COLOR_RGB2BGR)

    def start_screen_capture(self):
        self.hide()                          # ẨN APP
        self.cropper = ScreenCropper()
        self.cropper.crop_finished.connect(self.handle_crop)
        self.cropper.crop_done.connect(self.show)   # HIỆN APP LẠI
        self.cropper.show()