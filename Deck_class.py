import random

class Card:

    def __init__(self):
        self.base = {
            'Hearts':['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K'],
            'Spades':['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K'],
            'Clubs':['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K'],
            'Diamonds':['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        }

    def  card_values(self):
        self.card_value = {
            'Ace': 1,
            '2': 2,
            '3': 3,
            '4': 4,
            '5': 5,
            '6': 6,
            '7': 7,
            '8': 8,
            '9': 9,
            '10': 10,
            'J': 10,
            'Q': 10,
            'K':10
        }



class Deck:
    def __init__(self):
        self.deck = Card().base
    
    def draw_card(self):
        self.suits_drawn = random.choice(list(self.deck.keys()))
        self.num_drawn = random.choice(self.deck[self.suits_drawn])
        self.index_num = self.deck[self.suits_drawn].index(self.num_drawn)

    def pop_deck(self):
        print(self.suits_drawn,self.num_drawn,self.index_num)
        self.deck[self.suits_drawn].pop(self.index_num)
        # print((self.deck[self.suits_drawn]))

    def reset_deck(self):
        self.deck = Card().base

    def deck_empty_check(self):
        if(not (self.deck['Hearts'] and self.deck['Spades'] and self.deck['Clubs'] and self.deck['Diamonds'])):
            print('Deck is empty and ned to reset')
