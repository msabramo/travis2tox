from .travisconfig import TravisConfig
from .toxconfig import ToxConfig


def travis_env_to_tox_env(travis_env):
    travis_env = str(travis_env)

    if not travis_env.startswith('py') and travis_env[1] == '.':
        return 'py' + travis_env.replace('.', '')
    else:
        return travis_env


def travis2tox(in_file):
    config = TravisConfig(in_file)
    envlist = map(travis_env_to_tox_env, config.python)
    commands = config.get_all_commands()

    return ToxConfig(envlist, commands)
