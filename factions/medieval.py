"""Class for Medieval"""

from __future__ import annotations

class medieval:
    morale: int
    max_troops: int
    num_archer: int
    num_foot_soldier: int
    troop_strength: int

    def __init__(self) -> None:
        self.morale = 100
        self.max_troops = 5
        self.num_archer = 0
        self.num_foot_soldier = 0
        troop_strength = 0

    def add_foot_soldier(self, amount_of_troops):
        self.morale += (foot_soldier.health * amount_of_troops)
        self.troop_strength += (foot_soldier.strength * amount_of_troops)

    def add_archer(self, amount_of_troops):
        self.morale += (archer.health * amount_of_troops)
        self.troop_strength += (archer.strength * amount_of_troops)
        

class foot_soldier:
    strength: int
    health: int

    def __init__(self) -> None:
        self.strength = 2
        self.health = 10

class archer:
    strength: int
    health: int

    def __init__(self) -> None:
        self.strength = 3
        self.health = 5