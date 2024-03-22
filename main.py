import matplotlib.pyplot as plt
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

from Menu import Menu

import sys

wiek = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
waga = [10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100]

centyl_3_wiek = [3, 3.5, 4, 4.5, 5, 5.5, 6, 6.5, 7, 7.5, 8, 8.5, 9, 9.5, 10, 10.5, 11, 11.5, 12, 12.5, 13, 13.5, 14, 14.5, 15, 15.5, 16, 16.5, 17, 17.5, 18]
centyl_3_waga = [12, 13, 14, 14.5, 15, 16, 17, 18, 18.5, 19, 20.5, 21.5, 22.5, 23.5, 24.5, 26, 27, 28, 30, 31.5, 33.5, 35, 38, 40, 43, 45, 47, 49.5, 51, 52.5, 54]

centyl_10_wiek = [3, 3.5, 4, 4.5, 5, 5.5, 6, 6.5, 7, 7.5, 8, 8.5, 9, 9.5, 10, 10.5, 11, 11.5, 12, 12.5, 13, 13.5, 14, 14.5, 15, 15.5, 16, 16.5, 17, 17.5, 18]
centyl_10_waga = [13, 13.75, 14.75, 15.5, 16, 17, 18, 19, 20.25, 21.25, 22.5, 23.5, 24.75, 25.75, 27, 28, 29.75, 31.25, 33, 35, 37, 39.75, 42, 44.75, 47, 49.25, 51.5, 53.5, 55.25, 57, 58.25]

centyl_25_wiek = [3, 3.5, 4, 4.5, 5, 5.5, 6, 6.5, 7, 7.5, 8, 8.5, 9, 9.5, 10, 10.5, 11, 11.5, 12, 12.5, 13, 13.5, 14, 14.5, 15, 15.5, 16, 16.5, 17, 17.5, 18]
centyl_25_waga = [13.75, 14.75, 15.75, 16.5, 17.25, 18.5, 19.5, 20.5, 22, 23, 24.75, 26, 27, 28.5, 30, 31.5, 33.1, 35, 37, 39.25, 41.5, 44.25, 46.75, 49.9, 52, 54.5, 56.5, 58.5, 60, 61.75, 63.5]

centyl_50_wiek = [3, 3.5, 4, 4.5, 5, 5.5, 6, 6.5, 7, 7.5, 8, 8.5, 9, 9.5, 10, 10.5, 11, 11.5, 12, 12.5, 13, 13.5, 14, 14.5, 15, 15.5, 16, 16.5, 17, 17.5, 18]
centyl_50_waga = [15, 16, 17, 18, 19, 20.25, 21.5, 22.9, 24.5, 26, 27.5, 29, 30.75, 32.5, 34.25, 36, 38, 40.25, 43, 45.25, 48, 51, 53.75, 56.25, 59, 61, 63, 65, 67, 68.5, 70]

centyl_75_wiek = [3, 3.5, 4, 4.5, 5, 5.5, 6, 6.5, 7, 7.5, 8, 8.5, 9, 9.5, 10, 10.5, 11, 11.5, 12, 12.5, 13, 13.5, 14, 14.5, 15, 15.5, 16, 16.5, 17, 17.5, 18]
centyl_75_waga = [16.5, 17.5, 18.75, 20, 21.25, 22.5, 24.5, 26, 27.75, 29.9, 31.5, 33.25, 35.5, 37.25, 39.9, 41.9, 44.75, 47, 50, 53, 55.75, 59, 62, 64.75, 67, 69.25, 71.25, 73.1, 74.9, 76.5, 78]

centyl_90_wiek = [3, 3.5, 4, 4.5, 5, 5.5, 6, 6.5, 7, 7.5, 8, 8.5, 9, 9.5, 10, 10.5, 11, 11.5, 12, 12.5, 13, 13.5, 14, 14.5, 15, 15.5, 16, 16.5, 17, 17.5, 18]
centyl_90_waga = [18, 19.25, 20.75, 22, 23.5, 25.5, 27.5, 29.5, 32, 34.25, 36.75, 38.75, 41.25, 44, 46.75, 49.75, 52.5, 55.1, 58.6, 61.9, 65, 68.5, 71, 73.75, 76, 78.25, 80, 82, 83.25, 84.9, 86]

centyl_97_wiek = [3, 3.5, 4, 4.5, 5, 5.5, 6, 6.5, 7, 7.5, 8, 8.5, 9, 9.5, 10, 10.5, 11, 11.5, 12, 12.5, 13, 13.5, 14, 14.5, 15, 15.5, 16, 16.5, 17, 17.5, 18]
centyl_97_waga = [20, 21.5, 23, 24.9, 26.75, 29.75, 32.1, 34.9, 37.5, 40.5, 43.5, 46.25, 49.5, 52.5, 56, 59, 62.75, 66, 69.75, 73.1, 76.5, 80, 82.75, 85, 87, 89, 90.5, 92.1, 93.5, 94.75, 96]



def frame(x,y):
    plt.figure(figsize=(6, 9))
    plt.plot(centyl_3_wiek, centyl_3_waga, label='Centyl 3', color='black')
    plt.plot(centyl_10_wiek, centyl_10_waga, label='Centyl 10', color='black',  linestyle='--')
    plt.plot(centyl_25_wiek, centyl_25_waga, label='Centyl 25', color='black',  linestyle=':')
    plt.plot(centyl_50_wiek, centyl_50_waga, label='Centyl 50', color='black',  linestyle='solid')
    plt.plot(centyl_75_wiek, centyl_75_waga, label='Centyl 75', color='black',  linestyle=':')
    plt.plot(centyl_90_wiek, centyl_90_waga, label='Centyl 90', color='black',  linestyle='--')
    plt.plot(centyl_97_wiek, centyl_97_waga, label='Centyl 97', color='black',  linestyle='solid')
    plt.scatter(x, y, label='Punkty XY', color='red', s=5)
    #if(z == 2):
    #    plt.plot(results[0], results[1], label='krzywa', color='red', linestyle=':')
    #if(z == 3):
    #    for i in range(results[2]):
    #        plt.scatter(results[0][i], results[1][i], label='Punkty XY', color='red', s=5)

    plt.text(centyl_3_wiek[-1], centyl_3_waga[-1], ' c3', verticalalignment='bottom')
    plt.text(centyl_10_wiek[-1], centyl_10_waga[-1], ' c10', verticalalignment='bottom')
    plt.text(centyl_25_wiek[-1], centyl_25_waga[-1], ' c25', verticalalignment='bottom')
    plt.text(centyl_50_wiek[-1], centyl_50_waga[-1], ' c50', verticalalignment='bottom')
    plt.text(centyl_75_wiek[-1], centyl_75_waga[-1], ' c75', verticalalignment='bottom')
    plt.text(centyl_90_wiek[-1], centyl_90_waga[-1], ' c90', verticalalignment='bottom')
    plt.text(centyl_97_wiek[-1], centyl_97_waga[-1], ' c97', verticalalignment='bottom')

    plt.title('Siatka centylowa')
    plt.xlabel('Wiek (lata)')
    plt.ylabel('Waga (kg)')

    plt.xticks(wiek)
    plt.xlim(3, 18)
    plt.ylim(10, 100)
    plt.yticks(waga)

    plt.grid(True)

    fig = plt.gcf()
    fig.tight_layout()
    fig.savefig('percentile_grid.png')
    plt.show(block=False)
    plt.show()

class SecondWindow(QDialog):
    def __init__(self, parent=None):
        super(SecondWindow, self).__init__(parent)
        self.setWindowTitle("Nowe Okno")

        layout = QVBoxLayout()
        self.lineEdit1 = QLineEdit()
        validator = QDoubleValidator()
        validator.setDecimals(2)
        validator.setLocale(QLocale(QLocale.English))
        self.lineEdit1.setValidator(validator)
        self.lineEdit2 = QLineEdit()
        self.lineEdit2.setValidator(validator)
        self.submit_button = QPushButton("Zatwierdź")
        layout.addWidget(self.lineEdit1)
        layout.addWidget(self.lineEdit2)
        layout.addWidget(self.submit_button)
        self.setLayout(layout)

        self.submit_button.clicked.connect(self.on_submit_clicked)
        self.x = None
        self.y = None

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

class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setWindowTitle("KidNet")
        self.setGeometry(200,200,300,300)

        central_widget = QWidget()
        layout = QVBoxLayout()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        self.button1 = QPushButton("Jedne dane")
        self.button1.setCheckable(True)
        layout.addWidget(self.button1)

        self.second_window = None
        self.button1.clicked.connect(self.open_second_window)

    def open_second_window(self):
        self.second_window = SecondWindow(self)
        self.second_window.exec_()

        if self.second_window.result() == QDialog.Accepted:
            x = self.second_window.x
            y = self.second_window.y
            frame(x, y)
if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()

#while True:
#    try:
#        z = input("Wybierz tryb \n '1' Jedna wartość \n '2' Podanie wartości od 3 lat do 18 lat(co pół roku) \n '3' Wiele wartości \n")
#        if z.isdigit():
#            z = int(z)
#            if 1 <= z <=3:
#                if(z == 1):
#                    results = menu.displey_First()
#                if(z == 2):
#                    results = menu.displey_second()
#                if (z == 3):
#                    results = menu.displey_trird()
#                break
#            else:
#                print("To nie jest poprawna liczba")
#        else:
#            print("To nie jest poprawna liczba.")
#    except ValueError:
#        print("To nie jest poprawna liczba")
