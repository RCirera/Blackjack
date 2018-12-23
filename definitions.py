import random


class Card:

    def __init__(self):
        card_list = [['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K'],
                     [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]]
        index = random.choice(range(0, 13))
        self.face = card_list[0][index]
        self.value = card_list[1][index]


class Hand:

    def __init__(self, size=0):
        self.cards = []
        self.card_faces = []
        self.card_values = []

        for _ in range(size):
            c = Card()
            self.cards.append(c)
            self.card_faces.append(c.face)
            self.card_values.append(c.value)

        self.value = self.count()

    def __len__(self):
        return len(self.cards)

    def empty(self):
        self.cards = []
        self.card_faces = []
        self.card_values = []
        self.value = self.count()

    def append(self, new_card):
        self.cards.append(new_card)
        self.card_faces.append(new_card.face)
        self.card_values.append(new_card.value)
        self.value = self.count()

    def count(self):
        count = sum(self.card_values)
        for ace in range(self.card_faces.count('A')):
            new_count = count + 10
            if new_count < 22:
                count = new_count
        return count


