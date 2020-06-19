# Created 17/06/20


class Game:
    def __init__(self, player_symbol, grid_size):
        self.GRID_SIZE = grid_size
        self.player_symbol = player_symbol
        self.computer_symbol = "X" if player_symbol == "O" else "O"

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
                if self.winning_move():
                    pass
                elif self.block_move():
                    pass
                else:  # Make the optimal move
                    self.optimal_move()

                self.playerTurn = not self.playerTurn

            self.squaresRemaining -= 1
            for row in self.board:
                print(row)
            self.won = self.check()  # False, "O" or "X"
            print()
        if self.won:
            print(f"{self.won} won the game!")
        else:
            print("It's a tie!")

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

    def winning_move(self):
        # Find a winning move in any row, if any
        for row_num, row in enumerate(self.board):
            if row.count(self.computer_symbol) == self.GRID_SIZE-1:
                q = next((index for index, value in enumerate(row) if value == "-"), None)
                if q:
                    self.board[row_num][q] = self.computer_symbol
                    return True

        # Find a winning move in any column, if any
        for i in range(self.GRID_SIZE):  # for each column number
            cols = [row[i] for row in self.board]
            if cols.count(self.computer_symbol) == self.GRID_SIZE-1:
                q = next((index for index, value in enumerate(cols) if value == "-"), None)
                if q:
                    self.board[q][i] = self.computer_symbol
                    return True

        # Find a winning move in diag from top left to bottom right, if any
        tl_br_diags = [self.board[i][i] for i in range(self.GRID_SIZE)]
        if tl_br_diags.count(self.computer_symbol) == self.GRID_SIZE-1:
            q = next((index for index, value in enumerate(tl_br_diags) if value == "-"), None)
            if q:
                self.board[q][q] = self.computer_symbol
                return True

        # Find a winning move in diag from bottom left to top right, if any
        bl_tr_diags = [self.board[self.GRID_SIZE - i - 1][i] for i in range(self.GRID_SIZE)]
        if bl_tr_diags.count(self.computer_symbol) == self.GRID_SIZE-1:
            q = next((index for index, value in enumerate(bl_tr_diags) if value == "-"), None)
            if q:
                self.board[self.GRID_SIZE-1-q][q] = self.computer_symbol
                return True

        return False

    def block_move(self):
        # Block the player's winning move in any row, if any
        for row_num, row in enumerate(self.board):
            if row.count(self.player_symbol) == self.GRID_SIZE-1:
                q = next((index for index, value in enumerate(row) if value == "-"), None)
                if q:
                    self.board[row_num][q] = self.computer_symbol
                    return True

        # Block the player's winning move in any col, if any
        for i in range(self.GRID_SIZE):  # for each column number
            cols = [row[i] for row in self.board]
            if cols.count(self.player_symbol) == self.GRID_SIZE-1:
                q = next((index for index, value in enumerate(cols) if value == "-"), None)
                if q:
                    self.board[q][i] = self.computer_symbol
                    return True

        # Block the player's winning move in top-left to bottom-right diag, if any
        tl_br_diags = [self.board[i][i] for i in range(self.GRID_SIZE)]
        if tl_br_diags.count(self.player_symbol) == self.GRID_SIZE-1:
            q = next((index for index, value in enumerate(tl_br_diags) if value == "-"), None)
            if q:
                self.board[q][q] = self.computer_symbol
                return True

        # Block the player's winning move in bottom-left to top-right diag, if any
        bl_tr_diags = [self.board[self.GRID_SIZE - i - 1][i] for i in range(self.GRID_SIZE)]
        if bl_tr_diags.count(self.player_symbol) == self.GRID_SIZE-1:
            q = next((index for index, value in enumerate(bl_tr_diags) if value == "-"), None)
            if q:
                self.board[self.GRID_SIZE-1-q][q] = self.computer_symbol
                return True

        return False

    def optimal_move(self):
        # if GRID_SIZE is odd, then there is a centre square
        if self.GRID_SIZE % 2 == 1 and self.board[self.GRID_SIZE//2][self.GRID_SIZE//2] == "-":
            self.board[self.GRID_SIZE//2][self.GRID_SIZE//2] = self.computer_symbol

        # If any of the corner squares are available, play it
        elif self.board[0][0] == "-":  # TOP LEFT
            self.board[0][0] = self.computer_symbol
        elif self.board[0][self.GRID_SIZE-1] == "-":  # TOP RIGHT
            self.board[0][self.GRID_SIZE-1] = self.computer_symbol
        elif self.board[self.GRID_SIZE-1][0] == "-":  # BOTTOM LEFT
            self.board[self.GRID_SIZE-1][0] = self.computer_symbol
        elif self.board[self.GRID_SIZE-1][self.GRID_SIZE-1] == "-":  # BOTTOM RIGHT
            self.board[self.GRID_SIZE-1][self.GRID_SIZE-1] = self.computer_symbol

        else:
            for row_num in range(self.GRID_SIZE):
                for col_num in range(self.GRID_SIZE):
                    if self.board[row_num][col_num] == "-":
                        self.board[row_num][col_num] = self.computer_symbol
                        break  # Needs to break out of both for loops
                else:
                    continue
                break


g = Game("X", 4)
g.play()
