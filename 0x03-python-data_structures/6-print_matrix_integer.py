#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    ln = len(matrix)
    for row in matrix:
        if len(row) == 0:
            print()
        for i in range(len(row)):
            if i < len(row) - 1:
                print("{:d}".format(row[i]), end=" ")
            else:
                print("{:d}".format(row[i]))
