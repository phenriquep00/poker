import os
import pygame


# functions:
# function to rotate an image object around it's center
def blit_rotate_center(surf, image, topleft, angle):
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center=image.get_rect(topleft=topleft).center)

    surf.blit(rotated_image, new_rect)


# core pygame configuration
WIDTH, HEIGHT = 901, 600  # window size
window = pygame.display.set_mode(WIDTH, HEIGHT)  # display object
pygame.display.set_caption("Pypoker")   # game caption change
fps = 60    # frames per second
timer = pygame.time.Clock()     # timer object


run = True

while run:
    timer.tick(fps)
