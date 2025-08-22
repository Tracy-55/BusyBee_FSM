"""
BEE SIMULATION ENVIRONMENT - by Traicy
Last updated: 2025-08-15 (late night coding session)
"""
import numpy as np

class Environment:
    def __init__(self, size=10):
        self.size = size
        # Grid notes:
        # - None = empty
        # - 'F' = flower
        # - 'T' = threat (wasps!)
        self.grid = np.full((size, size), None, dtype=object)  
        
        # Pheromone tracking (TO DO: optimize this later)
        self.pheromones = np.zeros((size, size))
        
        # Hive position (center of the world!)
        self.hive_pos = (size//2, size//2)  # Changed from 'hive' to 'hive_pos' for clarity?
        
        # Debugging stuff
        self.flower_count = 0  # Not really used but might need it.
        
    def add_flower(self, x, y):
        """Adds a flower at (x,y). Returns True if successful."""
        # Edge case check (copied from StackOverflow lol)
        if x < 0 or y < 0 or x >= self.size or y >= self.size:
            print(f"Can't place flower at ({x},{y}) - out of bounds!")
            return False
            
        self.grid[x][y] = 'F'
        self.flower_count += 1
        return True
        
    # TO DO: Maybe combine these two functions later?
    def get_threats(self):
        """Returns list of (x,y) positions of threats"""
        threats = []
        for x in range(self.size):
            for y in range(self.size):
                if self.grid[x][y] == 'T':
                    threats.append((x,y))
        return threats