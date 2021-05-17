# Source : https://leetcode.com/problems/path-with-minimum-effort/
# Author : foxfromworld
# Date  : 17/05/2021
# First attempt (Dijkstra's Algorithm)

"""

      col0  col1  col2
    ┌─────┬─────┬─────┐
row0│  1  │  2  │  2  │
    │(0,0)│(0,1)│(0,2)│
    ├─────┼─────┼─────┤
row1│  3  │  8  │  2  │
    │(1,0)│(1,1)│(1,2)│
    ├─────┼─────┼─────┤
row2│  5  │  3  │  5  │
    │(2,0)│(2,1)│(2,2)│
    └─────┴─────┴─────┘

Min heap
max_difference, x, y

Initial
---------------------
(0, 0, 0)

Visit (0, 0)
---------------------
(1, 0, 1)
(2, 1, 0)

Visit (0, 1)
---------------------
(1, 0, 2)
(2, 1, 0)
(6, 1, 1)

Visit (0, 2)
---------------------
(1, 1, 2)
(2, 1, 0)
(6, 1, 1)

Visit (1, 2)
---------------------
(2, 1, 0)
(3, 2, 2)
(6, 1, 1)

Visit (1, 0)
---------------------
(2, 2, 0)
(3, 2, 2)
(5, 1, 1)
(6, 1, 1)

Visit (2, 0)
---------------------
(2, 2, 1)
(3, 2, 2)
(5, 1, 1)
(6, 1, 1)

Visit (2, 1)
---------------------
(2, 2, 2)
(3, 2, 2)
(5, 1, 1)
(6, 1, 1)

Visit (2, 2)
---------------------
(3, 2, 2)
(5, 1, 1)
(6, 1, 1)

Visit (1, 1)
---------------------
(6, 1, 1)

Difference 
      col0  col1  col2
    ┌─────┬─────┬─────┐
row0│  0 │  1  │  1  │
    │(0,0)│(0,1)│(0,2)│
    ├─────┼─────┼─────┤
row1│  2  │  5  │  1  │
    │(1,0)│(1,1)│(1,2)│
    ├─────┼─────┼─────┤
row2│  2  │  2  │  2  │
    │(2,0)│(2,1)│(2,2)│
    └─────┴─────┴─────┘
"""
