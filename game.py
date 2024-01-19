import numpy as np

class game:
    def __init__(self,length):
        """ game name"""
        self.name = "Blockus"
        """description du jeu avec les règles du jeux"""
        self.description = "Blockus est un jeu de stratégie pour 2 à 4 joueurs. Le but du jeu est de placer toutes ses pièces sur le plateau de jeu. Chaque pièce posée doit toucher un coin de la pièce déjà posée, mais seulement par les coins. Les côtés des pièces de même couleur ne peuvent pas se toucher. Les pièces de même forme peuvent se toucher par les côtés."
        self.pices = []
        self.length = length
        self.mask_board= np.zeros((length,length))
        self.players_mask = [np.zeros((length,length)) ,np.zeros((length,length))]

    
    def __str__(self):
        return f"{self.name}\n{self.description}\n{self.items}\n{self.directions}"
    
    def update_mask_joueur(self, piece, coord):
        """Place une piece sur le plateau"""
        """piece : piece à placer"""
        """coord : coordonnées de la position du coin supéreiur gauche de la piece jouée"""
        
        x = coord[0]
        y = coord[1]
        
        for i in range(0, self.length):
            for j in range(0, self.length):
                if piece[i][j] == 1:
                    self.player_mask[x+i][y+j] = 1