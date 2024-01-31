import numpy as np
from game import Blockus_state

class Player():
    '''
    Classe représentant un joueur.
    '''
    def __init__(self):
        pass
    
    def play(self, state: Blockus_state) -> int:
        raise NotImplementedError("Please Implement this method")


class Player_Random(Player):
    '''
    Classe représentant un joueur aléatoire.
    '''
    def __init__(self):
        pass
    
    def play(self, state: Blockus_state) -> int:
        next_states = state.next_states()
        ind_coup = np.random.randint(len(next_states))
        return ind_coup

class Player_MinMax(Player):
    '''
    Classe représentant un joueur MinMax.
    '''
    def __init__(self, depth=2):
        self.depth = depth
    
    def play(self, state: Blockus_state) -> int:
        raise NotImplementedError("Ihsane et Marie ne veulent pas m'implementer :'(")