from random import shuffle, randint
from time import sleep
from snap.pile import Pile
from snap.player import Player

print("Welcome to SNAP\n")

# Instatiate players
no_of_players = 2
player1 = Player("Alex")
player2 = Player("Uncle Ben")

# Ask user for number of decks to use
user_input = ""
while not user_input.isdigit():
    user_input = input("Enter the number of decks you want to play with: ")
    print("")

no_of_decks = int(user_input)

# Shuffle the decks together and give them to players
suit = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
play_deck = suit * 4 * no_of_decks
shuffle(play_deck)

# Splits deck between players
cutoff = int(len(play_deck) / no_of_players)
player1.set_cards(play_deck[cutoff:])
player2.set_cards(play_deck[:cutoff])

# Instatiate pile
game_pile = Pile()
print("The deck has been shuffled and handed to the players\n")

# Set up game
game_won = False
turn = 1
print("Player '" + player1.name + "' goes first!")

# Game in progress
while not game_won:
    # Sleep for 1 second for user experience and suspense
    sleep(1)
    current_player = player1 if turn == 1 else player2

    # Gets card from current player and adds it to the pile
    try:
        new_card = current_player.play_card()
        game_pile.add_card(new_card)
        print(current_player.name + " plays a " + new_card)
    except IndexError:
        print(current_player.name + " has run out of card!")

    # When both players run out of cards
    if (len(player1.cards) == 0) and (len(player2.cards) == 0):
        print("\nBoth players have run out cards")
        print("TIE!!")
        break

    # Execute if the top 2 cards have same value
    if game_pile.can_snap():
        # Picks winning player by random
        sleep(0.5)
        x = randint(0, 1)
        winning_player = player1 if x == 0 else player2

        print("\nSNAP!!!")
        print(winning_player.name + " wins this round!\n")

        winning_player.add_pile(game_pile.get_pile())

        # Excecutes when one player has all the cards
        if len(winning_player.cards) == len(play_deck):
            print("\n" + winning_player.name + " WINS!!")
            game_won = True
            break

    turn = 1 if turn == 2 else 2
