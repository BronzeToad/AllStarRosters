import json
import os.path as osPath

from pathlib import Path as LibPath

from helpers.environment_helper import EnvironmentHelper as EnvHelper

# ============================================================================ #

ROOT_DIR = EnvHelper().workspace_dir


def force_extension(filename: str, extension: str) -> str:
    ext = LibPath(filename).suffix
    if ext == '':
        filename = f'{filename}.{extension}'
    elif extension not in ext and ext not in extension:
        raise ValueError(f'Invalid filename extension {ext}. Expected {extension}.')
    return filename


def get_json(folder: str, filename: str) -> dict:
    filename = force_extension(filename, 'json')
    filepath = f'{osPath.join(folder, filename)}'

    if LibPath(filepath).is_file():
        with open(filepath, 'r') as file:
            data = json.load(file)
    else:
        raise FileNotFoundError(f'{filename} not found in {folder}.')

    if len(data) < 1:
        raise ValueError(f'No data loaded. {filename} is empty...')

    return data


def get_filename_from_url(url: str) -> str:
    filename = url.split('/')[-1]
    return url.split('/')[-2] if filename == '' else filename


# ============================================================================ #

if __name__ == '__main__':
    print('\n\n-------------------------- Executing as standalone script...')
