#!/usr/bin/env python3
""" iterable object """


from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Element length function
    Args:
        lst (Iterable[Sequence]): Iterable list
    Returns:
        List[Tuple[Sequence, int]]:
        List of tuples, with secuence elements and size of list
    """
    return [(i, len(i)) for i in lst]
