#!/usr/bin/python3
def weight_average(my_list=[]):
    result = 0
    if my_list:
        weight_sum = 0
        base_sum = 0
        for i in my_list:
            base_sum += (i[0] * i[1])
            weight_sum = weight_sum + i[1]
        result = base_sum / weight_sum
    return result
