from blockus import player, blockus_state

class player_MonteCarlo(player):
    '''
    Classe représentant un joueur MinMax.
    '''
    def __init__(self, depth):
        self.depth = depth
    
    def play(self, state: blockus_state) -> int:
        raise NotImplementedError("Me llamo Monte Carlo y no soy implementado :'(")