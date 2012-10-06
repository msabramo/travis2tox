import unittest

try:
    # Python 2
    from StringIO import StringIO
except ImportError:
    # Python 3
    from io import StringIO

from travis2tox import travis2tox


class BasicTests(unittest.TestCase):

    def test_just_script_with_single_command(self):
        input = StringIO("""
language: python

python:
  - 2.5
  - 2.6
  - 2.7
  - 3.2
  - pypy

script: python setup.py nosetests
        """)

        expected_output = """
# Tox (http://tox.testrun.org/) is a tool for running tests
# in multiple virtualenvs. This configuration file will run the
# test suite on all supported python versions. To use it, "pip install tox"
# and then run "tox" from this directory.

[tox]
envlist = py25, py26, py27, py32, pypy

[testenv]
commands = python setup.py nosetests
"""

        self.assertEqual(travis2tox(input).getvalue().strip(), expected_output.strip())

    def test_script_with_multiple_commands(self):
        input = StringIO("""
language: python

python:
  - 2.5
  - 2.6
  - 2.7
  - 3.2
  - pypy

script:
  - python setup.py build
  - python setup.py install
  - python setup.py nosetests
        """)

        expected_output = """
# Tox (http://tox.testrun.org/) is a tool for running tests
# in multiple virtualenvs. This configuration file will run the
# test suite on all supported python versions. To use it, "pip install tox"
# and then run "tox" from this directory.

[tox]
envlist = py25, py26, py27, py32, pypy

[testenv]
commands = 
    python setup.py build
    python setup.py install
    python setup.py nosetests
"""

        self.assertEqual(travis2tox(input).getvalue().strip(), expected_output.strip())

    def test_many_stages_with_multiple_commands(self):
        input = StringIO("""
language: python

python:
  - 2.5
  - 2.6
  - 2.7
  - 3.2
  - pypy

before_install:
  - sudo apt-get install tmux

install:
  - python setup.py install

after_install:
  - echo "Hello world!"

before_script:
  - echo "before_script"

script:
  - python setup.py build
  - python setup.py nosetests

after_script:
  - echo "after_script"
        """)

        expected_output = """
# Tox (http://tox.testrun.org/) is a tool for running tests
# in multiple virtualenvs. This configuration file will run the
# test suite on all supported python versions. To use it, "pip install tox"
# and then run "tox" from this directory.

[tox]
envlist = py25, py26, py27, py32, pypy

[testenv]
commands = 
    sudo apt-get install tmux
    python setup.py install
    echo "Hello world!"
    echo "before_script"
    python setup.py build
    python setup.py nosetests
    echo "after_script"
"""

        self.assertEqual(travis2tox(input).getvalue().strip(), expected_output.strip())

    def test_many_stages_with_single_commands(self):
        input = StringIO("""
language: python

python:
  - 2.5
  - 2.6
  - 2.7
  - 3.2
  - pypy

before_install: pip install --use-mirrors nose

install: python setup.py install

script: python setup.py nosetests
        """)

        expected_output = """
# Tox (http://tox.testrun.org/) is a tool for running tests
# in multiple virtualenvs. This configuration file will run the
# test suite on all supported python versions. To use it, "pip install tox"
# and then run "tox" from this directory.

[tox]
envlist = py25, py26, py27, py32, pypy

[testenv]
commands = 
    pip install --use-mirrors nose
    python setup.py install
    python setup.py nosetests
"""

        self.assertEqual(travis2tox(input).getvalue().strip(), expected_output.strip())
