from setuptools import setup

setup(
    name="chem",
    version="0.1.2",
    packages=["chem"],
    install_requires=[
        "pyparsing",
        "numpy",
        "scipy",
        "nltk",
    ],
)
