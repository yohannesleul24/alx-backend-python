#!/usr/bin/env python3
"""type-annotated function, sum_mixed_list"""

from typing import Union
import typing
import math


def sum_mixed_list(mxd_lst: typing.List[typing.Union[int, float]]) -> float:
    """
    takes a list mxd_lst of integers and floats and
    returns their sum as a float
    """
    return math.fsum(mxd_lst)
