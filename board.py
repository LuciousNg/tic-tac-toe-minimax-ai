class Board:
    def __init__(self):
        self.state = [" " for _ in range(9)]
    
    def print_board(self):
        for i in range(3):
            rows = self.state[i*3 : (i+1)*3]
            print("| "+ " | ".join(rows) + " |")