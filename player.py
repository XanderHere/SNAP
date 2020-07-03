from collections import deque


class Player:

    def __init__(self, name):
        self.cards = deque('')
        self.name = name

    def set_cards(self, cards):
        self.cards = deque(cards)

    def add_pile(self, pile):
        self.cards.extend(pile)

    def play_card(self):
        top_card = self.cards.pop()
        return top_card
