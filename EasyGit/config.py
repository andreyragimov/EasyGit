import os.path

from configparser import ConfigParser

paths_section = 'PATHS'
default_path = "./cfg/config.ini"

# All options are placed here in dict with default values to be easier to configurate
default_options_dict = {
    "git_bash_path": "/bin/bash",
}


class Config:
    def __init__(self, path=default_path):
        self.path = path
        self.config_parser = ConfigParser()

        if os.path.isfile(self.path):
            self.config_parser.read(self.path)

        self.git_bash_path = self.get_paths_option("git_bash_path")

    def get_paths_option(self, option_name):
        """Returns PATHS option from config if exist, else returns default value"""
        if self.config_parser.has_option(paths_section, option_name):
            return self.config_parser[paths_section][option_name]
        else:
            return default_options_dict[option_name]