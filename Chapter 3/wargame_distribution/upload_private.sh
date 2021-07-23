#!/bin/bash

# Install the package
pip install pypiserver

# Create a new private source distribution
python setup.py sdist

# Start the local server
pypi-server -p 8081 ./dist

# Install your project from the local server
pip install -i http://localhost:8081 wsebas_attackoftheorcs
