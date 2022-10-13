
ownBoard_ = [0, 0, 5, 0, 3, 3, 0, 0, 0]
otherBoard_ = [4, 0, 0, 2, 0, 0, 1, 0, 0]

'''
首先，能进入这个函数，说明游戏还在进行，即双方都至少还有一个空位（否则游戏结束，直接计分）

'''


def nextStep(ownBoard, otherBoard, figure):
    x = -1

    k_count, e_count, x_count = count_kex(figure, otherBoard)

    # 优先考虑消掉对方的点数
    # 只要对方的棋盘有一行存在与figure相同的点数( 即max(count) > 0 )
    # 则开始判断
    max1 = max(k_count, e_count, x_count)
    if max1 > 0:  # 取 max1 = 1 2 3 共三种情况
        if (k_count == max1) & (ownBoard_exists_empty(ownBoard, 0, 3)) & (x == -1):
            for i in range(0, 3):
                if ownBoard[i] == 0:
                    x = i
                    break
        if (e_count == max1) & (ownBoard_exists_empty(ownBoard, 3, 6)) & (x == -1):
            for i in range(3, 6):
                if ownBoard[i] == 0:
                    x = i
                    break
        if (x_count == max1) & (ownBoard_exists_empty(ownBoard, 6, 9)) & (x == -1):
            for i in range(6, 9):
                if ownBoard[i] == 0:
                    x = i
                    break
    # 可能存在  对方取max时  我方对应的列满了  的情况
    # 因此要判断第二大的
    if x == -1:
        max2 = second_max(k_count, e_count, x_count)
        if max2 > 0:  # 取 max2 = 1 2 共两种情况
            if (k_count == max2) & (ownBoard_exists_empty(ownBoard, 0, 3)) & (x == -1):
                for i in range(0, 3):
                    if ownBoard[i] == 0:
                        x = i
                        break
            if (e_count == max2) & (ownBoard_exists_empty(ownBoard, 3, 6)) & (x == -1):
                for i in range(3, 6):
                    if ownBoard[i] == 0:
                        x = i
                        break
            if (x_count == max2) & (ownBoard_exists_empty(ownBoard, 6, 9)) & (x == -1):
                for i in range(6, 9):
                    if ownBoard[i] == 0:
                        x = i
                        break
    if x == -1:
        max3 = min(k_count, e_count, x_count)
        if max3 > 0:  # 取 max3 = 1 共一种情况
            if (x_count == max3) & (ownBoard_exists_empty(ownBoard, 0, 3)) & (x == -1):
                for i in range(0, 3):
                    if ownBoard[i] == 0:
                        x = i
                        break
            if (x_count == max3) & (ownBoard_exists_empty(ownBoard, 3, 6)) & (x == -1):
                for i in range(3, 6):
                    if ownBoard[i] == 0:
                        x = i
                        break
            if (x_count == max3) & (ownBoard_exists_empty(ownBoard, 6, 9)) & (x == -1):
                for i in range(6, 9):
                    if ownBoard[i] == 0:
                        x = i
                        break

    '''
    如果还是没有放进去
    说明对方棋盘没有figure这个元素
    或者是我方 对应对方max的行 都满了

    接下来考虑己方棋盘的排布
    '''
    k_count, e_count, x_count = count_kex(figure, ownBoard)
    print(k_count, e_count, x_count)
    max1 = max(k_count, e_count, x_count)
    if (max1 > 0) & (max1 < 3):  # 取 max1 = 1 2 共2种情况
        if (k_count == max1) & (x == -1):
            for i in range(0, 3):
                if ownBoard[i] == 0:
                    x = i
                    break
        if (e_count == max1) & (x == -1):
            for i in range(3, 6):
                if ownBoard[i] == 0:
                    x = i
                    break
        if (x_count == max1) & (x == -1):
            for i in range(6, 9):
                if ownBoard[i] == 0:
                    x = i
                    break

    if x == -1:
        max2 = second_max(k_count, e_count, x_count)
        if max2 == 1:  # 取 max2 =  1
            if (k_count == max2) & (x == -1):
                for i in range(0, 3):
                    if ownBoard[i] == 0:
                        x = i
                        break
            if (e_count == max2) & (x == -1):
                for i in range(3, 6):
                    if ownBoard[i] == 0:
                        x = i
                        break
            if (x_count == max2) & (x == -1):
                for i in range(6, 9):
                    if ownBoard[i] == 0:
                        x = i
                        break
    '''
    如果 max1 == 3
    那么说明 已经满了  无法再放进去了
    如果 max1 或 max2 == 0 
    那么说明 期望放的行是空的   那么就可以随便放了

    两者都要考虑   期望放的行是否已经满了
    '''
    return x


def ownBoard_exists_empty(Board, x, y):
    for i in range(x, y):
        if Board[i] == 0:
            return True
        return False


def count_kex(figure, Board):
    k_count = 0
    e_count = 0
    x_count = 0
    for i in range(0, 3):
        if Board[i] == figure:
            k_count += 1
    for i in range(3, 6):
        if Board[i] == figure:
            e_count += 1
    for i in range(6, 9):
        if Board[i] == figure:
            x_count += 1
    return k_count, e_count, x_count


def second_max(a, b, c):
    max1 = max(a, b, c)
    if a == max1 & b == max1 & c == max1:
        return -1  # 即没有第二大的值

    if a == max1:
        if b == max1:
            return c
        elif c == max1:
            return b
        elif b < c:
            return c
        else:
            return b
    elif b == max1:
        if a == max1:
            return c
        elif c == max1:
            return a
        elif a < c:
            return c
        else:
            return a
    else:
        if a == max1:
            return b
        elif a == max1:
            return b
        elif a < b:
            return b
        else:
            return a


for i in range(4):
    for j in range(4):
        for k in range(4):
            print(i, j, k, max(i, j, k), min(i, j, k), second_max(i, j, k))

print(nextStep(ownBoard_, otherBoard_, 3))


def main():
    nextStep(ownBoard_, otherBoard_, 3)
