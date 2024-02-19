import numpy as np
from blockus import blockus_state

class player():
    '''
    Classe représentant un joueur.
    '''
    def __init__(self):
        pass
    
    def play(self, state: blockus_state) -> blockus_state:
        raise NotImplementedError("Please Implement this method")


class player_random(player):
    '''
    Classe représentant un joueur aléatoire.
    '''
    def __init__(self):
        pass
    
    def play(self, state: blockus_state) -> blockus_state:
        next_states = state.next_states()
        next_state = next_states[np.random.randint(len(next_states))]
        return next_state