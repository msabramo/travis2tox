#!/usr/bin/env python

"""
Usage:
  travis2tox <dot_travis_dot_yml_file>
  travis2tox --help

Reads as input <dot_travis_dot_yml_file>, a path to a YAML file for Travis
(typically called ".travis.yml") and writes the contents of an equivalent
tox.ini file to stdout.

"""

import sys

# http://docopt.org/
# https://github.com/docopt/docopt
from docopt import docopt

from travis2tox import travis2tox


def main():
    optargs = docopt(__doc__)
    tox_config = travis2tox(optargs['<dot_travis_dot_yml_file>'])
    print(tox_config.getvalue())


if __name__ == '__main__':
    main()
