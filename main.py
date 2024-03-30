import matplotlib.pyplot as plt

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

from Menu import Menu
from Frame import Frame

import sys

class SecondWindow_for_single(QDialog):
    def __init__(self, parent=None):
        super(SecondWindow_for_single, self).__init__(parent)
        self.setWindowTitle("Nowe Okno")

        layout = QVBoxLayout()

        validator = QDoubleValidator()
        validator.setDecimals(2)
        validator.setLocale(QLocale(QLocale.English))

        self.lineEdit1 = QLineEdit()
        self.lineEdit1.setValidator(validator)

        self.lineEdit2 = QLineEdit()
        self.lineEdit2.setValidator(validator)

        self.submit_button = QPushButton("Zatwierdź")

        layout.addWidget(self.lineEdit1)
        layout.addWidget(self.lineEdit2)
        layout.addWidget(self.submit_button)
        self.setLayout(layout)

        self.submit_button.clicked.connect(self.on_submit_clicked)

    def on_submit_clicked(self):
        try:
            self.x = float(self.lineEdit1.text())
            self.y = float(self.lineEdit2.text())

            if not (3 <= self.x <= 18 and 10 <= self.y <= 100):
                raise ValueError("Wartości poza zakresem")
        except ValueError:
            self.submit_button.setEnabled(False)
            self.submit_button.setEnabled(True)
        else:
            self.accept()
            self.submit_button.setEnabled(True)
class SecondWindow_for_multiple(QDialog):
    def __init__(self, parent=None):
        super(SecondWindow_for_multiple, self).__init__(parent)
        self.setWindowTitle("Nowe Okno")

        layout = QVBoxLayout()

        validator = QDoubleValidator()
        validator.setDecimals(0)
        validator.setLocale(QLocale(QLocale.English))

        self.lineEdit1 = QLineEdit()
        self.lineEdit1.setValidator(validator)

        self.submit_button = QPushButton("Zatwierdź")

        layout.addWidget(self.lineEdit1)
        layout.addWidget(self.submit_button)
        self.setLayout(layout)

        self.submit_button.clicked.connect(self.on_submit_clicked)

    def on_submit_clicked(self):
        try:
            self.a = int(self.lineEdit1.text())
            self.x = []
            self.y = []
            for i in range(self.a):
                self.open_second_window_for_single()
            else:
                frame.frame_init(self.x, self.y, 3, self.a)

            if not (100 > self.a > 0 ):
                raise ValueError("Wartości poza zakresem")
        except ValueError:
            self.submit_button.setEnabled(False)
            self.submit_button.setEnabled(True)
        else:
            self.accept()
            self.submit_button.setEnabled(True)

    def open_second_window_for_single(self):
        self.second_window = SecondWindow_for_single(self)
        self.second_window.exec_()

        if self.second_window.result() == QDialog.Accepted:
            self.x.append(self.second_window.x)
            self.y.append(self.second_window.y)

class SecondWindow_for_curve(QDialog):
    def __init__(self, age, parent=None):
        super(SecondWindow_for_curve, self).__init__(parent)
        self.setWindowTitle("Nowe Okno")

        layout = QVBoxLayout()

        self.text = QLabel("Wprowadź wage dla wieku " + str(age))

        validator = QDoubleValidator()
        validator.setDecimals(2)
        validator.setLocale(QLocale(QLocale.English))

        self.lineEdit1 = QLineEdit()
        self.lineEdit1.setValidator(validator)

        self.submit_button = QPushButton("Zatwierdź")

        layout.addWidget(self.text)
        layout.addWidget(self.lineEdit1)
        layout.addWidget(self.submit_button)
        self.setLayout(layout)

        self.submit_button.clicked.connect(self.on_submit_clicked)

    def on_submit_clicked(self):
        try:
            self.x = float(self.lineEdit1.text())

            if not (10 <= self.x <= 100):
                raise ValueError("Wartości poza zakresem")
        except ValueError:
            self.submit_button.setEnabled(False)
            self.submit_button.setEnabled(True)
        else:
            self.accept()
            self.submit_button.setEnabled(True)


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setWindowTitle("KidNet")
        self.setGeometry(200,40,300,300)
        self.setFixedSize(1000,900)

        central_widget = QWidget()
        main_layout = QHBoxLayout()
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)

        left_layout = QVBoxLayout()
        main_layout.addLayout(left_layout)

        right_layout = QVBoxLayout()
        main_layout.addLayout(right_layout)

        self.button_s = QPushButton("Jedne dane")
        self.button_s.setCheckable(True)
        self.button_s.setFixedSize(QSize(250,30))
        left_layout.addWidget(self.button_s)

        self.button_m = QPushButton("Wiele danych")
        self.button_m.setCheckable(True)
        self.button_m.setFixedSize(QSize(250, 30))
        left_layout.addWidget(self.button_m)

        self.button_c = QPushButton("Krzywa danych")
        self.button_c.setCheckable(True)
        self.button_c.setFixedSize(QSize(250, 30))
        left_layout.addWidget(self.button_c)

        self.label_image = QLabel()
        right_layout.addWidget(self.label_image)

        self.second_window = None
        self.button_s.clicked.connect(self.open_second_window_for_single)
        self.button_m.clicked.connect(self.open_second_window_for_multiple)
        self.button_c.clicked.connect(self.open_second_window_for_curve)

    def open_second_window_for_single(self):
        self.second_window = SecondWindow_for_single(self)
        self.second_window.exec_()

        if self.second_window.result() == QDialog.Accepted:
            x = self.second_window.x
            y = self.second_window.y
            frame.frame_init(x, y, 1, 0)
            self.label_image.setPixmap(QPixmap('percentile_grid.png'))

    def open_second_window_for_multiple(self):
        self.second_window = SecondWindow_for_multiple(self)
        self.second_window.exec_()
        self.label_image.setPixmap(QPixmap('percentile_grid.png'))

    def open_second_window_for_curve(self):
        age = 3
        self.x = []
        self.y = [3, 3.5, 4, 4.5, 5, 5.5, 6, 6.5, 7, 7.5, 8, 8.5, 9, 9.5, 10, 10.5, 11, 11.5, 12, 12.5, 13, 13.5, 14,
                  14.5, 15, 15.5, 16, 16.5, 17, 17.5, 18]

        while age <= 18:
            if self.second_window is not None:
                self.second_window.deleteLater()
            self.second_window = SecondWindow_for_curve(age, self)
            self.second_window.exec_()
            if self.second_window.result() == QDialog.Accepted:
                self.x.append(self.second_window.x)
            age += 0.5

        if self.x:
            frame.frame_init(self.x, self.y, 2, 0)
            self.label_image.setPixmap(QPixmap('percentile_grid.png'))


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    frame = Frame()
    window.show()
    app.exec_()

