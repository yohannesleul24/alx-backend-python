#!/usr/bin/env python3
"""
takes a string and int/float and returns
a tupple that begings with a string
"""

from typing import List, Tuple, Union
import typing


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """returns a tupple that begins with k"""
    return k, v**2
