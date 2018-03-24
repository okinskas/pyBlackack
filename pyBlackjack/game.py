from pyBlackjack.player import Player
from pyBlackjack.dealer import Dealer
from pyBlackjack.deck import Deck


class Game(object):

    def __init__(self, name):
        self.player = Player(name)
        self.dealer = Dealer()
        self.deck = Deck()
        self.turn_token = (1, 0)

    def get_turn_hand(self):
        if self.turn_token == (0, 0):
            return self.dealer.hand_main
        elif self.turn_token == (1, 0):
            return self.player.hand_main
        else:
            return self.player.hand_alt

    def reset(self):
        self.player.reset_hands()
        self.dealer.reset_hands()
        self.deck = Deck()

    def setup_deal(self):
        self.reset()
        if self.player.stack >= 10:
            self.dealer.hand_main.add_card(self.deck.get_card())
            self.dealer.hand_main.add_card(self.deck.get_card())
            self.player.hand_main.add_card(self.deck.get_card())
            self.player.hand_main.add_card(self.deck.get_card())
            self.player.stack -= 10
            return True
        else:
            return False

    def move_turn(self):
        if self.turn_token == (0, 0):
            self.turn_token = (1, 0)
        elif self.turn_token == (1, 0) and self.player.has_split():
            self.turn_token = (1, 1)
        else:
            self.turn_token = (0, 0)

    def split(self):
        if self.turn_token == (1, 0):
            if self.player.split():
                self.player.hand_main.add_card(self.deck.get_card())
                self.player.stack -= 10
                self.player.hand_alt.add_card(self.deck.get_card())
                return True
        return False

    def hit(self):
        hand = self.get_turn_hand()
        if hand.is_finished:
            return False
        if hand.is_blackjack():
            hand.finish()
            self.move_turn()
            return False

        hand.add_card(self.deck.get_card())

        if hand.is_bust():
            hand.finish()
            self.move_turn()
            return False
        else:
            return True

    def stick(self):
        hand = self.get_turn_hand()
        hand.finish()
        self.move_turn()

    def double_down(self):
        hand = self.get_turn_hand()
        x, y = self.turn_token
        if x == 1 and not hand.is_finished:
            self.player.stack -= hand.stake
            hand.double_down()
            self.hit()
            return True
        return False

    def is_winner(self, hand):
        dealer_total = self.dealer.hand_main.calc_total()
        total = hand.calc_total()
        if total == dealer_total:
            return None
        return 21 >= total > dealer_total

    def end_round(self):
        player_hands = [self.player.hand_main]
        if self.player.hand_alt is not None:
            player_hands.append(self.player.hand_alt)

        for hand in player_hands:
            try:
                if self.is_winner(hand):
                    self.player.stack += hand.stake * 2
            except None:
                self.player.stack += hand.stake

        if self.player.stack < 0:
            quit()

# w/o interface, sequence should be as follows:

# create game - initialise player name and stacks
# deal hands (initialise deck)
# player actions
# dealer actions
# calculate winner + distribute bets
# deal new hands (initialise deck)


