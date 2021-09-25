# game_of_life

To run the game, run rules.py using python3.6. It uses the modules pygame and numpy.

The game is zero player cellular automaton inspired by the mathematician John Conway. 

Click on cells to make them alive, or press 'f' to fill the grid with live cells, 'c' to clear the grid of live cells, 't' to turn every other cell alive, 'x' to turn every other cell alive within the central region of the grid, 'r' to randomly select cells to be alive, 'm' to randomly select cells to be alive in the central region of the grid, 'h' to randomly select cells to be alive with a high probability, 'l' to randomly select cells to be alive with a low probability.

New cells (which were not alive for the past 2 iterations) will appear red, oscillating cells (a cell which was alive 2 iterations ago) will appear yellow, stable cells (which were alive the last iteration) will appear green, and dead cells will appear black.
