import random
import numpy 
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
        self.card_value = None
        self.game_deck = self.deck_class.deck
        self.player_hand = numpy.array([])
        self.house_hand = numpy.array([])
        self.current = ()

    
    def current_hand(self):
        self.current = self.deck_class.draw_card()
        # deck_status = self.deck_class.deck_empty_check()
        if (self.deck_class.deck_status_empty  != True):
            self.deck_class.pop_deck()
            # print(current)
        else:
            pass
            
    def game_rule(self,hand):
        if self.add_cards(hand) > 21:
            return True
        elif self.add_cards(hand) == 21:
            return False
        else:
            pass

    def player_hand_game(self):
        if (self.deck_class.deck_status_empty  != True):
            current_suits, current_num_drawn, current_index_num  = self.current 
            self.card_value = self.card_class.card_value[current_num_drawn]
            self.player_hand = numpy.append(self.player_hand,self.card_value)
        else:
            pass

    def house_hand_game(self):
        current_suits, current_num_drawn, current_index_num  = self.current
        self.card_value = self.card_class.card_value[current_num_drawn]
        self.house_hand = numpy.append(self.house_hand,self.card_value)

    def empty_hand(self):
        self.player_hand = numpy.array([])
        self.house_hand = numpy.array([])


    def num_of_cards(self,hand):
        return numpy.size(hand)


    def add_cards(self,hand):
        if self.num_of_cards(hand) >= 2:
            return numpy.sum(hand)
        else:
            pass
    
    def game_reset(self):
        reset = input("Deck is empty, Do you want to cont or no:")
        if reset == 'y':
            self.deck_class.reset_deck()
            self.current_hand()
        else:
            print('bye')



black_jack = BlackJack()
print()
game_start = input("You wanna play:")
while game_start == 'y':
   
    try:
        if black_jack.deck_class.deck_status_empty == True:
            black_jack.game_reset()
            break
    except:
        pass

    if black_jack.num_of_cards(black_jack.player_hand) < 2:
        black_jack.current_hand()
        black_jack.player_hand_game()

    
    if black_jack.num_of_cards(black_jack.player_hand) >= 2:
        print(black_jack.player_hand)
        print(black_jack.add_cards(black_jack.player_hand))
        hit = input('you wanna hit:')

        if hit == 'y' and black_jack.deck_class.deck_status_empty != True:
            black_jack.current_hand()
            black_jack.player_hand_game()
        
        try:
            if black_jack.game_rule(black_jack.player_hand):
                print('YOU LOST')
                game_start = input("You wanna play again:")
                black_jack.empty_hand()
            
        except:
            pass
        
        try:
            if black_jack.game_rule(black_jack.player_hand) == False:
                print('YOU WON')
                print(black_jack.player_hand)
                print(black_jack.add_cards(black_jack.player_hand))
                game_start = input("You wanna play again:")
                black_jack.empty_hand()
            
        except:
            pass

        try:
            if hit != 'y':
                game_start = input("You wanna play again:")
                black_jack.empty_hand()
        except:
            pass


print('Thanks',black_jack.game_deck)
     
    

