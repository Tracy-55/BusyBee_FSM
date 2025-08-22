# HELPER FUNCTIONS FILE
# (I should probably organize these better)
# Note to self: fix random import later

def distance(x1, y1, x2, y2):
    """Calculates Euclidean distance between two points"""
    # Pythagoras would be proud!
    return ((x1 - x2)**2 + (y1 - y2)**2)**0.5
    
def random_direction():
    """Returns random (dx, dy) movement vector"""
    directions = [(0,1), (1,0), (0,-1), (-1,0)]
    
    return random.choice(directions) # import random!
    
# TODO: Add more utility functions here:
# - Pheromone diffusion
# - Pathfinding helpers
# - etc.