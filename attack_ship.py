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


class Attack:

    def clear_screen(self):
        print("\033c", end="")

    def attacking(self, board, guess_board, ship_hp):
        self.get_coordinates(guess_board)
        if board[self.row_index][self.col_index] == '.':
            print("You have already shot at {}{}, try somewhere else."
                  .format(self.col_alpha, self.row_index_str))
            self.attacking(board, guess_board, ship_hp)

        elif board[self.row_index][self.col_index] == '*':
            print("You have already shot at {}{}, try somewhere else."
                  .format(self.col_alpha, self.row_index_str))
            self.attacking(board, guess_board, ship_hp)

        elif board[self.row_index][self.col_index] == '#':
            print("You have already shot at {}{}, try somewhere else."
                  .format(self.col_alpha, self.row_index_str))
            self.attacking(board, guess_board, ship_hp)
        else:
            self.check_hit(board, guess_board, ship_hp)

    def get_coordinates(self, guess_board):
        cond1 = False
        cond2 = False

        while cond1 is False or cond2 is False:
            coord_chosen = input("At what coordinate do you want to attack?")
            coord_chosen.replace(" ", "")
            coord_seperated = list(coord_chosen)
            self.col_alpha = coord_seperated[0]

            try:
                if len(coord_seperated) == 3:
                    self.row_index_str = coord_seperated[1] + coord_seperated[2]
                else:
                    self.row_index_str = coord_seperated[1]
            except IndexError:
                print("Alphabet letter and a number between 1 - {}"
                      .format(BOARD_SIZE))
                self.clear_screen()
                cond1 = False

            try:
                if self.col_alpha.upper() in alpha_list[:BOARD_SIZE]:
                    self.col_index = alpha_list.index(self.col_alpha.upper())
                    cond1 = True
                else:
                    print("Invalid letter, use letter from A to {}"
                          .format(alpha_list[BOARD_SIZE-1]))
                    self.clear_screen()
                    cond1 = False
            except AttributeError:
                print("Alphabet letter and a number between 1 - {}"
                      .format(BOARD_SIZE))
                cond1 = False

            try:
                if int(self.row_index_str) > BOARD_SIZE:
                    print("That row does not exist in this game! "
                          "Try a number from 1 to {}!".format(BOARD_SIZE))
                    press_enter = input("Press enter to continue")
                    self.clear_screen()
                    cond2 = False
                else:
                    self.row_index = int(self.row_index_str) - 1
                    cond2 = True
            except ValueError:
                print("Input should be one letter and a number between 1 and {}"
                      .format(BOARD_SIZE))
                press_enter = input("Press enter to continue")
                self.clear_screen()
                cond1 = False
                    
        return self.row_index, self.col_index

    def check_hit(self, board, guess_board, ship_hp):
        condition1 = True
        while condition1 is True:
            if board[self.row_index][self.col_index] == 'O':
                guess_board[self.row_index][self.col_index] = '.'
                print("Miss!")
                press_enter = input("Press enter to continue")
                self.clear_screen()
                condition1 = False

            elif board[self.row_index][self.col_index] == VERTICAL_SHIP:
                board[self.row_index][self.col_index] = HIT
                guess_board[self.row_index][self.col_index] = HIT
                print("HIT!")
                press_enter = input("Press enter to continue")
                self.clear_screen()
                ship_hp.append(1)
                condition1 = False

            elif board[self.row_index][self.col_index] == HORIZONTAL_SHIP:
                board[self.row_index][self.col_index] = HIT
                guess_board[self.row_index][self.col_index] = HIT
                print("HIT!")
                press_enter = input("Press enter to continue")
                self.clear_screen()
                ship_hp.append(1)
                condition1 = False

    def check_sunk(self, board, guess_board, location_dict):
        num_hits = {}
        for key, value in location_dict.items():
            num_hits[key] = 0
            for coordi in value:
                if board[coordi[0]][coordi[1]] == HIT:
                    num_hits[key] += 1
                else:
                    continue
            for self.ship, self.length in SHIP_INFO:
                if self.ship == key and self.length == num_hits[key]:
                    for coordi in value:
                        board[coordi[0]][coordi[1]] = SUNK
                        guess_board[coordi[0]][coordi[1]] = SUNK
                    print("You sunk a {}.".format(key))
