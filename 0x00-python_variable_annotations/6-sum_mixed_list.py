#!/usr/bin/env python3


'''A python module that which takes a list mxd_lst of integers
   and floats and returns their sum as a float.
'''


from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    '''a type_annotated function that returns float sum of mxd_lst'''

    total = 0.00
    for i in mxd_lst:
        total += i
    return total
