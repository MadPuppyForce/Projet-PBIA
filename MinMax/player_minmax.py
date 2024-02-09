from blockus import player, blockus_state

class player_MinMax(player):
    '''
    Classe représentant un joueur MinMax.
    '''
    def __init__(self, depth=2):
        self.depth = depth
    
    def play(self, state: blockus_state) -> int:
        raise NotImplementedError("Ihsane et Marie ne veulent pas m'implementer :'(")