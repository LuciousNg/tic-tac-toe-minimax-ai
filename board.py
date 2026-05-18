class Board:
    def __init__(self):
        self.state = [" " for _ in range(9)]
        self.current_winner = None
    
    def print_board(self):
        for i in range(3):
            rows = self.state[i*3 : (i+1)*3]
            print("| "+ " | ".join(rows) + " |")
    
    def available_moves(self):
        moves = []
        for i, spot in enumerate(self.state):
            if spot == " ":
                moves.append(i)
        return moves
    
    def winner(self, square, letter):
        row_ind = square // 3
        row = self.state[row_ind*3 : (row_ind + 1) * 3]
        if all([spot == letter for spot in row]):
            return True

        col_ind = square % 3
        column = [self.state[col_ind+i*3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True

        if square % 2 == 0:
            diagonal1 = [self.state[i] for i in [0, 4, 8]]
            if all([spot == letter for spot in diagonal1]):
                return True
            diagonal2 = [self.state[i] for i in [2, 4, 6]]
            if all([spot == letter for spot in diagonal2]):
                return True

        return False

    def make_move(self, square, letter):
        if self.state[square] == " ":
            self.state[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False