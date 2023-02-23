import sys

import pygame

pygame.init()

screen_width, screen_height = 800, 600
screen_fill_color = (32, 52, 71)
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("Awesome shooter game")

fighter_image = pygame.image.load('images/fighter.png')
fighter_width, fighter_heigth = fighter_image.get_size()
fighter_x, fighter_y = (screen_width / 2) - (fighter_width / 2), screen_height - fighter_heigth
FIGHTER_STEP = 10

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and fighter_x >= FIGHTER_STEP:
                fighter_x -= FIGHTER_STEP

            if event.key == pygame.K_RIGHT and fighter_x <= screen_width - fighter_width - FIGHTER_STEP:
                fighter_x += FIGHTER_STEP

    screen.fill(screen_fill_color)
    screen.blit(fighter_image, (fighter_x, fighter_y))

    pygame.display.update()
