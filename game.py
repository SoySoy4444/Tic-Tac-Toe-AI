# Created 17/06/20


class Game:
    def __init__(self, player_symbol, grid_size):
        self.GRID_SIZE = grid_size
        self.player_symbol = player_symbol

        self.board = [["-" for _ in range(self.GRID_SIZE)] for _ in range(self.GRID_SIZE)]
        self.playerTurn = True if player_symbol == "O" else False

        self.squaresRemaining = self.GRID_SIZE ** 2
        self.won = False

    def play(self):
        while self.squaresRemaining > 0 and not self.won:
            if self.playerTurn:
                print("It's your turn!")
                while True:
                    coordinate = input("Enter your square: ")
                    if (coordinate.isdigit() and len(coordinate) == 2 and
                            int(coordinate[0]) < self.GRID_SIZE and int(coordinate[1]) < self.GRID_SIZE and
                            self.board[int(coordinate[0])][int(coordinate[1])] == "-"):
                        break
                    print("Try again!")

                self.board[int(coordinate[0])][int(coordinate[1])] = self.player_symbol
                self.playerTurn = not self.playerTurn
            else:
                print("Computer turn")
                self.playerTurn = not self.playerTurn

            self.squaresRemaining -= 1
            for row in self.board:
                print(row)


g = Game("O", 3)
g.play()
