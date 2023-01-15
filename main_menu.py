# здесь подключаются модули
import os

import pygame

import sys

# здесь определяются константы,
# классы и функции
FPS = 60
# была кнопка, но не получилось подключение второго экрана
# здесь происходит инициация,
# создание объектов
# подключение изображения
pygame.init()
pygame.display.set_mode((1300, 600))
clock = pygame.time.Clock()
intro_text = ["«Три в ряд» – классическая игра, которую знают и взрослые, и дети.",
              "Правила игры следующие: пользователь должен собрать комбинацию из",
              "трех или более фишек одного вида на игровом поле путем их перемещения.",
              "В ходе игры на поле добавляются новые фишки, которые также могут",
              "складываться в комбинации при совпадении их вида.", "",
              'Цель игры: набрать как можно большее количество очков за отведенное количество ходов.',
              'Удачи!']
screen = pygame.display.get_surface()
surface = pygame.image.load(os.path.join('images', 'fon1.jpg'))
text_coord = 50
screen.blit(surface, (0, 0))
font = pygame.font.SysFont('Arial', 30)
for line in intro_text:
    string_rendered = font.render(line, 1, pygame.Color('white'))
    intro_rect = string_rendered.get_rect()
    text_coord += 10
    intro_rect.top = text_coord
    intro_rect.x = 10
    text_coord += intro_rect.height
    screen.blit(string_rendered, intro_rect)


# если надо до цикла отобразить
# какие-то объекты, обновляем экран
pygame.display.update()

# главный цикл
while True:

    # задержка
    clock.tick(FPS)

    # цикл обработки событий
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.flip()

    # обновление экрана
    pygame.display.update()
