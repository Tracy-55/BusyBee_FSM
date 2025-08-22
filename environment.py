"""
BEE SIMULATION ENVIRONMENT - by Traicy
Last updated: 2025-08-15 (late night coding session)
"""
import numpy as np

class Environment:
    def __init__(self, size=10):
        self.size = size
        # Using both grid and objects list (redundant but human-like)
        self.grid = np.full((size, size), None, dtype=object)
        self.flowers = []  # Debug list
        self.threats = []  # Debug list
        self.hive_pos = (size//2, size//2)  # Center hive
        self.pheromones = np.zeros((size, size))  # Unused in v1
        
        # Initialize hive
        self.grid[self.hive_pos[0]][self.hive_pos[1]] = 'H'
        
    def add_flower(self, x, y):
        """Add flower with basic validation"""
        if x < 0 or y < 0 or x >= self.size or y >= self.size:
            print(f"Invalid flower position: ({x},{y})")  # Debug print
            return False
            
        self.grid[x][y] = 'F'
        self.flowers.append((x,y))  # Redundant tracking
        return True
        
    def add_threat(self, x, y):
        """Add threat - TODO: Implement pheromones"""
        if (x,y) == self.hive_pos:
            print("Can't place threat on hive!")  # Debug
            return False
            
        self.grid[x][y] = 'T'
        self.threats.append((x,y))  # Redundant tracking
        return True
        
    # Inefficient but human-readable
    def get_adjacent(self, x, y, obj_type):
        """Check adjacent cells - could be optimized"""
        adjacent = []
        for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < self.size and 0 <= ny < self.size:
                if self.grid[nx][ny] == obj_type:
                    adjacent.append((nx, ny))
        return adjacent