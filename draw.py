import pygame

images = {}


def images_loading():
    image_names = ["img1", "img2", "img3", "img8", "img5", "img6", "img7"]
    for i in range(len(image_names)):
        file_path = "images/" + image_names[i] + ".jpg"
        images[image_names[i]] = pygame.image.load(file_path)


def screen(grid_width, grid_height, box_length):
    global BOX_LENGTH, screen
    BOX_LENGTH = box_length

    images_loading()
    window_icon = images["img7"]
    pygame.display.set_icon(window_icon)
    pygame.display.set_caption("Три в ряд")

    screen = pygame.display.set_mode((BOX_LENGTH * (grid_width + 2),
                                      BOX_LENGTH * grid_height))
    return screen


def to_pix(x):
    return x * BOX_LENGTH


def window(board, turns_left, score, goal_score):
    screen.fill((255, 255, 255))
    drawing(turns_left, score, goal_score)
    desk_drawing(board)


def drawing(turns_left, score, goal_score):
    font = pygame.font.SysFont("Times New Roman", 35)

    text = font.render("GOAL:", True, (255, 192, 203))
    screen.blit(text, (to_pix(7.25), to_pix(0)))
    pygame.draw.line(screen, (255, 192, 203), (to_pix(7), to_pix(0.6)),
                     (to_pix(8.75), to_pix(0.6)), 1)
    text = font.render(str(goal_score), True, (255, 192, 203))
    screen.blit(text, (to_pix(7.4), to_pix(0.6)))

    text = font.render("TURNS", True, (255, 192, 203))
    screen.blit(text, (to_pix(7.2), to_pix(1.5)))
    text = font.render("LEFT:", True, (255, 192, 203))
    screen.blit(text, (to_pix(7.3), to_pix(2)))
    pygame.draw.line(screen, (255, 192, 203), (to_pix(7), to_pix(2.6)),
                     (to_pix(8.75), to_pix(2.6)), 1)
    text = font.render(str(turns_left), True, (255, 192, 203))
    screen.blit(text, (to_pix(7.5), to_pix(2.6)))

    text = font.render("SCORE:", True, (255, 192, 203))
    screen.blit(text, (to_pix(7), to_pix(3.5)))
    pygame.draw.line(screen, (255, 192, 203), (to_pix(7), to_pix(4.1)),
                     (to_pix(8.9), to_pix(4.1)), 1)

    offset = 0
    if score >= 100:
        offset = -0.3
    elif score >= 10:
        offset = -0.15
    text = font.render(str(score), True, (255, 192, 203))
    screen.blit(text, (to_pix(7.75 + offset), to_pix(4.1)))


def desk_drawing(board):
    for y in range(len(board)):
        for x in range(len(board[y])):
            image_drawing(board[y][x], x, y)


# загрузка и изображение всех ассетов
def image_drawing(num, x, y):
    icon = None
    x = to_pix(x) + 3
    y = to_pix(y) + 3

    if num == 1:
        icon = images["img1"]
    elif num == 2:
        icon = images["img2"]
    elif num == 3:
        icon = images["img3"]
    elif num == 4:
        icon = images["img8"]
    elif num == 5:
        icon = images["img5"]
    elif num == 6:
        icon = images["img6"]
    if num != 0:
        screen.blit(icon, (x, y))


def selected(x, y):
    x = to_pix(x)
    y = to_pix(y)
    rect = pygame.Rect(x, y, BOX_LENGTH, BOX_LENGTH)
    pygame.draw.rect(screen, (255, 192, 203), rect, 3)


def winner():
    msg("Win!")


def loser():
    msg("Lose!")


# вывод результата игры на центр экрана
def msg(msg):
    color = (255, 192, 203)
    if msg == "You Win!":
        color = (255, 192, 203)
    elif msg == "You Lose":
        color = (255, 192, 203)

    rect = pygame.Rect(to_pix(2), to_pix(3),
                       to_pix(3), to_pix(2))
    pygame.draw.rect(screen, (255, 255, 255), rect, 0)
    pygame.draw.rect(screen, color, rect, 4)
    font = pygame.font.SysFont("Times New Roman", 70)
    text = font.render("You", True, color)
    screen.blit(text, (to_pix(2.4), to_pix(3)))
    text = font.render(msg, True, color)
    screen.blit(text, (to_pix(2.4), to_pix(4)))


def combinations(combo_count):
    msg = ""
    color = (0, 0, 0)
    x = 0.1

    if combo_count == 4:
        color = (255, 192, 203)
        msg = "COOL"
        x = 2.25
    elif combo_count == 3:
        color = (255, 192, 203)
        msg = "TRIPLE"
        x = 1.65
    elif combo_count == 2:
        color = (255, 192, 203)
        msg = "DOUBLE"
        x = 1.2

    rect = pygame.Rect(0, to_pix(4), to_pix(7), to_pix(1))
    pygame.draw.rect(screen, (255, 255, 255), rect, 0)
    pygame.draw.rect(screen, color, rect, 4)

    font = pygame.font.SysFont("Times New Roman", 79)
    text = font.render(msg, True, color)
    screen.blit(text, (to_pix(x), to_pix(3.9)))
