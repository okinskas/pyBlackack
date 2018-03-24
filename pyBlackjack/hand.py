class Hand(object):

    def __init__(self, cards=[]):
        self.cards = cards
        self.is_finished = False
        self.has_doubled_down = False
        self.stake = 10

    def __str__(self):
        out = ""
        for card in self.cards:
            out += str(card) + " "
        return out

    def __len__(self):
        return len(self.cards)

    def add_stake(self, amount):
        self.stake += amount

    def add_card(self, card):
        self.cards.append(card)

    def double_down(self):
        self.stake = self.stake * 2
        self.has_doubled_down = True
        self.finish()

    def split_hand(self):
        if self.cards[0].get_key() == self.cards[1].get_key():
            hand1 = Hand([self.cards[0]])
            hand2 = Hand([self.cards[1]])
            return hand1, hand2
        else:
            return None, None

    def get_hand(self):
        return self.cards

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

    def finish(self):
        self.is_finished = True

    def calc_total(self, total=0, n=0, ace_count=0):
        if n >= len(self.cards):
            return total
        if self.cards[n].get_rank() == ('Ace', 11):
            ace_count += 1
        total += self.cards[n].get_value()
        if total > 21 and ace_count > 0:
            total -= 10
            ace_count -= 1
        return self.calc_total(total, n + 1, ace_count)
