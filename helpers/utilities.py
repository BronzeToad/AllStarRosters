from pandas import read_csv, DataFrame
import json
import os
from pathlib import Path
from typing import Union


# ============================================================================ #

def force_extension(filename: str, extension: str) -> str:
    suffix = Path(filename).suffix

    if suffix == '':
        filename = f'{filename}.{extension}'
    elif extension not in suffix and suffix not in extension:
        raise ValueError(f'Invalid filename extension {suffix}. Expected {extension}.')

    return filename


# ============================================================================ #

def get_json(folder: str, filename: str) -> dict:
    filename = force_extension(filename, 'json')
    filepath = f'{os.path.join(folder, filename)}'

    if Path(filepath).is_file():
        with open(filepath, 'r') as file:
            data = json.load(file)
    else:
        raise FileNotFoundError(f'{filename} not found in {folder}.')

    if len(data) < 1:
        raise ValueError(f'No data loaded. {filename} is empty...')

    return data


# ============================================================================ #

def get_filename_from_url(url: str) -> str:
    filename = url.split('/')[-1]
    return url.split('/')[-2] if filename == '' else filename


# ============================================================================ #

def get_csv(folder: str, filename: str) -> DataFrame:
    filename = force_extension(filename, 'csv')
    filepath = os.path.join(folder, filename)

    if Path(filepath).is_file():
        df = read_csv(filepath)
        print(f'Loaded {filename} into space.'
              f'Dataframe rows: {df.shape[0]}, Dataframe columns: {df.shape[-1]}')
    else:
        raise FileNotFoundError(f'{filename} not found in {folder}.')

    return df


# ============================================================================ #

def tally(df: DataFrame, fields: Union[str, list] = None, compare: bool = False) -> None:
    if fields is None:
        cols = list(df.columns)
    elif isinstance(fields, str):
        cols = [fields]
    elif isinstance(fields, list) and len(fields) > 0:
        cols = fields
    else:
        raise RuntimeError('Something went wrong...')

    print('\n\n------------------')
    if compare:
        tab = df.groupby(cols).size().sort_values(ascending=False).reset_index(name='count')
        print(f'{tab}\n')
    else:
        for col in cols:
            tab = df.groupby(col).size().sort_values(ascending=False).reset_index(name='count')
            print(f'{tab}\n')


# ============================================================================ #

if __name__ == '__main__':
    print('\n\n-------------------------- Executing as standalone script...')
