from __future__ import annotations
import numpy as np
from blockus.piece import piece

class blockus_state():
    '''
    Classe représentant un état du jeu Blockus
        :param width: largeur du plateau de jeu
        :param height: hauteur du plateau de jeu
        :param player_pieces: liste des pieces de chacun des 2 joueurs
        :param players_mask: masques des pieces de chacun des 2 des joueurs
        :param player_turn: joueur dont c'est le tour de jouer
        :param previous_state: etat precedent
    '''
    def __init__(self, width, height, player_pieces, players_mask=None, player_turn=0, previous_state=None):
        self.width = width
        self.height = height
        self.player_pieces = player_pieces
        
        # initialisation des masques des joueurs
        if players_mask == None: # initialisation des masques des joueurs si non fournis
            self.players_mask = [np.zeros((height+2, width+2), dtype=bool), np.zeros((height+2, width+2), dtype=bool)]
            self.players_mask[0][ 0, 0] = True
            self.players_mask[1][-1,-1] = True
        else:
            self.players_mask = players_mask
            
        self.player_turn = player_turn
        self.previous_state = previous_state if previous_state != None else self
        self._next_states = None
        self._mask_board = None
        self._nb_coups = None
    
    @property
    def mask_board(self) -> np.array:
        if self._mask_board == None:
            self._mask_board = self.players_mask[0] | self.players_mask[1]
        return self._mask_board
    
    @mask_board.setter
    def mask_board(self, value):
        raise AttributeError("You can't set attribute mask_board")
    
    @property
    def next_states(self) -> list:
        if self._next_states == None:
            self._next_states = self.__compute_next_states()
        return self._next_states
    
    @next_states.setter
    def next_states(self, value):
        raise AttributeError("You can't set attribute next_states")      
    
    @property
    def nb_coups(self) -> int:
        if self._next_states == None:
            self._next_states = self.__compute_next_states()
        return self._nb_coups
    
    @nb_coups.setter
    def next_states(self, value):
        raise AttributeError("You can't set attribute next_states")  
    
    def __get_next_state(self, piece:piece, mask_piece, coord) -> blockus_state:
        '''
        Retourne le nouvel etat du jeu apres avoir joue la piece aux coordonnees donnees
        '''
        current_player = self.player_turn
        i, j = coord
        h_mask, w_mask = mask_piece.shape
        
        # changement du joueur
        next_player_turn = 0 if current_player == 1 else 1
        
        # mise a jour des masques
        next_players_mask = self.players_mask.deepcopy()
        next_players_mask[current_player][1+i:1+i+h_mask, 1+j:1+j+w_mask] |= mask_piece
        
        # mise a jour des pieces
        next_player_pieces = [self.player_pieces[0].copy(), self.player_pieces[1].copy()]
        next_player_pieces[current_player].remove(piece)
        
        # creation du nouvel etat
        next_state = blockus_state(self.width, self.height, next_players_mask, next_player_pieces, next_player_turn, self)
        
        return next_state
        
    def __compute_next_states(self):
        '''
        Calcule les etats suivants
        '''
        next_states = []
        current_player_pieces = self.player_pieces[self.player_turn]
        for piece in current_player_pieces:
            for masks in piece.liste_masks:
                w_mask, h_mask = masks[0].shape
                for j in range(self.width - w_mask):
                    for i in range(self.height - h_mask):
                        if self.__is_valid(masks, (i, j)):
                            next_state = self.__get_next_state(piece, masks[0], (i, j))
                            next_states.append(next_state)
        
        self._nb_coups = len(next_states)
        
        # si aucun coup possible et que le jeu n'est pas fini, on passe le tour du joueur courant
        if self._nb_coups == 0 and self.previous_state.nb_coups != 0:
            next_player_turn = 0 if self.player_turn == 1 else 1
            next_state = blockus_state(self.width, self.height, self.players_mask, self.player_pieces, next_player_turn, self)
            next_states.append(next_state)
        
        return next_states
    
    def __is_valid(self, masks, coord) -> bool:
        '''
        Verifie si la piece peut etre placee aux coordonnees donnees
            - masks : tuple (mask_piece, mask_piece_adj, mask_piece_diag)
            - coord : coordonnees de la position du coin superieur gauche de la piece jouee
        '''
        i, j = coord
        mask_board = self.mask_board
        mask_pieces_current_player = self.players_mask[self.player_turn]
        mask_piece, mask_piece_adj, mask_piece_diag = masks
        h_mask, w_mask = mask_piece.shape
        
        # verification que les cases sont libres
        if np.any(mask_board[1+i:1+i+h_mask, 1+j:1+j+w_mask] & mask_piece):
            return False
        
        # verification que les cases adjacentes a la piece ne sont pas occupees par des pieces du joueur
        if np.any(mask_pieces_current_player[i:i+h_mask+2, j:j+w_mask+2] & mask_piece_adj):
            return False
        
        # verification que au moins une case dans une diagonale a la piece est occupee par une piece du joueur
        if not np.any(mask_pieces_current_player[i:i+h_mask+2, j:j+w_mask+2] & mask_piece_diag):
            return False
        
        return True
    
    def is_final(self) -> bool:
        return self.previous_state.nb_coups == 0 and self.nb_coups == 0
    
    def result(self) -> int:
        '''
        Retourne le resultat du jeu : 1 si le joueur 1 a gagne, -1 si le joueur 2 a gagne, 0 sinon
        '''
        score = np.sum(self.players_mask[0]) - np.sum(self.players_mask[1])
        
        return 1 if score > 0 else -1 if score < 0 else 0
    
    def __str__(self) -> str:
        J1_CHAR = 'X'
        J2_CHAR = 'O'
        EMPTY_CHAR = '.'
        
        board = np.full((self.height, self.width), EMPTY_CHAR)
        board[self.players_mask[0][1:-1, 1:-1]] = J1_CHAR
        board[self.players_mask[1][1:-1, 1:-1]] = J2_CHAR
        
        str_board = ''
        for i in range(self.height):
            str_board += ''.join(board[i]) + '\n'
        
        return str_board
        