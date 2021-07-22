#	Build a source code dist
python3 setup.py sdist

#	Check if there are no error in the dist files
twine check dist/*

#	Upload your project on PyPi (with twine)
twine upload -r pypi dist/*
