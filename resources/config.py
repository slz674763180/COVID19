import argparse

import yaml


class Config:
    def __init__(self, **entries):
        self.__dict__.update(entries)


def get_configs():
    return _load_config_yaml("./resources/train_config.yaml")


def _load_config_yaml(config_file):
    config_dict = yaml.load(open(config_file, 'rb'))
    return Config(**config_dict)

