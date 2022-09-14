#!/usr/bin/python3
def weight_average(my_list=[]):
    num = 0
    em = 0
    for elem in my_list:
        num += elem[0] * elem[1]
        em += elem[1]
    return(num / em)
