import numpy as np

class piece:
    '''Classe représentant une piece.'''
    def __init__(self, mask):
        '''
        Constructeur de la classe piece.
            - mask : mask de la piece provenant du fichier .txt
        '''
        self.liste_masks = self.initialiser_liste_masks(mask)
    
    def initialiser_liste_masks(self, mask):
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
        
        config = self.__generer_config(mask)
        liste_masks=[]
        for choice in config:
            mask_piece      = choice
            mask_piece_adj  = self.__generer_adj(choice)
            mask_piece_diag = self.__generer_diag(choice, mask_piece_adj)
            liste_masks.append((mask_piece, mask_piece_adj, mask_piece_diag))
        return liste_masks
    
    def __generer_config(self,mask) -> list:
        rotations = [np.rot90(mask, k=i) for i in range(4)]
        # flipped_rotations = [np.flip(rot,0) for rot in rotations]
        configs = rotations # + flipped_rotations
        config_unique= []
        for config in configs:
            if not any(np.array_equal(config, unique) for unique in config_unique):
                config_unique.append(config)
        
        return config_unique
            
    def __generer_adj(self,piece) -> np.ndarray:
        '''
        Genere le masque des cases adjacentes a la piece
        a partir du masque de base
        '''
        h, w = piece.shape
        adj = np.zeros((h+2,w+2),dtype=bool)

        # gauche
        adj[1:1+len(piece),  0:len(piece[0])] |= piece
        # droite
        adj[1:1+len(piece),2:2+len(piece[0])] |= piece
        # haut
        adj[  0:len(piece),1:1+len(piece[0])] |= piece
        # bas
        adj[2:2+len(piece),1:1+len(piece[0])] |= piece

        # enlever la piece initiale
        adj[1:len(piece)+1,1:len(piece[0])+1] ^= piece

        return adj
        
    def __generer_diag(self,piece, adj) -> np.ndarray:
        '''
        Genere le masque des cases diagonales a la piece
        a partir du masque de base et du masque des cases adjacentes
        '''
        h, w = piece.shape
        diag = np.zeros((h+2,w+2),dtype=bool)

        # haut gauche
        diag[  0:h,  0:w] |= piece
        # haut droite
        diag[  0:h,2:2+w] |= piece
        # bas gauche
        diag[2:2+h,  0:w] |= piece
        # bas droite
        diag[2:2+h,2:2+w] |= piece

        #enlever la piece initiale
        diag[1:h+1,1:w+1] ^= piece

        #enlever les cases adjacentes
        diag = diag & ~adj

        return diag

def charger_piece(file_path) -> np.ndarray :
    '''
    Charge une pièce du jeu Blockus a partir de fichiers
    '''
    mask = np.loadtxt(file_path, dtype=bool)
    if mask.ndim == 0:
        mask = mask[np.newaxis, np.newaxis]
    if mask.ndim == 1:
        mask = mask[np.newaxis, :]
    p = piece(mask)
    return p


