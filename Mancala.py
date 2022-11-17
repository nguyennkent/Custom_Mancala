# Author: Kent Nguyen
# GitHub username: nguyennkent
# Date: December 4 2022
# Description:


end_game = [0, 0, 0, 0, 0, 0]

special_rule_p1 = {0: 12, 1: 11, 2: 10, 3: 9, 4: 8, 5: 7}
special_rule_p2 = {12: 0, 11: 1, 10: 2, 9: 3, 8: 4, 7: 5}


class Mancala:
    def __init__(self):
        self._player_list = []
        self._board = [4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4, 0]
        # index 6 and index 13 are player stores
        self._playing = True

    """Successfully takes the player’s name as a string argument and returns the Player object."""

    def create_player(self, name):
        self._player_list.append(Player(name))
        return Player(name)

    """"Takes no parameter and will print the current board information in this READme format"""

    def print_board(self):
        print("player 1:")
        print("store: " + str(self._board[6]))
        print(self._board[0:6])
        print("player 2:")
        print("store: " + str(self._board[13]))
        print(self._board[7:13])

    def play_game(self, player, pit):
        if pit > 6 or pit <= 0:
            return "Invalid number for pit index"

        if not self._playing:
            print("Game is ended")

        while self._playing:
            if player == 1:
                # get seed count for move counts
                seed_count = self._board[pit - 1]
                # set seed hole to 0
                self._board[pit - 1] = 0
                # where to add
                add_count = pit

                while seed_count != 0:
                    if seed_count == 1:
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

                    # ends in store
                    if seed_count == 0 and add_count == 7:
                        print("player 1 take another turn")

                    # start from front again
                    if add_count > 12:
                        add_count = 0

            if player == 2:
                pit += 6
                # get seed count for move counts
                seed_count = self._board[pit]
                # set seed hole to 0
                self._board[pit] = 0
                # where to add
                add_count = pit + 1

                while seed_count != 0:
                    if seed_count == 1:
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

                    # ends in store
                    if seed_count == 0 and add_count == 14:
                        print("player 2 take another turn")

                    # start from front again
                    if add_count > 13:
                        add_count = 0

            if str(self._board[0:6]) == str(end_game) or str(self._board[7:13]) == str(end_game):
                p1_results = 0
                p2_results = 0

                for i in self._board[:7]:
                    p1_results += i
                self._board[6] = p1_results
                self._board[:6] = [0, 0, 0, 0, 0, 0]

                for i in self._board[7:13]:
                    p2_results += i

                self._board[7:12] = [0, 0, 0, 0, 0, 0]
                self._board[13] = p2_results
                self._playing = False

            return self._board

    """Takes no parameter, prints the outcome of the game"""

    def return_winner(self):
        if self._playing:
            return "Game has not ended"
        else:
            p1_store = self._board[6]
            p2_store = self._board[13]

            if p1_store == p2_store:
                print("It's a tie")
            if p1_store > p2_store:
                print("Winner is player 1: " + self._player_list[0].get_name())
            if p2_store > p1_store:
                print("Winner is player 2: " + self._player_list[1].get_name())


class Player:
    def __init__(self, name):
        self._name = name

    def get_name(self):
        return self._name


game = Mancala()
player1 = game.create_player("Lily")
player2 = game.create_player("Lucy")
print("turn 1" + str(game.play_game(1, 1)))
print("turn 2" + str(game.play_game(1, 2)))
print("turn 3" + str(game.play_game(1, 3)))
print("turn 4" + str(game.play_game(1, 4)))
print("turn 5" + str(game.play_game(1, 5)))
print("turn 6" + str(game.play_game(1, 6)))
game.print_board()
game.return_winner()

# game = Mancala()
# player1 = game.create_player("Lily")
# player2 = game.create_player("Lucy")
# print("turn 1" + str(game.play_game(1, 3)))
# print("turn 2" + str(game.play_game(1, 1)))
# print("turn 3" + str(game.play_game(2, 3)))
# print("turn 4" + str(game.play_game(2, 4)))
# print("turn 5" + str(game.play_game(1, 2)))
# print("turn 6" + str(game.play_game(2, 2)))
# print("turn 7" + str(game.play_game(1, 1)))
# game.print_board()
# print(game.return_winner())
