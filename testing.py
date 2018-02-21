import blackjack as bj

# Ensuring calculation of hand is correct when accounting for aces.
def calc_test():
    hand = bj.Hand()

    c1 = bj.Card((('Ace', 11), 'Clubs'))
    c2 = bj.Card((('Ace', 11), 'Diamonds'))
    c3 = bj.Card((('Ace', 11), 'Hearts'))
    c4 = bj.Card((('Ace', 11), 'Spades'))

    hand.add_card(c1)
    hand.add_card(c2)
    hand.add_card(c3)
    hand.add_card(c4)

    total = hand.calc_total()
    print(total)

    return total == 14


if __name__ == "__main__":
    calc_test()
