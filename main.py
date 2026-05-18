from board import Board
from player import HumanPlayer, UnbeatableAI

def play(game, x_player, o_player):
    game.print_board()
    print("\n")
    
    letter = 'X'
    
    while game.available_moves():
        if letter == 'O':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)

        if game.make_move(square, letter):
            print(f"Player {letter} play {square}")
            game.print_board()
            print("\n")

            if game.current_winner:
                print(f"Game over. {letter} win!")
                return letter

            letter = 'O' if letter == 'X' else 'X'

    print("Game over. Draw!")

if __name__ == '__main__':
    print("Tic-Tac-Toe game starting...\n")
    
    x_player = HumanPlayer('X')
    o_player = UnbeatableAI('O')
    t = Board()
    
    play(t, x_player, o_player)