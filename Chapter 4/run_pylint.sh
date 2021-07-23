# Install the package

pip install pylint

# Create the following file in home directory

touch ~/.pylintrc

# Update the init-hook entry with the following line

init-hook='import sys; sys.path.append("/path/to/wargame")'

# Run pylint with the following syntax

pylint hut.py
