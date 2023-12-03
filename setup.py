from setuptools import setup

setup(
    name="pytools",
    version="0.1",
    author="Melano",
    py_modules=[
        "randname",
        "randclip"
    ],
    install_requires=[
        # randname
        "colorama==0.4.3",
        "fire==0.4.0",
        # randclip
        "pyperclip==1.8.2",
    ],
    entry_points={
        "console_scripts": [
            "randname = randname:main",
            "randclip = randclip:main"
        ]
    }
)
