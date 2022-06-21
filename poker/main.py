import os
import pygame

from poker.functions import COLOR
from Classes.Game.game import Game
from Classes.Buttons.buttons import Button
from Classes.Configurations.configurations import Configurations
from Classes.HandRanking.hand_ranking import HandRanking

# core pygame configuration
WIDTH, HEIGHT = 901, 600  # window size
window = pygame.display.set_mode([WIDTH, HEIGHT])  # display object
pygame.display.set_caption("Pypoker")  # game caption change
# set window icon
icon = pygame.image.load(os.path.join('pics', 'poker_icon.png'))
pygame.display.set_icon(icon)
fps = 60  # frames per second
timer = pygame.time.Clock()  # timer object
pygame.init()
FONT_G = pygame.font.Font('freesansbold.ttf', 40)

# image
background = pygame.image.load(os.path.join('pics', 'poker_background.jpeg'))

# text
title = FONT_G.render('Pypoker', True, COLOR.white)

# components
# menu screen components
play = Button(window, COLOR.dark_green1, ((WIDTH // 2) - 150), ((HEIGHT // 2) - 120), 300, 100, 'Play',
              'g')  # play button
# configurations button
config = Button(window, COLOR.dark_blue1, ((WIDTH // 2) - 150), ((HEIGHT // 2) + 20), 300, 100, 'Configuration', 'g')  #
# configurations button
terminate = Button(window, COLOR.dark_red1, ((WIDTH // 2) - 150), ((HEIGHT // 2) + 160), 300, 100, 'EXIT', 'g')

# game window
game = Game(window)
# config windows
configs = Configurations(window)
# card combination
hand_ranking = HandRanking(window, 0, 0, 389, 590)

run = True  # game loop control variable
is_menu_active = True

while run:
    window.blit(background, (0, 0))
    window.blit(title, ((WIDTH // 2 - 80), 80))
    play.draw()
    config.draw()
    terminate.draw()

    # check if whether the game or the configs object is active, to blit them and toggle the is_menu_active variable
    # to deactivate the menu buttons
    if game.active:  # game is currently going
        game.draw()
        is_menu_active = False
        for current_player in game.players:
            # loop through the players list, and get every bot to make its action in order
            if current_player.playing:
                # verify if the player hasn't folded or lost
                if current_player.name.startswith('Bot') and current_player.active:  # check if the current player
                    # is a bot and is currently active
                    if game.round == 0:  # First round
                        if game.small == current_player:
                            if game.table.pot == 0:  # small bet
                                game.table.get_chips(current_player.bet(game.min))
                                game.min *= 2
                            else:
                                game.table.get_chips(current_player.bet(game.min // 2))

                                game.next_round()
                                break

                        elif game.big == current_player and game.table.pot == game.min:  # big bet
                            game.table.get_chips(current_player.bet(game.min))

                        else:
                            game.table.get_chips(current_player.bet(game.min))  # change this to a custom value

                        game.next()
                    elif 4 > game.round >= 1:
                        game.table.get_chips(current_player.bet(game.min))  # change this to a custom value

                        game.next()
                        if current_player == game.bot3:
                            game.next_round()

    elif configs.active:  # configuration window is currently open
        configs.draw()
        is_menu_active = False

    if hand_ranking.active:
        hand_ranking.draw()

    # event loop
    for event in pygame.event.get():
        # close the window and terminate the application if the user clicks on the close button
        if event.type == pygame.QUIT:
            run = False

        # check if the mouse was clicked
        if event.type == pygame.MOUSEBUTTONUP:
            # Config screen buttons event catch
            if configs.active:
                if configs.back_button.handle_click.collidepoint(event.pos):
                    configs.toggle_config()
                    is_menu_active = True

            # Game screen buttons event catch
            if game.active:

                # hand ranking
                if hand_ranking.active:
                    if hand_ranking.close_button.handle_click.collidepoint(event.pos):  # close button clicked
                        hand_ranking.toggle()   # close hand ranking window
                # Menu
                if game.game_menu.bg.handle_click.collidepoint(event.pos):  # toggle game_menu object
                    game.game_menu.toggle()
                # game menu interactions
                elif game.game_menu.active:
                    if game.game_menu.exit_button.handle_click.collidepoint(event.pos):     # exit button clicked
                        game.active = False
                        is_menu_active = True
                        game.game_menu.toggle()
                        game.restart()

                    if game.game_menu.restart_button.handle_click.collidepoint(event.pos):  # restart button clicked
                        game.restart()
                        game.game_menu.toggle()

                    if game.game_menu.card_combination_button.handle_click.collidepoint(event.pos):     # combinations
                        # clicked
                        hand_ranking.toggle()
                        game.game_menu.toggle()

                # ChipSelector
                if game.player.active:  # check if it's the player's turn
                    if game.chip_selector.active:  # chip_selector buttons click handler

                        if game.chip_selector.add.handle_click.collidepoint(event.pos):  # "ADD" button
                            if game.chip_selector.amount < game.player.chips:  # check if the amount is already the max
                                game.chip_selector.add_chips()  # if the value isn't the max, adds 5 to the amount
                        elif game.chip_selector.sub.handle_click.collidepoint(event.pos):  # "SUB" button
                            game.chip_selector.sub_chips()  # Subtracts 5 from the amount, if it's more than 0
                        elif game.chip_selector.max.handle_click.collidepoint(event.pos):  # "MAX" button
                            if game.chip_selector.amount < game.player.chips:  # check if the amount is already the max
                                game.chip_selector.add_chips(value=game.player.chips)  # Add the player's total chips
                                # to the amount
                        elif game.chip_selector.min.handle_click.collidepoint(event.pos):
                            game.chip_selector.min_value(game.min)

                    # BetMenu
                    if game.round < 4:
                        if game.bet_menu.bet_btn.handle_click.collidepoint(event.pos):  # "BET" was clicked
                            if game.round == 0 and game.player == game.small:
                                # check if the player is small bet
                                if game.table.pot == 0:  # first action
                                    game.table.get_chips(game.player.bet(game.min))
                                    game.min *= 2

                                    game.next()
                                else:  # equalize the amount of chips
                                    game.table.get_chips(game.player.bet(game.min // 2))
                                    game.next_round()

                            elif game.round == 0 and game.player == game.big:
                                # check if the player is the big bet and give him the chance of only betting the double
                                # of the small amount
                                game.table.get_chips(game.player.bet(game.min))

                                game.next()
                            elif game.chip_selector.active:  # chip_selector is already open
                                if game.chip_selector.amount >= game.min:  # amount bigger than zero
                                    # Take chips from player and give them to table, then closes the chip_selector
                                    # only if the chip_selector was already open
                                    # and the amount to be bet isn't smaller than the minimum amount
                                    game.table.get_chips(game.player.bet(game.chip_selector.amount))

                                    game.min = game.chip_selector.amount
                                    game.next()
                                    game.chip_selector.close()
                            elif not game.chip_selector.active:  # opens the chip selector
                                # opens the chip selector for the player to bet a custom amount
                                game.chip_selector.open()
                        elif game.bet_menu.pass_btn.handle_click.collidepoint(event.pos):
                            # "PASS" was clicked
                            if game.min == 0:
                                game.next()

                        elif game.bet_menu.fold_btn.handle_click.collidepoint(event.pos):
                            # "FOLD" was clicked
                            game.player.fold()  # user leave the round
                            game.next()  # continue the game
                    else:
                        if game.end_btn.handle_click.collidepoint(event.pos):
                            game.end_round()

            # Buttons of menu screen event catch
            if is_menu_active:
                if play.handle_click.collidepoint(event.pos):  # play button clicked
                    game.start_game()
                if config.handle_click.collidepoint(event.pos):  # configuration button clicked
                    configs.toggle_config()
                    is_menu_active = False
                if terminate.handle_click.collidepoint(event.pos):  # user pressed the exit button
                    run = False

    pygame.display.update()
    timer.tick(fps)
