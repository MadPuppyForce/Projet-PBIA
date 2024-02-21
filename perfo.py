from blockus import piece, blockus, joueur
from MinMax import player_MinMax, heuristics
from MonteCarlo import player_MonteCarlo
import numpy as np
import os
from tqdm import tqdm,trange

'''
Constantes
'''
WIDTH = 12  # largeur du plateau de jeu
HEIGHT = 12 # hauteur du plateau de jeu


N = 50 # nombre de parties a simuler

nb_coups_aleatoires = 6
'''
Initialisation du blockus
'''
# Création des pièces
pieces = []
for file in os.listdir("pieces"):
    pieces.append(piece.charger_piece("pieces/" + file))

# creation des joueurs
# player1 = joueur.player_random()
# player1 = player_MinMax(3, heuristics.heuristicV1)
player2 = player_MinMax(2, heuristics.heuristicV1, verbose=False)
#player1 = player_MonteCarlo(1000, 20, 1)
#player2 = joueur.player_random()
# player2 = player_MinMax(3, heuristics.heuristicV1)
player1 = player_MinMax(2, heuristics.heuristicV2, verbose=False)

players = [player1, player2]

# creation du plateau de jeu
game = blockus(WIDTH,HEIGHT,players,pieces)

resultats = [0,0,0] # (nb_victoires_j1, nb_victoires_j2, nb_match_nul)
# Simuler N parties
for _ in trange(N, desc="Parties"):
    game.reset()
    for _ in range(nb_coups_aleatoires):
        game.play_turn_random()
    while not game.current_state.is_final():
        game.play_turn()

    # resultat de la partie
    result = game.current_state.result()
    if result == 1:
        resultats[0] += 1
    elif result == -1:
        resultats[1] += 1
    else:
        resultats[2] += 1
    
print("Résultats (nb_victoires_j1, nb_victoires_j2, nb_match_nul): ", resultats)