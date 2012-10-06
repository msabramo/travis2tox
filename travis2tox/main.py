#!/usr/bin/env python

"""
Usage:
  travis2tox <dot_travis_dot_yml_file>
  travis2tox --help

Reads as input <dot_travis_dot_yml_file>, a path to a YAML file for Travis
(typically called ".travis.yml") and writes the contents of an equivalent
tox.ini file to stdout.

"""

import argparse
import sys

from travis2tox import travis2tox


def main():
    parser = argparse.ArgumentParser(
        description='Convert a .travis.yml file to a tox.ini file.')
    parser.add_argument(
        'dot_travis_dot_yml_file',
        help='path to a .travis.yml file')
    args = parser.parse_args()

    tox_config = travis2tox(args.dot_travis_dot_yml_file)
    print(tox_config.getvalue())


if __name__ == '__main__':
    main()
