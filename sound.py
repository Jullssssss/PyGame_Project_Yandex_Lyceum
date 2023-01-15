# файл подключения звука
import pygame

sound = {}


def load():
    sound_names = ["win", "lose", "bonus", "pop"]
    for i in range(len(sound_names)):
        path = "sounds/" + sound_names[i] + ".wav"
        sound[sound_names[i]] = pygame.mixer.Sound(path)


def play(name):
    zvuk = sound[name]
    zvuk.play()


def bonus(combo_count):
    if combo_count == 4:
        play("bonus")
    elif combo_count == 3:
        play("bonus")
    elif combo_count == 2:
        play("bonus")
