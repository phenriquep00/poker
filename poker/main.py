import os
import pygame
import deck
import player
import bots


# function to rotate a image object around it's center
def blit_rotate_center(surf, image, topleft, angle):
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center=image.get_rect(topleft=topleft).center)

    surf.blit(rotated_image, new_rect)


# function to flip the bots' cards backwards
def hide_card(card):
    card.image = pygame.image.load(os.path.join('pics', 'card-back.png'))


# function to flip the bots' cards to their front side
def show_card(card, value, suit):
    card.image = pygame.image.load(os.path.join('pics', f'{suit}', f'{value}'))


X, Y = 901, 600
bg = pygame.image.load(os.path.join('pics', 'poker_background.jpeg'))
deck = deck.Deck()
deck.shuffle()

# Generate player object and setting it's card hand
player = player.Player()
player.hand = deck.give_cards()

# Generate table object
table = bots.Table()
table.cards = deck.give_table_cards()

# Generate bot object
# bot1
bot1 = bots.Bot()
bot1.hand = deck.give_cards()
hide_card(bot1.hand[0])
hide_card(bot1.hand[1])
# show_card(card=bot1.hand[0], suit=f'{bot1.hand[0].suit}', value=f'{bot1.hand[0].value}.png')
# show_card(card=bot1.hand[1], suit=f'{bot1.hand[1].suit}', value=f'{bot1.hand[1].value}.png')

# bot2
bot2 = bots.Bot()
bot2.hand = deck.give_cards()
hide_card(bot2.hand[0])
hide_card(bot2.hand[1])

# bot3
bot3 = bots.Bot()
bot3.hand = deck.give_cards()
hide_card(bot3.hand[0])
hide_card(bot3.hand[1])

window = pygame.display.set_mode((X, Y))
while ...:
    # completely fill the surface object
    window.blit(bg, (0, 0))

    # draw cards on the window
    # player's cards
    window.blit(player.hand[0].image, (380, 500))
    window.blit(player.hand[1].image, (420, 500))

    # table cards
    coor = [(200, 230), (300, 230), (400, 230), (500, 230), (600, 230)]
    for _ in range(5):
        window.blit(table.cards[_].image, coor[_])

    # bots' cards
    # bot1
    blit_rotate_center(window, bot1.hand[0].image, (0, 240), 90)
    blit_rotate_center(window, bot1.hand[1].image, (0, 280), 90)

    # bot2
    window.blit(bot2.hand[0].image, (380, 0))
    window.blit(bot2.hand[1].image, (420, 0))

    # bot3
    blit_rotate_center(window, bot3.hand[0].image, (901-90, 240), 90)
    blit_rotate_center(window, bot3.hand[1].image, (901-90, 280), 90)

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
