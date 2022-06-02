import os
import pygame

from poker.functions import COLOR
from Classes.Game.game import Game
from Classes.Buttons.buttons import Button
from Classes.Configurations.configurations import Configurations


# core pygame configuration
WIDTH, HEIGHT = 901, 600  # window size
window = pygame.display.set_mode([WIDTH, HEIGHT])  # display object
pygame.display.set_caption("Pypoker")   # game caption change
# set window icon
icon = pygame.image.load(os.path.join('pics', 'poker_icon.png'))
pygame.display.set_icon(icon)
fps = 60    # frames per second
timer = pygame.time.Clock()     # timer object
pygame.init()
FONT_G = pygame.font.Font('freesansbold.ttf', 40)

# image
background = pygame.image.load(os.path.join('pics', 'poker_background.jpeg'))

# text
title = FONT_G.render('Pypoker', True, COLOR.white)


# components
# menu screen components
play = Button(window, COLOR.dark_green1, ((WIDTH//2) - 150), ((HEIGHT//2) - 120), 300, 100, 'Play', 'g')  # play button
# configurations button
config = Button(window, COLOR.dark_blue1, ((WIDTH//2) - 150), ((HEIGHT//2) + 20), 300, 100, 'Configuration', 'g')  #
# configurations button
terminate = Button(window, COLOR.dark_red1, ((WIDTH//2) - 150), ((HEIGHT//2) + 160), 300, 100, 'EXIT', 'g')

# game window
game = Game(window)
# config windows
configs = Configurations(window)


run = True  # game loop control variable
is_menu_active = True

while run:
    window.blit(background, (0, 0))
    window.blit(title, ((WIDTH//2 - 80), 80))
    play.draw()
    config.draw()
    terminate.draw()

    # check if whether the game or the configs object is active, to blit them and toggle the is_menu_active variable
    # to deactivate the menu buttons
    if game.active:
        game.draw()
        is_menu_active = False
    elif configs.active:
        configs.draw()
        is_menu_active = False

    # event loop
    for event in pygame.event.get():
        # close the window and terminate the application if the user clicks on the close button
        if event.type == pygame.QUIT:
            run = False

        # check if the mouse was clicked
        if event.type == pygame.MOUSEBUTTONUP:
            # Config screen buttons event catch
            if configs.active:
                if configs.back_button.handle_click.collidepoint(event.pos):
                    configs.toggle_config()
                    is_menu_active = True

            # Buttons of menu screen event catch
            if is_menu_active:
                if play.handle_click.collidepoint(event.pos):   # play button clicked
                    game.start_game()
                if config.handle_click.collidepoint(event.pos):     # configuration button clicked
                    configs.toggle_config()
                    is_menu_active = False
                if terminate.handle_click.collidepoint(event.pos):  # user pressed the exit button
                    run = False

    pygame.display.update()
    timer.tick(fps)
