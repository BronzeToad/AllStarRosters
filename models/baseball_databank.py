import os.path as osPath

from helpers.environment_helper import EnvironmentHelper as EnvHelper
from helpers.downloader import Downloader
import helpers.data_utilities as dataUtils

from icecream import ic


# ============================================================================ #

class BaseballDataBank:
    SOURCE_URL = 'https://raw.githubusercontent.com/chadwickbureau/baseballdatabank/master'
    ROOT_DIR = EnvHelper().workspace_dir
    CONFIG = dataUtils.get_json(folder=osPath.join(ROOT_DIR, 'configs'),
                                filename='baseball_databank')

    # ============================================================================ #

    def __init__(self, filenames: list = None):
        self.VALID_FILENAMES = None
        self.filenames = filenames

    @property
    def VALID_FILENAMES(self) -> list:
        return self._VALID_FILENAMES

    @VALID_FILENAMES.setter
    def VALID_FILENAMES(self, val: list) -> None:
        val = []
        for _key in self.CONFIG:
            _name = _key['fileName']
            val.append(_name)
        self._VALID_FILENAMES = val

    @property
    def filenames(self) -> list:
        return self._filenames

    @filenames.setter
    def filenames(self, val) -> None:
        if val is None:
            val = self.VALID_FILENAMES
        else:
            val = [val] if isinstance(val, str) else val
            _invalid_filenames = []
            for _name in val:
                if _name not in self.VALID_FILENAMES:
                    _invalid_filenames.append(_name)
                    val.remove(_name)
            if len(_invalid_filenames) > 0:
                print(f'Removed {len(_invalid_filenames)} invalid filenames...')
                ic(_invalid_filenames)
        self._filenames = val

# ============================================================================ #
