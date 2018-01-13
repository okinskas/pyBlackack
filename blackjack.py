import math
import random

class Card(object):

    ranks = [(2,2),(3,3),(4,4),(5,5),(6,6),(7,7),(8,8),(9,9),(10,10),('Jack',10),('Queen',10),('King',10),('Ace',11)]
    suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']

    def __init__(self, card_tuple):
        self.rank, self.suit = card_tuple

    def __str__(self):
        return str(self.rank[0]) + " of " + self.suit + "."

    def get_suit(self):
        return self.suit

    def get_value(self):
        return self.rank[1]

class Deck(object):

    def __init__(self):
        self.cards = []
        for suit in Card.suits:
            for rank in Card.ranks:
                self.cards.append(Card((rank, suit)))

    def __str__(self):
        return str(self.cards)

    def remove(self, index):
        del self.cards[index] # check this is correct...

    def get_card(self):
        position = random.randint(0, len(self.cards) - 1)
        card = self.cards[position] # check this is correct
        self.remove(position)
        return card

class Hand(object):

    def __init__(self, cards):
        self.cards = cards
        self.handled = False
        self.doubled_down = False

    def __str__(self):
        out = ""
        for card in self.cards:
            out += str(card) + " "
        return out
    
    def add_card(self, card):
        # sort from smallest to largest with each addition, either add and sort, or check, insert, shift
        for i in range(0, len(self.cards)):
            if self.cards[i].get_value() > card.get_value():
                self.cards.insert(i, card)
                return
        self.cards.append(card)     
    
    def get_hand(self):
        return self.cards

    def split_hand(self):
        return Hand(self.cards[0]), Hand(self.cards[1])

    def has_doubled_down(self):
        return self.doubled_down

    def finish(self):
        self.handled = True

    def has_finished(self):
        return self.handled

    def clear_hand(self):
        self.cards = []

    def can_split(self):
        return self.cards[0].get_suit() == self.cards[1].get_suit()

    def calc_total(self, total=0, n=0): # likely still wrong
        if (n >= len(self.cards)):
            return total
        
        card_value = self.cards[n].get_value()
        if card_value == 11 and total + card_value > 21:
            card_value = 1
        new_total = total + card_value
        return self.calc_total(new_total, n + 1)


class Player(object):

    def __init__(self, name):
        self.name = name
        self.hand_main = Hand([])
        self.hand_split = None

    def __str__(self):
        out = self.name + ": "
        out += str(self.hand_main)
        out += str(self.hand_split)
        return out + "\n"

    def split(self):
        if self.hand_main.can_split():
            self.hand_main, self.hand_split = self.hand_main.split_hand()
            return True
        else:
            return False

    def reset_hands(self):
        self.hand_main = Hand([])
        self.hand_split = None

class Dealer(Player):

    def __init__(self):
        Player.__init__(self, "Dealer")

    def show_one(self):
        return self.name + ": " + str(self.hand_main.get_hand()[0])

    def choice(self):
        return self.hand_main.calc_total() < 17

class Game(object):

    def __init__(self, name):
        self.player = Player(name)
        self.dealer = Dealer()
        self.deck = Deck()

    def reset_deck(self):
        self.deck = Deck()

    def setup_deal(self):
        
        self.dealer.hand_main.add_card(self.deck.get_card())
        self.dealer.hand_main.add_card(self.deck.get_card())
        print(self.dealer.show_one())
        self.player.hand_main.add_card(self.deck.get_card())
        self.player.hand_main.add_card(self.deck.get_card())

# change all below to work with main/split hands
    def hit(self, hand):
        hand.add_card(self.deck.get_card())

    def stick(self):
        self.hand_position += 1
        if self.hand_position < len(self.player.hands):
            self.hand_position = 0
            self.turn_position += 1

    def split(self, player):
        return player.split_hand(self.hand_position)

    def player_cycle(self, hand):
        while True:
            print(str(self.player))
            choice = input("What do you do?\n").lower()
            if choice == "stick":
                hand.finish()
                break
            elif choice == "hit":
                hand.add_card(self.deck.get_card())
                if hand.calc_total() >= 21:
                    print(str(hand))
                    hand.finish()
                    break
            elif choice == "split":
                if not self.player.split():
                    print("You cannot split this hand.\n")
                else:
                    break
            elif choice == "double down" or "dd":
                hand.add_card(self.deck.get_card())
                hand.has_doubled_down = True
                hand.finish()
                break
            elif choice == "quit":
                SystemExit
            else:
                print("Not a valid choice.\n")

    def dealer_cycle(self):
        while True:
            print(str(self.dealer))
            if self.dealer.choice():
                self.dealer.hand_main.add_card(self.deck.get_card())
                continue
            break
    
    def play(self): # need to prevent dealer from playing if other hands are bust already
        self.player_cycle(self.player.hand_main)
        if not self.player.hand_main.has_finished():
            self.player_cycle(self.player.hand_main)
        player_total1 = self.player.hand_main.calc_total()
        player_total2 = None
        if self.player.hand_split != None:
            self.player_cycle(self.player.hand_split)
            player_total2 = self.player.hand_split.calc_total()
        if player_total1 < 21 or (player_total2 != None and player_total2 < 21):
            self.dealer_cycle()
        self.calc_winner()

    def calc_winner(self): # need to check split hand and account for blackjack
        dealer_total = self.dealer.hand_main.calc_total()
        player_total1 = self.player.hand_main.calc_total()

        if player_total1 > 21 or (player_total1 < dealer_total and dealer_total <= 21):
            print("Dealer wins with: " + str(self.dealer.hand_main))
        elif player_total1 > dealer_total or dealer_total > 21:
            print(self.player.name + " wins with: " + str(self.player.hand_main))
            pass
        else:
            print("Tied result")
            print("Dealer: " + str(self.dealer.hand_main))
            print(self.player.name + ": " + str(self.player.hand_main))


class Controller(object):
    
    def __init__(self, name):
        game = Game(name)
        game.setup_deal()
        game.play()

# account for earlier ace in calculation -> solved, hands are now ordered, moved calc total to hand
# change game to account for multiple hands per player
# need to add split option, will mean increasing the number of hands ^
# add betting
# add double down
if __name__ == "__main__":

    while True:
        name = input("What is your name?\n")
        if name == "Dealer":
            print("Nice try, your name cannot be dealer. Please enter a different name.")
            continue
        break
    Controller(name)