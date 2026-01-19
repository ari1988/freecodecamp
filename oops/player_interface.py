import abc
import random


class Player(abc.ABC):
    """Abstract Player class that defines the interface for game players."""
    
    def __init__(self):
        """Initialize a Player with default attributes."""
        self.moves = []
        self.position = (0, 0)
        self.path = [self.position]
    
    def make_move(self):
        move = random.choice(self.moves)
        
        # Add the move to current position
        new_x = self.position[0] + move[0]
        new_y = self.position[1] + move[1]
        
        # Update position
        self.position = (new_x, new_y)
        
        # Append new position to path
        self.path.append(self.position)
        
        return self.position
    
    @abc.abstractmethod
    def level_up(self):
        """Abstract method to be implemented by concrete classes."""
        pass


class Pawn(Player):
    """Pawn class that represents a player with basic and diagonal moves."""
    
    def __init__(self):
        """Initialize a Pawn with basic directional moves."""
        super().__init__()
        # Basic moves: up, down, left, right (1 unit each)
        self.moves = [
            (0, 1),   # up
            (0, -1),  # down
            (-1, 0),  # left
            (1, 0)    # right
        ]
    
    def level_up(self):
        """Add diagonal moves to the Pawn's available moves."""
        # Diagonal moves
        diagonal_moves = [
            (1, 1),    # up-right
            (1, -1),   # down-right
            (-1, 1),   # up-left
            (-1, -1)   # down-left
        ]
        self.moves.extend(diagonal_moves)
