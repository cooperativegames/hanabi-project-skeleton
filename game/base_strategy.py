#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .card import Card, CardAppearance
from .action import Action
from typing import List, Dict


class BaseStrategy(object):
    """
    Subclass this class once for each AI.
    """
    
    def __init__(self, verbose: bool = False, params: dict={}):
        self.verbose = verbose
    
    
    def initialize(self, id: int, num_players: int, k: int, board: Dict[str, int], deck_type, 
                         my_hand: List[CardAppearance], hands: List[List[CardAppearance]], 
                         discard_pile: List[Card], deck_size: int, game) -> None:
        """
        To be called once before the beginning.
        """
        self.id: int = id
        self.num_players: int = num_players
        self.k: int = k  # number of cards per hand
        self.board: Dict[str, int] = board # board state, a dict of color to int
        self.deck_type = deck_type
        
        self.my_hand: List[CardAppearance] = my_hand 
        self.hands: List[List[CardAppearance]] = hands
        self.discard_pile: List[CardAppearance] = discard_pile
        self.deck_size: int = deck_size
        self.game = game
    
    
    def update(self, clues: int, lives: int, my_hand: List[CardAppearance], hands: List[List[CardAppearance]], 
                     discard_pile: List[Card], turn: int, last_turn: bool, deck_size: int, game) -> None:
        """
        To be called immediately after every turn.
        """
        self.clues: int = clues
        self.lives: int = lives
        self.turn: int = turn
        self.last_turn: bool = last_turn
        self.deck_size: int = deck_size
        
        self.my_hand: List[CardAppearance] = my_hand  # says in which positions there is actually a card
        self.hands: List[List[CardAppearance]] = hands
        self.discard_pile: List[CardAppearance] = discard_pile
        self.game = game
    
    
    def feed_turn(self, player_id: int, action: Action) -> None:
        """
        Receive information about a played turn.
        """
        raise NotImplementedError
    
    
    def get_turn_action(self) -> Action:
        """
        Choose action for this turn.
        """
        raise NotImplementedError


    def log(self, message):
        if self.verbose:
            print("Player %d: %s" % (self.id, message))


