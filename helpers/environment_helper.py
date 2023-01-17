import os
from enum import Enum
from pathlib import Path

from dotenv import dotenv_values as dotenvValues


# =================================================================================================================== #

class EnvFile(Enum):
    SECRET = '.env'
    PYTHON = '.env-py'


class EnvironmentHelper:

    def __init__(self, env_file: EnvFile):
        self.env_file = env_file
        self._post_init()


    def _post_init(self):
        self.env_dir = os.path.join(Path(__file__).parent.parent, 'environment')
        self.env_path = os.path.join(self.env_dir, self.env_file.value)
        self.env_vals_dict = dotenvValues(self.env_path)


    def get_env_value(self, env_key: str) -> str:
        _key = env_key.upper()
        if _key not in self.env_vals_dict:
            raise KeyError(f'Could not find environment variable {_key} in .env file...')
        return self.env_vals_dict[_key]


# =================================================================================================================== #

if __name__ == '__main__':
    print('\n\n-------------------------- Executing as standalone script...')
