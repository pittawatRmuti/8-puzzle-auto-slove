
class Random_Model():

    def setRandomStart(self, arr_Start):
        self.arr_Start = arr_Start

    def setRadomGoal(self, arr_Goal):
        self.arr_Goal = arr_Goal

    def set_H(self, h):
        self.h = h

    def set_lastMove(self, move):
        self.lastmove = move

    def setPosition(self, Row, Col):
        self.row = Row
        self.col = Col

    def setmoveText(self, move):
        self.textmove = move

    def getStart(self):
        return self.arr_Start

    def getGoal(self):
        return self.arr_Goal

    def get_H(self):
        return self.h

    def get_lastMove(self):
        return self.lastmove

    def getPosition(self):
        return self.row, self.col

    def getTextmove(self):
        return self.textmove
