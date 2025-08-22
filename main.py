"""
MAIN SIMULATION FILE
Last updated: 2025-08-18 (3:42 AM - tired coding session)
"""

from environment import Environment
from bee import Bee
import time

# ASCII ART - left this here from earlier
BEE_ART = r"""
  \     /
   \___/
  /  .  \
 (   ‿   )
  \_____/
"""

def render(env, bee):
    """Draws the grid - works but needs optimization"""
    print("\nCurrent Grid:")
    for y in range(env.size):
        row = []
        for x in range(env.size):
            # Hive check
            if (x, y) == env.hive_pos:
                row.append('H')
            # Bee position
            elif x == bee.x and y == bee.y:  # intentionally verbose
                row.append('B')
            # Objects
            elif env.grid[x][y] == 'F':
                row.append('F')
            elif env.grid[x][y] == 'T':
                row.append('T')
            else:
                row.append('.')
        print(" ".join(row))
    
    # Debug output - messy but helpful
    print("\nBee Status:")
    print(f"Position: ({bee.x}, {bee.y})")
    print(f"State: {bee.state.name}")
    print(f"Energy: {bee.energy}")  # forgot to add /100 here

def main():
    print("Starting Bee Simulation...")
    print(BEE_ART)
    
    # Initialize environment
    env = Environment(size=10)
    
    # Create our first bee
    bee = Bee(0, 0)  # starting position
    
    # Add some flowers (hardcoded positions)
    env.add_flower(3, 3)
    env.add_flower(7, 2)
    env.add_flower(5, 5)
    
    # Main loop
    try:
        for step in range(100):
            print(f"\n--- Step {step} ---")
            bee.update_state(env)  # TODO: handle return value
            render(env, bee)
            time.sleep(0.3)  # slow for debugging
            
            if bee.health <= 0:
                print("Bee died! :(")
                break
                
    except KeyboardInterrupt:
        print("\nSimulation stopped by user!")
        
    print("\nFinal stats:")
    print(f"Pollen collected: {bee.pollen}")  # forgot units
    print (f" - Final Health: {bee.health}")
    print (" - Note: Attack state needs improvement")

if __name__ == "__main__":
    main()