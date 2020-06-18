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
            self.won = self.check()  # False, "O" or "X"
        print(f"{self.won} won the game!")

    def check(self):
        # Check for horizontal row
        for row in self.board:
            if row[0] != "-" and all(coordinate == row[0] for coordinate in row):
                return row[0]  # return "O" or "X"

        # Check for vertical column
        for i in range(self.GRID_SIZE):  # for each column number
            cols = [row[i] for row in self.board]
            if cols[0] != "-" and all(coordinate == cols[0] for coordinate in cols):
                return cols[0]  # return "O" or "X"

        # check from top left to bottom right diagonal
        if self.board[0][0] != "-" and all(self.board[i][i] == self.board[0][0] for i in range(self.GRID_SIZE)):
            return self.board[0][0]  # return "O" or "X"

        # check from bottom left to top right diagonal
        if(self.board[self.GRID_SIZE-1][0] != "-" and
                all(self.board[self.GRID_SIZE-i-1][i] == self.board[self.GRID_SIZE-1][0] for i in range(self.GRID_SIZE))):
            return self.board[self.GRID_SIZE-1][0]  # return "O" or "X"

        # Otherwise, nobody has won yet
        return False


g = Game("O", 3)
g.play()
