# Author: Kent Nguyen
# GitHub username: nguyennkent
# Date: December 4 2022
# Description: Custom implementation of a Mancala game with two special rules

end_game = [0, 0, 0, 0, 0, 0]
special_rule_p1 = {0: 12, 1: 11, 2: 10, 3: 9, 4: 8, 5: 7}
special_rule_p2 = {12: 0, 11: 1, 10: 2, 9: 3, 8: 4, 7: 5}

class Mancala:
    """Mancala class to represent Mancala game"""

    def __init__(self):
        self._player_list = []
        self._board = [4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4, 0]
        # index 6 and index 13 are player stores
        self._playing = True

    def create_player(self, name):
        """Creates a player with given name"""
        self._player_list.append(Player(name))
        return Player(name)

    def print_board(self):
        """"Takes no parameter and will print the current board information in READme format"""
        print("player 1:")
        print("store: " + str(self._board[6]))
        print(self._board[0:6])
        print("player 2:")
        print("store: " + str(self._board[13]))
        print(self._board[7:13])

    def play_game(self, player, pit):
        """Make indicated move based on player and pit index"""
        if pit > 6 or pit <= 0:
            return "Invalid number for pit index"

        if not self._playing:
            return "Game is ended"

        while self._playing:
            if player == 1:
                seed_count = self._board[pit - 1]  # Get seed count for move counts
                self._board[pit - 1] = 0  # Set seed hole to 0
                add_count = pit  # Where to add next seed

                while seed_count != 0:
                    if seed_count == 1:  # Special Rule Condition
                        if self._board[add_count] == 0:
                            if add_count in range(0, 6):
                                index_rule = special_rule_p1.get(add_count)
                                add_seeds = self._board[index_rule] + 1
                                self._board[index_rule] = 0
                                self._board[6] += add_seeds
                                self._board[add_count] = 0
                                break

                    self._board[add_count] += 1
                    add_count += 1
                    seed_count -= 1

                    if seed_count == 0 and add_count == 7:  # End in store case
                        print("player 1 take another turn")

                    if add_count > 12:  # Start from front again
                        add_count = 0

            if player == 2:
                pit += 6
                seed_count = self._board[pit]  # Get seed count for move counts
                self._board[pit] = 0  # Set seed hole to 0
                add_count = pit + 1  # Where to add next seed

                while seed_count != 0:
                    if seed_count == 1:  # Special Rule Condition
                        if self._board[add_count] == 0:
                            if add_count in range(7, 13):
                                index_rule = special_rule_p2.get(add_count)
                                add_seeds = self._board[index_rule] + 1
                                self._board[index_rule] = 0
                                self._board[13] += add_seeds
                                self._board[add_count] = 0
                                break

                    self._board[add_count] += 1
                    add_count += 1
                    seed_count -= 1

                    if seed_count == 0 and add_count == 14:  # End in store case
                        print("player 2 take another turn")

                    if add_count > 13:  # Start from front again
                        add_count = 0

            if str(self._board[0:6]) == str(end_game) or str(self._board[7:13]) == str(end_game):  # Game ends
                p1_results = 0
                p2_results = 0

                for i in self._board[:7]:  # Sum player 1 board for score
                    p1_results += i
                self._board[6] = p1_results
                self._board[:6] = [0, 0, 0, 0, 0, 0]

                for i in self._board[7:13]:  # Sum player 2 board for score
                    p2_results += i

                self._board[7:12] = [0, 0, 0, 0, 0, 0]
                self._board[13] = p2_results
                self._playing = False

            return self._board[:14]

    def return_winner(self):
        """Prints outcome of the game"""
        if self._playing:
            return "Game has not ended"
        else:
            p1_store = self._board[6]
            p2_store = self._board[13]

            if p1_store == p2_store:
                return "It's a tie"
            if p1_store > p2_store:
                return "Winner is player 1: " + self._player_list[0].get_name()
            if p2_store > p1_store:
                return "Winner is player 2: " + self._player_list[1].get_name()


class Player:
    """Player class to represent Player object inside Mancala game"""
    def __init__(self, name):
        self._name = name

    def get_name(self):
        """Get method for Player name"""
        return self._name
