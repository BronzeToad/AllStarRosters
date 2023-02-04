import os
from pathlib import Path
from enum import Enum, auto
import requests
from typing import Optional

import helpers.toad_utils as toadUtils
from helpers.environment_helper import EnvironmentHelper as EnvHelper, EnvFile

import json

# TODO: review - may need updating/fixing after lost work
# =================================================================================================================== #


class ResponseResult(Enum):
    FAILURE = auto()
    SUCCESS = auto()
    UNKNOWN = auto()


class DownloadHelper:

    def __init__(
        self,
        url: str,
        save_dir: str,
        filename: str = None
    ):
        self.url = url
        self.save_dir = save_dir
        self.filename = filename
        self.response = None
        self.payload = None
        self.status_code = None
        self.result = ResponseResult.UNKNOWN
        self._post_init()


    def _post_init(self):
        self.root_dir = EnvHelper(EnvFile.PYTHON).get_env_value('WORKSPACE_DIR')
        self.save_dir = self._get_save_dir()
        self.filename = self.filename or toadUtils.get_filename_from_url(self.url)


    def download(self):
        self.response = requests.get(self.url)
        self.status_code = self._get_status()
        self._set_result()
        if self.result == ResponseResult.SUCCESS:
            self.payload = self.response.content
            self._save_content()
            print(f'Content from {self.url} downloaded successfully.')
        else:
            print(f'Request failed with status code {self.status_code}.')


    def _get_save_dir(self) -> str:
        if Path(self.save_dir).is_dir():
            return self.save_dir
        else:
            _abs_path = os.path.join(self.root_dir, self.save_dir)
            if not Path(_abs_path).is_dir():
                os.makedirs(_abs_path)
            return _abs_path


    def _get_status(self):
        return self.response.status_code


    def _set_result(self) -> None:
        if self.status_code is None:
            self.result = ResponseResult.UNKNOWN
        elif isinstance(self.status_code, int):
            if self.status_code == 200:
                self.result = ResponseResult.SUCCESS
            else:
                self.result = ResponseResult.FAILURE
        else:
            self.result = ResponseResult.UNKNOWN


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
