#!/bin/bash

# Build a source code dist
python3 setup.py sdist

# Check if there are errors in dist files
twine check dist/*

#	Upload project to PyPi
twine upload -r pypi dist/*
