# setup.py

from setuptools import setup, find_packages

setup(
    name="yourpackage",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "numpy==1.21.0"
    ],
)
