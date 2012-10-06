import sys
from setuptools import setup, find_packages

install_requires = ['PyYAML']

version = sys.version_info[:2]

if version < (2,7) or (3,0) <= version <= (3,1):
    install_requires += ['argparse']

setup(name='travis2tox',
      version='0.0',
      description=('Convert between Travis-CI and tox'),
      # long_description=README + '\n\n' +  CHANGES,
      packages=find_packages(),
      zip_safe=False,
      install_requires=install_requires,
      test_suite='tests',
      entry_points = """\
        [console_scripts]
        travis2tox = travis2tox.main:main
      """
      )

