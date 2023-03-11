import os
from pathlib import Path
from typing import Union, Optional

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


def drop_columns(
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
    _filename = force_extension(filename, extension='csv')
    _path = os.path.join(folder, _filename)

    if Path(_path).is_file():
        _df = pd.read_csv(_path)
        print(f'Dataframe shape (rows, cols): {_df.shape}')
    else:
        raise FileNotFoundError(f'{_filename} not found in {folder}.')

    return _df


def update_headers(
        dataframe: pd.DataFrame,
        update_dict: dict,
        drop_missing_cols: Optional[bool] = False
) -> pd.DataFrame:
    _df = copy(dataframe)
    _df.rename(columns=update_dict, inplace=True)

    _og_cols = list(dataframe.columns)
    _new_cols = list(_df.columns)
    _missing_cols = []
    _update_count = 0

    for _col in _og_cols:
        if _col not in _new_cols:
            _update_count += 1
        else:
            _missing_cols.append(_col)

    print(f"Updated {_update_count} header {'name' if _update_count == 1 else 'names'}.")

    if drop_missing_cols and len(_missing_cols) > 0:
        print(f'Dropping {len(_missing_cols)} columns with no matching key in update dictionary...')
        return drop_columns(_df, _missing_cols)
    else:
        return _df

# =================================================================================================================== #

if __name__ == '__main__':
    print(f"\n\n---------------------------------------- {__file__.split('/')[-1]}")

    # create data frame
    df = pd.DataFrame({
                              'First Name': ["Mukul", "Rohan", "Mayank",
                                             "Vedansh", "Krishna"],

                              'Location'  : ["Saharanpur", "Rampur", "Agra",
                                             "Saharanpur", "Noida"],

                              'Pay'       : [56000.0, 55000.0, 61000.0, 45000.0, 62000.0]})

    # print original data frame
    print(f'{df}\n\n')


    update1 = {
            'First Name' : "name_first",
            'Location'   : "location",
            'Pay'        : "salary"
    }
    df1 = update_headers(dataframe=df, update_dict=update1)
    print(f'{df1}\n\n')


    update2 = {
            'First Name' : "name_first",
            "doot Doot" : 'blah',
            'salary' : 'im_old_GREG'
    }
    df2 = update_headers(dataframe=df1, update_dict=update2, drop_missing_cols=True)
    print(f'\n\n{df2}\n\n')