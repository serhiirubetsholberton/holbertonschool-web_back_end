#!/usr/bin/env python3
""" duck-typed annotations """


# The types of the elements of the input are not know
from typing import Any, Sequence, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """Safe first element function
    Args:
        lst (Sequence[Any]): Secuence in list type any
    Returns:
        Union[Any, None]: Any type or None
    """
    if lst:
        return lst[0]
    else:
        return None
