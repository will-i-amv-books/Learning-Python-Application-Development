#!/bin/bash

# Go to app's docs directory, and run sphinx-quickstart

cd ./wargame
mkdir docs

cd docs
sphinx-quickstart
cd ..

"""Use the following options:

> Separate source and build directories (y/n) [n]: y
> Project name: wargame
> Author name(s): William
> Project release: 2.0.1
"""

# Edit the ./wargame/docs/source/conf.py as follows

"""Add the following extension list:

extensions = [
'sphinx.ext.autodoc', 'sphinx.ext.todo', ]
"""

"""Uncomment the following lines:

import os
import sys

wargame_dir = '/absolute/path/to/wargame_parent_dir' 
sys.path.insert(0, os.path.abspath('.'))
sys.path.insert(0, wargame_dir)
"""

# Run sphinx-apidoc

sphinx-apidoc -o ./docs/source .

# Build the documentation with sphinx-build 

sphinx-build ./docs/source ./docs/build

# (Optional) Build the documentation with Makefile

cd docs
make html
