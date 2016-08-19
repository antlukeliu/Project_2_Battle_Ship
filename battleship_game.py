from ship import Ship
from attack_ship import Attack

p1_board = []
p2_board = []
p1_guess_board = []
p2_guess_board = []
p1_location_dict = {}
p2_location_dict = {}
p1_hp = []
p2_hp = []
BOARD_SIZE = 10
VERTICAL_SHIP = '|'
HORIZONTAL_SHIP = '-'
EMPTY = 'O'
MISS = '.'
HIT = '*'
SUNK = '#'
alpha_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G',
              'H', 'I', 'J', 'K', 'L', 'M', 'N',
              'O', 'P', 'Q', 'R', 'S', 'T', 'U',
              'V', 'W', 'X', 'Y', 'Z']

SHIP_INFO = [
    ("Aircraft Carrier", 5),
    ("Battleship", 4),
    ("Submarine", 3),
    ("Cruiser", 3),
    ("Patrol Boat", 2)
]


def create_board(board):
    for x in range(BOARD_SIZE):
        board.append([EMPTY] * 10)


def print_board_heading():
        print("   " + " "
              .join([chr(c) for c in range(ord('A'), ord('A') + BOARD_SIZE)]))


def print_board(board):

    print_board_heading()

    row_num = 1
    for row in board:
        print(str(row_num).rjust(2) + " " + (" ".join(row)))
        row_num += 1


def clear_screen():
    print("\033c", end="")


class game:
    total_length = 0

    def __init__(self, **kwargs):
        self.condition = True
        for self.ship, self.length in SHIP_INFO:
            self.total_length += self.length

        print("{} choose where to place your ships".format(player_1))
        print_board(p1_board)
        ship_class.ship_placement(p1_board, p1_location_dict)
        clear_screen()
        player_2_enter = input("{} your turn to place ships. Press Enter "
                               .format(player_2))
        print_board(p2_board)
        print("{} choose where to place your ships".format(player_2))
        ship_class.ship_placement(p2_board, p2_location_dict)
        while self.condition is True:
            clear_screen()
            player1_enter = input("{} it is your turn, press Enter to continue"
                                  .format(player_1))
            print("{} where do you want to attack".format(player_1))
            print_board(p1_guess_board)
            attack_class.attacking(p2_board, p1_guess_board, p2_hp)
            attack_class.check_sunk(p2_board, p1_guess_board, p2_location_dict)
            print(len(p2_hp))
            if len(p2_hp) == self.total_length:
                break
            player2_enter = input("{} it is your turn, press enter to continue"
                                  .format(player_2))
            print("{} where do you want to attack".format(player_2))
            print_board(p2_guess_board)
            attack_class.attacking(p1_board, p2_guess_board, p1_hp)
            attack_class.check_sunk(p1_board, p2_guess_board, p1_location_dict)
            if len(p1_hp) == self.total_length:
                break
        if p1_hp == self.total_length:
            print("{} you won".format(player_2))
        else:
            print("{} you won".format(player_1))

if __name__ == '__main__':
    create_board(p1_board)
    create_board(p2_board)
    create_board(p1_guess_board)
    create_board(p2_guess_board)

    ship_class = Ship()
    attack_class = Attack()

    player_1 = input("Player 1 what is your name? ")
    player_2 = input("Player 2 what is your name? ")
    game()
