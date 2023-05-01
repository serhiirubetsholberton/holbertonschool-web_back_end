#!/usr/bin/env python3
"""type-annotated function sum_list"""


from typing import List


def sum_list(input_list: List[float]) -> float:
    """type-annotated function sum_list
    Args:
        input_list (List[float]): List of floats
    Returns:
        float: sum as a float
    """
    return sum(input_list)
