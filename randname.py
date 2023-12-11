import os
from random import choices
from string import ascii_letters, digits

from colorama import Fore, init
import fire


def randname(dst=None, n=30):
    print("This program will randomize all file names in a directory."\
          "\nDo not use in wrong directory.",)

    if not dst:
        dst = input("\nEnter the full path of the directory to rename: ")

    # directory check
    if not os.path.isdir(dst):
        return Fore.RED + "\nERROR: Directory does not exist."

    print(Fore.GREEN + f"\nRenaming all files in {dst}")

    if input("\nDo you want to run it in this directory? [y/N]: ").lower() in ["y", "ye", "yes"]:
        for i in os.listdir(dst):
            src = os.path.join(dst, i)
            if os.path.isfile(src):
                extension = os.path.splitext(src)[1]

                # duplicate check
                while True:
                    filename = "".join(choices(ascii_letters+digits, k=n)) + extension
                    if filename not in os.listdir(dst):
                        break

                os.rename(src, os.path.join(dst, filename))

    return Fore.GREEN + "\nDone!"


def main():
    init(autoreset=True)
    fire.Fire(randname)
