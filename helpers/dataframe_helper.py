from typing import Union

import pandas as pd


# ============================================================================ #

def tally(dataframe: pd.DataFrame,
          column: str = None,
          columns: list[str] = None,
          compare: bool = False) -> None:

    if column is None and columns is None:
        cols = list(dataframe.columns)
    elif column is None and len(columns) > 0:
        cols = columns
    elif columns is None:
        cols = [column]
    else:
        raise RuntimeError('Something went wrong...')

    print('\n\n------------------')

    def _groupme(data: pd.DataFrame,
                 colz: Union[str, list[str]]) -> pd.DataFrameGroupBy:
        return data.groupby(colz).size().sort_values(ascending=False).reset_index(name='count')

    if compare:
        print(f'{_groupme(dataframe, cols)}\n')
    else:
        [print(f'{_groupme(dataframe, col)}\n') for col in cols]


# ============================================================================ #

def copy(dataframe: pd.DataFrame) -> pd.DataFrame:
    return dataframe.copy().reset_index(drop=True)


# ============================================================================ #

def add_column(dataframe_a: pd.DataFrame, dataframe_b: pd.DataFrame) -> pd.DataFrame:
    return pd.concat([dataframe_a, dataframe_b], axis=1)


# ============================================================================ #

if __name__ == '__main__':
    print('\n\n-------------------------- Executing as standalone script...')
