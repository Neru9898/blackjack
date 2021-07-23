import random
import numpy
# https://www.fallsviewcasinoresort.com/files/cn_gaming/table_games/pdf/Blackjack_EN.pdf


class Card:

    def __init__(self):
        self.base = {
            'Hearts': ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K'],
            'Spades': ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K'],
            'Clubs': ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K'],
            'Diamonds': ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        }

        self.card_value = {
            'Ace': [1, 11],
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
            'K': 10
        }


class Deck:
    def __init__(self):
        self.deck = Card().base
        self.deck_status_empty = 0

    def draw_card(self):
        self.suits_drawn = random.choice(list(self.deck.keys()))
        for suits in self.deck:
            self.deck_empty_check()
            if self.deck_status_empty != True:
                if self.deck[self.suits_drawn] != []:
                    self.num_drawn = random.choice(self.deck[self.suits_drawn])
                    self.index_num = self.deck[self.suits_drawn].index(
                        self.num_drawn)
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


class Player:

    def __init__(self):
        pass


class House:

    def __init__(self):
        pass


class BlackJack:

    def __init__(self):
        self.card_class = Card()

        self.deck_class = Deck()

        self.card_value = None

        self.game_deck = self.deck_class.deck

        self.player_hand = numpy.array([])

        self.player_hand_suite = numpy.array([])

        self.house_hand = numpy.array([])

        self.current = ()

        self.game_results = None

    def current_hand(self):
        self.current = self.deck_class.draw_card()
        if (self.deck_class.deck_status_empty != True):
            self.deck_class.pop_deck()
        else:
            pass

    def game_rule(self, player_hand):
        if self.add_cards(player_hand) > 21:
            return True
        elif self.add_cards(player_hand) == 21:
            return False
        else:
            pass

    def player_hand_game(self):
        if (self.deck_class.deck_status_empty != True):
            current_suits, current_num_drawn, current_index_num = self.current
            self.card_value = self.card_class.card_value[current_num_drawn]
            self.player_hand = numpy.append(self.player_hand, self.card_value)

    def house_hand_game(self):
        if (self.deck_class.deck_status_empty != True):
            current_suits, current_num_drawn, current_index_num = self.current
            self.card_value = self.card_class.card_value[current_num_drawn]
            self.house_hand = numpy.append(self.house_hand, self.card_value)

    def empty_hand(self):
        self.player_hand = numpy.array([])
        self.house_hand = numpy.array([])
        self.game_results = None

    def num_of_cards(self, hand):
        return numpy.size(hand)

    def add_cards(self, hand):
        if self.num_of_cards(hand) >= 2:
            return numpy.sum(hand)
        else:
            pass

    def game_reset(self):
        reset = input("Deck is empty, Do you want to cont or no: ")
        if reset == 'y':
            self.deck_class.reset_deck()
            self.current_hand()
        else:
            print('bye')
            self.game_results = 'Done'

    def player_double_down(self):
        if self.num_of_cards(self.player_hand) >= 2:
            double_down = input("Double Down: ")
            if double_down == 'y':
                self.current_hand()
                self.player_hand_game()
                # something that will let it know this is it

    def house_brain(self):
        player = self.add_cards(self.player_hand)
        house = self.add_cards(self.house_hand)

        if (house < player or house <= 16) and player <= 21:
            print('House turn')
            self.current_hand()
            self.house_hand_game()

    def black_jack_logic(self):
        player = self.add_cards(self.player_hand)
        house = self.add_cards(self.house_hand)
        if (house > player and house <= 21) or (house <= 21 and player != 21) or player > 21:
            self.game_results = "House"
        elif (player > house and player <= 21) or (player <= 21 and house != 21) or (house > 21):
            self.game_results = "Player"
        elif house == player:
            self.game_results = "Draw"
        else:
            pass


# black_jack = BlackJack()
# print()
# game_start = input("You wanna play: ")
# while game_start == 'y':
#     # ensure to check deck is full when drawing
#     try:
#         if black_jack.deck_class.deck_status_empty == True:
#             black_jack.game_reset()
#     except:
#         pass


#     if black_jack.game_results == 'Done':
#         break

#     # Dealing cards for both house and player
#     if black_jack.num_of_cards(black_jack.player_hand) < 2 and  black_jack.num_of_cards(black_jack.house_hand) < 2:
#         black_jack.current_hand()
#         black_jack.player_hand_game()
#         black_jack.current_hand()
#         black_jack.house_hand_game()

#     if black_jack.num_of_cards(black_jack.player_hand) >= 2:
#         print("House")
#         print(black_jack.house_hand)
#         print(black_jack.add_cards(black_jack.house_hand))
#         print("You")
#         print(black_jack.player_hand)
#         print(black_jack.add_cards(black_jack.player_hand))
#         black_jack.players_rule()
#         hit = input('Hit or Stay:')

#         if hit == 'y' and black_jack.deck_class.deck_status_empty != True:
#             black_jack.current_hand()
#             black_jack.player_hand_game()
#             black_jack.players_rule()


#         if (hit != 'y' and black_jack.game_results == None) or black_jack.game_rule(black_jack.player_hand):
#             black_jack.house_brain()


#         if black_jack.game_results == 'House':
#             print("House")
#             # print(black_jack.house_hand)
#             print(black_jack.add_cards(black_jack.house_hand))
#             print("You",black_jack.game_results)
#             # print(black_jack.player_hand)
#             print(black_jack.add_cards(black_jack.player_hand))
#             game_start = input("House wins, You wanna play again:")
#             black_jack.empty_hand()
#         elif black_jack.game_results == 'Player':
#             print("House")
#             # print(black_jack.house_hand)
#             print(black_jack.add_cards(black_jack.house_hand))
#             print("You")
#             # print(black_jack.player_hand)
#             print(black_jack.add_cards(black_jack.player_hand))
#             game_start = input("Player wins, You wanna play again:")
#             black_jack.empty_hand()
#         elif black_jack.game_results == 'Draw':
#             game_start = input("Issa Draw ya both wankers, You wanna play again tho:")
#             black_jack.empty_hand()
print('Thanks u twat')
# TESTING
