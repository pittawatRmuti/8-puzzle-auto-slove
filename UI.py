import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QGridLayout
from PyQt5.QtGui import QFont, QPalette
from PyQt5.QtCore import QTimer, Qt
from PyQt5 import QtWidgets
import numpy as np
from tabulate import tabulate
import random_State
import randomModel
import algorithm


class UI_main(QWidget):

    def __init__(self):
        super().__init__()
        self.Main = QWidget()
        self.Main.setFixedSize(820, 620)
        self.Main.setWindowTitle('Hill-climbing search 8-puzzle')
        self.Box_Goal = []
        self.Box_Start = []
        self.Button_()
        self.Display_()
        self.BoxStart_()
        self.BoxGoal_()
        self.sloveButton.clicked.connect(self.Slove_)
        self.startButton.clicked.connect(self.Start_)
        self.resetButton.clicked.connect(self.Reset_)
        self.timer = QTimer(self)
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.checkResult)
        self.Main.show()

    def Slove_(self):
        random_start = radomState_class.randomNumber()
        random_goal = random_start
        arr_Start = radomState_class.checkStart(random_start)
        arr_Goal = radomState_class.checkGoal(random_goal)
        randommodel.setRandomStart(arr_Start)
        randommodel.setRadomGoal(arr_Goal)
        self.disPlay.setPlainText('')
        self.disPlay.setPlainText('Please press the start button')
        self.UpdateBoxStart_(arr_Start)
        self.UpdateBoxGoal_(arr_Goal)

    def Start_(self):
        lastMove = 'down'
        arr_Start = randommodel.getStart()
        arr_Goal = randommodel.getGoal()
        h, row, col = al_control.firstround(arr_Start, arr_Goal)
        randommodel.set_H(h)
        randommodel.setPosition(row, col)
        randommodel.set_lastMove(lastMove)
        self.disPlay.setPlainText('')
        self.timer.start()

    def Reset_(self):
        firstRun()
        Start = randommodel.getStart()
        Goal = randommodel.getGoal()
        self.UpdateBoxStart_(Start)
        self.UpdateBoxGoal_(Goal)
        self.disPlay.setPlainText(
            'Press the Start button or the Slove button.')

    def checkResult(self):
        h = randommodel.get_H()
        row, col = randommodel.getPosition()
        lastMove = randommodel.get_lastMove()
        arr_Start = randommodel.getStart()
        arr_Goal = randommodel.getGoal()

        if h > 0:
            h, arr_Start, lastMove, row, col, Move = al_control.algorithm(
                row, col, arr_Start, arr_Goal, h, lastMove)
            randommodel.set_H(h)
            randommodel.setPosition(row, col)
            randommodel.set_lastMove(lastMove)
            randommodel.setRandomStart(arr_Start)
            randommodel.setmoveText(Move)
            self.UpdateBoxStart_(arr_Start)
            self.DisplayShow_()
        else:
            self.timer.stop()

    def Button_(self):
        # Font
        self.font = QFont()
        self.font.setPointSize(15)
        self.font.setBold(True)
        self.font.setWeight(75)
        # Slove Button
        self.sloveButton = QPushButton('Slove', self.Main)
        self.sloveButton.setGeometry(330, 60, 110, 40)
        self.sloveButton.setFont(self.font)
        # StartButton
        self.startButton = QPushButton('Start', self.Main)
        self.startButton.setGeometry(450, 60, 110, 40)
        self.startButton.setFont(self.font)
        # ResetButton
        self.resetButton = QPushButton('Reset', self.Main)
        self.resetButton.setGeometry(570, 60, 111, 41)
        self.resetButton.setFont(self.font)

    def Display_(self):
        self.disPlay = QtWidgets.QPlainTextEdit(self.Main)
        self.disPlay.setGeometry(330, 160, 350, 380)
        font = QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.setFont(font)
        font.setWeight(75)
        self.disPlay.setFont(font)
        self.disPlay.setPlainText(
            'Press the Start button or the Slove button.')

    def DisplayShow_(self):
        numStart = randommodel.getStart()
        move = randommodel.getTextmove()
        H = randommodel.get_H()
        self.disPlay.appendPlainText(f'-> Move : {move}  Heuristic : {H}')
        self.disPlay.appendPlainText(tabulate(numStart))

    def BoxStart_(self):
        self.gridwidgetStart = QWidget(self.Main)
        self.gridwidgetStart.setGeometry(30, 10, 270, 270)
        self.TextStart = QLabel('Start State', self.Main)
        self.TextStart.setGeometry(100, 275, 270, 40)
        self.TextStart.setFont(self.font)
        self.grid_Start = QGridLayout()
        self.grid_Start.setSpacing(10)
        self.gridwidgetStart.setLayout(self.grid_Start)
        self.UpdateBoxStart_(randommodel.getStart())

    def UpdateBoxStart_(self, num):
        self.Box_Start = num.reshape(3, 3)
        for Row in range(len(self.Box_Start)):
            for Column in range(len(self.Box_Start - 1)):
                self.grid_Start.addWidget(Label_Block(
                    self.Box_Start[Row][Column]), Row, Column)
        self.gridwidgetStart.setLayout(self.grid_Start)

    def BoxGoal_(self):
        self.gridwidgetGoal = QWidget(self.Main)
        self.gridwidgetGoal.setGeometry(30, 310, 270, 270)
        self.TextGoal = QLabel('Goal State', self.Main)
        self.TextGoal.setGeometry(100, 575, 270, 40)
        self.TextGoal.setFont(self.font)
        self.grid_Goal = QGridLayout()
        self.grid_Goal.setSpacing(10)
        self.gridwidgetGoal.setLayout(self.grid_Goal)
        self.UpdateBoxGoal_(randommodel.getGoal())

    def UpdateBoxGoal_(self, num):
        self.Box_Goal = num.reshape(3, 3)
        for Row in range(len(self.Box_Goal)):
            for Column in range(len(self.Box_Goal - 1)):
                self.grid_Goal.addWidget(Label_Block(
                    self.Box_Goal[Row][Column]), Row, Column)
        self.gridwidgetGoal.setLayout(self.grid_Goal)


class Label_Block(QLabel):
    def __init__(self, box):
        super().__init__()
        self.box = box
        self.setFixedSize(80, 80)
        font = QFont()
        font.setPointSize(30)
        font.setBold(True)
        self.setFont(font)
        pa = QPalette()
        pa.setColor(QPalette.WindowText, Qt.black)
        self.setPalette(pa)
        self.setAlignment(Qt.AlignCenter)
        if self.box == 0:
            self.setStyleSheet("background-color:gray;border-radius:10px;")
        else:
            self.setStyleSheet("background-color:white;border-radius:10px;")
            self.setText(str(self.box))


def firstRun():
    numStart = np.array([2, 8, 3, 1, 6, 4, 7, 0, 5])
    numGoal = np.array([1, 2, 3, 8, 0, 4, 7, 6, 5])
    randommodel.setRandomStart(numStart)
    randommodel.setRadomGoal(numGoal)


radomState_class = random_State.Random_State()
randommodel = randomModel.Random_Model()
al_control = algorithm.Algorithm()

if __name__ == "__main__":
    firstRun()
    app = QApplication(sys.argv)
    ui = UI_main()
    sys.exit(app.exec_())
