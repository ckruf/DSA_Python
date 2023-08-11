"""This file contains solution attempt for exercise 7.9"""
import sys
import os
from pathlib import Path

# add root dir of project to sys path
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
script_path = Path(SCRIPT_DIR)
src_dir = script_path.parent.absolute()
dsa_python_dir = src_dir.parent.absolute()
sys.path.insert(0, str(dsa_python_dir))

from ch07.my_practice_implementations.positional_list import PositionalList
from typing import Any


def max(L: PositionalList) -> Any:
    """
    Implement a function, with calling syntax max(L), that returns the maximum
    element from a PositionalList instance L containing comparable elements.
    """
    maximum = L.first().element()
    for e in L:
        if e > maximum:
            maximum = e
    return maximum
