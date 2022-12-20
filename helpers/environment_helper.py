import os.path as osPath
from dotenv import dotenv_values as dotenvVals
from pathlib import Path as LibPath
from icecream import ic

# ============================================================================ #

class EnvironmentHelper:
    
    def __init__(self, env_file: str = None):
        self.env_file = env_file
        self.env_vals = None
        self.workspace_dir = None
        
        
    @property
    def env_file(self) -> str:
        return self._env_file
    
    @env_file.setter
    def env_file(self, val: str) -> None:
        if val is None:
            val = osPath.join(LibPath(__file__).parent.parent, '.env')
        if not LibPath(val).is_file():
            raise FileNotFoundError(f'Unable to locate .env file: {val}')
        self._env_file = val


    @property
    def env_vals(self) -> dict:
        return self._env_vals

    @env_vals.setter
    def env_vals(self, val: dict) -> None:
        val = dotenvVals(self.env_file)
        self._env_vals = val

# ============================================================================ #

    @property
    def workspace_dir(self) -> str:
        return self._workspace_dir
    
    @workspace_dir.setter
    def workspace_dir(self, val: str) -> None:
        val = self.env_vals['WORKSPACE_DIR']
        self._workspace_dir = val

# ============================================================================ #

    def get_other_env_val(self, env_key: str) -> str:
        if env_key not in self.env_vals:
            raise KeyError(f'Could not find environment variable {env_key} in .env file...')
        return self.env_vals[env_key]

# ============================================================================ #

if __name__ == '__main__':
    print('\n\n-------------------------- Executing as standalone script...')
    
    tst = EnvironmentHelper()
    
    ic(tst.env_file)
    ic(tst.env_vals)
    ic(tst.workspace_dir)
    ic(tst.get_other_env_val('PYTHONPATH'))
    