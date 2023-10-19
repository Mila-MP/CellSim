# CellSim
This code is inspired by Conway's Game of life.
It simulates the growth and death of a population of cells, represented by a 2D array of which you can choose the dimensions. Each cell can be in one of two states: dead or alive. The next state of each cell is determined by the current state of its 8 neighbours and the type of the cell (regular cells or cancer cells).

# Rules for regular cells
A dead cell is represented by a dot, while a living cell is represented by a O.

- If a cell has four or more alive neighbours, it dies from overpopulation.
- If a cell has one or fewer alive neighbours, it dies from loneliness.
- If a cell is dead and has exactly 3 alive neighbours, it will come to life.
- In all other cases, the state of the cell does not change.

# Rules for cancer cells
A dead cancer cell is represented by a dot, while a living cancer cell is represented by a X.
- If a cancer cell has five or more neighbours it dies from overpopulation.
- If a cancer cell has one or fewer alive neighbours, it dies from loneliness.
- If a cancer cell is dead and had exactly 3 alive neighbours, it will come to life.
- In all other cases, the state of the cancer cell remains the same.

# Playing around with the code
This code is meant to be run from your terminal: move your current working directory to the folder where you downloaded the code, then run "python script.py". You can play around with the code in the script to generate different outputs.
