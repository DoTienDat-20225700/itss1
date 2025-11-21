from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QPainter, QPen, QColor
from PyQt5.QtCore import Qt, QRect, pyqtSignal

class ScreenCropper(QWidget):
    crop_finished = pyqtSignal(QRect)      # gởi rect
    crop_done = pyqtSignal()               # báo cho main để hiện lại

    def __init__(self):
        super().__init__()

        self.start_pos = None
        self.end_pos = None
        self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint)
        self.setWindowState(Qt.WindowFullScreen)
        self.setAttribute(Qt.WA_TranslucentBackground)

    def mousePressEvent(self, event):
        self.start_pos = event.pos()
        self.end_pos = event.pos()
        self.update()

    def mouseMoveEvent(self, event):
        self.end_pos = event.pos()
        self.update()

    def mouseReleaseEvent(self, event):
        rect = QRect(self.start_pos, self.end_pos).normalized()
        self.crop_finished.emit(rect)
        self.crop_done.emit()              # báo hoàn thành
        self.close()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.fillRect(self.rect(), QColor(0, 0, 0, 100))

        if self.start_pos and self.end_pos:
            painter.setPen(QPen(Qt.green, 2))
            painter.drawRect(QRect(self.start_pos, self.end_pos))
