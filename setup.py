from setuptools import setup

setup(
    name="pytools",
    version="0.2",
    author="Melano",
    py_modules=[
        "randname",
        "randclip",
        "renbname",
    ],
    install_requires=[
        # randname, renbname
        "colorama==0.4.3",
        "fire==0.4.0",
        # randclip
        "pyperclip==1.8.2",
    ],
    entry_points={
        "console_scripts": [
            "randname = randname:main",
            "randclip = randclip:main",
            "renbname = renbname:main",
        ]
    }
)
