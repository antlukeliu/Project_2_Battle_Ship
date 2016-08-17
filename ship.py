SHIP_INFO = [
    #("Aircraft Carrier", 5),
    #("Battleship", 4),
    #("Submarine", 3),
    #("Cruiser", 3),
    ("Patrol Boat", 2)
]
board = []
BOARD_SIZE = 10
V_SHIP = '|'
H_SHIP = '-'
EMPTY = 'O'
MISS = '.'
HIT = '*'
SUNK = '#'
alpha_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G',
              'H', 'I', 'J', 'K', 'L', 'M', 'N',
              'O', 'P', 'Q', 'R', 'S', 'T', 'U',
              'V', 'W', 'X', 'Y', 'Z']


class Ship:

    def create_board(self):
        for x in range(BOARD_SIZE):
            board.append([EMPTY] * 10)

    def print_board_heading(self):
        print("   " + " "
              .join([chr(c) for c in range(ord('A'), ord('A') + BOARD_SIZE)]))

    def print_board(self, board):

        self.print_board_heading()

        row_num = 1
        for row in board:
            print(str(row_num).rjust(2) + " " + (" ".join(row)))
            row_num += 1

    def clear_screen():
        print("\033c", end="")
        print('\n'*25)

    def ship_placement(self, board, location_dict):
        for self.ship, self.length in SHIP_INFO:
            self.check_ship_coordinates(board, location_dict)

        

    def check_ship_coordinates(self, board, location_dict):
        location = []
        cond1 = False
        cond2 = False
        cond3 = False
        cond4 = False

        while (cond1 is False or cond2 is False or
               cond3 is False or cond4 is False):
            self.coord_chosen = input("Where do you want to place your {}? "
                                      .format(self.ship))
            self.h_yes_or_no = input("Would you like the {} place "
                                     "horizontally?(Y/N): ".format(self.ship))
            self.coord_chosen.replace(" ", "")
            coord_seperated = list(self.coord_chosen)
            self.col_alpha = coord_seperated[0]


            
            # if the Board_Size is 10 or greater,
            # makes sure double dight value does not throw an error
            if len(coord_seperated) == 3:
                self.row_index_str = coord_seperated[1] + coord_seperated[2]
            else:
                self.row_index_str = coord_seperated[1]

            # cond1 makes sure the column index
            # is a valid alphabet letter on the board
            if self.col_alpha.upper() in alpha_list[:BOARD_SIZE]:
                self.col_index = alpha_list.index(self.col_alpha.upper())
                cond1 = True
            else:
                print("Invalid letter, use letter from A to {}"
                      .format(alpha_list[BOARD_SIZE-1]))
                self.clear_screen()
                cond1 = False

            # cond2 makes sure the row index is a valid number on the board
            if int(self.row_index_str) > BOARD_SIZE:
                print("Number not on board! Try a number from 1 to {}!"
                      .format(BOARD_SIZE))
                self.clear_screen()
                cond2 = False
            else:
                self.row_index = int(self.row_index_str) - 1
                cond2 = True

            # Given ship length cond3 makes sure the ship can fit on the board
            if self.h_yes_or_no.lower() == 'y':
                if self.col_index + self.length > BOARD_SIZE:
                    print("Your ship doesn't fit on the board,"
                          "try again with a new location or new coordinate")
                    self.clear_screen()
                    cond3 = False
                else:
                    cond3 = True

            elif self.h_yes_or_no.lower() == 'n':
                if self.row_index + self.length > BOARD_SIZE:
                    print("Your ship doesn't fit on the board,"
                          "try again with a new location or new coordinate")
                    self.clear_screen()
                    cond3 = False
                else:
                    cond3 = True

            # cond4 makes sure there is on overlap and
            # if all 4 conditions are met then the board apprend the ship
            if cond1 is True and cond2 is True and cond3 is True:
                for i in range(self.length):
                    if self.h_yes_or_no.lower() == 'n':
                        if (board[self.row_index + i][self.col_index] == V_SHIP or
                                board[self.row_index + i][self.col_index] == H_SHIP):

                            print("Your placement of {} is overlapping with"
                                  "another ship.".format(self.ship))
                            self.clear_screen()
                            cond4 = False
                            break
                        else:
                            cond4 = True
                            if (self.length - 1) - i == 0:
                                if self.h_yes_or_no.lower() == 'n':
                                    for i in range(self.length):
                                        board[self.row_index + i][self.col_index] = V_SHIP
                                        location.append([self.row_index + i, self.col_index])
                                location_dict[self.ship] = location

                    if self.h_yes_or_no.lower() == 'y':
                        if (board[self.row_index][self.col_index + i] == H_SHIP or
                                board[self.row_index][self.col_index + i] == V_SHIP):
                            print("Your placement of {} is overlapping"
                                  "with another ship.".format(self.ship))
                            self.clear_screen()
                            cond4 = False
                            break
                        else:
                            cond4 = True
                            if (self.length - 1) - i == 0:
                                if self.h_yes_or_no.lower() == 'y':
                                    for i in range(self.length):
                                        board[self.row_index][self.col_index + i] = H_SHIP
                                        location.append([self.row_index + i, self.col_index])
                                location_dict[self.ship] = location
            self.print_board(board)
