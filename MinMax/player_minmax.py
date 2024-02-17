from blockus import player, blockus_state
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
        next_states.sort(key=lambda x: self.state_evaluation(x),reverse=True)
        return next_states
    
    
    def MaxValue(self, state: blockus_state, depth: int, alpha: int, beta: int) -> int:
        '''
        Fonction MaxValue de l'algorithme MinMax.
        Récupérer la valeur maximale pour un noeud.
        '''
        next_states = state.next_states
        
        if state.is_terminal() or depth == 0:
            return self.heuristic(state, self.maximizing_player, self.minimizing_player)
        
        value = -2147483647
        
        next_states = self.trie_elagage(state)
        
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
            return self.heuristic(state, self.maximizing_player, self.minimizing_player)
        
        value = 2147483647
        
        next_states = self.trie_elagage(state)
        
        for possible_move in next_states:
            value = min(value, self.MaxValue(possible_move, depth - 1, alpha, beta))
            beta = min(beta, value)
            
        return value
    
    def play(self, state: blockus_state) -> blockus_state:
        '''
        Fonction de décision de l'algorithme MinMax.
        Récupérer le meilleur coup à jouer.
        Contient l'élagage alpha-beta.
        '''
        next_states = state.next_states()
        value = -float('inf')
        best_move = None
        
        self.maximizing_player = state.player_turn
        self.minimizing_player = 0 if self.maximizing_player == 1 else 1
        
        
        alpha = -2147483647
        beta = 2147483647
        
        next_states = self.trie_elagage(state)
        
        for i, possible_move in enumerate(next_states):
            max_value = self.MinValue(possible_move, self.depth, alpha, beta)
            alpha = max(alpha, max_value)
            if max_value > value:
                value = max_value
                best_move = possible_move
        
        return best_move

    


def heuristicV1(state: blockus_state, maximizing_player, minimizing_player) -> int:
        '''
        Première heuristique de l'algorithme MinMax.
        On regarde les pièces du joueur courant.
        Plus il y a de pièces non posèes qui ont de la "valeur", plus la valeur de l'état est petit.
        La valeur d'une pièce est représenté par le nombre de case qu'elle occupe et le nombre de possibilités de placement qu'elle offre.
        '''
        eval = 0
        maximizing_player_pieces = state.player_pieces[maximizing_player]
        minimizing_player_pieces = state.player_pieces[minimizing_player]
        for piece in maximizing_player_pieces:
            for masks in piece.liste_masks:
                nb_cube = np.sum(masks[0])  # nombre de cases occupées par la pièce
                nb_diag = np.sum(masks[2])  # nombre de possibilités de placement d'une prochaine pièce 
                eval = eval - nb_cube - nb_diag
        
        for piece in minimizing_player_pieces:
            for masks in piece.liste_masks:
                nb_cube = np.sum(masks[0])   
                nb_diag = np.sum(masks[2])
                eval = eval + nb_cube + nb_diag
                
        '''
        On pourrait pré-calculer le nombre de case qu'occupe chaque pièce
        et le nombre de possibilités de placement qu'elle offre,
        directement dans la classe pièce comme des attributs.
        '''
        return eval  