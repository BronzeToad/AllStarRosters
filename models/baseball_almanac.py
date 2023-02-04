import os
from enum import Enum

import numpy as np
import pandas as pd

from helpers.download_helper import DownloadHelper
from helpers.environment_helper import EnvFile, EnvironmentHelper as EnvHelper


# =================================================================================================================== #

class MovingRangeCalc(Enum):
    MEAN = 'mean'
    MIN = 'min'
    MAX = 'max'


class BaseballAlmanac:
    def __init__(
            self,
            download_url: str = None,
            data_dir: str = None
    ):
        self.download_url = download_url
        self.data_dir = data_dir
        self._post_init()


    def _post_init(self):
        self.root_dir = EnvHelper(EnvFile.PYTHON).get_env_value('PYTHONPATH')
        self.download_url = self.download_url or self._get_download_url()
        self.data_dir = self.data_dir or os.path.join(self.root_dir, 'data', 'baseball-almanac')


    def download(self) -> None:
        DownloadHelper(url=self.download_url, save_dir=self.data_dir).download()


    @staticmethod
    def _get_download_url() -> str:
        _blob = '87d0391b48e4a05b3cd1e3bcf7f000e62623ede8'
        _url = ('https://github.com/BronzeToad/AllStarRosters/blob/'
                f'{_blob}/data/baseball-almanac/all_star_game_tv_stats.csv')
        return _url


    @staticmethod
    def get_moving_range(
            dataframe: pd.DataFrame,
            column: str,
            calculation: MovingRangeCalc,
            window_size: int = None
    ) -> list:
        """ Function to get moving/rolling range for given dataframe series."""

        _winsize = window_size or 10
        _arr = dataframe[column]

        if _winsize < 2 or _winsize >= len(_arr):
            raise ValueError(f'Window size must be between 2 and {len(_arr)}...')

        match calculation:
            case MovingRangeCalc.MEAN:
                _dirty_windows = pd.Series(_arr).rolling(_winsize).mean()
            case MovingRangeCalc.MIN:
                _dirty_windows = pd.Series(_arr).rolling(_winsize).min()
            case MovingRangeCalc.MAX:
                _dirty_windows = pd.Series(_arr).rolling(_winsize).max()
            case _:
                raise RuntimeError('Something went wrong...')

        _clean_windows = []
        for window in _dirty_windows.tolist():
            if not np.isnan(window):
                if MovingRangeCalc == MovingRangeCalc.MEAN:
                    window = round(window, 2)
                else:
                    window = int(window)
                _clean_windows.append(window)

        return _clean_windows


    @staticmethod
    def _check_list_len(checkme: list) -> bool:
        if len(checkme) < 2:
            raise ValueError('Input list must have length >= 2...')
        else:
            return True


    def get_first_last(self, input_list: list) -> list:
        """ Returns first and last element of input_list as new list."""

        if self._check_list_len(input_list):
            _first_last = []
            [_first_last.append(input_list[i]) for i in [0, -1]]
            return _first_last
        else:
            return None


    def get_percent_change(self, input_list: list) -> list:
        """ Returns percent change between first and last element of input_list."""

        if self._check_list_len(input_list):
            _first = input_list[0]
            _last = input_list[-1]
            _delta_raw = round(((_first - _last) / _first), 2)
            _delta_pct = [np.nan, _delta_raw]
            return _delta_pct
        else:
            return None


# =================================================================================================================== #

if __name__ == '__main__':
    print('\n\n-------------------------- Executing as standalone script...')
