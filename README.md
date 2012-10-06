travis2tox
==========

[![Build Status](https://secure.travis-ci.org/msabramo/travis2tox.png)](http://travis-ci.org/msabramo/travis2tox)

Convert a `.travis.yml` file for a Python project to a `tox.ini` file

Example
-------

    $ cat .travis.yml 
    language: python
    
    python:
      - 2.6
      - 2.7
      - 3.2
      - pypy
    
    script: python setup.py test
    
    $ travis2tox .travis.yml
    # Tox (http://tox.testrun.org/) is a tool for running tests
    # in multiple virtualenvs. This configuration file will run the
    # test suite on all supported python versions. To use it, "pip install tox"
    # and then run "tox" from this directory.
    
    [tox]
    envlist = py26, py27, py32, pypy
    
    [testenv]
    commands = python setup.py test
