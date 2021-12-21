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
card1_x, card1_y, card2_x, card2_y = 380, 500, 420, 500
bg = pygame.image.load(os.path.join('pics', 'poker_background.jpeg'))
deck = deck.Deck()
deck.shuffle()

# chip img
chip_img = pygame.image.load(os.path.join('pics', 'bet-img.png'))

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

# font
pygame.init()
font = pygame.font.Font('freesansbold.ttf', 24)
player_text = font.render(player.name, True, (255, 255, 255))
# TODO: give the bots random actual names somehow
bot1_text = font.render("bot1", True, (255, 255, 255))
bot2_text = font.render("bot2", True, (255, 255, 255))
bot3_text = font.render("bot3", True, (255, 255, 255))
# chips
player_chips = font.render(f': {player.chips}', True, (255, 255, 255))
bot1_chips = font.render(f': {bot1.chips}', True, (255, 255, 255))
bot2_chips = font.render(f': {bot2.chips}', True, (255, 255, 255))
bot3_chips = font.render(f': {bot3.chips}', True, (255, 255, 255))
table_pot = font.render(f': {table.pot}', True, (255, 255, 255))


# sound FX
pygame.mixer.init()
card_FX = pygame.mixer.Sound(os.path.join('sounds', 'card.mp3'))    # from freesound

window = pygame.display.set_mode((X, Y))
while ...:
    # completely fill the surface object
    window.blit(bg, (0, 0))

    # text drawing
    # names
    window.blit(player_text, (510, 510))
    window.blit(bot1_text, (10, 170))
    window.blit(bot2_text, (500, 20))
    window.blit(bot3_text, (811, 170))
    # chips values
    window.blit(player_chips, (550, 550))
    window.blit(bot1_chips, (40, 220))
    window.blit(bot2_chips, (540, 60))
    window.blit(bot3_chips, (820, 220))
    # table pot
    window.blit(table_pot, (440, 350))
    # pot chips img
    window.blit(chip_img, (405, 350))
    # chip img draw
    window.blit(chip_img, (515, 550))
    window.blit(chip_img, (5, 220))
    window.blit(chip_img, (505, 60))
    window.blit(chip_img, (785, 220))

    # table cards
    coor = [(200, 230), (300, 230), (400, 230), (500, 230), (600, 230)]
    for _ in range(5):
        window.blit(table.cards[_].image, coor[_])

    # draw cards on the window
    # player's cards
    window.blit(player.hand[0].image, (card1_x, card1_y))
    window.blit(player.hand[1].image, (card2_x, card2_y))

    # bots' cards
    # bot1
    blit_rotate_center(window, bot1.hand[0].image, (0, 240), 90)
    blit_rotate_center(window, bot1.hand[1].image, (0, 280), 90)

    # bot2
    window.blit(bot2.hand[0].image, (380, 0))
    window.blit(bot2.hand[1].image, (420, 0))

    # bot3
    blit_rotate_center(window, bot3.hand[0].image, (811, 240), 90)
    blit_rotate_center(window, bot3.hand[1].image, (811, 280), 90)

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

        # mouse events

        if event.type == pygame.MOUSEBUTTONDOWN:
            # (380, 500) (420, 500)
            # click on player's card 1
            if 420 > pygame.mouse.get_pos()[0] > 380 and 600 > pygame.mouse.get_pos()[1] > 500:
                card1_x, card1_y = 370, 490
                card2_x, card2_y = 420, 500
                card_FX.play()

            # click on player's card 2
            elif 515 > pygame.mouse.get_pos()[0] > 420 and 600 > pygame.mouse.get_pos()[1] > 500:
                card2_x, card2_y = 430, 490
                card1_x, card1_y = 380, 500
                card_FX.play()

            # click outside a card
            else:
                # make the card sound effect if one of player's card is out of place
                if card1_x == 370 or card2_x == 430:
                    card_FX.play()
                card2_x, card2_y = 420, 500
                card1_x, card1_y = 380, 500

        # Draws the surface object to the screen.
        pygame.display.update()
