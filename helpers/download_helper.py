import os
from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional

import requests

import helpers.toad_utils as toadUtils
from helpers.environment_helper import EnvHelper


# =================================================================================================================== #

@dataclass
class DownloadHelper:
    url: str
    save_dir: str
    filename: Optional[str] = None
    response: requests.Response = field(init=False, repr=False, default=None)
    status_code: int = field(init=False, repr=False, default=None)
    payload: dict = field(init=False, repr=False, default=None)


    def __post_init__(self):
        self.root_dir = EnvHelper().workspace
        self.save_dir = self._get_save_dir()
        self.filename = self.filename or toadUtils.get_url_filename(url=self.url)


    def download(self) -> None:
        self.response = requests.get(self.url)
        self.status_code = self.response.status_code

        if isinstance(self.status_code, int) and self.status_code == 200:
            self.payload = self.response.content
            self._save_content()
        elif isinstance(self.status_code, int) and self.status_code != 200:
            print(f'Request failed with status code {self.status_code}.')
        else:
            print(f'Unable to capture content from {self.url}.')


    def _get_save_dir(self) -> str:
        if Path(self.save_dir).is_dir():
            return self.save_dir
        else:
            _abs_path = os.path.join(self.root_dir, self.save_dir)
            if not Path(_abs_path).is_dir():
                os.makedirs(_abs_path)
            return _abs_path


    def _save_content(self):
        _path = os.path.join(self.save_dir, self.filename)
        with open(_path, 'wb') as file:
            file.write(self.payload)
            file.close()

        if Path(_path).is_file():
            print(f'Filename {self.filename} saved successfully to {self.save_dir}.')
        else:
            print(f'Error saving filename {self.filename} to {self.save_dir}...')


# =================================================================================================================== #

if __name__ == '__main__':
    print(f"\n\n---------------------------------------- {__file__.split('/')[-1]}")
