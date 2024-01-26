import numpy as np

class piece:
    '''Classe représentant une piece.'''
    
    def _init_(self, mask):
        '''
        Constructeur de la classe piece.
            - mask : mask de la piece provenant du fichier .txt
        '''
        self.liste_masks = self.initialiser_liste_masks(mask)
    
    def initialiser_liste_masks(self,mask):
        '''
        Initialise la liste des masks de la piece. 
        Chaque element correspond a un mask de la piece dans une orientation differente.
            - liste de tuple (mask_piece, mask_piece_adj, mask_piece_diag)
            
            Exemple d'element de la liste pour une piece de taille 3x3 en forme de L :
                - le masque de la piece :
                      1 1 0
                      0 1 0
                      0 1 0
                - le masque des cases adjacentes a la piece :
                    0 1 1 0 0
                    1 0 0 1 0
                    0 1 0 1 0
                    0 1 0 1 0
                    0 0 1 0 0
                - le masque des cases diagonales a la piece :
                    1 0 0 1 0
                    0 0 0 0 0
                    1 0 0 0 0
                    0 0 0 0 0
                    0 1 0 1 0  
        '''
        liste_masks = []
        
        return liste_masks


def charger_pieces() -> list[piece] :
    '''
    Charge les pieces du jeu Blockus a partir de fichiers
    '''
    pieces = []
    
    return pieces