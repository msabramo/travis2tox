from setuptools import setup, find_packages

setup(name='travis2tox',
      version='0.0',
      description=('Convert between Travis-CI and tox'),
      # long_description=README + '\n\n' +  CHANGES,
      packages=find_packages(),
      zip_safe=False,
      install_requires=['PyYAML'],
      entry_points = """\
        [console_scripts]
        travis2tox = travis2tox.main:main
      """
      )

