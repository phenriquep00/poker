import os

import pygame

import bots
import deck
import hand_value
import player
import functions


# function to rotate an image object around it's center
def blit_rotate_center(surf, image, topleft, angle):
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center=image.get_rect(topleft=topleft).center)

    surf.blit(rotated_image, new_rect)


def bet_menu(max_chips):
    # TODO: create a menu for the player to chose a specific amount of chips to bet
    pass


clock = pygame.time.Clock()
X, Y = 901, 600
card1_x, card1_y, card2_x, card2_y = 380, 500, 420, 500
bg = pygame.image.load(os.path.join('pics', 'poker_background.jpeg'))
deck = deck.Deck()
deck.shuffle()

# chip img
chip_img = pygame.image.load(os.path.join('pics', 'bet-img.png'))

# Generate player object and setting its card hand
player = player.Player(name='player')
player.hand = deck.give_cards()

# Generate table object
table = bots.Table()
table.cards = deck.give_table_cards()

# Generate bot object
# bot1
bot1 = bots.Bot(name='bot1')
bot1.hand = deck.give_cards()

# bot2
bot2 = bots.Bot(name='bot2')
bot2.hand = deck.give_cards()

# bot3
bot3 = bots.Bot(name='bot3')
bot3.hand = deck.give_cards()

# font
# main font
pygame.init()
font = pygame.font.Font('freesansbold.ttf', 24)
player_text = font.render(player.name, True, (255, 255, 255))  # player name
# bots' names
bot1_text = font.render("bot1", True, (255, 255, 255))
bot2_text = font.render("bot2", True, (255, 255, 255))
bot3_text = font.render("bot3", True, (255, 255, 255))

# button font
button_font = pygame.font.Font("freesansbold.ttf", 16)
BET_TEXT = button_font.render('BET', True, (207, 222, 227))
PASS_TEXT = button_font.render('PASS', True, (207, 222, 227))
FOLD_TEXT = button_font.render('FOLD', True, (207, 222, 227))
OK_TEXT = button_font.render('OK', True, (207, 222, 227))
# sound FX
pygame.mixer.init()
card_FX = pygame.mixer.Sound(os.path.join('sounds', 'card.mp3'))  # from free sound

window = pygame.display.set_mode((X, Y))
game_round = 0  # variable do control current game round

slider = functions.Slider(400, 200, 200, 20, screen=window)

while ...:  # game loop
    # completely fill the surface object
    window.blit(bg, (0, 0))
    # render chips image
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

    # buttons draw on screen
    pygame.draw.rect(window, (25, 105, 123), [650, 500, 60, 30])  # bet button
    window.blit(BET_TEXT, (660, 507))
    pygame.draw.rect(window, (25, 56, 125), [720, 500, 60, 30])  # pass button
    window.blit(PASS_TEXT, (727, 507))
    pygame.draw.rect(window, (25, 135, 123), [790, 500, 60, 30])  # fold button
    window.blit(FOLD_TEXT, (797, 507))
    # ok button
    # pygame.draw.rect(window, (25, 105, 123), [0, 0, 60, 30])  # bet button
    # window.blit(OK_TEXT, (0, 0))

    # draw cards on the window
    # player's cards
    window.blit(player.hand[0].image, (card1_x, card1_y))
    window.blit(player.hand[1].image, (card2_x, card2_y))

    slider.draw(window)

    # bots' cards
    if game_round < 5:
        # bot1
        blit_rotate_center(window, bot1.hand[0].image_back, (0, 240), 90)
        blit_rotate_center(window, bot1.hand[1].image_back, (0, 280), 90)

        # bot2
        window.blit(bot2.hand[0].image_back, (380, 0))
        window.blit(bot2.hand[1].image_back, (420, 0))

        # bot3
        blit_rotate_center(window, bot3.hand[0].image_back, (811, 240), 90)
        blit_rotate_center(window, bot3.hand[1].image_back, (811, 280), 90)

    else:
        # bot1
        blit_rotate_center(window, bot1.hand[0].image, (0, 240), 90)
        blit_rotate_center(window, bot1.hand[1].image, (0, 280), 90)

        # bot2
        window.blit(bot2.hand[0].image, (380, 0))
        window.blit(bot2.hand[1].image, (420, 0))

        # bot3
        blit_rotate_center(window, bot3.hand[0].image, (811, 240), 90)
        blit_rotate_center(window, bot3.hand[1].image, (811, 280), 90)
        # TODO: if there is more than 1 person with two pair or if the game is decided only with high cards,
        #  give priority to the one with the highest pairs get the hands values
        player.value = hand_value.hand_value(player, table)
        bot1.value = hand_value.hand_value(bot1, table)
        bot2.value = hand_value.hand_value(bot2, table)
        bot3.value = hand_value.hand_value(bot3, table)

        rankings = {'royal flush': 1, 'straight flush': 2, 'four of a kind': 3, 'full house': 4, 'flush': 5,
                    'straight': 6, 'three of a kind': 6, 'two pair': 8, 'pair': 9, 'high card 14': 10,
                    'high card 13': 11, 'high card 12': 12, 'high card 11': 13, 'high card 10': 14, 'high card 9': 15,
                    'high card 8': 16, 'high card 7': 17, 'high card 6': 18, 'high card 5': 19, 'high card 4': 20,
                    'high card 3': 21, 'high card 2': 22}

        for _ in [player, bot1, bot2, bot3]:
            for rank, value in rankings.items():
                if _.value == rank:
                    _.rank = value

        winner_value = 23
        for _ in [player.rank, bot1.rank, bot2.rank, bot2.rank]:
            if _ < winner_value:
                winner_value = _

        for _ in [player, bot1, bot2, bot2]:
            if _.rank == winner_value:
                _.win = True
                _.chips += table.pot
                table.pot = 0
                _.win = False
                winner_text = font.render(f'winner: {_.name} with {_.value}', True, (255, 255, 255))
                player_value_text = font.render(f'rank: {player.value}', True, (255, 255, 255))
                bot1_value_text = font.render(f'rank: {bot1.value}', True, (255, 255, 255))
                bot2_value_text = font.render(f'rank: {bot2.value}', True, (255, 255, 255))
                bot3_value_text = font.render(f'rank: {bot3.value}', True, (255, 255, 255))
                window.blit(winner_text, (320, 200))
                window.blit(player_value_text, (130, 500))
                window.blit(bot1_value_text, (0, 370))
                window.blit(bot2_value_text, (100, 0))
                window.blit(bot3_value_text, (650, 370))

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
                card_FX.play()  # play sound when a card is clicked

            # if the click is on player's card 2
            elif 515 > pygame.mouse.get_pos()[0] > 420 and 600 > pygame.mouse.get_pos()[1] > 500:
                card2_x, card2_y = 430, 490
                card1_x, card1_y = 380, 500
                card_FX.play()  # play sound when a card is clicked

            # if the click is outside a card
            else:
                # make the card sound effect if one of player's card is out of place
                if card1_x == 370 or card2_x == 430:
                    card_FX.play()  # play sound when a card is clicked
                card2_x, card2_y = 420, 500
                card1_x, card1_y = 380, 500

            # click at a button:
            # (650, 500) -> button 1 (bet)
            # (720, 500) -> button 2 (pass)
            # (790, 500) -> button 3 (fold)
            # (60, 30) -> buttons dimensions
            # bet button clicked
            if 710 > pygame.mouse.get_pos()[0] > 650 and 530 > pygame.mouse.get_pos()[1] > 500:
                while game_round < 5:

                    if game_round == 0:  # player starts the game by betting the small amount = 20

                        player.bet(20)
                        # bot1 action
                        bot1.do()
                        # bot2 action
                        bot2.do()
                        # bot3 action
                        bot3.do()
                        # pass the game to the next round
                        game_round += 1
                        break

                    elif game_round == 1:  # at round 1, the player has to equal his amount of chips in the table
                        # with the
                        # bot's amount
                        player.bet(20)
                        # add the chips to the pot
                        table.get_chips(player.bet_chips + bot1.bet_chips + bot2.bet_chips + bot2.bet_chips)
                        # clear the chips at the table
                        player.bet_chips = 0
                        bot1.bet_chips = 0
                        bot2.bet_chips = 0
                        bot3.bet_chips = 0
                        game_round += 1
                        break

                    elif game_round >= 2:  # After the first flop round, the game will follow this sequence: player
                        # -> bot1
                        # -> bot2 -> bot3 -> chips to pot -> next round
                        # TODO:  give the player the choice to bet a specific amount
                        player.bet(40)
                        # bot1 action
                        # TODO:  MAKE THE BOTS LESS DUMB
                        bot1.do()
                        # bot2 action
                        bot2.do()
                        # bot3 action
                        bot3.do()

                        # add the chips to the pot
                        table.get_chips(player.bet_chips + bot1.bet_chips + bot2.bet_chips + bot2.bet_chips)
                        # clear the chips at the table
                        player.bet_chips = 0
                        bot1.bet_chips = 0
                        bot2.bet_chips = 0
                        bot3.bet_chips = 0
                        game_round += 1
                        break

                # pass button clicked
                if 780 > pygame.mouse.get_pos()[0] > 720 and 530 > pygame.mouse.get_pos()[1] > 500:
                    # pass function
                    if game_round < 2:
                        # make the button unclickable
                        pass
                # fold button clicked
                if 850 > pygame.mouse.get_pos()[0] > 790 and 530 > pygame.mouse.get_pos()[1] > 500:
                    # fold function
                    if game_round < 2:
                        # make the button unclickable
                        pass

            if slider.on_slider(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]):
                slider.handle_event(window, pygame.mouse.get_pos()[0])

                # Instead of filling the entire screen, draw a rect over the old slider before creating the new one
                window.fill((0, 0, 0))

        # Draws the surface object to the screen.
        # pygame.display.update()
        pygame.display.flip()
        clock.tick(30)
