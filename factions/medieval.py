"""Class for Medieval"""

class medieval:
    morale: int
    max_troops: int
    num_archer: int
    num_foot_soldier: int

    def __init__(self) -> None:
        self.morale = 100
        self.max_troops = 5
        self.num_archer = 0
        self.num_foot_soldier = 0