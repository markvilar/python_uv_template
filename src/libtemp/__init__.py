"""Template package."""

from .common import print_hello_to, print_hello_from
from .math import add, multiply

__all__ = [
    "print_hello_to",
    "print_hello_from",
    "add",
    "multiply",
]
