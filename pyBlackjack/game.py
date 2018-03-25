from pyBlackjack.player import Player
from pyBlackjack.dealer import Dealer
from pyBlackjack.deck import Deck
import pyBlackjack.operations as ops


class Game(object):

    def __init__(self, name):
        self.player = Player(name)
        self.dealer = Dealer()
        self.deck = Deck()
        self.deck.shuffle()

    def reset(self):
        self.player.reset()
        self.dealer.reset()
        self.deck = Deck()
        self.deck.shuffle()

    def deal_round(self):
        self.reset()
        if not ops.bet(self.player, self.player.hand):
            return False
        else:
            ops.hit(self.player.hand, self.deck)
            ops.hit(self.dealer.hand, self.deck)

            ops.hit(self.player.hand, self.deck)
            ops.hit(self.dealer.hand, self.deck)
            return True

    def hit(self, hand):
        return ops.hit(hand, self.deck)

    def split(self):
        return ops.split(self.player)

    def stick(self, hand):
        ops.stick(hand)
        return True

    def double_down(self, player, hand):
        return ops.double_down(player, hand, self.deck)

    def dealer_turn(self):
        hit = self.dealer.choice()
        if hit:
            return self.hit(self.dealer.hand)
        else:
            self.stick(self.dealer.hand)
            return False

    def reward(self):
        ops.reward(self.player, self.dealer)
