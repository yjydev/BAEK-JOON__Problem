
def find_empty():
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return i,j
    # 다 돌아도 0이 없으면 모두 채운것이므로 None 리턴
    return None,None


def check(r,c, num):
    for i in range(9):
        if board[i][c] == num:
            return False

    for j in range(9):
        if board[r][j] == num:
            return False

    box_r = r//3*3
    box_c = c//3*3
    for i in range(3):
        for j in range(3):
            if board[box_r+i][box_c+j] == num:
                return False

    return True


def add():
    r,c = find_empty()
    if r is None or c is None:
        return True
    else:
        for i in range(1,10):
            if check(r,c,i):
                board[r][c] = i
                if add():
                    return True
                board[r][c] = 0
        return False



board = [list(map(int,input())) for _ in range(9)]

add()


for i in range(9):
    for j in range(9):
        print(board[i][j], end='')
    print()






