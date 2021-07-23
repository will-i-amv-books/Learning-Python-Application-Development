#!/bin/bash

# Run pyment with a py file as argument
pyment knight.py

# Merge the patch file with the original file
patch knight.py knight.py.patch
