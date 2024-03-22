from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class Menu:
    def displey_First(self):
        while True:
            try:
                x = input("Podaj wiek z zekresu (3-18): ")
                if x.replace('.', '', 1).isdigit():
                    x = float(x)
                    if 3 <= x <= 18:
                        break
                    else:
                        print("Wiek musi być z zakresu 3-18")
                else:
                    print("To nie jest poprawna liczba.")
            except ValueError:
                print("To nie jest poprawna liczba")

        while True:
            try:
                y = input("Podaj wagę z zakresu (10-100): ")
                if y.replace('.', '', 1).isdigit():
                    y = float(y)
                    if 10 <= y <= 100:
                        break
                    else:
                        print("Waga musi być z zakresu od 10 do 100.")
                else:
                    print("To nie jest poprawna liczba.")
            except ValueError:
                print("To nie jest poprawna liczba.")

        return x, y

    def displey_second(self):
        c = 3
        krzywa_wiek = [3, 3.5, 4, 4.5, 5, 5.5, 6, 6.5, 7, 7.5, 8, 8.5, 9, 9.5, 10, 10.5, 11, 11.5, 12, 12.5, 13, 13.5,
                       14, 14.5, 15, 15.5, 16, 16.5, 17, 17.5, 18]
        krzywa_waga = []

        while True:
            try:
                i = float(input("Podaj wartość dla wieku " + str(c) + ":\n"))
                if 10 <= i <= 100:
                    krzywa_waga.append(i)
                    c += 0.5
                    if c == 18.5:
                        break
                else:
                    print("Wartość musi być z zakresu od 10 do 100.")
            except ValueError:
                print("To nie jest poprawna liczba.")

        return krzywa_wiek, krzywa_waga

    def displey_trird(self):
        punkty_wiek = []
        punkty_waga = []
        while True:
            try:
                x = input("Podaj ilość punktów: ")
                if x.isdigit():
                    x = int(x)
                    if 0 < x:
                        break
                    else:
                        print("To nie jest poprawna liczba")
                else:
                    print("To nie jest poprawna liczba.")
            except ValueError:
                print("To nie jest poprawna liczba")

        for i in range(x):
            while True:
                try:
                    y_wiek = input("Podaj wiek dla " + str(i + 1) + " wartości z zekresu (3-18): ")
                    if y_wiek.replace('.', '', 1).isdigit():
                        y_wiek = float(y_wiek)
                        if 3 <= y_wiek <= 18:
                            punkty_wiek.append(y_wiek)
                            break
                        else:
                            print("Wiek musi być z zakresu 3-18")
                    else:
                        print("To nie jest poprawna liczba.")
                except ValueError:
                    print("To nie jest poprawna liczba")

            while True:
                try:
                    y_waga = input("Podaj wagę z zakresu (10-100): ")
                    if y_waga.replace('.', '', 1).isdigit():
                        y_waga = float(y_waga)
                        if 10 <= y_waga <= 100:
                            punkty_waga.append(y_waga)
                            break
                        else:
                            print("Waga musi być z zakresu od 10 do 100.")
                    else:
                        print("To nie jest poprawna liczba.")
                except ValueError:
                    print("To nie jest poprawna liczba.")

        return punkty_wiek, punkty_waga, x
#-------------------------------------------------------------------------------------------------------------
