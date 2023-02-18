from helpers.enum_factory import MovingRangeCalc
import numpy as np
import pandas as pd

from helpers.environment_helper import EnvHelper

# TODO: review - may need updating/fixing after lost work
# =================================================================================================================== #

ROOT_DIR = EnvHelper().workspace



# =================================================================================================================== #
# =================================================================================================================== #


def get_moving_range(
        dataframe: pd.DataFrame,
        column: str,
        calculation: MovingRangeCalc,
        window_size: int = 10
) -> list:
    """ Function to get moving/rolling range for given dataframe series."""

    target_array = dataframe[column]

    if window_size < 2 or window_size >= len(target_array):
        raise ValueError(f'Window size must be between 2 and {len(target_array)}...')

    match calculation:
        case MovingRangeCalc.MEAN:
            dirty_windows = pd.Series(target_array).rolling(window_size).mean()
        case MovingRangeCalc.MIN:
            dirty_windows = pd.Series(target_array).rolling(window_size).min()
        case MovingRangeCalc.MAX:
            dirty_windows = pd.Series(target_array).rolling(window_size).max()
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


# =================================================================================================================== #

if __name__ == '__main__':
    print(f"\n\n---------------------------------------- {__file__.split('/')[-1]}")
