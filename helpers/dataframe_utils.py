from typing import Union

import pandas as pd


# =================================================================================================================== #

def tally(
        dataframe: pd.DataFrame,
        columns: Union[str, list]
) -> None:

    cols = columns if isinstance(columns, list) else [columns]

    for col in cols:
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

    df = copy(dataframe)
    cols = columns if isinstance(columns, list) else [columns]

    for col in cols:
        if col in list(df.columns):
            df.drop(columns=[col], inplace=True)
        else:
            print(f"Column '{col}' does not exist...")

    return df


# =================================================================================================================== #

if __name__ == '__main__':
    print(f"\n\n---------------------------------------- {__file__.split('/')[-1]}")
