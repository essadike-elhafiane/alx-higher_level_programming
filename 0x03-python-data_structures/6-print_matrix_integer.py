#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for r in matrix:
        for i, n in enumerate(r):
            print("{:d}".format(n), end="")
            if i < len(r) - 1:
                print(" ", end="")
        print("")
