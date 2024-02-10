from glob import glob
from os import mkdir
from os.path import abspath, basename, dirname, isdir, isfile, join, splitext
from shutil import make_archive, move, rmtree

from bs4 import BeautifulSoup
import mobi
import fire


def azw2cbz(src, dst=None):
    """convert fixed layout azw to cbz

    Args:
        src (str): source file (azw, azw3, azw4)
        dst (str): optionally, specify the destination folder
                   or if not specified, it will be saved in the src folder
    """
    if not isfile(src):
        return "file does not exist"
    fname, ext = splitext(basename(src))
    if ext.lower() not in [".azw", ".azw3", ".azw4"]:
        return "unsupported file format"
    if dst is None:
        dst = join(dirname(abspath(src)), fname)
    else:
        if not isdir(dst):
            return "destination directory cannot be found"
        dst = join(dst, fname)

    # unpack and get temp folder
    temp = mobi.extract(src)[0]
    # content files in temp folder after unpacking
    unpack_dir = join(temp, "mobi8", "OEBPS")
    # before zip
    temp_dst = join(temp, "azw2cbz")

    mkdir(temp_dst)

    cnt = 0

    # processing when cover_page.xhtml exists
    # This case is found when converting to azw3 in calibre!
    text_dir = join(unpack_dir, "Text")
    cover_page = join(text_dir, "cover_page.xhtml")
    if isfile(cover_page):
        soup = BeautifulSoup(open(cover_page, encoding="utf_8"), "html.parser")
        img = soup.find("image")
        split_txt = splitext(basename(img["xlink:href"]))
        move(join(unpack_dir, "Images", "".join(split_txt)),
             join(temp_dst, f"{str(cnt).zfill(5)}{split_txt[1]}"))
        cnt += 1

    # sequence xhtml files in text folder
    for f in glob(f"{text_dir}/part*.xhtml"):
        soup = BeautifulSoup(open(f, encoding="utf_8"), "html.parser")

        # There was a pattern of <img> or <image> in the sequence of xhtml file.
        if (img := soup.find("img")):
            split_txt = splitext(basename(img["src"]))
        elif (img := soup.find("image")):
            split_txt = splitext(basename(img["xlink:href"]))
        else:
            continue

        move(join(unpack_dir, "Images", "".join(split_txt)),
             join(temp_dst, f"{str(cnt).zfill(5)}{split_txt[1]}"))
        cnt += 1

    # zip to cbz
    make_archive(temp_dst, "zip", temp_dst)
    move(temp_dst+".zip", dst+".cbz")

    rmtree(temp)


def main():
    fire.Fire(azw2cbz)
