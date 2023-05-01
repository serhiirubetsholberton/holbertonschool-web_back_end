#!/usr/bin/env python3
""" TypeVar Annonation """


from typing import Any, Mapping, TypeVar, Union

T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any, default: Union[T, None] = None)\
        -> Union[Any, T]:
    """Safely get value
    Args:
        dct (Mapping): Mapping dictionary
        key (Any): Key value of the dict
        default (Union[TypeVar, None], optional): Defaults to None.
    Returns:
        Union[Any, TypeVar]:
        Returns the element of key as any type or typevar
    """
    if key in dct:
        return dct[key]
    else:
        return default
