import sys
import random
from functools import partial
from PySide2.QtWidgets import (QApplication, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout, QPushButton, QLabel, QMessageBox, QSizePolicy)
from PySide2.QtGui import QFont
from PySide2.QtCore import Qt

class UI_MainWindow(QWidget):
    def __init__(self):
        super(UI_MainWindow, self).__init__()
        
        self.setFixedSize(600, 700)
        self.setStyleSheet('background-color: #323232')

        v_layout = QVBoxLayout(self)

        h_layout = QHBoxLayout()
        h_layout.setContentsMargins(0, 0, 0, 20)
        v_layout.addLayout(h_layout)

        grid_layout = QGridLayout()
        v_layout.addLayout(grid_layout)

        self.btnExit = QPushButton('Exit')
        self.btnExit.setStyleSheet('background-color: #ff1e56; font-size:24px;border-radius: 10px;')
        self.btnExit.setFixedSize(180, 60)
        self.btnExit.clicked.connect(self.exitApp)
        h_layout.addWidget(self.btnExit, alignment=Qt.AlignLeft)

        self.btns = [[QPushButton() for _ in range(4)]for _ in range(4)]

        for i in range(4):
            for j in range(4):
                while True:
                    x = random.randint(1, 16)
                    if all(self.btns[k][l].text() != str(x) for k in range(4) for l in range(4)):
                        self.btns[i][j].setText(str(x))
                        break

        for i in range(4):
            for j in range(4):
                self.btns[i][j].setStyleSheet('background-color: #FF8C00; font-size:48px; border-radius: 10px;')
                sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
                self.btns[i][j].setSizePolicy(sizePolicy)
                self.btns[i][j].clicked.connect(partial(self.play, i, j))
                self.btns[i][j].setMaximumSize(150, 150)
                grid_layout.addWidget(self.btns[i][j], i, j)

                if self.btns[i][j].text() == str(16):
                    self.btns[i][j].hide()
                    self.x_empty = i
                    self.y_empty = j
                    
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.show()

    def play(self, x, y):
        if (x == self.x_empty and abs(y - self.y_empty) == 1) or (abs(x - self.x_empty) == 1 and y == self.y_empty):
            self.btns[self.x_empty][self.y_empty].show()
            self.btns[self.x_empty][self.y_empty]. setText(self.btns[x][y].text())

            self.btns[x][y].hide()
            self.x_empty = x
            self.y_empty = y

        self.check()
    
    def check(self):
        check_list = []
        for i in range(4):
            for j in range(4):
                check_list.append(int(self.btns[i][j].text()))
        if check_list == sorted(check_list):
            self.winBox()
    
    def winBox(self):
        MessageBox = QMessageBox()
        MessageBox.setStyleSheet("QLabel{min-width: 150px; min-height: 50px; color: #FF8C00;} QPushButton{min-width: 120px; min-height: 40px;} QMessageBox { background-color: #323232; font-size: 24px;}")
        MessageBox.setText('YOU WIN!')
        
        MessageBox.setStandardButtons(QMessageBox.Ok)

        buttonOK = MessageBox.button(QMessageBox.Ok)
        buttonOK.setText('OK!')
        buttonOK.setStyleSheet('background-color: #ff1e56; border-radius: 10px; font-size:20px')
        MessageBox.exec()
        
        if MessageBox.clickedButton() == buttonOK:
            MessageBox.close()
    
    def exitApp(self):
        self.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = UI_MainWindow()
    sys.exit(app.exec_())