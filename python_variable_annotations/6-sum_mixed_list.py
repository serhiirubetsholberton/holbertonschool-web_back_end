#!/usr/bin/env python3
"""type-annotated function sum_mixed_list"""


from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """type-annotated function sum_mixed_list
    Args:
        mxd_lst (List[int, float]): List of integers and floats
    Returns:
        float: their sum as a float.
    """
    return sum(mxd_lst)
