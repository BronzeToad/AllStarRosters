from helpers.environment_helper import EnvironmentHelper as EnvHelper, EnvFile
import helpers.toad_utils as ToadUtils
import os
from helpers.download_helper import DownloadHelper
from pprint import pprint
from typing import Union


# =================================================================================================================== #


class BaseballDatabank:
    def __init__(
            self,
            source_url: str = None,
            data_dir: str = None,
            databank_filenames: Union[str, list] = None,
            config_folder: str = None,
    ):
        self.source_url = source_url
        self.data_dir = data_dir
        self.databank_filenames = databank_filenames
        self.config_folder = config_folder
        self._post_init()


    def _post_init(self):
        self.root_dir = EnvHelper(EnvFile.PYTHON).get_env_value('PYTHONPATH')
        self.source_url = self.source_url or 'https://raw.githubusercontent.com/chadwickbureau/baseballdatabank/master'
        self.data_dir = self.data_dir or os.path.join(self.root_dir, 'data', 'baseball-databank')
        self.config_folder = self.config_folder or os.path.join(self.root_dir, 'configs')
        self.config_filenames = ToadUtils.get_json(folder=self.config_folder, filename='databank_filenames')
        self.config_headers = ToadUtils.get_json(folder=self.config_folder, filename='databank_headers')
        self.filenames = self._get_databank_filenames()
        self.urls = self._get_download_urls()


    def download(self) -> None:
        for _url in self.urls:
            _save_dir = os.path.join(self.data_dir, 'raw')
            DownloadHelper(url=_url, save_dir=_save_dir).download()


    def _get_databank_filenames(self) -> list:

        def _get_valid() -> list:
            _names = []
            for _key in self.config_filenames:
                _name = _key['fileName']
                _names.append(_name)
            return _names

        _filenames = self.databank_filenames or _get_valid()
        _files = [_filenames] if isinstance(_filenames, str) else _filenames
        _invalid = []

        for _file in _files:
            if _file not in _get_valid():
                _invalid.append(_file)
                _files.remove(_file)

            if len(_invalid) > 0:
                print(f'Removed {len(_invalid)} invalid filenames...')
                pprint(_invalid)

        if len(_files) < 1:
            raise RuntimeError(f'No valid download filenames...')
        else:
            return _files


    def _get_download_urls(self) -> list:
        _urls = []

        for _file in self.filenames:
            for _item in self.config_filenames:
                if _file == _item['fileName']:
                    _type = _item['fileType']

                    if isinstance(_type, list):
                        for _t in _type:
                            _urls.append(f'{self.source_url}/{_t}/{_file}.csv')
                    else:
                        _urls.append(f'{self.source_url}/{_type}/{_file}.csv')

        return _urls


# =================================================================================================================== #

if __name__ == '__main__':
    print('\n\n-------------------------- Executing as standalone script...')
