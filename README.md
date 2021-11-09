My Python Project
=================

[![Build](https://travis-ci.com/acoomans/python_project_template.svg?branch=master)](https://travis-ci.org/acoomans/python_project_template)
[![Pypi version](http://img.shields.io/pypi/v/acoomans_python_project_template.svg)](https://pypi.python.org/pypi/acoomans_python_project_template)
[![Pypi license](http://img.shields.io/pypi/l/acoomans_python_project_template.svg)](https://pypi.python.org/pypi/acoomans_python_project_template)
![Python 2](http://img.shields.io/badge/python-2-blue.svg)
![Python 3](http://img.shields.io/badge/python-3-blue.svg)

## Install

	python setup.py install

## Developing

	python setup.py develop
	python setup.py develop --uninstall

## Running tests

	python setup.py test
	
## Submitting to PyPi

### Config

Add the following to ~/.pypirc

	[distutils]
	index-servers =
			pypi
			testpypi
	
	[pypi]
	repository: https://upload.pypi.org/legacy/
	username = acoomans
	
	[testpypi]
	repository: https://test.pypi.org/legacy/
	username = acoomans
	
### Upload

	python3 setup.py sdist upload
	
Note: uploading with python2 seems to be broken

### Test PyPi
	
	python3 setup.py sdist upload --repository testpypi
	pip install acoomans_python_project_template --extra-index-url https://testpypi.python.org/pypi


