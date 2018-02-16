import math
import random
#card implementation is fine
class Card(object):

    ranks = [(2,2),(3,3),(4,4),(5,5),(6,6),(7,7),(8,8),(9,9),(10,10),('Jack',10),('Queen',10),('King',10),('Ace',11)]
    suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']

    def __init__(self, card_tuple):
        self.rank, self.suit = card_tuple

    def __str__(self):
        return str(self.rank[0]) + " of " + self.suit + "."

    def get_suit(self):
        return self.suit

    def get_key(self):
        return self.rank[0]

    def get_value(self):
        return self.rank[1]

    def get_rank(self):
        return self.rank


# deck implementation is fine
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
    # implement preserve order for printing purposes
    # for some reason cards=[] is not working, setting manually on creation while I figure it out
    def __init__(self, cards):
        self.cards = cards
        self.has_finished = False
        self.has_doubled_down = False

    def __str__(self):
        out = ""
        for card in self.cards:
            out += str(card) + " "
        return out
    
    def add_card(self, card):
        self.cards.append(card)     
    
    def get_hand(self):
        return self.cards

    def split_hand(self):
        if self.cards[0].get_key() == self.cards[1].get_key():
            hand1 = Hand([self.cards[0]])
            hand2 = Hand([self.cards[1]])
            return hand1, hand2
        else:
            return None, None

    def clear_hand(self):
        self.cards = []

    def is_blackjack(self):
        cards = self.cards
        if len(cards) == 2:
            has_ace = ("Ace", 11) in cards 
            has_value_10 = ('Jack',10) in cards or ('Queen',10) in cards or ('King',10) in cards
            return has_ace and has_value_10
        else:
            return False

    def calc_total(self, total=0, n=0, ace_count=0):
        if (n >= len(self.cards)):
            return total
        if self.cards[n].get_rank() == ('Ace', 11):
            ace_count += 1
        total += self.cards[n].get_value()
        if total > 21 and ace_count > 0:
            total -= 10
            ace_count -= 1
        return self.calc_total(total, n + 1, ace_count)

class Player(object):

    def __init__(self, name):
        self.name = name
        self.hand_main = Hand([])
        self.hand_alt = None

    def __str__(self):
        out = self.name + ": "
        out += str(self.hand_main) + "\n"
        out += str(self.hand_alt)
        return out + "\n"

    def split(self):
        main, alt = self.hand_main.split()
        if main == None:
            return False
        else:
            self.hand_main, self.hand_alt = main, alt
            return True

    def reset_hands(self):
        self.hand_main = Hand([])
        self.hand_alt = None

    def has_split(self):
        return self.hand_alt != None

class Dealer(Player):

    def __init__(self):
        Player.__init__(self, "Dealer")

    def __str__(self):
        out = self.name + ": "
        out += str(self.hand_main) + "\n"
        return out + "\n"

    def show_one(self):
        return self.name + ": " + str(self.hand_main.get_hand()[0])

    def choice(self, player):
        dealer_hand = self.hand_main
        player_hand1 = player.hand_main.calc_total()
        player_hand2 = 0

        if player.hand_alt != None:
            player_hand2 = player.hand_alt.calc_total()
        if player_hand1 > 21 and player_hand2 > 21:
            return False
        else:
            # hit on < 17 or is soft-seventeen
            is_soft_seventeen = dealer_hand.calc_total() == 17 and ('Ace',11) in dealer_hand.get_hand()
            return dealer_hand.calc_total() < 17 or is_soft_seventeen

# standard game actions
class Game(object):

    def __init__(self, name):
        self.player = Player(name)
        self.dealer = Dealer()
        self.deck = Deck()
        self.turn_token = (0, 0)

    def get_turn_hand(self):
        if self.turn_token == (0, 0):
            return self.dealer.hand_main
        elif self.turn_token == (1, 0):
            return self.player.hand_main
        else:
            return self.player.hand_alt

    def reset_deck(self):
        self.deck = Deck()

    def setup_deal(self):
        self.dealer.hand_main.add_card(self.deck.get_card())
        self.dealer.hand_main.add_card(self.deck.get_card())
        self.player.hand_main.add_card(self.deck.get_card())
        self.player.hand_main.add_card(self.deck.get_card())

    def move_turn(self):
        if self.turn_token == (0, 0):
            self.turn_token = (1, 0)
        elif self.turn_token == (1, 0) and  self.player.has_split():
            self.turn_token = (1, 1)
        else:
            self.turn_token = (0,0)

    def split(self):
        if self.turn_token == (1, 0):
            return self.player.split()
        return False

    def hit(self):
        hand = self.get_turn_hand()
        if hand.is_blackjack():
            return False

        hand.add_card(self.deck.get_card())

        if hand.is_bust():
            return False
        else:
            return True


# w/o interface, sequence should be as follows:

# create game - initialise player name and stacks
# deal hands (initialise deck)
# player actions
# dealer actions
# calculate winner + distribute bets
# deal new hands (initialise deck)

# might make sense to use generators for getting cards from deck?

