import sys
import matplotlib.pyplot as plt
from math import ceil, fabs, tan, sin, cos, exp, log
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setGeometry(200, 200, 1240, 500)
        self.setWindowTitle('Метод Рунге-Кутта')

        self.L0 = QLabel(self)
        self.L1 = QLabel(self)
        self.L1.resize(300, 40)
        self.L12 = QLabel(self)
        self.L13 = QLabel(self)
        self.L14 = QLabel(self)
        self.L0.setFont(QFont('Calibri', 15))
        self.L1.setFont(QFont('Gotham', 15))
        self.L12.setFont(QFont('Calibri', 15))
        self.L13.setFont(QFont('Calibri', 10))
        self.L14.setFont(QFont('Calibri', 10))
        self.L1.setText("y' = -y * tg(x) + sin(2x)")
        self.L0.move(105, 10)
        self.L1.move(50, 20)
        self.L12.move(105, 45)
        self.L13.move(113, 35)
        self.L14.move(160, 5)

        self.L2 = QLabel(self)
        self.L2.setFont(QFont('Gotham', 12))
        self.L2.setText("Начальная точка:")
        self.L2.resize(200, 30)
        self.L2.move(10, 100)
        self.input2 = QLineEdit(self)
        self.input2.setFont(QFont('Gotham', 12))
        self.input2.resize(160, 35)
        self.input2.move(200, 100)

        self.L3 = QLabel(self)
        self.L3.setFont(QFont('Gotham', 12))
        self.L3.setText("Конечная точка:")
        self.L3.resize(200, 30)
        self.L3.move(10, 150)
        self.input3 = QLineEdit(self)
        self.input3.setFont(QFont('Gotham', 12))
        self.input3.resize(160, 35)
        self.input3.move(200, 150)

        self.L4 = QLabel(self)
        self.L4.setFont(QFont('Gotham', 12))
        self.L4.resize(200, 30)
        self.L4.setText("Шаг:")
        self.L4.move(10, 200)
        self.input4 = QLineEdit(self)
        self.input4.setFont(QFont('Gotham', 12))
        self.input4.resize(160, 35)
        self.input4.move(200, 200)

        self.L5 = QLabel(self)
        self.L5.setFont(QFont('Gotham', 12))
        self.L5.resize(200, 30)
        self.L5.setText("Начальное X:")
        self.L5.move(10, 250)
        self.input5 = QLineEdit(self)
        self.input5.setFont(QFont('Gotham', 12))
        self.input5.resize(160, 35)
        self.input5.move(200, 250)

        self.L6 = QLabel(self)
        self.L6.setFont(QFont('Gotham', 12))
        self.L6.resize(200, 30)
        self.L6.setText("Начальное Y:")
        self.L6.move(10, 300)
        self.input6 = QLineEdit(self)
        self.input6.setFont(QFont('Gotham', 12))
        self.input6.resize(160, 35)
        self.input6.move(200, 300)

        # BUTTONS
        self.btn1 = QPushButton('Запуск программы', self)
        self.btn1.setFont(QFont('Gotham', 15))
        self.btn1.resize(250, 80)
        self.btn1.move(50, 370)
        self.btn1.clicked.connect(self.go)

        # TABLE
        self.table = QTableWidget(self)
        self.table.setFont(QFont('Times', 10))
        self.table.move(370, 12)
        self.table.resize(860, 480)
        self.table.setColumnCount(4)
        self.table.setColumnWidth(0, 200)
        self.table.setColumnWidth(1, 200)
        self.table.setColumnWidth(2, 200)
        self.table.setColumnWidth(3, 200)
        self.table.setStyleSheet("QTableWidget {border: 2px solid black;}")
        self.table.setHorizontalHeaderLabels(['X', 'Y точное', 'Y приближ.', 'Погрешность'], )

    def go(self):

        def f(x, y):
            return -y * tan(x) + sin(2 * x)

        def g(x):
            return cos(x) - 2 * cos(x) ** 2

        a, b = float(self.input2.text()), float(self.input3.text())
        x0, y0 = float(self.input5.text()), float(self.input6.text())
        h = float(self.input4.text())

        eps = 1e-3
        epsp = 15 * eps
        n = ceil((b - a) / h)

        x = [x0]
        y = [y0]
        for i in range(1, n + 1):
            k1 = f(x[i - 1], y[i - 1])
            k2 = f(x[i - 1] + h / 2, y[i - 1] + h / 2 * k1)
            k3 = f(x[i - 1] + h / 2, y[i - 1] + h / 2 * k2)
            k4 = f(x[i - 1] + h, y[i - 1] + h * k3)
            new_x_value = x[i - 1] + h
            new_y_value = y[i - 1] + h * (k1 + 2 * k2 + 2 * k3 + k4) / 6
            x.append(new_x_value)
            y.append(new_y_value)

        while True:
            is_last = True
            old_x, old_y = x, y
            h = h / 2
            n = 2 * n
            self.table.setRowCount(n + 1)
            x = [x0]
            y = [y0]
            for i in range(1, n + 1):
                k1 = f(x[i - 1], y[i - 1])
                k2 = f(x[i - 1] + h / 2, y[i - 1] + h / 2 * k1)
                k3 = f(x[i - 1] + h / 2, y[i - 1] + h / 2 * k2)
                k4 = f(x[i - 1] + h, y[i - 1] + h * k3)
                new_x_value = x[i - 1] + h
                new_y_value = y[i - 1] + h * (k1 + 2 * k2 + 2 * k3 + k4) / 6
                x.append(new_x_value)
                y.append(new_y_value)
                if i % 2 == 0:
                    if fabs(y[i] - old_y[i // 2]) >= epsp:
                        is_last = False
            if is_last:
                break

        z = [g(x_value) for x_value in x]

        for i in range(n + 1):
            a = str(round(x[i], 1))
            b = str(round(z[i], 7))
            c = str(round(y[i], 7))
            d = str(round(fabs(y[i] - z[i]), 13))
            self.table.setItem(i, 0, QTableWidgetItem(a))
            self.table.setItem(i, 1, QTableWidgetItem(b))
            self.table.setItem(i, 2, QTableWidgetItem(c))
            self.table.setItem(i, 3, QTableWidgetItem(d))

        fig = plt.figure(figsize=(7, 5))
        ax = fig.add_subplot()
        ax.set_xlabel('X')
        ax.set_ylabel('Y')

        ax.grid(which='major', color='black', linewidth=1, linestyle='--')
        plt.plot(x, y, label="Приближённое решение", ms=6, mfc='k', mew=4, marker='.', color='r')
        plt.plot(x, z, label="Аналитическое решение", color='b')

        plt.legend()
        plt.show()


app = QApplication(sys.argv)
ex = MainWindow()
ex.show()
sys.exit(app.exec())
