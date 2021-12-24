import os
import pygame
import deck
import player
import bots


# function to rotate an image object around it's center
def blit_rotate_center(surf, image, topleft, angle):
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center=image.get_rect(topleft=topleft).center)

    surf.blit(rotated_image, new_rect)


# unused functions
# function to flip the bots' cards backwards
# def hide_card(card):
    # card.image = pygame.image.load(os.path.join('pics', 'card-back.png'))


# function to flip the bots' cards to their front side
# def show_card(card, value, suit):
    # card.image = pygame.image.load(os.path.join('pics', f'{suit}', f'{value}'))


X, Y = 901, 600
card1_x, card1_y, card2_x, card2_y = 380, 500, 420, 500
bg = pygame.image.load(os.path.join('pics', 'poker_background.jpeg'))
deck = deck.Deck()
deck.shuffle()

# chip img
chip_img = pygame.image.load(os.path.join('pics', 'bet-img.png'))

# Generate player object and setting its card hand
player = player.Player()
player.hand = deck.give_cards()

# Generate table object
table = bots.Table()
table.cards = deck.give_table_cards()

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

# font
# main font
pygame.init()
font = pygame.font.Font('freesansbold.ttf', 24)
player_text = font.render(player.name, True, (255, 255, 255))   # player name
# bots' names
bot1_text = font.render("bot1", True, (255, 255, 255))
bot2_text = font.render("bot2", True, (255, 255, 255))
bot3_text = font.render("bot3", True, (255, 255, 255))

# button font
button_font = pygame.font.Font("freesansbold.ttf", 16)
BET_TEXT = button_font.render('BET', True, (207, 222, 227))
PASS_TEXT = button_font.render('PASS', True, (207, 222, 227))
FOLD_TEXT = button_font.render('FOLD', True, (207, 222, 227))

# sound FX
pygame.mixer.init()
card_FX = pygame.mixer.Sound(os.path.join('sounds', 'card.mp3'))    # from free sound

window = pygame.display.set_mode((X, Y))
game_round = 0  # variable do control current game round
while ...:  # game loop
    # completely fill the surface object
    window.blit(bg, (0, 0))
    # chips
    player_chips = font.render(f': {player.chips}', True, (255, 255, 255))
    bot1_chips = font.render(f': {bot1.chips}', True, (255, 255, 255))
    bot2_chips = font.render(f': {bot2.chips}', True, (255, 255, 255))
    bot3_chips = font.render(f': {bot3.chips}', True, (255, 255, 255))
    table_pot = font.render(f': {table.pot}', True, (255, 255, 255))

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

    # buttons draw
    pygame.draw.rect(window, (25, 105, 123), [650, 500, 60, 30])    # bet button
    window.blit(BET_TEXT, (660, 507))
    pygame.draw.rect(window, (25, 56, 125), [720, 500, 60, 30])     # pass button
    window.blit(PASS_TEXT, (727, 507))
    pygame.draw.rect(window, (25, 135, 123), [790, 500, 60, 30])    # fold button
    window.blit(FOLD_TEXT, (797, 507))

    # draw cards on the window
    # player's cards
    window.blit(player.hand[0].image, (card1_x, card1_y))
    window.blit(player.hand[1].image, (card2_x, card2_y))

    # bots' cards
    # bot1
    if game_round < 5:
        blit_rotate_center(window, bot1.hand[0].image_back, (0, 240), 90)
        blit_rotate_center(window, bot1.hand[1].image_back, (0, 280), 90)

        # bot2
        window.blit(bot2.hand[0].image_back, (380, 0))
        window.blit(bot2.hand[1].image_back, (420, 0))

        # bot3
        blit_rotate_center(window, bot3.hand[0].image_back, (811, 240), 90)
        blit_rotate_center(window, bot3.hand[1].image_back, (811, 280), 90)

    else:
        blit_rotate_center(window, bot1.hand[0].image, (0, 240), 90)
        blit_rotate_center(window, bot1.hand[1].image, (0, 280), 90)

        # bot2
        window.blit(bot2.hand[0].image, (380, 0))
        window.blit(bot2.hand[1].image, (420, 0))

        # bot3
        blit_rotate_center(window, bot3.hand[0].image, (811, 240), 90)
        blit_rotate_center(window, bot3.hand[1].image, (811, 280), 90)
        # TODO: look who won the round, give the pot to them, pass small/big bet and continue the game

    # table cards
    if game_round == 2:
        coordinates = [(200, 230), (300, 230), (400, 230)]
        for _ in range(3):
            window.blit(table.cards[_].image, coordinates[_])
    elif game_round == 3:
        coordinates = [(200, 230), (300, 230), (400, 230), (500, 230)]
        for _ in range(4):
            window.blit(table.cards[_].image, coordinates[_])
    elif game_round >= 4:
        coordinates = [(200, 230), (300, 230), (400, 230), (500, 230), (600, 230)]
        for _ in range(5):
            window.blit(table.cards[_].image, coordinates[_])

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
            # animation when a player's card is clicked
            # if the click is on player's card 1
            if 420 > pygame.mouse.get_pos()[0] > 380 and 600 > pygame.mouse.get_pos()[1] > 500:
                card1_x, card1_y = 370, 490
                card2_x, card2_y = 420, 500
                card_FX.play()

            # if the click is on player's card 2
            elif 515 > pygame.mouse.get_pos()[0] > 420 and 600 > pygame.mouse.get_pos()[1] > 500:
                card2_x, card2_y = 430, 490
                card1_x, card1_y = 380, 500
                card_FX.play()

            # if the click is outside a card
            else:
                # make the card sound effect if one of player's card is out of place
                if card1_x == 370 or card2_x == 430:
                    card_FX.play()
                card2_x, card2_y = 420, 500
                card1_x, card1_y = 380, 500

            # click at a button:
            # (650, 500) -> button 1 (bet)
            # (720, 500) -> button 2 (pass)
            # (790, 500) -> button 3 (fold)
            # (60, 30) -> buttons dimensions
            # bet button clicked
            if 710 > pygame.mouse.get_pos()[0] > 650 and 530 > pygame.mouse.get_pos()[1] > 500:
                # bet function
                if game_round < 5:
                    if player.action:
                        if player.chips >= 1:
                            if game_round == 0:
                                player.bet(20)
                                table.get_chips(20)
                            else:
                                # TODO: give the player a choice to select the amount of chips they will bet or to
                                #  fold/pass
                                player.bet(40)
                                table.get_chips(40)
                            player.action = False
                            bot1.action = True
                            # TODO: make bots see the chance they have to win and make a action accordingly
                            bot1.do()
                            table.get_chips(40)

                            if bot1.next:
                                bot2.action = True
                                bot2.do()
                                table.get_chips(40)

                                bot3.action = True
                                bot3.do()
                                table.get_chips(40)
                                player.action = True
                                game_round += 1
            # pass button clicked
            elif 780 > pygame.mouse.get_pos()[0] > 720 and 530 > pygame.mouse.get_pos()[1] > 500:
                # pass function
                pass
            # fold button clicked
            elif 850 > pygame.mouse.get_pos()[0] > 790 and 530 > pygame.mouse.get_pos()[1] > 500:
                # fold function
                player.fold()

        # Draws the surface object to the screen.
        pygame.display.update()
