import matplotlib.pyplot as plt

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

from Modes import *
from Frame import Frame

import sys

class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        self.Diagram = 1
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setWindowTitle("KidNet")
        self.setGeometry(200,40,300,300)
        self.setFixedSize(1500,900)

        central_widget = QWidget()
        main_layout = QHBoxLayout()
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)

        left_layout = QVBoxLayout()
        main_layout.addLayout(left_layout)

        right_layout = QVBoxLayout()
        main_layout.addLayout(right_layout)

        self.Name = QLineEdit()
        self.Name.setFixedSize(QSize(250,50))
        left_layout.addWidget(self.Name)

        self.button_single = QPushButton("Single data")
        self.button_single.setCheckable(True)
        self.button_single.setFixedSize(QSize(250, 50))
        left_layout.addWidget(self.button_single)

        self.button_multi = QPushButton("Multi data")
        self.button_multi.setCheckable(True)
        self.button_multi.setFixedSize(QSize(250, 50))
        left_layout.addWidget(self.button_multi)

        self.button_curve = QPushButton("Data curve")
        self.button_curve.setCheckable(True)
        self.button_curve.setFixedSize(QSize(250, 50))
        left_layout.addWidget(self.button_curve)

        self.combo_box = QComboBox()
        self.combo_box.addItems(["body weight to age 3-18 (OLAF)", "body weight to age 3-18 (OLA)", "height to age 3-18 (OLAF)", "height to age 3-18 (OLA)", "BMI (OLAF)"])
        self.combo_box.setFixedSize(250,50)
        self.combo_box.currentIndexChanged.connect(self.set_diagram_value)
        left_layout.addWidget(self.combo_box)

        right_layout.setAlignment(Qt.AlignRight)
        self.label_image = QLabel()
        right_layout.addWidget(self.label_image)

        self.second_window = None
        self.button_single.clicked.connect(self.open_second_window_for_single)
        self.button_multi.clicked.connect(self.open_second_window_for_multiple)
        self.button_curve.clicked.connect(self.open_second_window_for_curve)

    def open_second_window_for_single(self):
        self.Name_Grid = str(self.Name.text())
        self.second_window = SecondWindow_for_single(self.Diagram)
        self.second_window.exec_()

        if self.second_window.result() == QDialog.Accepted:
            Weight = self.second_window.x
            Age = self.second_window.y
            frame.frame_init(self.Name_Grid , Weight, Age, 1, 0, self.Diagram)
            self.label_image.setPixmap(QPixmap('percentile_grid.png'))

    def open_second_window_for_multiple(self):
        self.Name_Grid = str(self.Name.text())
        self.second_window = SecondWindow_for_multiple(self.Diagram, self.Name_Grid)
        self.second_window.exec_()
        self.label_image.setPixmap(QPixmap('percentile_grid.png'))

    def open_second_window_for_curve(self):
        self.Name_Grid = str(self.Name.text())

        if self.Diagram == 1:
            x_current = 3
            x_end = 18
            y_data = []
            x_data = [3, 3.5, 4, 4.5, 5, 5.5, 6, 6.5, 7, 7.5, 8, 8.5, 9, 9.5, 10, 10.5, 11, 11.5, 12, 12.5, 13, 13.5, 14, 14.5, 15, 15.5, 16, 16.5, 17, 17.5, 18]
        if self.Diagram == 2:
            x_current = 3
            x_end = 18
            y_data = []
            x_data = [3, 3.5, 4, 4.5, 5, 5.5, 6, 6.5, 7, 7.5, 8, 8.5, 9, 9.5, 10, 10.5, 11, 11.5, 12, 12.5, 13, 13.5, 14, 14.5, 15, 15.5, 16, 16.5, 17, 17.5, 18]
        if self.Diagram == 3:
            x_current = 3
            x_end = 18
            y_data = []
            x_data = [3, 3.5, 4, 4.5, 5, 5.5, 6, 6.5, 7, 7.5, 8, 8.5, 9, 9.5, 10, 10.5, 11, 11.5, 12, 12.5, 13, 13.5, 14, 14.5, 15, 15.5, 16, 16.5, 17, 17.5, 18]
        if self.Diagram == 4:
            x_current = 3
            x_end = 18
            y_data = []
            x_data = [3, 3.5, 4, 4.5, 5, 5.5, 6, 6.5, 7, 7.5, 8, 8.5, 9, 9.5, 10, 10.5, 11, 11.5, 12, 12.5, 13, 13.5, 14, 14.5, 15, 15.5, 16, 16.5, 17, 17.5, 18]
        if self.Diagram == 5:
            x_current = 3
            x_end = 18
            y_data = []
            x_data = [3, 3.5, 4, 4.5, 5, 5.5, 6, 6.5, 7, 7.5, 8, 8.5, 9, 9.5, 10, 10.5, 11, 11.5, 12, 12.5, 13, 13.5,
                      14, 14.5, 15, 15.5, 16, 16.5, 17, 17.5, 18]

        while x_current <= x_end:
            if self.second_window is not None:
                self.second_window.deleteLater()
            self.second_window = SecondWindow_for_curve(x_current, self.Diagram)
            self.second_window.exec_()
            if self.second_window.result() == QDialog.Accepted:
                y_data.append(self.second_window.y)
            x_current += 0.5

        if y_data:
            frame.frame_init(self.Name_Grid ,y_data ,x_data ,3, 0, self.Diagram)
            self.label_image.setPixmap(QPixmap('percentile_grid.png'))

    def set_diagram_value(self, index):
        if index == 0:
            self.Diagram = 1
        elif index == 1:
            self.Diagram = 2
        elif index == 2:
            self.Diagram = 3
        elif index == 3:
            self.Diagram = 4
        elif index == 4:
            self.Diagram = 5

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    frame = Frame()
  #  with open('styles.css', 'r') as file:
  #      style = file.read()
  #  app.setStyleSheet(style)
    window.show()
    app.exec_()

