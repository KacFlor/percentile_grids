from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

from Frame import Frame

class SecondWindow_for_single(QDialog):
    def __init__(self, diagram_value ,parent=None):
        super(SecondWindow_for_single, self).__init__(parent)
        self.setWindowTitle("Single")
        self.Diagram = diagram_value

        if self.Diagram == 1:
            self.min_x = 3
            self.max_x = 18
            self.min_y = 10
            self.max_y = 100
            self.y_type = "weight"
        if self.Diagram == 2:
            self.min_x = 3
            self.max_x = 18
            self.min_y = 10
            self.max_y = 80
            self.y_type = "weight"
        if self.Diagram == 3:
            self.min_x = 3
            self.max_x = 18
            self.min_y = 90
            self.max_y = 195
            self.y_type = "height"
        if self.Diagram == 4:
            self.min_x = 3
            self.max_x = 18
            self.min_y = 90
            self.max_y = 180
            self.y_type = "height"
        if self.Diagram == 5:
            self.min_x = 3
            self.max_x = 18
            self.min_y = 13
            self.max_y = 31
            self.y_type = "BMI"

        layout = QVBoxLayout()

        validator = QDoubleValidator()
        validator.setDecimals(2)
        validator.setLocale(QLocale(QLocale.English))

        self.text = QLabel("Enter age (" + str(self.min_x) + "-" + str(self.max_x)+ ")")

        self.lineEdit1 = QLineEdit()
        self.lineEdit1.setValidator(validator)

        self.text2 = QLabel("Enter " + self.y_type + " (" + str(self.min_y) + "-" + str(self.max_y) + ")")

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

            if not (self.min_x <= self.x <= self.max_x and self.min_y <= self.y <= self.max_y):
                raise ValueError("Value out of range")
        except ValueError:
            self.submit_button.setEnabled(False)
            self.submit_button.setEnabled(True)
        else:
            self.accept()
            self.submit_button.setEnabled(True)
class SecondWindow_for_multiple(QDialog):
    def __init__(self, diagram_value ,Name_Grid ,parent=None):
        super(SecondWindow_for_multiple, self).__init__(parent)
        self.setWindowTitle("Multi")
        self.Diagram = diagram_value
        self.Name = Name_Grid

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
            self.y = []
            self.Age = []
            for i in range(self.Repeats):
                self.open_second_window_for_single()
            else:
                frame = Frame()
                frame.frame_init(self.Name ,self.y, self.Age, 2, self.Repeats, self.Diagram)

            if not (100 > self.Repeats > 0):
                raise ValueError("Value out of range")
        except ValueError:
            self.submit_button.setEnabled(False)
            self.submit_button.setEnabled(True)
        else:
            self.accept()
            self.submit_button.setEnabled(True)

    def open_second_window_for_single(self):
        self.second_window = SecondWindow_for_single(self.Diagram)
        self.second_window.exec_()

        if self.second_window.result() == QDialog.Accepted:
            self.y.append(self.second_window.x)
            self.Age.append(self.second_window.y)
class SecondWindow_for_curve(QDialog):
    def __init__(self, age, diagram_value, parent=None):
        super(SecondWindow_for_curve, self).__init__(parent)
        self.setWindowTitle("Curve")
        self.Diagram = diagram_value

        if self.Diagram == 1:
            self.min_y = 10
            self.max_y = 100
            self.y_type = "weight"
        if self.Diagram == 2:
            self.min_y = 10
            self.max_y = 80
            self.y_type = "weight"
        if self.Diagram == 3:
            self.min_y = 90
            self.max_y = 195
            self.y_type = "height"
        if self.Diagram == 4:
            self.min_y = 90
            self.max_y = 180
            self.y_type = "height"
        if self.Diagram == 5:
            self.min_y = 13
            self.max_y = 31
            self.y_type = "BMI"

        layout = QVBoxLayout()

        self.text = QLabel("Enter " + self.y_type + " for age " + str(age))

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
            self.y = float(self.lineEdit1.text())

            if not (self.min_y <= self.y <= self.max_y):
                raise ValueError("Value out of range")
        except ValueError:
            self.submit_button.setEnabled(False)
            self.submit_button.setEnabled(True)
        else:
            self.accept()
            self.submit_button.setEnabled(True)