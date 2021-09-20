# Author: Prasanna Thapa
# Date : 8/4/2021
# Description: add description here
# "DETAILED TEXT DESCRIPTIONS OF HOW TO HANDLE THE SCENARIOS"

class QuoridorGame:
    """Game Engine for the Quoridor Game. Contains the private __init__ method which contains the quoridor board
     and keeps track of which player's turn it is. Also contains the methods
    method board_printer which gives a string representation of the board,
    _check_fence: private method that checks if there is a fence between two adjacent squares supplied as parameters
    place_fence: which places a fence in the board specified as vertical or horizontal
    _get_current_pawn_position is a private method that returns a tuple with  a current pawn position
    _legal_move is a private method that checks if the supplied move is legal
    move_pawn checks that the move is legal and it is the player's turn. It then changes the board appropriately
    is_winner checks that the player is at the end of the board and declares that player as the winner in that condition.
    Instantiates classes Pawn and Player to create an instance of two Pawns and two Players"""

    def __init__(self):
        """Contains the Quoridor board with two pieces. The board is a 3d list, with rows as the first dimension,
        columns as the second dimension and the vertical fence, horizontal fence and pawn as the third dimension.
        Also contains: a list of players, where Player object is specified by integers,
        current player and current pawn position for each player. Uses class Pawn and Player to initialise players and
        pawns"""
        self._players = [Player(1), Player(2)]
        self._current_player = self._players[0]
        self._player1_position = (4, 0)
        self._player2_position = (4, 8)
        self._board = [[['vedge', 'hedge', 'no_pawn' ], [ 'vedge', "no_fence", 'no_pawn' ], [ 'vedge', "no_fence", 'no_pawn' ],
                        ['vedge', "no_fence", 'no_pawn'], ['vedge', "no_fence", 'no_pawn'], ['vedge', "no_fence", 'no_pawn'],
                        ['vedge', "no_fence", 'no_pawn'], ['vedge', "no_fence", 'no_pawn'], ['vedge', "no_fence", 'no_pawn'] ],
                       [["no_fence","hedge", 'no_pawn'], ['no_fence', "no_fence", 'no_pawn'], ['no_fence', "no_fence", 'no_pawn'],
                       ['no_fence', "no_fence", 'no_pawn'], ['no_fence', "no_fence", 'no_pawn'], ['no_fence', "no_fence", 'no_pawn'],
                       ['no_fence',  "no_fence", 'no_pawn'], ['no_fence', "no_fence", 'no_pawn'], [ "no_fence", "no_fence", 'no_pawn']],
                       [["no_fence","hedge", 'no_pawn'], ['no_fence', "no_fence", 'no_pawn'], ['no_fence', "no_fence", 'no_pawn'],
                       ['no_fence', "no_fence", 'no_pawn'], ['no_fence', "no_fence", 'no_pawn'], ['no_fence', "no_fence", 'no_pawn'],
                       ['no_fence',  "no_fence", 'no_pawn'], ['no_fence', "no_fence", 'no_pawn'], [ "no_fence", "no_fence", 'no_pawn']],
                       [["no_fence","hedge", 'no_pawn'], ['no_fence', "no_fence", 'no_pawn'], ['no_fence', "no_fence", 'no_pawn'],
                       ['no_fence', "no_fence", 'no_pawn'], ['no_fence', "no_fence", 'no_pawn'], ['no_fence', "no_fence", 'no_pawn'],
                       ['no_fence',  "no_fence", 'no_pawn'], ['no_fence', "no_fence", 'no_pawn'], [ "no_fence", "no_fence", 'no_pawn']],
                       [["no_fence","hedge", Pawn(self._players[0])], [ 'no_fence', "no_fence", 'no_pawn'], ['no_fence', "no_fence", 'no_pawn' ],
                        ['no_fence', "no_fence", 'no_pawn'], ['no_fence', "no_fence", 'no_pawn'], ['no_fence', "no_fence", 'no_pawn'],
                        ['no_fence',  "no_fence", 'no_pawn'], ['no_fence', "no_fence", 'no_pawn'], [ "no_fence", "no_fence", Pawn(self._players[1 ]) ] ],
                        [[ "no_fence","hedge", 'no_pawn'], ['no_fence', "no_fence", 'no_pawn'], ['no_fence', "no_fence", 'no_pawn'],
                       ['no_fence', "no_fence", 'no_pawn'], ['no_fence', "no_fence", 'no_pawn'], ['no_fence', "no_fence", 'no_pawn'],
                       ['no_fence',  "no_fence", 'no_pawn'], ['no_fence', "no_fence", 'no_pawn'], [ "no_fence", "no_fence", 'no_pawn']],
                        [[ "no_fence","hedge", 'no_pawn'], ['no_fence', "no_fence", 'no_pawn'], ['no_fence', "no_fence", 'no_pawn'],
                       ['no_fence', "no_fence", 'no_pawn'], ['no_fence', "no_fence", 'no_pawn'], ['no_fence', "no_fence", 'no_pawn'],
                       ['no_fence',  "no_fence", 'no_pawn'], ['no_fence', "no_fence", 'no_pawn'], [ "no_fence", "no_fence", 'no_pawn']],
                        [[ "no_fence","hedge", 'no_pawn'], ['no_fence', "no_fence", 'no_pawn'], ['no_fence', "no_fence", 'no_pawn'],
                       ['no_fence', "no_fence", 'no_pawn'], ['no_fence', "no_fence", 'no_pawn'], ['no_fence', "no_fence", 'no_pawn'],
                       ['no_fence',  "no_fence", 'no_pawn'], ['no_fence', "no_fence", 'no_pawn'], [ "no_fence", "no_fence", 'no_pawn']],
                        [[ "no_fence","hedge", 'no_pawn'], ['no_fence', "no_fence", 'no_pawn'], ['no_fence', "no_fence", 'no_pawn'],
                       ['no_fence', "no_fence", 'no_pawn'], ['no_fence', "no_fence", 'no_pawn'], ['no_fence', "no_fence", 'no_pawn'],
                       ['no_fence',  "no_fence", 'no_pawn'], ['no_fence', "no_fence", 'no_pawn'], [ "no_fence", "no_fence", 'no_pawn']],
                        [[ "no_fence", "hedge", 'no_pawn'], ['no_fence', "no_fence", 'no_pawn'], ['no_fence', "no_fence", 'no_pawn'],
                       ['no_fence', "no_fence", 'no_pawn'], ['no_fence', "no_fence", 'no_pawn'], ['no_fence', "no_fence", 'no_pawn'],
                       ['no_fence',  "no_fence", 'no_pawn'], ['no_fence', "no_fence", 'no_pawn'], [ "no_fence", "no_fence", 'no_pawn']] ]

    def _get_board_item(self, input_tuple):
        """::parameter tuple provides the coordianate of the board
        ::returns the list at that co-ordinate"""
        return self._board[input_tuple[0 ] ][input_tuple[1 ] ]

    def _get_current_player(self):
        """
        :return: Current player in data member
        """
        return self._current_player

    def board_printer(self):
        """Print method for the board
        :returns: None"""
        current_line = ""
        for i in range(9):
            for j in range(9):
                for k in range(3):
                    if self._board[j][i][k] == "hfence":
                        current_line += "--"
                    elif self._board[j][i][k] == 'vfence':
                        current_line += "|"
                    if self._board[j][i][k] == "no_pawn":
                        current_line += "O"
                    elif isinstance(self._board[j ][i][k], Pawn):
                        current_line += str(self._board[j][i][k].pawn)[0 ]

            current_line += "\n"
        print(current_line)

    def _check_fence(self, position_a, position_b):
        """given two adjacent positions on the board, returns True if there is a fence between two positions, false
        otherwise
        ::parameter:: position_a is the starting position of the pawn
        ::parameter postion_b is the ending position of the pawn.
        ::returns:: True if there is a fence between the two parameters, False otherwise"""
        if position_a[0] == position_b[0]:
            # in the same column, check for horizontal fence between
            if position_b[1] > position_a[1]:
                # check position b's horizontal fence
                return self._board[position_b[0 ] ][position_b[1 ] ][1 ] == "hfence"
            elif position_a[1] > position_b[1]:
                # check position a's horizontal fence
                return self._board[position_a[0 ] ][position_a[1 ] ][1 ] == "hfence"
        elif position_a[1] == position_b[1]:
            # in the same row check for vertical fence between
            if position_b[0] > position_a[0]:
                # check position b's vertical fence
                return self._board[position_b[0 ] ][position_b[1 ] ][0 ] == "vfence"
            elif position_a[0] > position_b[0]:
                # check position a's horizontal fence
                return self._board[position_a[0 ] ][position_a[1 ] ][0 ] == "vfence"
        # raise exception that no fence can be checked unless adjacent

    def place_fence(self, player, orientation, input_tuple):
        """Method to place a fence in the board if within the rules of the game.
        ::parameter player: 1 or 2 depending on the player
        ::parameter orientation: v or h which is a string to declare the orientation of the fence
        ::parameter tuple: tuple indicating co-ordinate to place the fence in.
        The method checks if it is :param player turn. Otherwise prints appropriate message.
        Then it ascertains the player still has a fence remaining. If not, it print appropriate message
        Then it ascertains the position indicated is not the edge or that there isn't a fence already in that position.
        If all these conditions are met, it places a fence indicated by the tuple and the orientation,
        and decreases the fence available and changes player turn
        :returns True if fence placed, false otherwise"""
        # check if game has been won by either player
        if self.is_winner(1):
            return False
        elif self.is_winner(2):
            return False

        list_index = int
        if orientation == "h":
            list_index = 1
        elif orientation == "v":
            list_index = 0
        attempted_placement = self._board[input_tuple[0 ] ][input_tuple[1 ] ][list_index ]

        # select the given player
        given_player = self._players[ player - 1 ]

        if self._current_player is given_player:

            # check they have fence remaining. If none remaining, return True
            if self._current_player.get_fence() > 0:
                if attempted_placement == "no_fence":
                    self._board[input_tuple[0 ] ][input_tuple[1 ] ][list_index ] = orientation + "fence"

                    # update the fence count
                    self._current_player.fence_placed()

                    # update the current player
                    if player == 1:
                        self._current_player = self._players[1 ]
                    elif player == 2:
                        self._current_player = self._players[0 ]
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False

    def _get_current_pawn_position(self, player):
        """
        Description: private method that returns the tuple of a player's pawn.
        :param player: Players whose current pawn position is needed
        :return: current pawn position data member
        """
        if player == 1:
            return self._player1_position
        else:
            return self._player2_position

    def _update_pawn_position(self, player, new_position):
        """
        Description: private method that updates data for current pawn position
        :param player: Given player whose position is to be updated
        :param new_position: Player's new pawn positio
        :return: None
        """
        if player == 1:
            self._player1_position = new_position
        elif player == 2:
            self._player2_position = new_position

    def _legal_move(self, initial_square, final_square):
        """private method that ascertains if a move is legal. Three methods of ascertaining legality of a move is listed
        below
        :parameter initial_square: starting position of the pawn
        :parameter:: final_square  is the position to place the pawn
        :returns:: true if a legal move, False otherwise"""
        # if the difference between the initial and the final position is 1 in either X-cordinate(column) or Y-cordiante(row)
        # then a) check between two positions that there is no fence (using check fence method), and b)At final position,
        # there is no pawn. If both a and b is met, method returns True for legal move
        if abs(initial_square[0] - final_square[0]) == 1 or abs(initial_square[1] - final_square[1]) == 1:

            # a) check there is no fence between the two squares
            if self._check_fence(initial_square, final_square) is False:

                # b) check that the final square has no pawn
                if isinstance(self._get_board_item(final_square)[2], Pawn) is False:
                    return True

        # if the move is two positions in either X or Y cordinate then a) check that the square between the inital and final
        # position contains a paw. b) check twice (first between initial and middle squares, then middle and final) that
        # there are no fences or edges in between.  If both a and b is met, method return True for legal move
        if abs(initial_square[0] - final_square[0]) == 2:

            middle_square = (initial_square[0]+1, initial_square[1])

            # no fence between initial and middle square
            if self._check_fence(initial_square, middle_square) is False:

                # pawn in middle square
                if isinstance(self._get_board_item(middle_square)[2], Pawn):

                    # no fence between pawn and final square:
                    if self._check_fence(middle_square, final_square) is False:
                        # this is a legal leap
                        return True

        if abs(initial_square[1] - final_square[1]) == 2:
            middle_square = (initial_square[0], initial_square[1]+1)
            # no fence between initial and middle square
            if self._check_fence(initial_square, middle_square) is False:

                # pawn in middle square
                if isinstance(self._get_board_item(middle_square)[2], Pawn):

                    # no fence between pawn and final square:
                    if self._check_fence(middle_square, final_square) is False:
                        print("no blocking fence again")
                        # this is a legal leap
                        return True

        # if the |difference in X| = |difference in Y|, then the move is diagonal. If final X and final Y are greater, then the move
        # right and down. If both are smaller, then the move is left and up. If X is greater but Y is smaller, then the move is
        # left and up. IF X is smaller and Y is greater then the move is right and down.
        # for each move, check that in the two directions the adjacent square has a pawn. If there is a pawn, check there is a
        # fence associated with that co-ordinate. If this is the case, then the move is legal and method should return True
        # for the legal move.
        if abs(initial_square[0] - final_square[0]) == abs(initial_square[1] - final_square[1]):
            # if both final X & Y are greater, move is right and down. Check for right or down conditions
            if final_square[0] > initial_square[0] and final_square[1] > initial_square[1]:
                if self._check_right_diagonal(initial_square, final_square) or self._check_lower_diagonal(initial_square, final_square):
                    return True

            # if both final X&Y are smaller, move is left and up. Check for left and up.
            elif final_square[0] < initial_square[0] and final_square[1] < initial_square[1]:
                if self._check_upper_diagonal(initial_square, final_square) or self._check_left_diagonal(initial_square, final_square):
                    return True

            # if X is greater and Y is smaller, the move is up and right. Check up and right diagonal moves
            elif final_square[0] > initial_square[0] and final_square[1] < initial_square[1]:
                if self._check_right_diagonal(initial_square, final_square) or self._check_upper_diagonal(initial_square, final_square):
                    return True

            # if X is smaller but Y is greater, then the move is down and left
            elif final_square[0] < initial_square[0] and final_square[1] > initial_square[1]:
                if self._check_left_diagonal(initial_square, final_square) or self._check_lower_diagonal(initial_square,final_square):
                    return True

        # any other move is illegal. Return False in that case
        return False

    def _check_right_diagonal(self, initial_square, final_square):
        """helper method to check if the square to the right of a given square meets the condition for a diagonal move
        ::parameter initial_square: given square
        :returns True if conditions for diagonal move is met"""
        square_to_right = (initial_square[0] + 1, initial_square[1])

        # check of square to right contains pawn
        if isinstance(self._get_board_item(square_to_right)[2], Pawn):

            # check no fence between initial square and square to right
            if self._check_fence(initial_square, square_to_right) is False:

                # check if at the right edge of the board or else there is a fence behind the square
                if square_to_right[0] == 8:

                    # check there is no fence between this square and the diagonal sqquare
                    if self._check_fence(square_to_right, final_square) is False:
                        return True

                # else part:
                elif self._check_fence(square_to_right, (square_to_right[0 ] + 1, square_to_right[1 ])):

                    # check there is no fence between this square and the diagonal square
                    if self._check_fence(square_to_right, final_square) is False:
                        return True
        return False

    def _check_lower_diagonal(self, initial_square, final_square):
        """helper method to check if the diagonal move is valid through pawn placed at a square below
        :parameter initial_square: square where the pawn whch is being moved currently resides
        :param final_square: square to move to
        :returns True if conditions for diagonal move is met"""
        square_below = (initial_square[0], initial_square[1] + 1)
        # check if square below contains pawn
        if isinstance(self._get_board_item(square_below)[2], Pawn):

            # check no fence between initial sqyare and the square below:
            if self._check_fence(initial_square, square_below) is False:
                # check if square below is at the bottom of the board, or else there is a fence below it
                if square_below[1] == 8:

                    # check there is no fence between the square nelow and the diagonal square
                    if self._check_fence(square_below, final_square) is False:
                        return True

                # else part:
                elif self._check_fence(square_below, (square_below[0 ], square_below[1 ] + 1)):

                    # check there is no fence between this square and the diagonal square
                    if self._check_fence(square_below, final_square) is False:
                        return True
        return False

    def _check_upper_diagonal(self, initial_square, final_square):
        """helper method to check if the diagonal move is valid through pawn placed at a square above
        :parameter initial_square: square where the pawn whch is being moved currently resides
        :param final_square: square to move to
        :returns True if conditions for diagonal move is met"""
        square_above = (initial_square[0], initial_square[1] - 1)
        # check if square above contains pawn
        if isinstance(self._get_board_item(square_above)[2], Pawn):

            # check no fence between initial sqyare and the square above:
            if self._check_fence(initial_square, square_above) is False:

                # check if square above is at the top of the board, or else there is a fence below it
                if square_above[1] == 0:

                    # check there is no fence between the square above and the diagonal square
                    if self._check_fence(square_above, final_square) is False:
                        return True

                # else part:
                elif self._check_fence(square_above, (square_above[0 ], square_above[1 ] - 1)):

                    # check there is no fence between this square and the diagonal square
                    if self._check_fence(square_above, final_square) is False:
                        return True
        return False

    def _check_left_diagonal(self, initial_square, final_square):
        """helper method to check if the square to the left of a given square meets the condition for a diagonal move
        ::parameter initial_square: square at which the pawn being moved is
        :parameter final_square: diagonal square to which teh pawn wants to move
        :returns True if conditions for diagonal move is met"""
        square_to_left = (initial_square[0] - 1, initial_square[1])

        # check of square to left contains pawn
        if isinstance(self._get_board_item(square_to_left)[2], Pawn):

            # check no fence between initial square and square to right
            if self._check_fence(initial_square, square_to_left) is False:

                # check if at the left edge of the board or else there is a fence ahead the square
                if square_to_left[0] == 0:

                    # check there is no fence between this square and the diagonal sqquare
                    if self._check_fence(square_to_left, final_square) is False:
                        return True

                # else part:
                elif self._check_fence(square_to_left, (square_to_left[0 ] - 1, square_to_left[1 ])):

                    # check there is no fence between this square and the diagonal square
                    if self._check_fence(square_to_left, final_square) is False:
                        return True
        return False

    def move_pawn(self, given_player, move_to):
        """
        Method to move pawn for legal moves and change player turn. Move is legal as described in ReadMe.
        :param given_player: int 1 or 2 to indicate player
        :param move_to: tuple indicating coordinate to move the pawn to
        :return: True if pawn moved or False otherwise
        """
        if self.is_winner(1):
            return False
        elif self.is_winner(2):
            return False

        player = self._players[ given_player - 1 ]
        initial_pawn_square = self._get_current_pawn_position(given_player)
        final_pawn_square = move_to

        # if player is the current player, then move proceeds. Otherwise return False
        if self._current_player == player:

            # if legal move, change the position of the Pawn from initial_square to final_square and return True
            if self._legal_move(initial_pawn_square, final_pawn_square):
                self._board[final_pawn_square[0 ] ][final_pawn_square[1 ] ][2 ] = Pawn(self._players[ given_player - 1 ])
                self._update_pawn_position(given_player, final_pawn_square)
                self._board[initial_pawn_square[0 ] ][initial_pawn_square[1 ] ][2 ] = "no_pawn"

                # update the current player turn
                if given_player == 1:
                    self._current_player = self._players[1 ]
                elif given_player == 2:
                    self._current_player = self._players[0 ]
                return True
            else:
                return False
        else:
            return False

    def is_winner(self, player):
        """if first player, get_current_pawn_position. If pawn is at Y-coordinate 8, return True
        IF second player, ger their pawn. IF pawn is at Y-coordinate 0, return True.
        Otherwise print appropriate message
        :parameter player: int 1 or 2 to indicate player
        :returns: False if Player has not won, True otherwise"""
        if player == 1:
            current_position = self._get_current_pawn_position(1)
            if current_position[1] == 8:
                return True
            return False

        if player == 2:
            current_position = self._get_current_pawn_position(2)
            if current_position[1] == 0:
                return True
            return False


class Pawn:
    """Pawn class that tracks which pawn is which players
    Contains the method legal_pawn_move that gets two parameters,
    initial pawn position  and final pawn position.
    Added pawn color for later GUI integration."""

    def __init__(self, player):
        """Contains data member player and pawn"""
        self._player = player

        if player.get_player() == "player_1":
            self._pawn = "green_pawn"
        elif player.get_player() == "player_2":
            self._pawn = "yellow_pawn"

    def get_pawn(self):
        """getter method for pawn color
        :returns current pawn color"""
        return self._pawn


class Player:
    """Player class that initialises a player with 10 fences. Added player name for later GUI integration
    Contains methods get_player, get_fence and update_fence that return player, number of remainig fence
    and updates fences respectively."""
    def __init__(self, player):
        """Contains data member player name and fences of the player"""
        self._player = "player_" + str(player)
        self._fence = 10

    def get_player(self):
        """Getter method for player name
        :returns: player name"""
        return self._player

    def get_fence(self):
        """getter method for number of fences remaining
        :returns: fences remaining"""
        return self._fence

    def fence_placed(self):
        """decreases fence by 1 once called"""
        self._fence -= 1
