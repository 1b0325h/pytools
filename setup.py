from setuptools import setup

setup(
    name="pytools",
    version="0.4",
    author="Melano",
    py_modules=[
        "randname",
        "randclip",
        "renbname",
        "azw2cbz",
        "folderzip",
    ],
    install_requires=[
        "fire==0.4.0",
        "colorama==0.4.3",
        # randclip
        "pyperclip==1.8.2",
        # azw2cbz
        "mobi==0.3.3",
        "beautifulsoup4==4.9.3",
    ],
    entry_points={
        "console_scripts": [
            "randname = randname:main",
            "randclip = randclip:main",
            "renbname = renbname:main",
            "azw2cbz = azw2cbz:main",
            "folderzip = folderzip:main",
        ]
    }
)
