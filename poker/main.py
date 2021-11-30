import os

import pygame

import deck
import player
import bots

# TODO: place the cards correctly, and create a function to rotate a card's image

X, Y = 901, 600
bg = pygame.image.load(os.path.join('pics', 'poker_background.jpeg'))
deck = deck.Deck()
deck.shuffle()

# Generate player object and setting it's card hand
player = player.Player()
player.hand = deck.give_cards()

# Generate bot object
# bot1
bot1 = bots.Bot()
bot1.hand = deck.give_cards()

# bot2
bot2 = bots.Bot()
bot2.hand = deck.give_cards()

# bot3
bot3 = bots.Bot()
bot3.hand = deck.give_cards()

window = pygame.display.set_mode((X, Y))
while ...:
    # completely fill the surface object
    window.blit(bg, (0, 0))

    # draw cards on the window
    # player's cards
    window.blit(player.hand[0].image, (0, 0))
    window.blit(player.hand[1].image, (40, 0))

    # bots' cards
    # bot1
    window.blit(bot1.hand[0].image, (80, 0))
    window.blit(bot1.hand[1].image, (120, 0))

    # bot2
    window.blit(bot2.hand[0].image, (160, 0))
    window.blit(bot2.hand[1].image, (200, 0))

    # bot3
    window.blit(bot3.hand[0].image, (240, 0))
    window.blit(bot3.hand[1].image, (280, 0))

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
