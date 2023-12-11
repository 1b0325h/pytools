import os, glob

from colorama import Fore, init
import fire


def winsort(lst):
    import ctypes
    from functools import cmp_to_key

    SHLWAPI = ctypes.windll.LoadLibrary("SHLWAPI.dll")
    def strcmp(a, b):
        return SHLWAPI.StrCmpLogicalW(a, b)

    return sorted(lst, key=cmp_to_key(strcmp))


def renbname(dst=None):
    print("This program numbers all file names in a directory sequentially."\
          "\nDo not use in wrong directory.",)

    if not dst:
        dst = input("\nEnter the full path of the directory to rename: ")

    # directory check
    if not os.path.isdir(dst):
        return Fore.RED + "\nERROR: Directory does not exist."

    print(Fore.GREEN + f"\nRenaming all files in {dst}")

    if input("\nDo you want to run it in this directory? [y/N]: ").lower() in ["y", "ye", "yes"]:
        lst = glob.glob(f"{dst}/*.*")
        for i, f in enumerate(winsort(lst)):
            filename = "{0:04d}".format(i) + os.path.splitext(f)[1]
            os.rename(f, os.path.join(os.path.dirname(f), filename))

    return Fore.GREEN + "\nDone!"


def main():
    init(autoreset=True)
    fire.Fire(renbname)
