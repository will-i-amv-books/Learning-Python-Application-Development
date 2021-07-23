#!/bin/bash

# Install the package
pip install twine

# Create the following file in home dir

touch ~/.pypirc

# Create the following entries in the file

[distutils]
index-servers= pypi

[pypi]
repository = https://upload.pypi.org/legacy/
username=YOUR_USERNAME
password=YOUR_PASSWORD

# Build a source code dist
python3 setup.py sdist

# Check if there are errors in dist files
twine check dist/*

#	Upload project to PyPi
twine upload -r pypi dist/*
