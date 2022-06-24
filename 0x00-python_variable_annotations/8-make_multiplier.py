#!/usr/bin/env python3
"""
takes a float multiplier as an argument and returns a function
that multiplies a float with an argument
"""


from typing import Callable
import typing


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """returns a function that multiplies a float with a multiplier"""
    def my_mustiple(multiple: float) -> float:
        """creates a new multiple function"""
        return float(multiplier * multiple)

    return my_mustiple
