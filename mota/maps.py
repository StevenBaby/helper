
import numpy as np
import matplotlib.pyplot as plt

M = np.array([
    # 0
    [
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 87, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 53, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    ],
    # 1
    [
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 87, 0, 201, 202, 201, 0, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
        [1, 31, 0, 0, 81, 0, 1, 27, 21, 0, 1, 0, 1],
        [1, 0, 209, 0, 1, 0, 1, 28, 31, 0, 1, 0, 1],
        [1, 1, 81, 1, 1, 0, 1, 1, 1, 81, 1, 0, 1],
        [1, 21, 0, 0, 1, 0, 81, 205, 217, 205, 1, 0, 1],
        [1, 0, 210, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1],
        [1, 1, 81, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 1, 1, 81, 1, 1, 1, 81, 1, 1],
        [1, 31, 0, 21, 1, 21, 0, 0, 1, 0, 205, 0, 1],
        [1, 31, 46, 21, 1, 0, 0, 0, 1, 201, 32, 201, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    ],
    # 2
    [
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 88, 0, 82, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 1, 1, 0, 222, 0, 222, 0, 1, 1, 1],
        [1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1],
        [1, 0, 1, 21, 21, 1, 0, 0, 0, 1, 0, 121, 1],
        [1, 0, 1, 21, 0, 86, 0, 0, 0, 86, 0, 0, 1],
        [1, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1],
        [1, 0, 1, 123, 0, 1, 0, 0, 0, 1, 0, 122, 1],
        [1, 0, 1, 0, 0, 86, 0, 0, 0, 86, 0, 0, 1],
        [1, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1],
        [1, 0, 1, 32, 32, 1, 0, 0, 0, 1, 0, 0, 1],
        [1, 87, 1, 32, 0, 86, 0, 0, 0, 86, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    ],
    # 3
    [
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 21, 28, 1, 21, 32, 21, 1, 0, 1, 0, 31, 1],
        [1, 0, 31, 1, 32, 21, 32, 1, 0, 81, 205, 0, 1],
        [1, 217, 0, 1, 21, 22, 21, 1, 0, 1, 1, 1, 1],
        [1, 81, 1, 1, 1, 0, 1, 1, 0, 1, 0, 121, 1],
        [1, 0, 0, 205, 0, 0, 0, 201, 0, 0, 0, 0, 1],
        [1, 81, 1, 1, 0, 0, 0, 1, 0, 1, 1, 1, 1],
        [1, 209, 0, 1, 1, 245, 1, 1, 0, 1, 0, 31, 1],
        [1, 0, 21, 1, 0, 126, 0, 1, 0, 81, 217, 21, 1],
        [1, 31, 27, 1, 126, 0, 126, 1, 0, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 126, 1, 1, 202, 1, 0, 0, 1],
        [1, 88, 0, 0, 0, 0, 0, 1, 0, 81, 0, 87, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    ],
    # 4
    [
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 22, 0, 1, 7, 131, 8, 1, 0, 121, 0, 1],
        [1, 31, 0, 21, 1, 0, 0, 0, 1, 21, 0, 32, 1],
        [1, 0, 217, 0, 1, 0, 0, 0, 1, 0, 210, 0, 1],
        [1, 1, 81, 1, 1, 1, 82, 1, 1, 1, 81, 1, 1],
        [1, 0, 0, 0, 81, 0, 202, 0, 0, 209, 0, 0, 1],
        [1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 202, 0, 201, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 81, 1, 1, 81, 1, 1, 1, 81, 1, 1, 81, 1],
        [1, 0, 1, 0, 205, 0, 1, 0, 217, 0, 1, 0, 1],
        [1, 0, 1, 201, 0, 21, 1, 27, 0, 31, 1, 0, 1],
        [1, 87, 1, 21, 201, 21, 1, 0, 201, 0, 1, 88, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    ],
    # 5
    [
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 87, 1, 0, 202, 81, 0, 1, 0, 0, 81, 0, 1],
        [1, 0, 1, 0, 0, 1, 21, 1, 201, 201, 1, 202, 1],
        [1, 0, 81, 205, 0, 1, 0, 1, 21, 21, 1, 0, 1],
        [1, 1, 1, 1, 81, 1, 205, 1, 21, 21, 1, 0, 1],
        [1, 21, 0, 217, 0, 1, 0, 1, 1, 1, 1, 0, 1],
        [1, 21, 0, 0, 205, 1, 0, 201, 0, 0, 0, 0, 1],
        [1, 1, 210, 1, 1, 1, 0, 1, 1, 1, 1, 202, 1],
        [1, 0, 0, 0, 0, 1, 201, 1, 0, 0, 0, 0, 1],
        [1, 28, 21, 31, 73, 1, 0, 1, 81, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 0, 1],
        [1, 88, 0, 0, 0, 0, 0, 1, 0, 3, 0, 35, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    ],
    # 6
    [
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 88, 1, 21, 21, 1, 0, 217, 0, 21, 201, 0, 1],
        [1, 0, 1, 21, 21, 1, 0, 1, 1, 1, 1, 81, 1],
        [1, 0, 1, 1, 202, 1, 0, 1, 31, 0, 209, 0, 1],
        [1, 0, 81, 81, 0, 81, 0, 1, 122, 0, 0, 205, 1],
        [1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 202, 217, 0, 21, 0, 209, 210, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1],
        [1, 217, 0, 0, 121, 1, 0, 81, 81, 0, 81, 0, 1],
        [1, 0, 205, 0, 28, 1, 0, 1, 1, 202, 1, 202, 1],
        [1, 81, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 1],
        [1, 0, 201, 0, 0, 209, 0, 1, 31, 31, 1, 87, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    ],
    # 7
    [
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 87, 1, 27, 1, 0, 122, 0, 1, 21, 1, 201, 1],
        [1, 0, 1, 31, 1, 0, 0, 0, 1, 21, 1, 202, 1],
        [1, 0, 1, 205, 1, 202, 1, 210, 1, 31, 1, 201, 1],
        [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
        [1, 81, 1, 81, 1, 82, 1, 81, 1, 209, 1, 81, 1],
        [1, 0, 210, 0, 217, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 81, 1, 81, 1, 81, 1, 81, 1, 210, 1, 81, 1],
        [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
        [1, 0, 1, 0, 1, 205, 1, 202, 1, 32, 1, 0, 1],
        [1, 201, 1, 201, 1, 21, 1, 217, 1, 21, 1, 0, 1],
        [1, 0, 202, 0, 1, 21, 1, 32, 1, 21, 1, 88, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    ],
    # 8
    [
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 88, 0, 81, 81, 0, 87, 0, 1, 21, 0, 21, 1],
        [1, 0, 0, 1, 1, 0, 0, 201, 1, 0, 23, 0, 1],
        [1, 81, 1, 1, 1, 1, 81, 1, 1, 32, 0, 31, 1],
        [1, 0, 1, 21, 21, 21, 0, 0, 1, 1, 85, 1, 1],
        [1, 31, 1, 1, 1, 1, 1, 217, 1, 221, 0, 221, 1],
        [1, 0, 202, 201, 202, 0, 1, 0, 1, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 81, 1, 205, 1, 1, 81, 1, 1],
        [1, 0, 0, 0, 205, 0, 209, 0, 217, 0, 0, 0, 1],
        [1, 81, 1, 1, 1, 1, 1, 1, 1, 1, 1, 81, 1],
        [1, 201, 0, 1, 27, 21, 1, 22, 31, 1, 0, 209, 1],
        [1, 0, 205, 82, 21, 28, 1, 21, 0, 81, 210, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    ],
    # 9
    [
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 209, 81, 0, 88, 0, 81, 201, 0, 31, 1],
        [1, 0, 21, 0, 1, 0, 0, 0, 1, 0, 201, 0, 1],
        [1, 210, 1, 1, 1, 1, 82, 1, 1, 1, 1, 0, 1],
        [1, 0, 21, 0, 1, 21, 0, 21, 81, 81, 0, 0, 1],
        [1, 28, 0, 205, 81, 0, 27, 0, 1, 1, 3, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 202, 1, 0, 0, 210, 1],
        [1, 21, 0, 81, 210, 21, 1, 0, 1, 36, 1, 0, 1],
        [1, 210, 0, 1, 0, 0, 1, 0, 1, 1, 1, 81, 1],
        [1, 81, 1, 1, 1, 81, 1, 0, 1, 21, 0, 217, 1],
        [1, 0, 31, 1, 0, 209, 1, 205, 1, 0, 209, 0, 1],
        [1, 87, 0, 82, 0, 0, 81, 0, 81, 217, 0, 31, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    ],
    # 10
    [
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1],
        [1, 209, 209, 209, 1, 1, 0, 1, 1, 209, 209, 209, 1],
        [1, 0, 210, 0, 85, 0, 211, 0, 85, 0, 210, 0, 1],
        [1, 1, 1, 1, 1, 0, 127, 0, 1, 1, 1, 1, 1],
        [1, 209, 28, 209, 1, 1, 0, 1, 1, 209, 27, 209, 1],
        [1, 0, 210, 0, 1, 1, 0, 1, 1, 0, 210, 0, 1],
        [1, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 1],
        [1, 81, 1, 81, 1, 1, 83, 1, 1, 81, 1, 81, 1],
        [1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1],
        [1, 88, 1, 0, 217, 0, 0, 0, 217, 0, 1, 32, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    ],
    # 11
    [
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 1, 27, 0, 81, 0, 1, 31, 21, 1],
        [1, 0, 38, 0, 1, 0, 205, 1, 213, 1, 0, 0, 1],
        [1, 0, 0, 0, 1, 81, 1, 1, 0, 81, 0, 0, 1],
        [1, 1, 85, 1, 1, 0, 206, 1, 1, 1, 1, 203, 1],
        [1, 218, 0, 218, 1, 213, 0, 81, 218, 0, 1, 0, 1],
        [1, 0, 0, 0, 1, 1, 1, 1, 0, 31, 1, 0, 1],
        [1, 32, 0, 0, 206, 0, 0, 81, 203, 0, 1, 0, 1],
        [1, 1, 82, 1, 1, 1, 1, 1, 1, 1, 1, 206, 1],
        [1, 0, 206, 0, 203, 81, 0, 0, 0, 0, 205, 0, 1],
        [1, 21, 0, 0, 0, 1, 0, 1, 1, 81, 1, 0, 1],
        [1, 21, 21, 21, 21, 1, 88, 1, 32, 206, 1, 87, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    ],
    # 12
    [
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 122, 3, 0, 1, 21, 27, 21, 1, 0, 3, 3, 1],
        [1, 1, 1, 206, 1, 0, 1, 0, 1, 0, 1, 1, 1],
        [1, 0, 0, 0, 1, 218, 0, 218, 1, 0, 213, 0, 1],
        [1, 81, 1, 1, 1, 1, 81, 1, 1, 1, 1, 0, 1],
        [1, 0, 218, 0, 81, 0, 213, 0, 1, 31, 0, 206, 1],
        [1, 1, 1, 1, 1, 0, 0, 218, 81, 0, 28, 0, 1],
        [1, 21, 21, 0, 1, 0, 32, 0, 1, 21, 0, 203, 1],
        [1, 21, 22, 0, 1, 1, 1, 1, 1, 82, 1, 81, 1],
        [1, 0, 0, 213, 1, 7, 131, 8, 1, 203, 0, 213, 1],
        [1, 1, 1, 81, 1, 31, 0, 31, 1, 1, 0, 1, 1],
        [1, 87, 0, 0, 205, 0, 0, 0, 205, 0, 0, 88, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    ],
    # 13
    [
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 1],
        [1, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 1],
        [1, 5, 5, 5, 5, 1, 1, 1, 5, 5, 5, 5, 1],
        [1, 5, 5, 5, 1, 1, 1, 1, 1, 5, 5, 5, 1],
        [1, 5, 5, 5, 1, 1, 43, 1, 1, 5, 5, 5, 1],
        [1, 5, 5, 5, 1, 1, 5, 1, 1, 5, 5, 5, 1],
        [1, 5, 5, 5, 5, 1, 5, 1, 5, 5, 5, 5, 1],
        [1, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 1],
        [1, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 1],
        [1, 1, 1, 1, 1, 1, 81, 1, 1, 1, 1, 1, 1],
        [1, 88, 0, 0, 0, 0, 0, 0, 0, 0, 0, 87, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    ],
    # 14
    [
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 214, 0, 214, 1, 28, 21, 31, 1, 21, 21, 21, 1],
        [1, 0, 214, 0, 1, 203, 1, 214, 1, 0, 0, 21, 1],
        [1, 1, 0, 0, 1, 0, 1, 0, 1, 1, 81, 1, 1],
        [1, 1, 82, 1, 1, 82, 1, 81, 1, 0, 214, 0, 1],
        [1, 31, 0, 0, 206, 0, 215, 0, 206, 0, 0, 0, 1],
        [1, 0, 203, 0, 1, 1, 81, 1, 1, 31, 0, 213, 1],
        [1, 81, 1, 81, 1, 0, 0, 0, 1, 1, 1, 81, 1],
        [1, 0, 1, 0, 213, 0, 81, 0, 203, 0, 203, 0, 1],
        [1, 218, 1, 218, 1, 1, 2, 1, 1, 81, 1, 1, 1],
        [1, 0, 1, 0, 1, 31, 0, 0, 1, 0, 0, 0, 1],
        [1, 22, 1, 0, 81, 0, 87, 0, 1, 0, 0, 88, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    ],
    # 15
    [
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 28, 214, 0, 81, 0, 87, 0, 1, 123, 0, 0, 1],
        [1, 213, 0, 0, 1, 0, 0, 0, 1, 0, 0, 203, 1],
        [1, 0, 0, 203, 1, 1, 85, 1, 1, 1, 1, 81, 1],
        [1, 81, 1, 1, 1, 0, 47, 0, 1, 206, 0, 0, 1],
        [1, 0, 1, 21, 1, 181, 182, 183, 1, 0, 206, 0, 1],
        [1, 0, 1, 22, 1, 184, 185, 186, 1, 81, 1, 218, 1],
        [1, 203, 1, 21, 1, 187, 258, 188, 1, 0, 1, 0, 1],
        [1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 32, 1],
        [1, 0, 81, 0, 1, 1, 0, 1, 1, 81, 1, 1, 1],
        [1, 206, 1, 206, 1, 0, 0, 0, 1, 0, 205, 0, 1],
        [1, 0, 218, 0, 1, 0, 88, 0, 81, 205, 0, 122, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    ],
    # 16
    [
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 21, 206, 0, 1, 0, 88, 0, 1, 0, 0, 206, 1],
        [1, 21, 218, 0, 81, 0, 0, 0, 81, 203, 0, 0, 1],
        [1, 21, 206, 0, 1, 213, 0, 21, 1, 0, 0, 31, 1],
        [1, 1, 1, 1, 1, 1, 82, 1, 1, 1, 81, 1, 1],
        [1, 27, 21, 0, 1, 31, 0, 0, 1, 0, 213, 0, 1],
        [1, 31, 0, 215, 81, 0, 214, 0, 1, 0, 0, 0, 1],
        [1, 28, 21, 0, 1, 0, 0, 21, 1, 206, 0, 22, 1],
        [1, 1, 3, 1, 1, 1, 81, 1, 1, 1, 81, 1, 1],
        [1, 0, 203, 0, 1, 206, 0, 206, 1, 0, 218, 0, 1],
        [1, 0, 0, 0, 81, 0, 0, 0, 81, 0, 1, 1, 1],
        [1, 121, 0, 0, 1, 0, 87, 0, 1, 216, 3, 320, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    ],
    # 17
    [
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 1, 0, 87, 0, 1, 27, 0, 28, 1],
        [1, 0, 37, 0, 1, 0, 0, 0, 1, 0, 32, 0, 1],
        [1, 0, 0, 0, 1, 214, 1, 206, 1, 21, 0, 21, 1],
        [1, 1, 85, 1, 1, 0, 1, 0, 1, 1, 85, 1, 1],
        [1, 221, 0, 221, 1, 81, 1, 82, 1, 214, 0, 214, 1],
        [1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1],
        [1, 1, 85, 1, 1, 213, 1, 203, 1, 1, 85, 1, 1],
        [1, 221, 0, 221, 1, 0, 0, 0, 1, 213, 0, 213, 1],
        [1, 0, 0, 0, 1, 1, 218, 1, 1, 0, 0, 0, 1],
        [1, 1, 81, 1, 1, 0, 0, 0, 1, 1, 81, 1, 1],
        [1, 31, 0, 0, 206, 0, 88, 0, 206, 0, 0, 31, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    ],
    # 18
    [
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 87, 0, 0, 82, 0, 88, 0, 81, 218, 0, 21, 1],
        [1, 0, 0, 121, 1, 0, 0, 0, 1, 0, 203, 21, 1],
        [1, 81, 1, 1, 1, 1, 3, 1, 1, 0, 0, 22, 1],
        [1, 0, 31, 0, 81, 214, 0, 214, 81, 213, 0, 21, 1],
        [1, 215, 0, 215, 1, 0, 0, 0, 1, 0, 206, 21, 1],
        [1, 1, 1, 1, 1, 1, 82, 1, 1, 1, 1, 1, 1],
        [1, 0, 213, 0, 0, 0, 0, 0, 0, 0, 215, 0, 1],
        [1, 81, 1, 1, 81, 1, 1, 1, 81, 1, 1, 81, 1],
        [1, 218, 0, 1, 206, 206, 1, 203, 203, 1, 0, 218, 1],
        [1, 0, 21, 1, 206, 206, 1, 203, 203, 1, 21, 0, 1],
        [1, 31, 27, 1, 0, 21, 1, 21, 0, 1, 28, 31, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    ],
    # 19
    [
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 88, 0, 1, 31, 0, 218, 0, 22, 1, 21, 27, 1],
        [1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 206, 0, 1],
        [1, 81, 1, 1, 214, 1, 321, 1, 214, 1, 81, 1, 1],
        [1, 205, 0, 1, 0, 0, 3, 0, 0, 1, 0, 0, 1],
        [1, 0, 0, 1, 21, 0, 1, 0, 21, 1, 203, 203, 1],
        [1, 81, 1, 1, 0, 215, 0, 215, 0, 1, 0, 0, 1],
        [1, 206, 0, 1, 1, 1, 82, 1, 1, 1, 1, 81, 1],
        [1, 0, 0, 203, 0, 0, 0, 0, 214, 0, 0, 213, 1],
        [1, 81, 1, 1, 1, 1, 214, 1, 1, 31, 21, 0, 1],
        [1, 0, 1, 0, 81, 21, 0, 21, 1, 1, 1, 206, 1],
        [1, 203, 0, 206, 1, 0, 87, 0, 81, 0, 205, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    ],
    # 20
    [
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 87, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 85, 1, 1, 1, 1, 1, 1],
        [1, 28, 27, 1, 0, 0, 0, 0, 0, 1, 31, 32, 1],
        [1, 21, 0, 1, 0, 206, 206, 206, 0, 1, 0, 21, 1],
        [1, 1, 82, 1, 0, 206, 0, 206, 0, 1, 82, 1, 1],
        [1, 205, 0, 1, 0, 206, 206, 206, 0, 1, 0, 205, 1],
        [1, 0, 205, 1, 0, 0, 127, 0, 0, 1, 205, 0, 1],
        [1, 81, 1, 1, 1, 1, 83, 1, 1, 1, 1, 81, 1],
        [1, 0, 215, 0, 1, 0, 0, 0, 1, 0, 215, 0, 1],
        [1, 31, 0, 0, 218, 0, 88, 0, 218, 0, 0, 31, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    ],
    # 21
    [
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 88, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 1],
        [1, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 121, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 1],
        [1, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 87, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    ],
    # 22
    [
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 0, 87, 0, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 0, 88, 0, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    ],
    # 23
    [
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 88, 0, 0, 0, 0, 0, 0, 0, 0, 0, 87, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 121, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    ],
    # 24
    [
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1],
        [1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1],
        [1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
        [1, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 1],
        [1, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 1],
        [1, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 1],
        [1, 0, 1, 1, 1, 1, 83, 1, 1, 1, 1, 0, 1],
        [1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0, 0, 1],
        [1, 0, 87, 0, 1, 1, 0, 1, 1, 0, 0, 0, 1],
        [1, 88, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    ],
    # 25
    [
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1],
        [1, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 1],
        [1, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 1],
        [1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1],
        [1, 0, 1, 0, 0, 0, 247, 0, 0, 0, 1, 0, 1],
        [1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1],
        [1, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 1],
        [1, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 1],
        [1, 0, 88, 0, 1, 1, 83, 1, 1, 0, 0, 0, 1],
        [1, 87, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    ],
    # 26
    [
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1],
        [1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1],
        [1, 0, 1, 1, 1, 5, 5, 5, 1, 1, 1, 0, 1],
        [1, 0, 1, 1, 5, 5, 5, 5, 5, 1, 1, 0, 1],
        [1, 0, 1, 1, 5, 5, 132, 5, 5, 1, 1, 0, 1],
        [1, 0, 1, 1, 5, 5, 5, 5, 5, 1, 1, 0, 1],
        [1, 0, 1, 1, 1, 5, 83, 5, 1, 1, 1, 0, 1],
        [1, 0, 0, 1, 1, 1, 83, 1, 1, 1, 0, 0, 1],
        [1, 0, 87, 0, 1, 1, 83, 1, 1, 0, 0, 0, 1],
        [1, 88, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    ],
    # 27
    [
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 0, 121, 0, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1],
        [1, 0, 88, 1, 1, 1, 0, 1, 1, 1, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 87, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    ],
    # 28
    [
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1],
        [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1],
        [1, 0, 0, 0, 0, 0, 1, 0, 124, 0, 1, 0, 1],
        [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1],
        [1, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 87, 0, 0, 0, 0, 0, 0, 0, 0, 0, 88, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    ],
    # 29
    [
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1],
        [1, 0, 0, 1, 1, 0, 123, 0, 1, 1, 1, 1, 1],
        [1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1],
        [1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1],
        [1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1],
        [1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1],
        [1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1],
        [1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1],
        [1, 88, 0, 1, 1, 0, 87, 0, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    ],
    # 30
    [
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 0, 87, 0, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 85, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 203, 202, 201, 0, 201, 202, 203, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 0, 88, 0, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    ],
    # 31
    [
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 21, 21, 1, 88, 1, 0, 0, 31, 121, 1],
        [1, 224, 0, 21, 21, 1, 0, 1, 225, 0, 0, 0, 1],
        [1, 0, 225, 1, 1, 1, 0, 1, 81, 1, 212, 212, 1],
        [1, 0, 0, 81, 22, 1, 0, 1, 27, 1, 0, 0, 1],
        [1, 81, 1, 1, 1, 1, 0, 1, 1, 1, 1, 81, 1],
        [1, 0, 212, 0, 0, 0, 0, 0, 0, 0, 212, 0, 1],
        [1, 81, 1, 1, 1, 1, 0, 1, 1, 1, 1, 81, 1],
        [1, 0, 0, 1, 28, 1, 214, 1, 32, 81, 0, 0, 1],
        [1, 212, 212, 1, 81, 1, 214, 1, 1, 1, 216, 0, 1],
        [1, 0, 0, 0, 227, 1, 0, 1, 21, 21, 0, 216, 1],
        [1, 122, 31, 0, 0, 1, 87, 1, 21, 21, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    ],
    # 32
    [
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 28, 0, 82, 0, 0, 0, 0, 0, 0, 0, 87, 1],
        [1, 0, 27, 1, 1, 1, 0, 1, 1, 1, 0, 0, 1],
        [1, 81, 1, 1, 0, 81, 0, 81, 0, 1, 1, 1, 1],
        [1, 225, 0, 216, 0, 1, 0, 1, 212, 1, 21, 32, 1],
        [1, 0, 21, 0, 216, 1, 0, 1, 0, 81, 0, 21, 1],
        [1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1],
        [1, 21, 21, 21, 21, 1, 0, 1, 227, 1, 21, 22, 1],
        [1, 0, 0, 0, 22, 1, 0, 1, 0, 81, 0, 21, 1],
        [1, 1, 85, 1, 1, 1, 226, 1, 1, 1, 1, 1, 1],
        [1, 222, 0, 222, 0, 0, 127, 0, 0, 7, 131, 8, 1],
        [1, 0, 0, 0, 0, 88, 0, 1, 212, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    ],
    # 33
    [
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 87, 0, 81, 214, 0, 216, 81, 0, 0, 0, 88, 1],
        [1, 0, 0, 1, 0, 31, 0, 1, 81, 1, 1, 1, 1],
        [1, 82, 1, 1, 121, 0, 21, 1, 0, 0, 0, 32, 1],
        [1, 0, 31, 1, 1, 81, 1, 1, 1, 1, 0, 1, 1],
        [1, 216, 0, 1, 0, 0, 214, 0, 1, 212, 127, 212, 1],
        [1, 0, 0, 1, 224, 1, 1, 81, 1, 0, 0, 0, 1],
        [1, 0, 216, 81, 0, 0, 212, 0, 1, 225, 0, 225, 1],
        [1, 81, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1],
        [1, 0, 0, 214, 1, 0, 225, 0, 1, 0, 0, 0, 1],
        [1, 224, 1, 0, 1, 21, 1, 216, 0, 127, 39, 0, 1],
        [1, 21, 225, 0, 82, 0, 81, 0, 1, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    ],
    # 34
    [
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 88, 0, 31, 1, 0, 21, 0, 1, 21, 21, 28, 1],
        [1, 0, 0, 0, 81, 216, 0, 227, 81, 0, 21, 31, 1],
        [1, 0, 216, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 81, 1, 1, 201, 1, 224, 1, 203, 1, 225, 1],
        [1, 0, 0, 0, 1, 81, 1, 81, 1, 81, 1, 81, 1],
        [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 1, 81, 1, 81, 1, 81, 1, 81, 1],
        [1, 1, 81, 1, 1, 212, 1, 202, 1, 227, 1, 205, 1],
        [1, 0, 0, 212, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 224, 1, 0, 81, 0, 0, 0, 81, 225, 0, 31, 1],
        [1, 32, 225, 0, 1, 0, 87, 0, 1, 0, 21, 27, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    ],
    # 35
    [
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 2, 2, 2, 2, 0, 0, 0, 0, 0, 0, 87, 1],
        [1, 2, 1, 1, 1, 1, 85, 1, 1, 1, 1, 1, 1],
        [1, 2, 1, 2, 1, 32, 32, 32, 1, 1, 1, 1, 1],
        [1, 2, 1, 2, 1, 0, 54, 0, 1, 1, 1, 1, 1],
        [1, 2, 1, 2, 1, 189, 190, 191, 1, 1, 1, 1, 1],
        [1, 2, 1, 2, 1, 192, 193, 194, 1, 1, 1, 1, 1],
        [1, 2, 1, 2, 1, 195, 257, 196, 1, 1, 1, 1, 1],
        [1, 2, 1, 2, 1, 0, 0, 0, 1, 1, 1, 1, 1],
        [1, 2, 1, 2, 1, 0, 0, 0, 1, 1, 1, 1, 1],
        [1, 2, 1, 2, 1, 0, 0, 0, 1, 1, 1, 1, 1],
        [1, 2, 2, 2, 1, 0, 88, 0, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    ],
    # 36
    [
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 121, 0, 225, 0, 0, 0, 214, 0, 227, 0, 88, 1],
        [1, 0, 0, 1, 1, 1, 81, 1, 1, 1, 0, 0, 1],
        [1, 216, 1, 1, 1, 1, 0, 1, 1, 1, 1, 216, 1],
        [1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1],
        [1, 227, 1, 1, 1, 0, 212, 0, 1, 1, 1, 224, 1],
        [1, 0, 81, 0, 0, 216, 0, 216, 0, 0, 81, 0, 1],
        [1, 0, 1, 1, 1, 0, 227, 0, 1, 1, 1, 227, 1],
        [1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1],
        [1, 224, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1],
        [1, 0, 0, 1, 1, 1, 81, 1, 1, 1, 0, 0, 1],
        [1, 32, 0, 225, 0, 21, 0, 214, 0, 224, 0, 87, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    ],
    # 37
    [
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 87, 0, 81, 0, 0, 0, 0, 0, 225, 0, 32, 1],
        [1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1],
        [1, 82, 1, 1, 31, 31, 1, 31, 31, 1, 1, 227, 1],
        [1, 0, 1, 31, 31, 21, 1, 31, 31, 31, 1, 0, 1],
        [1, 0, 1, 21, 21, 49, 1, 23, 21, 21, 1, 0, 1],
        [1, 31, 1, 1, 1, 1, 1, 1, 1, 1, 1, 224, 1],
        [1, 0, 1, 28, 27, 32, 1, 27, 27, 27, 1, 0, 1],
        [1, 0, 1, 21, 21, 21, 1, 28, 28, 28, 1, 0, 1],
        [1, 225, 1, 1, 22, 22, 1, 32, 21, 1, 1, 227, 1],
        [1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1],
        [1, 121, 0, 216, 0, 0, 0, 0, 0, 212, 0, 88, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    ],
    # 38
    [
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 88, 0, 83, 216, 0, 0, 0, 216, 81, 0, 87, 1],
        [1, 0, 0, 1, 0, 122, 21, 0, 0, 1, 0, 0, 1],
        [1, 212, 1, 1, 1, 1, 1, 81, 1, 1, 1, 81, 1],
        [1, 0, 0, 225, 225, 0, 1, 0, 1, 21, 1, 0, 1],
        [1, 1, 0, 1, 1, 82, 1, 0, 1, 21, 1, 0, 1],
        [1, 0, 127, 0, 82, 82, 1, 212, 1, 21, 1, 212, 1],
        [1, 0, 40, 0, 1, 1, 1, 224, 1, 0, 227, 0, 1],
        [1, 0, 0, 0, 1, 28, 31, 0, 1, 1, 1, 81, 1],
        [1, 1, 85, 1, 1, 1, 1, 1, 1, 21, 0, 212, 1],
        [1, 222, 0, 222, 1, 0, 0, 0, 1, 0, 227, 0, 1],
        [1, 0, 0, 0, 81, 224, 0, 213, 81, 225, 0, 32, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    ],
    # 39
    [
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 88, 1],
        [1, 0, 81, 0, 81, 0, 81, 0, 1, 122, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 21, 1],
        [1, 0, 81, 0, 81, 0, 81, 0, 1, 1, 81, 1, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 225, 1],
        [1, 0, 81, 0, 81, 0, 81, 0, 1, 216, 1, 27, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 212, 1],
        [1, 1, 82, 1, 1, 1, 1, 1, 1, 1, 81, 1, 1],
        [1, 0, 0, 212, 1, 224, 28, 227, 1, 0, 227, 0, 1],
        [1, 1, 212, 0, 81, 0, 1, 0, 81, 0, 0, 0, 1],
        [1, 121, 0, 21, 1, 0, 216, 0, 1, 31, 0, 87, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    ],
    # 40
    [
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 226, 0, 0, 0, 0, 0, 1],
        [1, 0, 224, 224, 224, 0, 0, 0, 227, 227, 227, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 212, 212, 212, 0, 225, 225, 225, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1],
        [1, 1, 1, 1, 0, 0, 127, 0, 0, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 83, 1, 1, 1, 1, 1, 1],
        [1, 28, 21, 0, 1, 216, 0, 216, 1, 31, 224, 0, 1],
        [1, 32, 0, 0, 1, 0, 0, 0, 1, 225, 0, 0, 1],
        [1, 27, 0, 227, 82, 0, 0, 0, 81, 0, 0, 88, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    ],
    # 41
    [
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 31, 1, 0, 22, 1, 88, 1, 22, 0, 1, 31, 1],
        [1, 81, 220, 0, 0, 1, 0, 1, 0, 0, 2, 81, 1],
        [1, 81, 1, 0, 1, 1, 0, 1, 1, 0, 1, 81, 1],
        [1, 81, 1, 81, 1, 246, 0, 246, 1, 81, 1, 81, 1],
        [1, 0, 0, 219, 1, 1, 0, 1, 1, 219, 0, 0, 1],
        [1, 207, 0, 0, 0, 82, 0, 82, 0, 0, 0, 207, 1],
        [1, 0, 207, 0, 204, 1, 81, 1, 204, 0, 207, 0, 1],
        [1, 81, 1, 1, 81, 1, 81, 1, 81, 1, 1, 81, 1],
        [1, 81, 1, 31, 0, 1, 81, 1, 0, 31, 1, 81, 1],
        [1, 81, 1, 21, 21, 1, 0, 1, 21, 21, 1, 81, 1],
        [1, 32, 1, 21, 27, 1, 87, 1, 28, 21, 1, 32, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    ],
    # 42
    [
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 87, 0, 0, 1, 0, 0, 23, 1, 21, 22, 21, 1],
        [1, 0, 0, 204, 1, 0, 0, 0, 1, 21, 21, 21, 1],
        [1, 1, 1, 81, 1, 0, 0, 0, 1, 1, 0, 1, 1],
        [1, 121, 0, 0, 1, 1, 228, 1, 1, 219, 0, 220, 1],
        [1, 0, 0, 204, 81, 0, 0, 0, 81, 0, 0, 0, 1],
        [1, 81, 1, 1, 1, 1, 0, 1, 1, 0, 0, 219, 1],
        [1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 1, 1],
        [1, 1, 1, 207, 1, 0, 0, 0, 1, 246, 0, 246, 1],
        [1, 32, 21, 21, 1, 1, 0, 1, 1, 1, 0, 1, 1],
        [1, 207, 1, 1, 1, 0, 0, 0, 1, 21, 21, 21, 1],
        [1, 21, 21, 28, 1, 0, 88, 0, 1, 21, 22, 21, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    ],
    # 43
    [
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 88, 0, 81, 0, 204, 0, 81, 81, 246, 0, 0, 1],
        [1, 0, 0, 1, 1, 1, 0, 1, 330, 0, 1, 0, 1],
        [1, 0, 0, 81, 0, 1, 228, 1, 0, 0, 1, 0, 1],
        [1, 82, 1, 1, 220, 1, 0, 228, 0, 42, 1, 0, 1],
        [1, 0, 204, 0, 0, 1, 1, 1, 1, 1, 1, 81, 1],
        [1, 0, 1, 81, 1, 1, 32, 0, 81, 0, 0, 0, 1],
        [1, 0, 1, 0, 0, 204, 0, 0, 1, 219, 0, 31, 1],
        [1, 81, 1, 1, 1, 1, 1, 1, 1, 0, 21, 0, 1],
        [1, 0, 207, 1, 32, 0, 228, 0, 1, 1, 1, 81, 1],
        [1, 0, 0, 1, 32, 1, 1, 0, 81, 0, 207, 0, 1],
        [1, 87, 0, 1, 32, 0, 82, 0, 1, 0, 0, 22, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    ],
    # 44
    [
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 87, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 1, 1, 31, 1, 1, 0, 0, 0, 1],
        [1, 0, 0, 1, 1, 31, 44, 31, 1, 1, 0, 0, 1],
        [1, 0, 0, 0, 1, 1, 31, 1, 1, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 1, 85, 1, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 223, 0, 223, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    ],
    # 45
    [
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 88, 0, 0, 0, 0, 0, 0, 0, 0, 0, 87, 1],
        [1, 1, 1, 1, 1, 1, 81, 1, 1, 1, 1, 1, 1],
        [1, 27, 27, 0, 1, 219, 0, 220, 1, 122, 0, 0, 1],
        [1, 82, 1, 228, 1, 0, 0, 0, 1, 0, 0, 204, 1],
        [1, 28, 28, 0, 1, 220, 0, 219, 1, 1, 1, 81, 1],
        [1, 82, 1, 228, 1, 1, 81, 1, 1, 121, 1, 0, 1],
        [1, 0, 0, 0, 81, 0, 0, 207, 0, 0, 0, 21, 1],
        [1, 1, 83, 1, 1, 1, 1, 1, 1, 1, 220, 0, 1],
        [1, 0, 0, 0, 1, 228, 0, 1, 246, 1, 1, 81, 1],
        [1, 0, 51, 0, 85, 0, 0, 85, 0, 81, 0, 0, 1],
        [1, 0, 0, 0, 1, 228, 0, 1, 246, 1, 0, 32, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    ],
    # 46
    [
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 220, 81, 0, 7, 131, 8, 0, 82, 0, 88, 1],
        [1, 31, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1],
        [1, 27, 0, 1, 1, 1, 1, 1, 1, 1, 1, 81, 1],
        [1, 0, 219, 81, 0, 0, 0, 0, 0, 207, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 81, 1],
        [1, 225, 0, 224, 0, 227, 1, 31, 0, 81, 204, 0, 1],
        [1, 0, 1, 1, 1, 0, 1, 0, 220, 1, 0, 0, 1],
        [1, 213, 1, 26, 1, 204, 1, 81, 1, 1, 1, 81, 1],
        [1, 0, 1, 0, 219, 0, 1, 0, 121, 1, 219, 0, 1],
        [1, 206, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1],
        [1, 0, 209, 0, 202, 0, 82, 0, 0, 81, 0, 87, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    ],
    # 47
    [
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 87, 0, 82, 0, 0, 0, 81, 0, 0, 0, 21, 1],
        [1, 0, 0, 1, 0, 122, 0, 1, 229, 1, 1, 28, 1],
        [1, 0, 1, 1, 1, 1, 1, 1, 0, 204, 0, 21, 1],
        [1, 0, 1, 0, 81, 220, 0, 1, 81, 1, 1, 1, 1],
        [1, 0, 1, 207, 1, 0, 219, 1, 0, 219, 0, 0, 1],
        [1, 0, 81, 0, 1, 0, 0, 1, 21, 0, 0, 207, 1],
        [1, 0, 1, 0, 1, 22, 21, 1, 1, 1, 1, 81, 1],
        [1, 0, 1, 0, 82, 27, 28, 1, 0, 0, 0, 0, 1],
        [1, 229, 1, 1, 1, 1, 1, 1, 204, 1, 1, 1, 1],
        [1, 0, 0, 1, 31, 0, 27, 1, 0, 1, 0, 0, 1],
        [1, 0, 0, 81, 0, 219, 0, 81, 0, 0, 0, 88, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    ],
    # 48
    [
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 32, 0, 1, 0, 0, 31, 31, 31, 0, 0, 1],
        [1, 0, 0, 121, 1, 82, 1, 1, 1, 1, 1, 82, 1],
        [1, 0, 220, 0, 1, 0, 1, 246, 1, 246, 1, 0, 1],
        [1, 1, 82, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 204, 0, 0, 1, 246, 1, 246, 1, 0, 1],
        [1, 0, 1, 1, 81, 1, 1, 1, 1, 1, 1, 0, 1],
        [1, 207, 1, 0, 219, 0, 1, 0, 0, 0, 219, 0, 1],
        [1, 0, 1, 27, 0, 31, 1, 1, 85, 1, 1, 0, 1],
        [1, 219, 1, 1, 81, 1, 1, 0, 0, 0, 1, 0, 1],
        [1, 0, 1, 0, 228, 0, 1, 0, 41, 0, 1, 0, 1],
        [1, 87, 1, 28, 0, 32, 1, 0, 0, 0, 1, 88, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    ],
    # 49
    [
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1],
        [1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1],
        [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
        [1, 0, 1, 0, 0, 0, 127, 0, 0, 0, 1, 0, 1],
        [1, 0, 1, 0, 1, 1, 85, 1, 1, 0, 1, 0, 1],
        [1, 0, 1, 0, 1, 228, 0, 228, 1, 0, 1, 0, 1],
        [1, 0, 0, 0, 1, 1, 85, 1, 1, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 220, 0, 220, 1, 1, 1, 1, 1],
        [1, 88, 0, 83, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    ],
    # 50
    [
        [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4],
        [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4],
        [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4],
        [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4],
        [4, 4, 4, 4, 1, 1, 1, 1, 1, 4, 4, 4, 4],
        [4, 4, 4, 4, 1, 0, 123, 0, 1, 4, 4, 4, 4],
        [4, 4, 4, 4, 1, 0, 0, 0, 1, 4, 4, 4, 4],
        [4, 4, 4, 4, 1, 0, 0, 0, 1, 4, 4, 4, 4],
        [4, 4, 4, 4, 1, 1, 1, 1, 1, 4, 4, 4, 4],
        [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4],
        [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4],
        [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4],
        [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4]
    ],
])
