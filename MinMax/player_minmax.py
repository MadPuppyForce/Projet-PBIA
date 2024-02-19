from blockus import blockus_state
from blockus.joueur import player
from tqdm import tqdm
import numpy as np

class player_MinMax(player):
    '''
    Classe représentant un joueur MinMax.
    '''
    def __init__(self, depth, heuristic):
        self.depth = depth
        self.heuristic = heuristic
        
    
    def trie_elagage(self, state: blockus_state) -> list:
        '''
        Fonction de tri des états pour l'élagage alpha-beta.
        On trie les états en fonction de leur valeur.
        '''
        next_states = state.next_states
        next_states.sort(key=lambda x: self.heuristic(x,self.maximizing_player, self.minimizing_player),reverse=True)
        return next_states
    
    
    def MaxValue(self, state: blockus_state, depth: int, alpha: int, beta: int) -> int:
        '''
        Fonction MaxValue de l'algorithme MinMax.
        Récupérer la valeur maximale pour un noeud.
        '''
        if state.is_final() or depth == 0:
            return self.heuristic(state, self.maximizing_player, self.minimizing_player)
        
        next_states = state.next_states
        
        value = -2147483647
        
        # next_states = self.trie_elagage(state)
        
        for possible_move in next_states:
            value = max(value, self.MinValue(possible_move, depth - 1, alpha, beta))
            alpha = max(alpha, value)
            if beta <= alpha:
                break
            
        return value
    
    def MinValue(self, state: blockus_state, depth: int, alpha: int, beta: int) -> int:
        '''
        Fonction MinValue de l'algorithme MinMax.
        Récupérer la valeur minimale pour un noeud.
        '''
        
        if state.is_final() or depth == 0:
            return self.heuristic(state, self.maximizing_player, self.minimizing_player)
        
        next_states = state.next_states
        
        value = 2147483647
        
        # next_states = self.trie_elagage(state)
        
        for possible_move in next_states:
            value = min(value, self.MaxValue(possible_move, depth - 1, alpha, beta))
            beta = min(beta, value)
            if beta <= alpha:
                break
            
        return value
    
    def play(self, state: blockus_state) -> blockus_state:
        '''
        Fonction de décision de l'algorithme MinMax.
        Récupérer le meilleur coup à jouer.
        Contient l'élagage alpha-beta.
        '''
        next_states = state.next_states
        value = -float('inf')
        best_move = None
        
        self.maximizing_player = state.player_turn
        self.minimizing_player = 0 if self.maximizing_player == 1 else 1
        
        
        alpha = -2147483647
        beta = 2147483647
        
        # next_states = self.trie_elagage(state)
        
        for i, possible_move in tqdm(enumerate(next_states), total=len(next_states), desc="MinMax"):
            max_value = self.MinValue(possible_move, self.depth, alpha, beta)
            alpha = max(alpha, max_value)
            if max_value > value:
                value = max_value
                best_move = possible_move
        
        # oublie des etats suivants pour liberer de la memoire
        state.forge_next_states()
        
        return best_move
