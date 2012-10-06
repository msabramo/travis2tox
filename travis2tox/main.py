#!/usr/bin/env python

import sys

from travis2tox import travis2tox


def main():
    tox_config = travis2tox(sys.argv[1])
    print(tox_config.getvalue())


if __name__ == '__main__':
    main()
