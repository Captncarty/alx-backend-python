#!/usr/bin/env python3


'''A module for returning the sum of a list'''


from typing import List


def sum_list(input_list: List[float]) -> float:
    '''A function thst returns the sum of a list'''

    total = 0.0
    for i in input_list:
        total += i
    return total
