from helpers.environment_helper import EnvHelper
import helpers.toad_utils as toadUtils
import os
from helpers.enum_factory import FileType
from dataclasses import dataclass

from helpers.download_helper import DownloadHelper
from pprint import pprint

# TODO: review - may need updating/fixing after lost work
# =================================================================================================================== #

@dataclass
class BaseballDatabank:
    pass


    def __post_init__(self):
        self.root_dir = EnvHelper().workspace


    def download(self):
        pass


    def get_valid_filenames(self):
        pass


    def get_download_filenames(self):
        pass


    def get_download_urls(self):
        pass

# =================================================================================================================== #
# =================================================================================================================== #

SOURCE_URL = 'https://raw.githubusercontent.com/chadwickbureau/baseballdatabank/master'

CONFIG = toadUtils.get_json(folder=os.path.join(ROOT_DIR, 'configs'),
                            filename='databank_files')
DATA_DIR = os.path.join(ROOT_DIR, 'data', 'baseball-databank')



def get_valid_filenames() -> list:
    _names = []

    for _key in CONFIG:
        _name = _key['fileName']
        _names.append(_name)

    return _names


def get_download_filenames(filenames: list = None) -> list:
    _valid_filenames = get_valid_filenames()

    if filenames is None:
        _files = _valid_filenames
    else:
        _files = [filenames] if isinstance(filenames, str) else filenames
        _invalid = []

        for _file in _files:
            if _file not in _valid_filenames:
                _invalid.append(_file)
                _files.remove(_file)

            if len(_invalid) > 0:
                print(f'Removed {len(_invalid)} invalid filenames...')
                pprint(_invalid)

    if len(_files) < 1:
        raise RuntimeError(f'No valid download filenames...')
    else:
        return _files


def get_download_urls(download_files: list) -> list:
    _urls = []

    for _file in download_files:
        for _item in CONFIG:
            if _file == _item['fileName']:
                _type = _item['fileType']

                if isinstance(_type, list):
                    for _t in _type:
                        _urls.append(f'{SOURCE_URL}/{_t}/{_file}.csv')
                else:
                    _urls.append(f'{SOURCE_URL}/{_type}/{_file}.csv')

    return _urls


# ============================================================================ #

def get_baseball_databank_data(filenames: list = None) -> None:
    _filenames = get_download_filenames(filenames)
    _urls = get_download_urls(_filenames)

    for _url in _urls:
        Downloader.download(url=_url,
                            save_dir=os.path.join(DATA_DIR, 'raw'),
                            ignore_errors=True)


# =================================================================================================================== #

if __name__ == '__main__':
    print(f"\n\n---------------------------------------- {__file__.split('/')[-1]}")
