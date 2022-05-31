import os
import pygame

from Classes.Game.game import Game
from Classes.Buttons.buttons import Button
from Classes.Colors.colors import Colors


# core pygame configuration
WIDTH, HEIGHT = 901, 600  # window size
window = pygame.display.set_mode([WIDTH, HEIGHT])  # display object
pygame.display.set_caption("Pypoker")   # game caption change
fps = 60    # frames per second
timer = pygame.time.Clock()     # timer object
pygame.init()
FONT_G = pygame.font.Font('freesansbold.ttf', 40)
colors = Colors()   # color handler

# image
background = pygame.image.load(os.path.join('pics', 'poker_background.jpeg'))

# text
title = FONT_G.render('Pypoker', True, colors.white)


# components
# menu screen components
play = Button(window, colors.dark_green1, ((WIDTH//2) - 150), ((HEIGHT//2) - 120), 300, 100, 'Play', 'g')  # play button
# configurations button
config = Button(window, colors.dark_blue1, ((WIDTH//2) - 150), ((HEIGHT//2) + 20), 300, 100, 'Configuration', 'g')  #
# configurations button
terminate = Button(window, colors.dark_red1, ((WIDTH//2) - 150), ((HEIGHT//2) + 160), 300, 100, 'EXIT', 'g')

# game window
game = Game(window)


run = True  # game loop control variable

while run:

    window.blit(background, (0, 0))
    window.blit(title, ((WIDTH//2 - 80), 80))
    play.draw()
    config.draw()
    terminate.draw()

    if game.active:
        game.draw()

    # event loop
    for event in pygame.event.get():
        # close the window and terminate the application if the user clicks on the close button
        if event.type == pygame.QUIT:
            run = False

        # check if the mouse was clicked
        if event.type == pygame.MOUSEBUTTONUP:
            if play.handle_click.collidepoint(event.pos):   # play button clicked
                game.start_game()
            if config.handle_click.collidepoint(event.pos):     # configuration button clicked
                pass
            if terminate.handle_click.collidepoint(event.pos):  # user pressed the exit button
                run = False

    pygame.display.update()
    timer.tick(fps)
