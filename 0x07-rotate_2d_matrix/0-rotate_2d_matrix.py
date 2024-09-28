#!/usr/bin/python3

""" Rotate 2D Matrix """


def swap(mat, x1, y1, x2, y2):
    """ swap elements """
    mat[x1][y1], mat[x2][y2] = mat[x2][y2], mat[x1][y1]


def rotate_2d_matrix(matrix):
    """ rotating 2D matrix """
    n = len(matrix)
    for i in range(n // 2):
        for j in range(i, n - i - 1):
            swap(matrix, i, j, j, n - i - 1)
            swap(matrix, i, j, n - i - 1, n - j - 1)
            swap(matrix, i, j, n - j - 1, i)
    return matrix
