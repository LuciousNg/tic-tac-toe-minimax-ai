import math

def minimax(state, player):
    max_player = 'O'
    other_player = 'O' if player == 'X' else 'X'

    if state.current_winner == other_player:
        if other_player == max_player:
            return {'position': None, 'score': 1}
        else:
            return {'position': None, 'score': -1}
    elif not state.available_moves():
        return {'position': None, 'score': 0}

    if player == max_player:
        best = {'position': None, 'score': -math.inf}
    else:
        best = {'position': None, 'score': math.inf}

    for possible_move in state.available_moves():
        state.make_move(possible_move, player)

        simulated_score = minimax(state, other_player)

        state.state[possible_move] = ' '
        state.current_winner = None
        simulated_score['position'] = possible_move

        if player == max_player:
            if simulated_score['score'] > best['score']:
                best = simulated_score
        else:
            if simulated_score['score'] < best['score']:
                best = simulated_score

    return best