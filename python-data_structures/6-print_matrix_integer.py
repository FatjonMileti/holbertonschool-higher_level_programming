#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix:
        for elem in matrix:
            for i in elem:
                print("{:d}".format(i), end="")
                if i != elem[-1]:
                    print(end=" ")
            print()
