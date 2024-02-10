import os
import glob
import shutil

import fire


def forderzip(dst=None, n=30):
    if not dst:
        dst = input("\nEnter the full path of the directory to rename: ")

    # directory check
    if not os.path.isdir(dst):
        print("ERROR: Directory does not exist.")

    for f in glob.glob(f"{dst}/*"):
        # except files
        if os.path.isfile(f):
            continue
        shutil.make_archive(f, "zip", root_dir=f)

def main():
    fire.Fire(forderzip)
