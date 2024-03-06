#!/usr/bin/python3

"""Define Island Perimeter function."""


def island_perimeter(grid):
    """Returns the perimeter of the island described in grid."""
    return sum(
        int(prev_cell != curr_cell)
        for row in grid + list(map(list, zip(*grid)))
        for prev_cell, curr_cell in zip([0] + row, row + [0])
    )
