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

# How to run the program

- python main.py

# Development Diary

# 2025-08-18 (Initial Version)

- Basic FSM structure implemented
- Wandering and foraging states working
- Simple ASCII visualization

# 2025-08-19 (Bug Fixes)

- Fixed bee getting stuck at (0,0)
- Added energy system
- Improved movement logic

# 2025-08-20 (Known Issues)

1. Attack state is basic (needs pheromones)
2. Bees sometimes ignore nearby flowers
3. No swarm intelligence yet
4. Energy drain might be too fast

## Future Improvements

- [ ] Implement pheromone tracking
- [ ] Add RESTING state
- [ ] Better pathfinding to hive
