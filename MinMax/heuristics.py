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
        
        if state.is_final():
            if eval > 0:
                return 1000
            elif eval < 0:
                return -1000
            else:
                return 0
        
        #maximizing_player_pieces = state.player_pieces[maximizing_player]
        #minimizing_player_pieces = state.player_pieces[minimizing_player]
        #for piece in maximizing_player_pieces:
        #    for masks in piece.liste_masks:
        #        nb_cube = np.sum(masks[0])  # nombre de cases occupées par la pièce
                #nb_diag = np.sum(masks[2])  # nombre de possibilités de placement d'une prochaine pièce 
        #        eval = eval - nb_cube #- nb_diag
        
        #for piece in minimizing_player_pieces:
        #    for masks in piece.liste_masks:
        #        nb_cube = np.sum(masks[0])   
        #        #nb_diag = np.sum(masks[2])
        #        eval = eval + nb_cube #+ nb_diag
        
        '''
        On pourrait pré-calculer le nombre de case qu'occupe chaque pièce
        et le nombre de possibilités de placement qu'elle offre,
        directement dans la classe pièce comme des attributs.
        '''
        return eval  
    
def heuristicV2(state: blockus_state, maximizing_player, minimizing_player) -> int:
        '''
        Deuxième heuristique de l'algorithme MinMax.
        On regarde les pièces du joueur courant.
        Plus il y a de pièces non posèes qui ont de la "valeur", plus la valeur de l'état est petit.
        La valeur d'une pièce est représenté par le nombre de case qu'elle occupe et le nombre de possibilités de placement qu'elle offre.
        De plus, on ajoute des points si le joueur maximisant a des pièces au milieu du plateau.
        '''
        height = state.height
        width = state.width
        
        # carte des positions qui ont de la valeur lors du placement d'une pièce
        valuable_position_map = np.zeros((height+2, width+2), dtype=bool) 
        valuable_position_map[height//2, width//2] = True       #les poisitions du millieu du plateau
        valuable_position_map[height//2+1, width//2] = True
        valuable_position_map[height//2, width//2+1] = True
        valuable_position_map[height//2+1, width//2+1] = True
        
        
        eval = (np.sum(state.players_mask[maximizing_player]) - np.sum(state.players_mask[minimizing_player]))
        
        if state.is_final():
            if eval > 0:
                return 1000
            elif eval < 0:
                return -1000
            else:
                return 0
            
        eval = eval + (np.sum( valuable_position_map * state.players_mask[maximizing_player]) * 5)
        
        maximizing_player_pieces = state.player_pieces[maximizing_player]
        minimizing_player_pieces = state.player_pieces[minimizing_player]
        for piece in maximizing_player_pieces:
            for masks in piece.liste_masks:
                #nb_cube = np.sum(masks[0])  # nombre de cases occupées par la pièce
                nb_diag = np.sum(masks[2])  # nombre de possibilités de placement d'une prochaine pièce 
                eval = eval - nb_diag #- nb_cube - nb_diag
        
        for piece in minimizing_player_pieces:
            for masks in piece.liste_masks:
                #nb_cube = np.sum(masks[0])   
                nb_diag = np.sum(masks[2])
                eval = eval + nb_diag#+ nb_cube + nb_diag
        
        '''
        On pourrait pré-calculer le nombre de case qu'occupe chaque pièce
        et le nombre de possibilités de placement qu'elle offre,
        directement dans la classe pièce comme des attributs.
        '''
        return eval 