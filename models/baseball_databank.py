import os
from dataclasses import dataclass
from typing import List, Optional

import helpers.toad_utils as toadUtils
from helpers.download_helper import DownloadHelper
from helpers.enum_factory import FileType
from helpers.environment_helper import EnvHelper
from helpers.config import get_config

# =================================================================================================================== #

@dataclass
class BaseballDatabank:
    source_url: Optional[str] = None
    save_dir: Optional[str] = None
    download_filenames: Optional[List[str]] = None


    def __post_init__(self):
        self.root_dir = EnvHelper().workspace
        self.config = self._get_config()
        self.source_url = self.source_url or self._get_source_url()
        self.save_dir = self.save_dir or self._get_save_dir()
        self.save_path = os.path.join(self.root_dir, self.save_dir)
        self.filenames = self._get_filenames()
        self.download_filenames = self._get_download_filenames()
        self.download_urls = self._get_download_urls()


    def download(self):
        for url in self.download_urls:
            downloader = DownloadHelper(
                    url=url,
                    save_dir=self.save_dir
            )
            downloader.download()


    @staticmethod
    def _get_config() -> dict:
        return get_config(
                filename='baseball_databank',
                section='main'
        )


    def _get_filenames(self) -> dict:
        return toadUtils.get_file(
                folder=os.path.join(self.root_dir, 'configs'),
                filename='databank_filenames',
                file_type=FileType.JSON
        )


    def _get_source_url(self) -> str:
        return self.config['source_url']


    def _get_save_dir(self) -> str:
        return self.config['data_dir']


    def _get_download_filenames(self) -> List[str]:
        _valid_filenames = []
        for f in self.config['files']:
            _valid_filenames.append(f['fileName'])

        if self.download_filenames is None:
            _download_filenames = _valid_filenames
        else:
            if isinstance(self.download_filenames, str):
                _download_filenames = [self.download_filenames]
            else:
                _download_filenames = self.download_filenames

            _invalid_filenames = []

            for file in _download_filenames:
                if file not in _valid_filenames:
                    _invalid_filenames.append(file)
                    _download_filenames.remove(file)

            if len(_invalid_filenames) > 0:
                print(f'Removed {len(_invalid_filenames)} invalid filenames...')
                print([f for f in _invalid_filenames])

        if len(_download_filenames) < 1:
            raise RuntimeError(f'No valid download filenames...')
        else:
            return _download_filenames


    def _get_download_urls(self):
        _urls = []

        for filename in self.download_filenames:
            for item in self.config['files']:
                if filename == item['fileName']:
                    filetype = item['fileType']

                    if isinstance(filetype, list):
                        for t in filetype:
                            _urls.append(f'{self.source_url}/{t}/{filename}.csv')
                    else:
                        _urls.append(f'{self.source_url}/{filetype}/{filename}.csv')

        return _urls


# =================================================================================================================== #

if __name__ == '__main__':
    print(f"\n\n---------------------------------------- {__file__.split('/')[-1]}")
