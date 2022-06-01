import pygame

pygame.init()
FONT_G = pygame.font.Font('freesansbold.ttf', 40)
FONT_M = pygame.font.Font('freesansbold.ttf', 24)
FONT_P = pygame.font.Font('freesansbold.ttf', 16)


def blit_rotate_center(surf, image, topleft, angle):
    """
    Rotate a pygame object
    :param surf: game surface
    :param image: image to be rotated
    :param topleft: topleft position of this image inside the surface
    :param angle: angle to rotate the image
    :return:
    None
    """
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center=image.get_rect(topleft=topleft).center)
    surf.blit(rotated_image, new_rect)
