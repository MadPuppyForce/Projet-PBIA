import numpy as np
import random
from blockus.blockus_state import blockus_state
from blockus.piece import piece
from blockus.joueur import player

class blockus:
    '''
    Classe représentant le jeu Blockus
    :param width: largeur du plateau de jeu
    :param height: hauteur du plateau de jeu
    :param players: liste des joueurs
    :param pieces: liste des pieces
    '''
    def __init__(self, width:int, height:int, players:list[player], pieces:list[piece]):
        self.name = "Blockus"
        self.description = "Blockus est un jeu de stratégie pour 2 à 4 joueurs. \
                            Le but du jeu est de placer toutes ses pièces sur le plateau de jeu. \
                            Chaque pièce posée doit toucher un coin de la pièce déjà posée, \
                            mais seulement par les coins. Les côtés des pièces de même couleur \
                            ne peuvent pas se toucher. Les pièces de même couleur peuvent se toucher par les côtés."
        
        self.players = players
        self.pieces = pieces
        # initialisation du jeu
        self.current_state = blockus_state(width, height, [pieces.copy(), pieces.copy()])
    
    def play_turn(self):
        '''
        Joue un tour de jeu
        '''
        current_player = self.players[self.current_state.player_turn]
        next_state = current_player.play(self.current_state)
        self.current_state = next_state
    
    def play_turn_random(self):
        '''
        Joue un tour de jeu aléatoirement
        '''
        next_state = random.choice(self.current_state.next_states)
        self.current_state = next_state
    
    def reset(self):
        '''
        Reinitialise le jeu
        '''
        self.current_state = blockus_state(self.current_state.width, self.current_state.height, \
            [self.pieces.copy(), self.pieces.copy()])