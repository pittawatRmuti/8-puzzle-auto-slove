
class Algorithm():

    def firstround(self, arr_Start, arr_Goal):
        arr_Start = arr_Start.reshape(3, 3)
        arr_Goal = arr_Goal.reshape(3, 3)
        Row = 0
        Col = 0
        h = 0
        for i in range(len(arr_Start)):
            for j in range(len(arr_Start)):
                if arr_Start[i][j] == arr_Goal[i][j]:
                    pass
                else:
                    if arr_Start[i][j] != 0:
                        h = h + 1
                    else:
                        pass
                if arr_Start[i][j] == 0:
                    Row = i
                    Col = j
        return h, Row, Col

    def algorithm(self, Row, Col, arr_Start, arr_Goal, H, lastmove):
        arr_Start = arr_Start.reshape(3, 3)
        arr_Goal = arr_Goal.reshape(3, 3)
        _move = lastmove
        Move = ""
        move = ["up", "down", "left", "right"]
        Row = Row
        Col = Col
        h = H
        TextMove = ''
        for move_ in range(len(move)):
            Start = arr_Start.copy()
            Move = move[move_]
            if Move == 'up':
                if Row == 0:
                    continue
                Start[Row][Col] = Start[Row-1][Col]
                Start[Row-1][Col] = 0
            elif Move == 'down':
                if Row == 2:
                    continue
                Start[Row][Col] = Start[Row + 1][Col]
                Start[Row+1][Col] = 0
            elif Move == 'left':
                if Col == 0:
                    continue
                Start[Row][Col] = Start[Row][Col-1]
                Start[Row][Col-1] = 0
            elif Move == 'right':
                if Col == 2:
                    continue
                Start[Row][Col] = Start[Row][Col+1]
                Start[Row][Col+1] = 0

            h2 = 0
            for i in range(len(Start)):
                for j in range(len(Start)):
                    if Start[i][j] == arr_Goal[i][j]:
                        pass
                    else:
                        if Start[i][j] != 0:
                            h2 = h2 + 1
                        else:
                            pass
                    if Start[i][j] == 0:
                        row = i
                        col = j

            if h2 < h:
                h = h2
                Row = row
                Col = col
                TextMove = Move
                if move[move_] == 'up':
                    _move = 'down'
                elif move[move_] == 'down':
                    _move = 'up'
                elif move[move_] == 'left':
                    _move = 'right'
                elif move[move_] == 'right':
                    _move = 'left'
                arr_Start = Start.copy()
                break
            elif h2 == h and move[move_] != _move:
                arr_Start = Start.copy()
                Row = row
                Col = col
                TextMove = Move
                if move[move_] == 'up':
                    _move = 'down'
                elif move[move_] == 'down':
                    _move = 'up'
                elif move[move_] == 'left':
                    _move = 'right'
                elif move[move_] == 'right':
                    _move = 'left'
                break
            else:
                pass

        return h, arr_Start, _move, Row, Col, TextMove
