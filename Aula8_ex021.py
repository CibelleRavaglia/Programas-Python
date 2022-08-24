"""
Exercício Python 021:
Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.

"""
#import os; print(os.getcwd())
#os.path.join(os.path.dirname('Aula8_exercicio021.mp3'))
"""
import pygame
pygame.init()
pygame.mixer.music.load('Aula8_exercicio021.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()
"""
"""
import pygame
# Inicializando o mixer PyGame
pygame.mixer.init()
# Iniciando o Pygame
pygame.init()
pygame.mixer.music.load('Aula8_exercicio021.mp3')
pygame.mixer.music.play(loops=0, start=0.0)
input()
pygame.event.wait()
"""
import pygame
pygame.mixer.init()
pygame.init()
pygame.mixer.music.load('C:\Users\cibel\PycharmProjects\guppe\venv\guanabara\Aula8_exercicio021.mp3')
pygame.mixer.music.play(loops=0, start=0.0)
pygame.event.wait()





