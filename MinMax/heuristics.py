import numpy as np
from blockus import blockus_state

def heuristicV1(state: blockus_state, maximizing_player, minimizing_player) -> int:
        '''
        Première heuristique de l'algorithme MinMax.
        On regarde les pièces du joueur courant.
        Plus il y a de pièces non posèes qui ont de la "valeur", plus la valeur de l'état est petit.
        La valeur d'une pièce est représenté par le nombre de case qu'elle occupe et le nombre de possibilités de placement qu'elle offre.
        '''
        eval = (np.sum(state.players_mask[maximizing_player]) - np.sum(state.players_mask[minimizing_player]))
        
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