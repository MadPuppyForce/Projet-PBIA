from blockus import piece, blockus, joueur
from MinMax import player_MinMax, heuristics
from MonteCarlo import player_MonteCarlo
import numpy as np
import os

'''
Constantes
'''
WIDTH = 12  # largeur du plateau de jeu
HEIGHT = 12 # hauteur du plateau de jeu


'''
Initialisation du blockus
'''

# Création des pièces
pieces = []
for file in os.listdir("pieces"):
    pieces.append(piece.charger_piece("pieces/" + file))


# creation des joueurs
#player1 = joueur.player_random()
#player1 = player_MinMax(3, heuristics.heuristicV1, verbose=True)
#player1 = player_MonteCarlo(1000, 120, 1, verbose=True)
player1 = player_MinMax(2, heuristics.heuristicV1, verbose=True)
#player2 = joueur.player_random()
player2 = player_MinMax(2, heuristics.heuristicV2, verbose=True)

players = [player1, player2]


# creation du plateau de jeu
game = blockus(WIDTH,HEIGHT,players,pieces)


'''
Tour de jeu
'''
turn = 0
while not game.current_state.is_final():
    # Affichage de l'état du jeu
    turn += 1
    nb_pieces_j1 = len(game.current_state.player_pieces[0])
    nb_pieces_j2 = len(game.current_state.player_pieces[1])
    print("\nTour ", turn, " - Joueur ", game.current_state.player_turn + 1)
    print("Nombre de pièces restantes : j1 -> ", nb_pieces_j1, " / j2 -> ", nb_pieces_j2)
    print(game.current_state)
    
    # Jouer un tour
    game.play_turn()

# Affichage de l'état final du jeu
turn += 1
nb_pieces_j1 = len(game.current_state.player_pieces[0])
nb_pieces_j2 = len(game.current_state.player_pieces[1])
print("\nTour ", turn, " - Joueur ", game.current_state.player_turn + 1)
print("Nombre de pièces restantes : j1 -> ", nb_pieces_j1, " / j2 -> ", nb_pieces_j2)
print(game.current_state)

# Calcul du score
# result = game.current_state.result()
score = game.current_state.score()

print("Score final : j1", score[0], "- j2", score[1])
if score[0] > score[1]:
    print("Joueur 1 gagne")
elif score[0] < score[1]:
    print("Joueur 2 gagne")
else:
    print("Match nul")