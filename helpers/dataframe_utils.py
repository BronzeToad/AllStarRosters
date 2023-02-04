from typing import Union

import pandas as pd

# TODO: review - may need updating/fixing after lost work
# =================================================================================================================== #

def tally(
        dataframe: pd.DataFrame,
        columns: Union[str, list],
        compare: bool = False
) -> None:

    if isinstance(columns, str):
        cols = [columns]
    elif isinstance(columns, list) and len(columns) > 0:
        cols = columns
    else:
        raise RuntimeError('Something went wrong...')

    print('\n\n----------------------------------------')

    def _groupme(
            _data: pd.DataFrame,
            _columns: Union[str, list[str]]
    ) -> pd.DataFrameGroupBy:
        return _data.groupby(_columns).size().sort_values(ascending=False).reset_index(name='count')

    if compare:
        print(f'{_groupme(dataframe, cols)}\n')
    else:
        [print(f'{_groupme(dataframe, col)}\n') for col in cols]


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

    df = copy(dataframe)

    if isinstance(columns, str):
        cols = [columns]
    elif isinstance(columns, list) and len(columns) > 0:
        cols = columns
    else:
        raise RuntimeError('Something went wrong...')

    for col in cols:
        if col in list(df.columns):
            df.drop(columns=[col], inplace=True)
        else:
            print(f"Column '{col}' does not exist...")

    return df


# =================================================================================================================== #

if __name__ == '__main__':
    print(f"\n\n---------------------------------------- {__file__.split('/')[-1]}")
