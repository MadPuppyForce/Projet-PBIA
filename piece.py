import numpy as np


class piece:
    '''Classe représentant une piece.'''
    
    def _init_(self, mask):
        '''
        Constructeur de la classe piece.
            - mask : mask de la piece provenant du fichier .txt
        '''
        self.liste_masks = self.initialiser_liste_masks(mask)
    
    def initialiser_liste_masks(self,mask,file_path):
        '''
        Initialise la liste des masks de la piece. 
        Chaque element correspond a un mask de la piece dans une orientation differente.
            - liste de tuple (mask_piece, mask_piece_adj, mask_piece_diag)
            
            Exemple d'element de la liste pour une piece de taille 3x2 en forme de L :
                - le masque de la piece :
                      1 1
                      0 1
                      0 1
                - le masque des cases adjacentes a la piece :
                    0 1 1 0
                    1 0 0 1
                    0 1 0 1
                    0 1 0 1
                    0 0 1 0
                - le masque des cases diagonales a la piece :
                    1 0 0 1
                    0 0 0 0
                    1 0 0 0
                    0 0 0 0
                    0 1 0 1
        '''
        liste_masks = []
        
        return liste_masks


def charger_pieces(file_path) -> np.ndarray :
    '''
    Charge une pièce du jeu Blockus a partir de fichiers
    '''
    try:
        piece = np.loadtxt(file_path)
        """ just in case lol"""
        piece = piece.astype(int)
        return piece
    except Exception as e:
        print("Erreur lors du chargement des pieces : ", e)
        return None

def generer_config(piece) -> list:
    
    rotations = [np.rot90(piece, k=i) for i in range(4)]
    flipped_rotations = [np.flip(rot,0) for rot in rotations]
    configs_ar= rotations + flipped_rotations
    configs=[arr.tolist() for arr in configs_ar]
    config_unique= []
    for config in configs:
        if not any(np.array_equal(config, unique) for unique in config_unique):
            config_unique.append(config)
    
    return config_unique
    #return type(configs)
    
def generer_adj(piece) -> np.ndarray:
    '''
    Genere le masque des cases adjacentes a la piece
    '''
    piece = np.array(piece)
    piece_pad= np.array(np.pad(piece, 1, mode='constant', constant_values=1),dtype=bool)
    piece_pad=np.invert(piece_pad)


    return piece_pad
 
