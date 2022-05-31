import os
import pygame

from Classes.Buttons.buttons import Button


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

# image
background = pygame.image.load(os.path.join('pics', 'poker_background.jpeg'))


# components
play = Button(window, (0, 255, 0), 200, 100, 200, 200)

run = True

while run:

    window.blit(background, (0, 0))
    play.draw()

    # event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()
    timer.tick(fps)

