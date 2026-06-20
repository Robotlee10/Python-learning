from abc import ABC, abstractmethod
import random

class Player(ABC):
    def __init__(self):
        self.moves = []
        self.position = (0, 0)
        self.path = [self.position]

    def make_move(self):
        move = random.choice(self.moves)
        # Update position by adding coordinates
        self.position = (self.position[0] + move[0], self.position[1] + move[1])
        self.path.append(self.position)
        return self.position

    @abstractmethod
    def level_up(self):
        pass

class Pawn(Player):
    def __init__(self):
        super().__init__()
        # Up, Down, Left, Right
        self.moves = [(0, 1), (0, -1), (-1, 0), (1, 0)]

    def level_up(self):
        # Adding diagonal moves: (1, 1), (1, -1), (-1, 1), (-1, -1)
        diagonal_moves = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
        self.moves.extend(diagonal_moves)
