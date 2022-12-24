# ============================================================================ #

def force_extension(filename: str, extension: str) -> str:
    from pathlib import Path
    suffix = Path(filename).suffix

    if suffix == '':
        filename = f'{filename}.{extension}'
    elif extension not in suffix and suffix not in extension:
        raise ValueError(f'Invalid filename extension {suffix}. Expected {extension}.')

    return filename


# ============================================================================ #

def get_json(folder: str, filename: str) -> dict:
    import json
    import os
    from pathlib import Path

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

if __name__ == '__main__':
    print('\n\n-------------------------- Executing as standalone script...')
