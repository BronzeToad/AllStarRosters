from enum import Enum

import numpy as np
import pandas as pd

from helpers.environment_helper import EnvHelper, EnvFile

# ============================================================================ #

ROOT_DIR = EnvHelper(EnvFile.PYTHON).get_env_value('PYTHONPATH')


# ============================================================================ #

class MovingRangeCalc(Enum):
    MEAN = 'mean'
    MIN = 'min'
    MAX = 'max'


# ============================================================================ #

def get_moving_range(dataframe: pd.DataFrame,
                     column: str,
                     calculation: MovingRangeCalc,
                     window_size: int = None) -> list:
    """ Function to get moving/rolling range for given dataframe series."""

    winsize = 10 if window_size is None else window_size
    arr = dataframe[column]

    if winsize < 2 or winsize >= len(arr):
        raise ValueError(f'Window size must be between 2 and {len(arr)}...')

    match calculation:
        case MovingRangeCalc.MEAN:
            dirty_windows = pd.Series(arr).rolling(winsize).mean()
        case MovingRangeCalc.MIN:
            dirty_windows = pd.Series(arr).rolling(winsize).min()
        case MovingRangeCalc.MAX:
            dirty_windows = pd.Series(arr).rolling(winsize).max()
        case _:
            raise RuntimeError('Something went wrong...')

    clean_windows = []
    for window in dirty_windows.tolist():
        if not np.isnan(window):
            if MovingRangeCalc == MovingRangeCalc.MEAN:
                window = round(window, 2)
            else:
                window = int(window)
            clean_windows.append(window)

    return clean_windows


# ============================================================================ #

def get_first_last(input_list: list) -> list:
    """ Returns first and last element of input_list as new list."""

    if len(input_list) < 2:
        raise ValueError('Input list must have length >= 2...')

    first_last = []

    for i in [0, -1]:
        first_last.append(input_list[i])

    return first_last


def get_percent_change(input_list: list) -> list:
    """ Returns percent change between first and last element of input_list."""

    if len(input_list) < 2:
        raise ValueError('Input list must have length >= 2...')

    first = input_list[0]
    last = input_list[-1]

    delta_raw = round(((first - last) / first), 2)
    delta_pct = [np.nan, delta_raw]

    return delta_pct


# ============================================================================ #

if __name__ == '__main__':
    print('\n\n-------------------------- Executing as standalone script...')