import pygame
import deck
import os

X = 901
Y = 600
white = (255, 255, 255)
bg = pygame.image.load(os.path.join('pics', 'poker_background.jpeg'))
deck = deck.Deck()
deck.shuffle()

display_surface = pygame.display.set_mode((X, Y))
while ...:
    # completely fill the surface object
    display_surface.blit(bg, (0, 0))

    # copying the image surface object
    # to the display surface object at
    # (0, 0) coordinate.
    display_surface.blit(deck.deck[0].image, (0, 0))

    # iterate over the list of Event objects
    # that was returned by pygame.event.get() method.
    for event in pygame.event.get():

        # if event object type is QUIT
        # then quitting the pygame
        # and program both.
        if event.type == pygame.QUIT:

            # deactivates the pygame library
            pygame.quit()

            # quit the program.
            quit()

        # Draws the surface object to the screen.
        pygame.display.update()
