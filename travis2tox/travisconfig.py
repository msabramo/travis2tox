import yaml


def listify(string_or_list):
    if hasattr(string_or_list, 'startswith'):
        return [string_or_list]
    else:
        return string_or_list


class TravisConfig(object):

    def __init__(self, in_file):
        if not hasattr(in_file, 'read'):
            in_file = open(in_file, 'r')

        self.__dict__ = yaml.load(in_file)

    def get_all_commands(self):
        commands = []

        for key in ['before_install', 'install', 'after_install',
                    'before_script', 'script', 'after_script']:
            commands.extend(listify(getattr(self, key, [])))

        return commands
