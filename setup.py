#!/usr/bin/env python3

import setuptools

with open("README.md", "r") as f:
    long_description = f.read()

setuptools.setup() (
    name = "dotman",
    version = "0.1.0",
    author = "Darrel Scott",
    author_email = "darrel.scott26@gmail.com",
    description = "A simple dotfile manager",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = "https://github.com/poltar/dotman",
    packages = setuptools.find_packages(),
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU GPLv3 License",
        "Operating System :: Linux",
    ],
)