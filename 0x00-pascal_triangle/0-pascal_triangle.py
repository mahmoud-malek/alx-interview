#!/usr/bin/python3

""" this is a module that contian a function
to get the pascal's triangle"""


def pascal_triangle(n):
    """ a function to return list of pascal's triangle """
    triangle = []

    for i in range(n):
        row = [None for _ in range(i + 1)]
        row[0], row[-1] = 1, 1

        for v in range(1, len(row) - 1):
            row[v] = triangle[i - 1][v - 1] + triangle[i - 1][v]

        triangle.append(row)

    return triangle
