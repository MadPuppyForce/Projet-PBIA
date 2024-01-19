import numpy as np

class piece:
    """Classe représentant une piece."""
    
    def _init_(self, mask):
        """
        Constructeur de la classe piece.
            - mask : mask de la piece provenant du fichier .txt
        """
        self.mask= mask
    
    def initialiser_mask(self):
        """
        Initialise le mask de la piece.
        """
        self.mask = np.zeros((5,5))