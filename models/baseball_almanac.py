import numpy as np
import pandas as pd

from helpers.enum_factory import MovingRangeCalc
from helpers.environment_helper import EnvHelper


# =================================================================================================================== #

ROOT_DIR = EnvHelper().workspace


def get_moving_range(
        dataframe: pd.DataFrame,
        column: str,
        calculation: MovingRangeCalc,
        window_size: int = 10
) -> list:
    """ Function to get moving/rolling range for given dataframe series."""

    _array = dataframe[column]

    if window_size < 2 or window_size >= len(_array):
        raise ValueError(f'Window size must be between 2 and {len(_array)}...')

    match calculation:
        case MovingRangeCalc.MEAN:
            _dirty_windows = pd.Series(_array).rolling(window_size).mean()
        case MovingRangeCalc.MIN:
            _dirty_windows = pd.Series(_array).rolling(window_size).min()
        case MovingRangeCalc.MAX:
            _dirty_windows = pd.Series(_array).rolling(window_size).max()
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


def get_first_last(input_list: list) -> list:
    """ Returns first and last element of input_list as new list."""

    if len(input_list) < 2:
        raise ValueError('Input list must have length >= 2...')

    _first_last = []

    for i in [0, -1]:
        _first_last.append(input_list[i])

    return _first_last


def get_percent_change(input_list: list) -> list:
    """ Returns percent change between first and last element of input_list."""

    if len(input_list) < 2:
        raise ValueError('Input list must have length >= 2...')

    _first = input_list[0]
    _last = input_list[-1]

    _delta_raw = round(((_first - _last) / _first), 2)
    _delta_pct = [np.nan, _delta_raw]

    return _delta_pct


# =================================================================================================================== #

if __name__ == '__main__':
    print(f"\n\n---------------------------------------- {__file__.split('/')[-1]}")
