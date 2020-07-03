class Pile:

    def __init__(self):

        self.card_pile = []
        self.topCard = None
        self.previousCard = None
        self.sameValue = False

    def add_card(self, value):

        # Checks if pile is empty or not
        if self.topCard is not None:
            self.card_pile.append(value)
            # Checks if top 2 cards are the same value
            self.previousCard = self.topCard
            self.topCard = value
            self.sameValue = True if self.topCard == self.previousCard else False

        else:
            self.card_pile.append(value)
            self.topCard = value
            print("The first card is a " + value + "!\n")

    def get_pile(self):
        old_pile = self.card_pile
        self.card_pile = []
        self.topCard = None
        self.previousCard = None
        self.sameValue = False
        return old_pile

    def can_snap(self):
        return self.sameValue
