#!/usr/bin/env python3
"""
duck notation
"""

from typing import Iterable, Sequence, List, Union, Any


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """argument the code"""
    if lst:
        return lst[0]
    else:
        return None
