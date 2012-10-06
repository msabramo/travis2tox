"""Provides a ``ToxConfig`` class for operating on ``tox.ini`` files"""

from string import Template


class ToxConfig(object):
    """Class for operating on ``tox.ini`` files"""

    def __init__(self, envlist, commands):
        """Create an object from a list of environments and a list of
        commands."""

        self.envlist = envlist
        self.commands = commands

    def getvalue(self):
        """Return a string with the contents of a ``tox.ini`` file."""

        envlist = ', '.join(self.envlist)
        commands = self.get_commands()

        return Template("""
# Tox (http://tox.testrun.org/) is a tool for running tests
# in multiple virtualenvs. This configuration file will run the
# test suite on all supported python versions. To use it, "pip install tox"
# and then run "tox" from this directory.

[tox]
envlist = $envlist

[testenv]
commands = $commands
        """).substitute(
            envlist=envlist,
            commands=commands,
        ).lstrip()

    def get_commands(self):
        """Return a string with the content of the ``commands`` key for a
        ``tox.ini`` file."""

        commands = []

        if hasattr(self.commands, 'startswith'):
            commands.append(self.commands)
        elif hasattr(self.commands, '__getitem__'):
            commands.extend(self.commands)

        if len(commands) == 1:
            return commands[0]
        elif len(commands) > 1:
            return "\n    " + "\n    ".join(commands)
