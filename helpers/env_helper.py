import os
from dotenv import dotenv_values
from pathlib import Path
from icecream import ic
from helpers.enum_factory import EnvFile


# ============================================================================ #

class EnvHelper:
    ENV_DIR: str = os.path.join(Path(__file__).parent.parent, 'environment')

    def __init__(self, env_file: EnvFile):
        self.env_file = env_file
        self.env_path = None
        self.env_vals = None
        self.root_dir = None

    @property
    def env_file(self) -> str:
        return self._env_file

    @env_file.setter
    def env_file(self, val):
        self._env_file = val.value

    @property
    def env_path(self) -> str:
        return self._env_path

    @env_path.setter
    def env_path(self, val):
        if val is None:
            val = os.path.join(self.ENV_DIR, self.env_file)
        self._env_path = val

    @property
    def env_vals(self) -> dict:
        return self._env_vals

    @env_vals.setter
    def env_vals(self, val):
        val = dotenv_values(self.env_path) if val is None else val
        self._env_vals = val

# ============================================================================ #

    def get_env_value(self, env_key: str) -> str:
        if env_key not in self.env_vals:
            raise KeyError(f'Could not find environment variable {env_key} in .env file...')
        return self.env_vals[env_key]


# ============================================================================ #

if __name__ == '__main__':
    print('\n\n-------------------------- Executing as standalone script...')
    
    tst = EnvHelper(EnvFile.PYTHON)

    ic(tst.ENV_DIR)
    ic(tst.env_file)
    ic(tst.env_path)
    ic(tst.env_vals)
    ic(tst.get_env_value('WORKSPACE_DIR'))
    ic(tst.get_env_value('PYTHONPATH'))
    