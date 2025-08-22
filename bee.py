import random
from enum import Enum, auto

class State(Enum):
    WANDERING = auto()  # Exploring
    FORAGING = auto()   # Collecting pollen
    ATTACKING = auto()  # Fighting threats
    # RESTING = auto()  # Future feature

class Bee:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.health = 100
        self.energy = 50  # Start with some energy
        self.pollen = 0
        self.state = State.WANDERING
        self.attack_counter = 0  # Temp solution
        
        # Debug variables
        self.last_action = None
        self.path = []  # Unused but looks like planning
        
    def move(self, env, dx, dy):
        """Basic movement with energy cost"""
        new_x, new_y = self.x + dx, self.y + dy
        
        # Boundary check
        if 0 <= new_x < env.size and 0 <= new_y < env.size:
            # Can't move onto other bees (placeholder)
            if env.grid[new_x][new_y] not in ['B']:  # Simple check
                self.x, self.y = new_x, new_y
                self.energy -= 0.5  # Energy cost
                self.last_action = f"Moved to ({new_x},{new_y})"
                return True
        return False
        
    def update_state(self, env):
        """FSM logic with some imperfections"""
        if self.health <= 0 or self.energy <= 0:
            print("Bee died!")  # Debug
            return False
            
        if self.state == State.WANDERING:
            # Random movement (could be improved)
            dx, dy = random.choice([(0,1),(1,0),(0,-1),(-1,0)])
            self.move(env, dx, dy)
            
            # Check for flowers
            if env.get_adjacent(self.x, self.y, 'F'):
                self.state = State.FORAGING
                
            # Basic threat detection (TODO: improve)
            threats = env.get_adjacent(self.x, self.y, 'T')
            if threats and random.random() > 0.5:  # 50% chance to notice
                self.state = State.ATTACKING
                
        elif self.state == State.FORAGING:
            # Simple foraging logic
            if env.grid[self.x][self.y] == 'F':
                self.pollen += 1
                self.energy = 100  # Full energy
                env.grid[self.x][self.y] = None
                print(f"Collected pollen! Total: {self.pollen}")  # Debug
                
            # Naive path to hive
            if (self.x, self.y) == env.hive_pos:
                self.state = State.WANDERING
            else:
                # Basic movement toward hive
                if self.x < env.hive_pos[0]:
                    self.move(env, 1, 0)
                elif self.x > env.hive_pos[0]:
                    self.move(env, -1, 0)
                elif self.y < env.hive_pos[1]:
                    self.move(env, 0, 1)
                else:
                    self.move(env, 0, -1)
                    
        elif self.state == State.ATTACKING:
            # Temporary attack logic
            threats = env.get_adjacent(self.x, self.y, 'T')
            if threats:
                target = threats[0]  # Attack first threat
                self.move(env, 
                    target[0]-self.x, 
                    target[1]-self.y)
                self.health -= 10
                self.attack_counter += 1
                
                if self.attack_counter > 2:  # Temp solution
                    env.grid[target[0]][target[1]] = None
                    self.state = State.WANDERING
            else:
                self.state = State.WANDERING
                
        return True