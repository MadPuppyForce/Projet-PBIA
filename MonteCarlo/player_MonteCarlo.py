import numpy as np
import random
from blockus import blockus_state
from blockus.joueur import player
from __future__ import annotations
class player_MonteCarlo(player):
    '''
    Classe représentant un joueur MinMax.
    '''
    def __init__(self, N_max, c):
        self.c = c
        self.N_max = N_max
    
    def play(self, state: blockus_state) -> blockus_state:
        
        root = Node(state)
        
        # algorithme de Monte Carlo
        for _ in range(self.N_max):
            node = root
            # selection
            node = self.selection(node)
            
            # expansion
            new_node = self.expansion(node)
            if new_node != None:
                node = new_node
            
            # simulation
            result = self.simulation(node)
            
            # backpropagation
            self.backpropagation(node, result)
        
        # selection du meilleur coup
        best_node = None
        best_score = -1
        for child in root.childrens:
            if child.visits > best_score:
                best_score = child.visits
                best_node = child
        
        return best_node.state
    
    def selection(self, root: Node):
        selected = root
        
        while not selected.is_leaf():
            next_node = None
            best_uct = -1
            for child in selected.childrens:
                if child.visits == 0:
                    return child
                uct = (child.wins / child.visits) + self.c * np.sqrt(selected.visits / child.visits)
                if uct > best_uct:
                    best_uct = uct
                    next_node = child
            
            selected = next_node
        
        return selected
    
    def expansion(self, node: Node) -> Node:
        if node.is_terminal():
            return None
        
        # selection aleatoire d'un noeud non explore
        state_to_expand = node.untried_actions.pop(random.randint(0, len(node.untried_actions) - 1))
        
        # creation du nouveau noeud
        new_node = Node(state_to_expand, node)
        
        # ajout du nouveau noeud a la liste des enfants du noeud courant
        node.childrens.append(new_node)
        
        return new_node
    
    def simulation(self, node: Node) -> int:
        state = node.state
        while not state.is_final():
            state = state.next_states[random.randint(0, len(state.next_states) - 1)]
        
        return state.result()
    
    def backpropagation(self, node: Node, result: int):
        loser = 0 if result == -1 else 1 if result == 1 else -1
        while node != None:
            node.visits += 1
            
            # on ajoute 1 au nombre de victoires si le joueur gagnant vient de jouer
            # c'est a dire si le joueur courant du noeud est le joueur perdant
            if node.state.player_turn == loser:
                node.wins += 1
            
            node = node.parent
            
        

class Node:
    def __init__(self, state: blockus_state, parent=None):
        self.state = state
        self.parent = parent
        self.childrens:list[Node] = []
        self.untried_actions:list[blockus_state] = state.next_states
        self.visits = 0
        self.wins = 0
    
    def is_terminal(self):
        return self.state.is_final()
    
    def is_leaf(self):
        return len(self.untried_actions) == 0
    
        