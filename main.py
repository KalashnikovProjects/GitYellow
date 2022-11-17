import sys
from random import randint

from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5 import uic


class DrawYellowCircle(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.initUI()
        self.draw = False

    def initUI(self):
        self.setGeometry(300, 300, 400, 400)
        self.btn.clicked.connect(self.run)

    def run(self):
        self.draw = True
        self.repaint()

    def paintEvent(self, event):
        if self.draw:
            qp = QPainter()
            qp.begin(self)
            self.draw_yellow_circle(qp)
            qp.end()

    def draw_yellow_circle(self, qp):
        qp.setBrush(QColor(255, 255, 0))
        for i in range(30):
            r = randint(0, 100)
            qp.drawEllipse(randint(0, 300), randint(0, 300), r, r)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = DrawYellowCircle()
    ex.show()
    sys.exit(app.exec())