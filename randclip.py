from random import choices
from string import ascii_letters, digits

import fire
import pyperclip


def randclip(n):
    x = "".join(choices(ascii_letters+digits, k=n))
    pyperclip.copy(x)
    return f"'{x}' generated and copied to clipboard"


def main():
    fire.Fire(randclip)
