import os
import pygame

from Classes.Game.game import Game
from Classes.Buttons.buttons import Button
from Classes.Colors.colors import Colors


# functions:
# function to rotate an image object around it's center
def blit_rotate_center(surf, image, topleft, angle):
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center=image.get_rect(topleft=topleft).center)

    surf.blit(rotated_image, new_rect)


# core pygame configuration
WIDTH, HEIGHT = 901, 600  # window size
window = pygame.display.set_mode([WIDTH, HEIGHT])  # display object
pygame.display.set_caption("Pypoker")   # game caption change
fps = 60    # frames per second
timer = pygame.time.Clock()     # timer object
colors = Colors()   # color handler

# image
background = pygame.image.load(os.path.join('pics', 'poker_background.jpeg'))


# components
# menu screen components
play = Button(window, colors.green, ((WIDTH//2) - 150), ((HEIGHT//2) - 120), 300, 100, 'Play')  # play button
# configurations button
config = Button(window, colors.red, ((WIDTH//2) - 150), ((HEIGHT//2) + 20), 300, 100, 'Configuration')  #

# game window
game = Game(window)


run = True  # game loop control variable

while run:

    window.blit(background, (0, 0))
    play.draw()
    config.draw()

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

    pygame.display.update()
    timer.tick(fps)

