from blockus import player, blockus_state
import numpy as np

class player_MinMax(player):
    '''
    Classe représentant un joueur MinMax.
    '''
    def __init__(self, depth=2):
        self.depth = depth
        
    def state_evaluation(self, state: blockus_state) -> int:
        '''
        Fonction d'évaluation de l'algorithme MinMax.
        On regarde les pièces du joueur courant.
        Plus il y a de pièces non posèes qui ont de la "valeur", plus la valeur de l'état est petit.
        La valeur d'une pièce est représenté par le nombre de case qu'elle occupe et le nombre de possibilités de placement qu'elle offre.
        '''
        eval = 0
        current_player_pieces = state.player_pieces[state.player_turn]
        for piece in current_player_pieces:
            for masks in piece.liste_masks:
                nb_cube = np.sum(masks[0])  # nombre de cases occupées par la pièce
                nb_diag = np.sum(masks[2])  # nombre de possibilités de placement d'une prochaine pièce 
                eval = eval - nb_cube - nb_diag
                
        return eval
    
    
    def MaxValue(self, state: blockus_state, depth: int, alpha: int, beta: int) -> int:
        '''
        Fonction MaxValue de l'algorithme MinMax.
        Récupérer la valeur maximale pour un noeud.
        '''
        next_states = state.next_states
        
        if state.is_terminal() or depth == 0:
            return self.state_evaluation(state)
        
        value = -2147483647
        
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
        next_states = state.next_states
        
        if state.is_terminal() or depth == 0:
            return self.state_evaluation(state)
        
        value = 2147483647
        
        for possible_move in next_states:
            value = min(value, self.MaxValue(possible_move, depth - 1, alpha, beta))
            beta = min(beta, value)
        return value
    
    def play(self, state: blockus_state) -> int:
        '''
        Fonction de décision de l'algorithme MinMax.
        Récupérer le meilleur coup à jouer.
        Contient l'élagage alpha-beta.
        '''
        next_states = state.next_states()
        value = -float('inf')
        ind_coup = 0
        
        alpha = -2147483647
        beta = 2147483647
        
        for i, possible_move in enumerate(next_states):
            min_value = self.MinValue(possible_move, self.depth, alpha, beta)
            if min_value > value:
                value = min_value
                ind_coup = i
        
        return ind_coup
    
    