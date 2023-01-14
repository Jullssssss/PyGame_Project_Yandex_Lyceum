import pygame
import draw
import random
import math
import sound
import os


# создание массива и его заполнение
def array(width, height):
    return [[random.randrange(1, 7) for x in range(width)] for y in range(height)]


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


# настройка игрового поля так, чтобы в начале игры на игровом поле не было совпадений
def nastroy(board):
    while coincidence(board):
        for y in range(len(board)):
            for x in range(len(board[y])):
                board[y][x] = random.randrange(1, 7)
    return board


# отображение текстового представления массива
def pokaz(grid):
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            print(grid[y][x], end=" ")
        print()


# обновление и приостановка элементов экрана
def stop_disp(clock, x):
    pygame.display.flip()
    clock.tick(x)


# проверяем, что ячейка, которую двигает игрок, находится рядом с первой
def standing_nearby(selected_x, selected_y, x, y):
    if selected_x + 1 == x and selected_y == y:
        return True
    elif selected_x - 1 == x and selected_y == y:
        return True
    elif selected_y + 1 == y and selected_x == x:
        return True
    elif selected_y - 1 == y and selected_x == x:
        return True
    return False


def moving(array, x1, y1, x2, y2):
    temp = array[y1][x1]
    array[y1][x1] = array[y2][x2]
    array[y2][x2] = temp


def matches(board):
    list = []
    # проверяем совпадения в строках
    for y in range(len(board)):
        streak = 1
        for x in range(1, len(board[y])):
            if board[y][x] == board[y][x - 1] and board[y][x] != 0:
                streak += 1
            else:
                streak = 1
            if streak == 3:
                list += [[y, x - 2]]
                list += [[y, x - 1]]
                list += [[y, x]]
            elif streak > 3:
                list += [[y, x]]
    # проверяем совпадения в столбцах
    for x in range(len(board[0])):
        streak = 1
        for y in range(1, len(board)):
            if board[y][x] == board[y - 1][x] and board[y][x] != 0:
                streak += 1
            else:
                streak = 1
            if streak == 3:
                list += [[y - 2, x]]
                list += [[y - 1, x]]
                list += [[y, x]]
            elif streak > 3:
                list += [[y, x]]

    # сводим все совпадения к нулю
    for i in range(len(list)):
        y = list[i][0]
        x = list[i][1]
        board[y][x] = 0

    return len(list)


# используем функцию если на поле есть пустые клетки
def desk_filling(board):
    for y in range(len(board)):
        if 0 in board[y]:  # 0 является пустой ячейкой
            return False
    return True


# спускаем пустые ячейки на одну клетку вниз
# проходимся по массиву от нижнего левого угла вверх по каждому столбцу
def spusk_kletok(board):
    for x in range(len(board[0])):
        for y in range(len(board) - 2, -1, -1):
            if board[y + 1][x] == 0 and board[y][x] != 0:
                moving(board, x, y + 1, x, y)


# заполняемм все пустые ячейки в верхней части поля
def zapoln_verh(board):
    for x in range(len(board[0])):
        if board[0][x] == 0:
            board[0][x] = random.randrange(1, 7)


# функция, запускающая игровой процесс
def play():
    WIDTH = 7
    HEIGHT = 9
    BOX_LENGTH = 70
    selected = False
    selected_x = None
    selected_y = None
    score = 0
    turns_left = 20
    GOAL_SCORE = 300
    exit_game = False
    gameover_displayed = False
    os.environ['SDL_VIDEO_CENTERED'] = '1'

    board = array(WIDTH, HEIGHT)
    nastroy(board)

    pygame.init()
    sound.load()
    screen = draw.screen(WIDTH, HEIGHT, BOX_LENGTH)
    clock = pygame.time.Clock()
    draw.window(board, turns_left, score, GOAL_SCORE)
    pygame.display.flip()

    # начинаем игровой цикл
    while not exit_game:
        while turns_left > 0 and not exit_game:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    coord_pair = pygame.mouse.get_pos()  # tuple from the left-click
                    x = math.floor(coord_pair[0] / BOX_LENGTH)
                    y = math.floor(coord_pair[1] / BOX_LENGTH)
                    if x < WIDTH and y < HEIGHT:
                        if selected == False:
                            selected = True
                            selected_x = x
                            selected_y = y
                            draw.selected(x, y)
                        elif selected == True:
                            if standing_nearby(selected_x, selected_y, x, y):
                                moving(board, selected_x, selected_y, x, y)
                                draw.window(board, turns_left, score, GOAL_SCORE)
                                stop_disp(clock, 2.5)

                                if coincidence(board):
                                    turns_left -= 1
                                    turn_score = 0
                                    combo_count = 1

                                    # пока не останется совпадающих ячеек
                                    while coincidence(board):
                                        turn_score += matches(board)
                                        draw.window(board, turns_left, score,
                                                    GOAL_SCORE)
                                        sound.play("pop")
                                        stop_disp(clock, 2.5)

                                        while not desk_filling(board):
                                            # заполнение доски пока не останется пустых ячеек
                                            spusk_kletok(board)
                                            zapoln_verh(board)
                                            draw.window(board, turns_left, score,
                                                        GOAL_SCORE)
                                            stop_disp(clock, 2.5)

                                        combo_count += 1

                                    combo_count -= 1
                                    score += turn_score * combo_count
                                    draw.window(board, turns_left, score,
                                                GOAL_SCORE)
                                    pygame.display.flip()

                                    if combo_count > 1:
                                        sound.bonus(combo_count)
                                        draw.combinations(combo_count)
                                        pygame.display.flip()
                                        pygame.time.delay(2000)
                                        draw.window(board, turns_left, score,
                                                    GOAL_SCORE)
                                        pygame.display.flip()


                                elif not coincidence(board):
                                    # возращает ячейки на места при их несовпадении
                                    moving(board, selected_x, selected_y, x, y)
                                    draw.window(board, turns_left, score,
                                                GOAL_SCORE)
                                    pygame.display.flip()

                            elif not standing_nearby(selected_x, selected_y, x, y):
                                draw.window(board, turns_left, score, GOAL_SCORE)
                                pygame.display.flip()

                            selected = False
                            selected_x = None
                            selected_y = None

            stop_disp(clock, 60)

        if not gameover_displayed:
            if score >= GOAL_SCORE:
                draw.winner()
                sound.play("win")
            else:
                draw.loser()
                sound.play("lose")
            gameover_displayed = True
            pygame.display.flip()

        # выход из игрового цикла
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True


if __name__ == "__main__": play()
