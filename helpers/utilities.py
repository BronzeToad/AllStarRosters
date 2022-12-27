import json
import os
from pathlib import Path

import pandas as pd
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

def get_csv(folder: str, filename: str) -> pd.DataFrame:
    filename = force_extension(filename, 'csv')
    filepath = os.path.join(folder, filename)

    if Path(filepath).is_file():
        df = pd.read_csv(filepath)
        print(f'Dataframe rows: {df.shape[0]}, Dataframe columns: {df.shape[-1]}')
    else:
        raise FileNotFoundError(f'{filename} not found in {folder}.')

    return df


# ============================================================================ #

def prant(printme: Union[list, dict]) -> None:

    if isinstance(printme, list):
        print('\nPrinting list...')
        [print(p) for p in printme]

    elif isinstance(printme, dict):
        print('\nPrinting dictionary...')
        for key, val in printme.items():
            print(f'{key}: {val}')

    else:
        raise TypeError(f'Invalid type: {type(printme)}...')


# ============================================================================ #

if __name__ == '__main__':
    print('\n\n-------------------------- Executing as standalone script...')
