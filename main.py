import matplotlib.pyplot as plt
from math import *
import decimal
import numpy as np
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QFileDialog
import matplotlib
import FirstWindow
from FirstWindow import Ui_GrafFunk
from HandW import Ui_HandW
from RandW import Ui_RandW

def openSecondWindow():
    global HandW
    HandW = QtWidgets.QMainWindow()
    ui = Ui_HandW()
    ui.setupUi(HandW)
    HandW.show()

    def returnToMain():
        HandW.close()

    def Function2():
        x = ui.HRSB1x.value()
        xk = ui.HRSB3xk.value()
        a = ui.HRSP2a.value()
        b = ui.HRSB4b.value()
        c = ui.HRSB4c.value()
        k = ui.HRSB4K.value()
        if x > xk:
            x, xk = xk, x
            ui.HRSB1x.setValue(xk)
            ui.HRSB3xk.setValue(x)
        if ui.HR1button.isChecked(): #y=kx+b
            xar, yar = graf1(x, xk, b, k)
            if x == 0 and xk == 0 :
                QtWidgets.QMessageBox.about(HandW, 'Внимание!!!', 'Введены не все данные!!!')
            else:
                plt.plot(xar, yar)
                plt.plot(0, 0, marker='x', color='g')
                plt.title('График линейной функции')
                plt.grid()
                plt.xlabel('Ось X')
                plt.ylabel('Ось Y')
                plt.show()
        elif ui.HR2button.isChecked(): # y=ax**2+bx+c
            if a == 0 or (x == 0 and xk == 0):
                QtWidgets.QMessageBox.about(HandW, 'Внимание!!!', 'Введены не все данные!!!')
            else:
                xar, yar = graf2(x, xk, a, b, c)
                plt.plot(xar, yar)
                plt.plot(0, 0, marker='x', color='g')
                plt.title('График параболы')
                plt.grid()
                plt.xlabel('Ось X')
                plt.ylabel('Ось Y')
                plt.show()
        elif ui.HR3button.isChecked(): #y=k/x
            if (k == 0) or (x == 0 and xk == 0):
                QtWidgets.QMessageBox.about(HandW, 'Внимание!!!', 'Введены не все данные!!!')
            else:
                xt, yt, xb, yb = graf3(x, xk, k)
                if x != 0 and xk != 0:
                    if x > 0 and xk > 0:
                        plt.plot(xt, yt)
                    elif x < 0 and xk < 0:
                        plt.plot(xb, yb)
                    else:
                        plt.plot(xb, yb)
                        plt.plot(xt, yt)
                elif x < 0 and xk == 0:
                    plt.plot(xb, yb)
                elif x == 0 and xk > 0:
                    plt.plot(xt, yt)
                plt.plot(0, 0, marker='x', color='g')
                plt.title('График гиперболы')
                plt.grid()
                plt.xlabel('Ось X')
                plt.ylabel('Ось Y')
                plt.show()
        elif ui.HR4button.isChecked(): #y=e**x
            xar, yar = graf4(x, xk)
            if x == 0 and xk == 0:
                QtWidgets.QMessageBox.about(HandW, 'Внимание!!!', 'Введены не все данные!!!')
            else:
                plt.plot(xar, yar)
                plt.plot(0, 0, marker='x', color='g')
                plt.title('График экспоненты')
                plt.grid()
                plt.xlabel('Ось X')
                plt.ylabel('Ось Y')
                plt.show()
        elif ui.HR5button.isChecked():
            xx, y = graf5(x,xk)
            if x == 0 and xk == 0:
                QtWidgets.QMessageBox.about(HandW, 'Внимание!!!', 'Введены не все данные!!!')
            else:
                plt.plot(xx, y)
                plt.plot(0, 0, marker='x', color='g')
                plt.title('График синусоиды')
                plt.grid()
                plt.xlabel('Ось X')
                plt.ylabel('Ось Y')
                plt.show()
        return x, xk, a, b, c, k

    def saveFiles():
        x, xk, a, b, c, k = Function2()
        f = QFileDialog.getSaveFileName(HandW, 'Сохранить ведомость ', 'results', "Текстовый документ (*.txt);;All Files (*)")[0]
        try:
            file = open(f, 'w', encoding='utf-8')
            if ui.HR1button.isChecked():
                file.write(f'График линейной функции\n')
                file.write(f'{x}\n')
                file.write(f'{xk}\n')
                file.write(f'{b}\n')
                file.write(f'{k}\n')
            elif ui.HR2button.isChecked():
                file.write(f'График параболы\n')
                file.write(f'{x}\n')
                file.write(f'{xk}\n')
                file.write(f'{a}\n')
                file.write(f'{b}\n')
                file.write(f'{c}\n')
            elif ui.HR3button.isChecked():
                file.write(f'График гиперболы\n')
                file.write(f'{x}\n')
                file.write(f'{xk}\n')
                file.write(f'{k}\n')
            elif ui.HR4button.isChecked():
                file.write(f'График экспоненты\n')
                file.write(f'{x}\n')
                file.write(f'{xk}\n')
            elif ui.HR5button.isChecked():
                file.write(f'График синусоиды\n')
                file.write(f'{x}\n')
                file.write(f'{xk}\n')
            file.close()
        except:
            pass

    def openFiles():
        try:
            f = QFileDialog.getOpenFileName(HandW, 'Открыть файл ', filter="Текстовый документ (*.txt);;All Files (*)")[0]
            file = open(f, 'r', encoding='utf-8')
            header = file.readline().replace('\n', '')
            if header == 'График линейной функции':
                x = float(file.readline())
                xk = float(file.readline())
                b = float(file.readline())
                k = float(file.readline())
                xar = []
                yar = []
                while x <= xk:
                    y = k * x + b
                    xar.append(x)
                    yar.append(y)
                    x += 0.5
                if x == 0 and xk ==0 :
                    QtWidgets.QMessageBox.about(HandW, 'Внимание!!!', 'Введены не все данные!!!')
                else:
                    plt.plot(xar, yar)
                    plt.plot(0, 0, marker='x', color='g')
                    plt.title('График линейной функции')
                    plt.grid()
                    plt.xlabel('Ось X')
                    plt.ylabel('Ось Y')
                    plt.show()
            elif header == 'График параболы':
                x = float(file.readline())
                xk = float(file.readline())
                a = float(file.readline())
                b = float(file.readline())
                c = float(file.readline())
                xar = []
                yar = []
                if a == 0 or (x == 0 and xk == 0):
                    QtWidgets.QMessageBox.about(HandW, 'Внимание!!!', 'Введены не все данные!!!')
                while x <= xk:
                    y = (a * (x ** 2)) + (b * x) + c
                    xar.append(x)
                    yar.append(y)
                    x += 0.5
                    plt.plot(xar, yar)
                    plt.plot(0, 0, marker='x', color='g')
                    plt.title('График параболы')
                    plt.grid()
                    plt.xlabel('Ось X')
                    plt.ylabel('Ось Y')
                    plt.show()
            elif header == 'График гиперболы':
                x = float(file.readline())
                xk = float(file.readline())
                k = float(file.readline())
                if (k == 0) or (x == 0 and xk == 0):
                    QtWidgets.QMessageBox.about(HandW, 'Внимание!!!', 'Введены не все данные!!!')
                else:
                    xt = np.linspace(0.5, xk)
                    xb = np.linspace(x, -0.5)
                    yt = k / xt
                    yb = k / xb
                    if x != 0 and xk != 0:
                        if x > 0 and xk > 0:
                            plt.plot(xt, yt)
                        elif x < 0 and xk < 0:
                            plt.plot(xb, yb)
                        else:
                            plt.plot(xb, yb)
                            plt.plot(xt, yt)
                    elif x < 0 and xk == 0:
                        plt.plot(xb, yb)
                    elif x == 0 and xk > 0:
                        plt.plot(xt, yt)
                    plt.plot(0, 0, marker='x', color='g')
                    plt.title('График гиперболы')
                    plt.grid()
                    plt.xlabel('Ось X')
                    plt.ylabel('Ось Y')
                    plt.show()
            elif header == 'График экспоненты':
                x = float(file.readline())
                xk = float(file.readline())
                xar = []
                yar = []
                while x <= xk:
                    y = exp(x)
                    xar.append(x)
                    yar.append(y)
                    x += 0.5
                if x == 0 and xk == 0:
                    QtWidgets.QMessageBox.about(HandW, 'Внимание!!!', 'Введены не все данные!!!')
                else:
                    plt.plot(xar, yar)
                    plt.plot(0, 0, marker='x', color='g')
                    plt.title('График экспоненты')
                    plt.grid()
                    plt.xlabel('Ось X')
                    plt.ylabel('Ось Y')
                    plt.show()
            elif header == 'График синусоиды':
                x = float(file.readline())
                xk = float(file.readline())
                xx = np.linspace(x, xk * np.pi)
                y = np.sin(xx)
                if x == 0 and xk == 0:
                    QtWidgets.QMessageBox.about(HandW, 'Внимание!!!', 'Введены не все данные!!!')
                else:
                    plt.plot(xx, y)
                    plt.plot(0, 0, marker='x', color='g')
                    plt.title('График синусоиды')
                    plt.grid()
                    plt.xlabel('Ось X')
                    plt.ylabel('Ось Y')
                    plt.show()
        except:
            pass

    ui.open.clicked.connect(openFiles)
    ui.save.clicked.connect(saveFiles)
    ui.HRButtonGen.clicked.connect(Function2)
    ui.pushButton.clicked.connect(returnToMain)

def graf1(x, xk, b, k):
    xar = []
    yar = []
    while x <= xk:
        y = k * x + b
        xar.append(x)
        yar.append(y)
        x += 0.5
    return xar, yar

def graf2(x, xk, a, b, c):
    xar = []
    yar = []
    while x <= xk:
        y = (a * (x ** 2)) + (b * x) + c
        xar.append(x)
        yar.append(y)
        x += 0.5
    return xar, yar

def graf3(x, xk, k):
    xt = np.around(np.linspace(0.5, xk), decimals=4)
    xb = np.around(np.linspace(x, -0.5), decimals=4)
    yt = k / xt
    yb = k / xb
    return xt, yt, xb, yb

def graf4(x, xk):
    xar = []
    yar = []
    while x <= xk:
        y = exp(x)
        xar.append(x)
        yar.append(y)
        x += 0.5
    return xar, yar

def graf5(x, xk):
    xx = np.linspace(x, xk * np.pi, 2000)
    y = np.sin(xx)
    return xx, y

def openThirdWindow():
    global RandW
    RandW = QtWidgets.QMainWindow()
    ui = Ui_RandW()
    ui.setupUi(RandW)
    RandW.show()

    def returnToMain2():
        RandW.close()

    def Function1():
        x = -10
        xk = 10
        dx = 1
        yy = []
        xx = []
        if ui.RR1button.isChecked():  # y=kx+b
            while x <= xk:
                y = 1 * x + 0
                xx.append(x)
                yy.append(y)
                x += 1
                plt.plot(xx, yy)
                plt.plot(0, 0, marker='x', color='g')
                plt.title('График линейной функции')
        elif ui.RR2button.isChecked(): #y=ax**2+bx+c
            xx = np.arange(x, xk, dx)
            plt.plot(xx, xx**2)
            plt.plot(0, 0, marker='x', color='g')
            plt.title('График параболы')
        elif ui.RR3button.isChecked(): #y=k/x
            xx = np.around(np.arange(x, xk, dx), decimals=4)
            yy = 1 / xx
            plt.plot(xx, yy)
            plt.plot(0, 0, marker='x', color='g')
            plt.title('График гиперболы')
        elif ui.RR4button.isChecked(): #y=e**x
            while x <= xk:
                y = exp(x)
                xx.append(x)
                yy.append(y)
                x += 1
                plt.plot(xx, yy)
                plt.plot(0, 0, marker='x', color='g')
                plt.title('График экспоненты')
        elif ui.RR5button.isChecked(): #y=sinx
            x = np.linspace(-10, 2.0*np.pi, 101)
            y = np.sin(x)
            plt.plot(x, y)
            plt.plot(0, 0, marker='x', color='g')
            plt.title('График синусоиды')
        plt.grid()
        plt.xlabel('Ось X')
        plt.ylabel('Ось Y')
        plt.show()


    ui.RRButtonGen.clicked.connect(Function1)
    ui.pushButton.clicked.connect(returnToMain2)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    GrafFunk = QtWidgets.QMainWindow()
    ui = Ui_GrafFunk()
    ui.setupUi(GrafFunk)
    ui.HRButton.clicked.connect(openSecondWindow)
    ui.RRButton.clicked.connect(openThirdWindow)
    GrafFunk.show()
    sys.exit(app.exec())