from random import choice
from string import (
    ascii_lowercase,
    ascii_uppercase,
    digits
)


def keyGenerator(length : int) -> str:

    symbols : str = ascii_lowercase + ascii_uppercase + digits
    secret_key : str = "".join([choice(symbols) for i in range(length)])
    return secret_key

