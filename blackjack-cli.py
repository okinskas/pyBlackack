from pyBlackjack.game import Game
import pyBlackjack.logic as logic


class TextDisplay(object):

    NAME_INDENT_COUNT = 10
    CARD_INDENT_COUNT = 6
    TABLE_EDGE_COUNT = 30
    TABLE_WHITESPACE_COUNT = TABLE_EDGE_COUNT - 2

    NAME_INDENT = ''.join([" " for _ in range(NAME_INDENT_COUNT)])
    CARD_INDENT = ''.join([" " for _ in range(CARD_INDENT_COUNT)])
    TABLE_EDGE = ''.join(["-" for _ in range(TABLE_EDGE_COUNT)])
    TABLE_WHITESPACE = ''.join(["|"] + [" " for _ in range(TABLE_WHITESPACE_COUNT)] + ["|"])

    def __init__(self, game):
        self.game = game

    def print_hand(self, name, hand):
        out = self.CARD_INDENT + name + ": "
        for card in hand.cards:
            out += "| " + card.rank + card.suit + " |"
        print(out)

    def print_dealer_reveal(self):
        cards = self.game.dealer.hand.cards
        print(self.CARD_INDENT + "Dealer: | " + cards[0].rank + cards[0].suit + " || ? |")

    def print_dealer(self):
        dealer = self.game.dealer
        self.print_hand(dealer.name, dealer.hand)

    def print_player(self):
        player = self.game.player
        self.print_hand(player.name, player.hand)
        if player.alt is not None:
            self.print_hand(player.name, player.hand)
        print(self.CARD_INDENT + "Stack: " + str(player.stack))

    def print_table(self, dealer_all=False):
        print(self.TABLE_EDGE)
        print(self.TABLE_WHITESPACE)
        if dealer_all:
            self.print_dealer()
        else:
            self.print_dealer_reveal()
        print(self.TABLE_WHITESPACE)
        self.print_player()
        print(self.TABLE_WHITESPACE)
        print(self.TABLE_EDGE)

    def print_leave(self):
        p = self.game.player
        print(p.name + " leaves with " + str(p.stack) + "chips.")


class Controller(object):

    def __init__(self, name):
        self.game = Game(name)
        self.display = TextDisplay(self.game)

    def play(self):
        while True:
            self.ask_to_start()
            self.start_round()
            self.player_turn(self.game.player.hand)
            self.dealer_turn()
            self.end_round()

    def ask_to_start(self):
        play = input("Start round? [y/n]\n")

        if play is "n":
            self.leave_table()
        else:
            return True

    def start_round(self):
        self.game.reset()
        self.game.deal_round()
        self.display.print_table()

    def player_turn(self, hand):
        while True:

            if logic.is_done(hand):
                break

            action = self.get_input("Choose action:\n")
            parsed = self.parse_player_input(action, hand, self.game.player)

            if not parsed:
                print("Invalid action")
                continue
            elif action in ["done", "stick"]:
                break

    def dealer_turn(self):
        while True:
            can_cont = self.game.dealer_turn()

            if not can_cont:
                break
            elif can_cont is "bust":
                print("bust")
                break

    def end_round(self):
        self.game.reward()
        self.display.print_table(dealer_all=True)

    def get_input(self, msg):
        self.display.print_table()
        return input(msg)

    def parse_player_input(self, msg, hand, player):
        msg = str(msg)
        if msg in 'hit':
            return self.game.hit(hand),
        elif msg in 'stick':
            return self.game.stick(hand)
        elif msg in 'split':
            return self.game.split()
        elif msg in 'dd':
            return self.game.double_down(player, hand)
        elif msg in 'leave':
            return self.leave_table()
        else:
            return False

    def leave_table(self):
        self.display.print_leave()
        quit()


if __name__ == "__main__":

    while True:
        name = input("What is your name?\n")
        if name == "Dealer":
            print("Nice try, your name cannot be dealer. Please enter a different name.")
            continue
        break

    controller = Controller(name)
    controller.play()
