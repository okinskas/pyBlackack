from pyBlackjack.player import Player


class Dealer(Player):

    def __init__(self):
        Player.__init__(self, "Dealer")

    def __str__(self):
        out = self.name + ": "
        out += str(self.hand_main) + "\n"
        return out + "\n"

    def choice(self, player):
        dealer_hand = self.hand_main
        player_hand1 = player.hand_main.calc_total()
        player_hand2 = 0

        if player.hand_alt is not None:
            player_hand2 = player.hand_alt.calc_total()
        if player_hand1 > 21 and player_hand2 > 21:
            return False
        else:
            # hit on < 17 or is soft-seventeen
            is_soft_seventeen = dealer_hand.calc_total() == 17 and ('Ace', 11) in dealer_hand.get_hand()
            return dealer_hand.calc_total() < 17 or is_soft_seventeen
