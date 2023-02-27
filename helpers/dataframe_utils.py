import os
from pathlib import Path
from typing import Union

import pandas as pd

from helpers.toad_utils import force_extension


# =================================================================================================================== #

def tally(
        dataframe: pd.DataFrame,
        columns: Union[str, list]
) -> None:

    _cols = columns if isinstance(columns, list) else [columns]

    for col in _cols:
        group_by_df = dataframe.groupby(col).size().sort_values(ascending=False).reset_index(name='count')
        print(f'{group_by_df}\n')


def copy(dataframe: pd.DataFrame) -> pd.DataFrame:
    return dataframe.copy().reset_index(drop=True)


def concat(
        dataframe_a: pd.DataFrame,
        dataframe_b: pd.DataFrame
) -> pd.DataFrame:
    return pd.concat([dataframe_a, dataframe_b], axis=1)


def drop(
        dataframe: pd.DataFrame,
        columns: Union[str, list]
) -> pd.DataFrame:

    _df = copy(dataframe)
    _cols = columns if isinstance(columns, list) else [columns]

    for col in _cols:
        if col in list(_df.columns):
            _df.drop(columns=[col], inplace=True)
        else:
            print(f"Column '{col}' does not exist...")

    return _df


def load_csv(
        folder: str,
        filename: str
) -> pd.DataFrame:
    """Loads a csv file as a dataframe object.

    Parameters
    ----------
    folder : str
        The folder where the file is located.
    filename : str
        The name of the file.

    Returns
    -------
    _df : pd.DataFrame
        The contents of the csv file.

    Raises
    ------
    FileNotFoundError
        If the file is not found in the given folder.
    """
    _filename = force_extension(filename, 'csv')
    _path = os.path.join(folder, _filename)

    if Path(_path).is_file():
        _df = pd.read_csv(_path)
        print(f'Dataframe shape (rows, cols): {_df.shape}')
    else:
        raise FileNotFoundError(f'{_filename} not found in {folder}.')

    return _df


# =================================================================================================================== #

if __name__ == '__main__':
    print(f"\n\n---------------------------------------- {__file__.split('/')[-1]}")
