#!/usr/bin/env python3
""" type-annotated function to_kv """


from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """type-annotated function to_kv
    Args:
        k (str): any string
        v (Union[int, float]): any integer or float
    Returns:
        Tuple[str, float]:
        Tuple with two elements, a string and a square as float
    """
    return (k, v ** 2)
