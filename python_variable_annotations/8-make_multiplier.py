#!/usr/bin/env python3
""" type-annotated function make_multiplier """


from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """type-annotated function make_multiplier
    Args:
        multiplier (float): Any number as float
    Returns:
        Callable[[float], float]:
        function that multiplies a float by multiplier
    """
    return lambda x: x * multiplier
