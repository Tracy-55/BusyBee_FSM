# Busy Bees FSM Simulation

# Project by Traicy Marutla

## About This Project

- The assumption is that Bees start with **engergy at 100** and **helath at 100**
- Each move costs **1 energy**
- If the health is less than/equals to 0 or energy us less than/eqyal to 0, the bees die.
- Hive and threats can share a cell with bees, but \*\*two bees cannot share a cell.
- Pheromones emitted after the attack has a radius of **10** and decays **1 per turn**

## Installation

'bash'
pip install numpy # Only dependency (for now)

### 2025-08-16 Hotfix

- Fixed `random_direction()` in utils.py (forgot import)
- Discovered during testing when bees stopped moving
