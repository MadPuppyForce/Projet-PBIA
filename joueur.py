

class Player:
    """Classe représentant un joueur."""

    def __init__(self, name, color, pieces, player_mask):
        """Constructeur de la classe Joueur."""
        """ name : nom du joueur"""
        """ color : couleur du joueur"""
        """ score : score du joueur"""
        """ pieces : liste des pieces du joueur, chaque possède sa liste de mask"""
        """ mask_joueur : mask indiquant les cases occupées par les pieces du joueur et les cases induites qui ne peuvent pas être jouées"""
        self.name = name
        self.color = color
        self.score = 0
        self.pieces = pieces
        self.player_mask = player_mask

    def __str__(self):
        """Méthode spéciale pour afficher un joueur."""
        return self.name + " (" + self.color + ")"

    def __eq__(self, autre):
        """Méthode spéciale pour comparer deux joueurs."""
        return self.name == autre.name and self.color == autre.color

    def get_score(self):
        """Retourne le score du joueur."""
        return self.score
    
    def get_pieces(self):
        """Retourne les pieces du joueur."""
        return self.pieces
    
    def get_mask(self):
        """Retourne le mask du joueur."""
        return self.player_mask
    
    def add_points(self, points):
        """Ajoute des points au score du joueur."""
        self.score += points
    
    def remove_points(self, points):
        """Retire des points au score du joueur."""
        self.score -= points
        
    def extract():
        
        
    def update_mask(self, coord, mask_piece):
        """Met à jour le mask du joueur."""
        """coord : coordonnées de la position du coin supéreiur gauche de la piece jouée"""
        """mask_piece : mask de la piece jouée"""
        
        x = coord[0]
        y = coord[1]
        
        self.player_mask[x][y] = 1
        
        for i in range(0, len(self.player_mask)):
            for j in range(0, len(self.player_mask)):
                if mask_piece[i][j] == 1:
                    self.player_mask[x+i][y+j] = 1