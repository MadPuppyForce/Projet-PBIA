import numpy as np
from blockus import blockus_state

class player():
    '''
    Classe représentant un joueur.
    '''
    def __init__(self):
        pass
    
    def play(self, state: blockus_state) -> int:
        raise NotImplementedError("Please Implement this method")


class player_random(player):
    '''
    Classe représentant un joueur aléatoire.
    '''
    def __init__(self):
        pass
    
    def play(self, state: blockus_state) -> int:
        next_states = state.next_states()
        ind_coup = np.random.randint(len(next_states))
        return ind_coup