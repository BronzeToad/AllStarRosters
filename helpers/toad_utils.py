import json
import os
from pathlib import Path
from typing import Optional, Union

from helpers.enum_factory import FileType


# =================================================================================================================== #

def force_extension(
        filename: str,
        extension: str
) -> str:
    """Force a filename to have a certain extension.

    If the filename already has an extension, it must be one of the allowed extensions.
    If the filename has no extension, the extension is added.
    If the filename has an extension that is not allowed, an error is raised.

    Parameters
    ----------
    filename : str
        The filename to check.
    extension : str
        The desired filename extension.

    Returns
    -------
    _filename : str
        The filename with the desired extension.

    Raises
    ------
    ValueError
        If the filename has an extension that is not allowed.
    """
    _ext = str(extension).lower().replace('.', '')
    _suffix = str(Path(filename).suffix).lower().replace('.', '')

    if _suffix == '':
        return f'{filename}.{_ext}'
    elif _ext != _suffix:
        raise ValueError(f'Invalid filename extension {_suffix}. Expected {_ext}.')
    else:
        return filename.replace(extension, _ext)


def get_file(
        folder: str,
        filename: str,
        file_type: FileType,
        find_replace: Optional[dict] = None
) -> Union[dict, str]:
    """Gets file and loads contents as a python object in memory.

    Parameters
    ----------
    folder : str
        The folder where the file is located.
    filename : str
        The name of the file.
    file_type: FileType,
        The type of file to be loaded (Enum).
    find_replace : dict, optional
        A dictionary of key/value pairs to replace in the file.
        Only supported for string-like file types for now.

    Returns
    -------
    _obj : Union[dict, str]
        The contents of the sql file.

    Raises
    ------
    FileNotFoundError
        If the file is not found in the given folder.
    RuntimeError
        If a find/replace dict is provided for FileType that does not support find/replace.
    """
    _filename = force_extension(filename, str(file_type.name).lower())
    _filepath = f'{os.path.join(folder, _filename)}'

    if not Path(_filepath).is_file():
        raise FileNotFoundError(f'{filename} not found in {folder}.')

    with open(_filepath, 'r') as file:
        if file_type == FileType.JSON:
            _obj = json.load(file)
        elif file_type in [FileType.HTML, FileType.SQL]:
            _obj = str(file.read())
        else:
            _obj = None
        file.close()

    if find_replace is not None:
        if file_type in [FileType.HTML, FileType.SQL]:
            for key, val in find_replace.items():
                _obj = _obj.replace(key, str(val))
        else:
            raise RuntimeError(f'Find/Replace not supported for {file_type}')

    return _obj


def get_url_filename(url: str) -> str:
    """Extracts the filename from a url. """
    _filename = url.split('/')[-1]
    return url.split('/')[-2] if _filename == '' else _filename


# =================================================================================================================== #

if __name__ == '__main__':
    print(f"\n\n---------------------------------------- {__file__.split('/')[-1]}")
