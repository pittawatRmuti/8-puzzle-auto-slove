import numpy as np
import random
import copy
# ***
Start_1 = np.array([2, 8, 3, 1, 6, 4, 7, 0, 5])
Goal_1 = np.array([1, 2, 3, 8, 0, 4, 7, 6, 5])

Start_2 = np.array([0, 2, 3, 1, 6, 4, 8, 7, 5])
Goal_2 = np.array([1, 2, 3, 8, 0, 4, 7, 6, 5])

Start_3 = np.array([4, 8, 7, 5, 6, 1, 3, 2, 0])
Goal_3 = np.array([0, 8, 7, 4, 5, 6, 3, 2, 1])

Start_4 = np.array([1, 2, 3, 5, 8, 6, 4, 7, 0])
Goal_4 = np.array([1, 2, 3, 4, 5, 6, 0, 8, 7])

Start_5 = np.array([6, 1, 3, 0, 2, 5, 7, 8, 4])
Goal_5 = np.array([1, 2, 3, 6, 5, 4, 7, 8, 0])

Start_6 = np.array([3, 0, 2, 6, 1, 5, 7, 4, 8])
Goal_6 = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8])

Start_7 = np.array([4, 0, 7, 1, 2, 5, 3, 6, 8])
Goal_7 = np.array([1, 4, 7, 2, 5, 8, 3, 6, 0])

Start_8 = np.array([0, 6, 7, 1, 5, 8, 2, 3, 4])
Goal_8 = np.array([1, 6, 7, 2, 5, 8, 3, 4, 0])

Start_9 = np.array([4, 0, 7, 1, 2, 5, 3, 6, 8])
Goal_9 = np.array([1, 4, 7, 2, 5, 8, 3, 6, 0])

Start_10 = np.array([0, 6, 7, 1, 5, 8, 2, 3, 4])
Goal_10 = np.array([1, 6, 7, 2, 5, 8, 3, 4, 0])

# ***


class Random_State():
    def randomNumber(self):
        randomnumber = random.randint(1, 10)
        return randomnumber

    def checkStart(self, random_start):
        if random_start == 1:
            arr_Start = copy.copy(Start_1)
        elif random_start == 2:
            arr_Start = copy.copy(Start_2)
        elif random_start == 3:
            arr_Start = copy.copy(Start_3)
        elif random_start == 4:
            arr_Start = copy.copy(Start_4)
        elif random_start == 5:
            arr_Start = copy.copy(Start_5)
        elif random_start == 6:
            arr_Start = copy.copy(Start_6)
        elif random_start == 7:
            arr_Start = copy.copy(Start_7)
        elif random_start == 8:
            arr_Start = copy.copy(Start_8)
        elif random_start == 9:
            arr_Start = copy.copy(Start_9)
        elif random_start == 10:
            arr_Start = copy.copy(Start_10)
        return arr_Start

    def checkGoal(self, random_goal):
        if random_goal == 1:
            arr_Goal = copy.copy(Goal_1)
        elif random_goal == 2:
            arr_Goal = copy.copy(Goal_2)
        elif random_goal == 3:
            arr_Goal = copy.copy(Goal_3)
        elif random_goal == 4:
            arr_Goal = copy.copy(Goal_4)
        elif random_goal == 5:
            arr_Goal = copy.copy(Goal_5)
        elif random_goal == 6:
            arr_Goal = copy.copy(Goal_6)
        elif random_goal == 7:
            arr_Goal = copy.copy(Goal_7)
        elif random_goal == 8:
            arr_Goal = copy.copy(Goal_8)
        elif random_goal == 9:
            arr_Goal = copy.copy(Goal_9)
        elif random_goal == 10:
            arr_Goal = copy.copy(Goal_10)
        return arr_Goal

    def check_arr_Start(self, arr_Start):
        arr_Start = arr_Start.reshape(3, 3)
        Row = np.array([], dtype="int")
        Col = np.array([], dtype="int")
        Num_check = 0
        while True:
            check_for = False
            for i in range(len(arr_Start)):
                for j in range(len(arr_Start)):
                    if arr_Start[i][j] == Num_check:
                        Row = np.append(Row, i)
                        Col = np.append(Col, j)
                        Num_check = Num_check + 1
                        check_for = True
                        break
                    else:
                        pass
                if check_for == True:
                    break
            if Num_check >= 9:
                break

        return Row, Col

    def check_arr_Goal(self, arr_Goal):
        arr_Goal = arr_Goal.reshape(3, 3)
        Row = np.array([], dtype="int")
        Col = np.array([], dtype="int")
        Num_check = 0
        while True:
            check_for = False
            for i in range(len(arr_Goal)):
                for j in range(len(arr_Goal)):
                    if arr_Goal[i][j] == Num_check:
                        Row = np.append(Row, i)
                        Col = np.append(Col, j)
                        Num_check = Num_check + 1
                        check_for = True
                        break
                    else:
                        pass
                if check_for == True:
                    break
            if Num_check >= 9:
                break
        return Row, Col


# ***************************************************************************************************************************************
