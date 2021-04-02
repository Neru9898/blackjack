import random
import numpy as np
class Card:

    def __init__(self):
        self.base = {
            'Hearts':['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K'],
            'Spades':['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K'],
            'Clubs':['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K'],
            'Diamonds':['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        }

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
        self.deck_status_empty  = 0
    
    def draw_card(self):
        self.suits_drawn = random.choice(list(self.deck.keys()))
        for suits in self.deck:
            self.deck_empty_check()
            if self.deck_status_empty  != True:
                if self.deck[self.suits_drawn] != []:
                    self.num_drawn = random.choice(self.deck[self.suits_drawn])
                    self.index_num = self.deck[self.suits_drawn].index(self.num_drawn)
                    return self.suits_drawn, self.num_drawn, self.index_num
                else:
                    self.draw_card()
            else:
                break

    def pop_deck(self):
        self.deck[self.suits_drawn].pop(self.index_num)
        # print((self.deck[self.suits_drawn]))

    def reset_deck(self):
        self.deck = Card().base

    def deck_empty_check(self):
        if((self.deck['Hearts'] == [] and self.deck['Spades'] == [] and self.deck['Clubs'] == [] and self.deck['Diamonds'] == [])):
            self.deck_status_empty = True
        else:
            self.deck_status_empty = False
        

        
    
            


class BlackJack:
    
    def __init__(self):
        self.card_class = Card()
        self.deck_class = Deck()
        self.game_value = self.card_class.card_value
        self.game_deck = self.deck_class.deck
        # self.player_hand = np.array([])
        # self.house_hand = np.array([])

    
    def current_hand(self):
        current = self.deck_class.draw_card()
        # deck_status = self.deck_class.deck_empty_check()
        if (self.deck_class.deck_status_empty  != True):
            self.deck_class.pop_deck()
            print(current)
            return current
        else:
            self.game_reset()
            

        
    def value_of_hand(self,hand):
        current_suits, current_num_drawn, current_index_num  = self.current_hand()

    def game_reset(self):
        reset = input("Deck is empty, Do you want to cont or no:")
        if reset == 'y':
            self.deck_class.reset_deck()
            self.current_hand()
        else:
            print('bye',self.game_deck)

            


f = BlackJack()
i = 0
while i < 56:
    i += 1
    f.current_hand()
