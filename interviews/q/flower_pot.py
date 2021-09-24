"""
I have a flower pot with a water particle sensor.
When I pour water into it, I want to tell if the water reaches the bottom of the pot.
The sensor provides a 2D grid of 1s and 0s. The 1s represent a solid ground and the 0s represent stones.
In short, given a grid of 1s and 0s determine whether there is a path of 1s from the top to the bottom of the grid.
The path cannot travel diagonally, nor can the water travel back upwards, due to the force of gravity.


[[0, 0, 0]
 [0, 1, 0]
 [0, 0, 0]]

[[0, 0, 0]
 [0, 1, 0]
 [0, 0, 1]]

"""