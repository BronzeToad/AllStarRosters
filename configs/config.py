from configparser import ConfigParser
from helpers.toad_utils import force_extension
from pathlib import Path
import os
from helpers.environment_helper import EnvHelper

# =================================================================================================================== #

def get_config(
        filename: str,
        section: str
) -> dict:
    _parser = ConfigParser()
    _filename = force_extension(filename, 'ini')
    _parser.read(_filename)

    _filepath = f"{os.path.join(EnvHelper().workspace, 'configs', _filename)}"
    if not Path(_filepath).is_file():
        raise FileNotFoundError(f'Config file {filename} does not exist.')

    _cfg = {}
    if _parser.has_section(section):
        _params = _parser.items(section)
        for _param in _params:
            _cfg[_param[0]] = _param[1]
    else:
        raise Exception(f"Section {section} not found in {filename} config file.")

    return _cfg

# =================================================================================================================== #

if __name__ == '__main__':
    print(f"\n\n---------------------------------------- {__file__.split('/')[-1]}")

    cfg = get_config('database', 'baseball_databank')
    print(cfg['host'])