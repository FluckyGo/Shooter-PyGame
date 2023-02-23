import sys
import pygame

pygame.init()

screen_width, screen_height = 800, 600

screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("Awesome shooter game")

fighter_image = pygame.image.load('images/fighter.png')
fighter_width, fighter_heigth = fighter_image.get_size()

fighter_x, fighter_y = (screen_width / 2) - (fighter_width / 2), screen_height - fighter_heigth

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()