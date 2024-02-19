from blockus import blockus_state, piece, blockus, joueur
import numpy as np
import os

'''
Constantes
'''
WIDTH = 20  # largeur du plateau de jeu
HEIGHT = 20 # hauteur du plateau de jeu


'''
Initialisation du blockus
'''

# Création des pièces
pieces = []

for file in os.listdir("pieces"):
    if file.endswith(".txt"):
        pieces.append(piece.charger_pieces(file))


# Création des joueurs

#nb_players = 2   #nombre de joueurs (de 2 à 4)
player1 = joueur.player_random()
player2 = joueur.player_random()

players = [player1, player2]


# Création du plateau de jeu

game = blockus(WIDTH,HEIGHT,players,pieces)


'''
Tour de jeu
'''

while not game.current_state.is_final():
    # Affichage de l'état du jeu
    print(game.current_state)
    game.play_turn()
    

# Calcul du score
score = blockus.current_state.score()
print("Score final : ", score)