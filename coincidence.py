# функция для файла game
# проверяем совпадение в столбцах и строках
def coincidence(board):
    # проверяем строки
    for y in range(len(board)):
        streak = 1
        for x in range(1, len(board[y])):
            if board[y][x] == board[y][x - 1] and board[y][x] != 0:
                streak += 1
            else:
                streak = 1
            if streak >= 3:
                return True
    # проверяем столбцы
    for x in range(len(board[0])):
        streak = 1
        for y in range(1, len(board)):
            if board[y][x] == board[y - 1][x] and board[y][x] != 0:
                streak += 1
            else:
                streak = 1
            if streak >= 3:
                return True
    return False
