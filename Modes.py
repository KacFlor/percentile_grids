from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

from Frame import Frame

class SecondWindow_for_single(QDialog):
    def __init__(self, parent=None):
        super(SecondWindow_for_single, self).__init__(parent)
        self.setWindowTitle("Single")

        layout = QVBoxLayout()

        validator = QDoubleValidator()
        validator.setDecimals(2)
        validator.setLocale(QLocale(QLocale.English))

        self.text = QLabel("Enter age (3-18)")

        self.lineEdit1 = QLineEdit()
        self.lineEdit1.setValidator(validator)

        self.text2 = QLabel("Enter weight (10-100)")

        self.lineEdit2 = QLineEdit()
        self.lineEdit2.setValidator(validator)

        self.submit_button = QPushButton("Confirm")

        layout.addWidget(self.text)
        layout.addWidget(self.lineEdit1)
        layout.addWidget(self.text2)
        layout.addWidget(self.lineEdit2)
        layout.addWidget(self.submit_button)
        self.setLayout(layout)

        self.submit_button.clicked.connect(self.on_submit_clicked)

    def on_submit_clicked(self):
        try:
            self.x = float(self.lineEdit1.text())
            self.y = float(self.lineEdit2.text())

            if not (3 <= self.x <= 18 and 10 <= self.y <= 100):
                raise ValueError("Value out of range")
        except ValueError:
            self.submit_button.setEnabled(False)
            self.submit_button.setEnabled(True)
        else:
            self.accept()
            self.submit_button.setEnabled(True)
class SecondWindow_for_multiple(QDialog):
    def __init__(self, parent=None):
        super(SecondWindow_for_multiple, self).__init__(parent)
        self.setWindowTitle("Multi")

        layout = QVBoxLayout()

        validator = QDoubleValidator()
        validator.setDecimals(0)
        validator.setLocale(QLocale(QLocale.English))

        self.text = QLabel("Enter the number of points")

        self.lineEdit1 = QLineEdit()
        self.lineEdit1.setValidator(validator)

        self.submit_button = QPushButton("Confirm")

        layout.addWidget(self.text)
        layout.addWidget(self.lineEdit1)
        layout.addWidget(self.submit_button)
        self.setLayout(layout)

        self.submit_button.clicked.connect(self.on_submit_clicked)

    def on_submit_clicked(self):
        try:
            self.Repeats = int(self.lineEdit1.text())
            self.Weight = []
            self.Age = []
            for i in range(self.Repeats):
                self.open_second_window_for_single()
            else:
                frame = Frame()
                frame.frame_init(self.Weight, self.Age, 2, self.Repeats)

            if not (100 > self.Repeats > 0):
                raise ValueError("Value out of range")
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
            self.Weight.append(self.second_window.x)
            self.Age.append(self.second_window.y)
class SecondWindow_for_curve(QDialog):
    def __init__(self, age, parent=None):
        super(SecondWindow_for_curve, self).__init__(parent)
        self.setWindowTitle("Curve")

        layout = QVBoxLayout()

        self.text = QLabel("Enter age for weight " + str(age))

        validator = QDoubleValidator()
        validator.setDecimals(2)
        validator.setLocale(QLocale(QLocale.English))

        self.lineEdit1 = QLineEdit()
        self.lineEdit1.setValidator(validator)

        self.submit_button = QPushButton("Confirm")

        layout.addWidget(self.text)
        layout.addWidget(self.lineEdit1)
        layout.addWidget(self.submit_button)
        self.setLayout(layout)

        self.submit_button.clicked.connect(self.on_submit_clicked)

    def on_submit_clicked(self):
        try:
            self.x = float(self.lineEdit1.text())

            if not (10 <= self.x <= 100):
                raise ValueError("Value out of range")
        except ValueError:
            self.submit_button.setEnabled(False)
            self.submit_button.setEnabled(True)
        else:
            self.accept()
            self.submit_button.setEnabled(True)