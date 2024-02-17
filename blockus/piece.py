import numpy as np

class piece:
    '''Classe représentant une piece.'''
    
    def _init_(self, mask):
        '''
        Constructeur de la classe piece.
            - mask : mask de la piece provenant du fichier .txt
        '''
        self.liste_masks = self.initialiser_liste_masks(mask)
    
    def initialiser_liste_masks(self,file_path):
        
        piece=charger_pieces(file_path)
        config=__generer_config(piece)
        liste_masks=[]
        for choice in config:
            mask_piece = choice
            mask_piece_adj = __generer_adj(choice)
            mask_piece_diag = __generer_diag(choice)
            liste_masks.append((mask_piece, mask_piece_adj, mask_piece_diag))
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
        
        return liste_masks
    
def __generer_config(piece) -> list:
        
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
        
def __generer_adj(piece) -> np.ndarray:
        '''
        Genere le masque des cases adjacentes a la piece
        '''
        piece = np.array(piece)
        piece_pad= np.array(np.pad(piece, 1, mode='constant', constant_values=0),dtype=int)



        #gauche
        piece_pad[1:1+len(piece),0:len(piece[0])] |= piece
        #droite
        piece_pad[1:1+len(piece),2:2+len(piece[0])] |= piece
        #haut
        piece_pad[0:len(piece),1:1+len(piece[0])] |= piece
        #bas
        piece_pad[2:2+len(piece),1:1+len(piece[0])] |= piece

        #enlever la piece initiale
        piece_pad[1:len(piece)+1,1:len(piece[0])+1]^= piece
   

        return piece_pad
def __generer_diag(piece) -> np.ndarray:
        '''
        Genere le masque des cases diagonales a la piece
        '''
        piece = np.array(piece)
        piece_pad= np.array(np.pad(piece, 1, mode='constant', constant_values=0),dtype=int)
        adj = __generer_adj(piece)

        #haut gauche
        piece_pad[0:len(piece),0:len(piece[0])] |= piece
        #haut droite
        piece_pad[0:len(piece),2:2+len(piece[0])] |= piece
        #bas gauche
        piece_pad[2:2+len(piece),0:len(piece[0])] |= piece
        #bas droite
        piece_pad[2:2+len(piece),2:2+len(piece[0])] |= piece

        #enlever la piece initiale
        piece_pad[1:len(piece)+1,1:len(piece[0])+1]^= piece

        #enlever les cases adjacentes
        piece_pad=piece_pad & np.invert(adj)

        return piece_pad    

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


