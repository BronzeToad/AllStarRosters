import os
from pathlib import Path

import requests

import helpers.utilities as toadUtils
from helpers.env_helper import EnvHelper, EnvFile

# ============================================================================ #


class Downloader:
    ROOT_DIR = EnvHelper(EnvFile.PYTHON).root_dir

    def __init__(self,
                 url: str,
                 save_dir: str,
                 filename: str = None,
                 ignore_errors: bool = False):

        self.url = url
        self.save_dir = save_dir
        self.filename = filename
        self.ignore_errors = ignore_errors
        self.response = None

    # ============================================================================ #

    @staticmethod
    def check_response_status(response: requests.Response, ignore_errors: bool = False) -> bool:
        if response.status_code != 200:
            if ignore_errors:
                print(f'Unable to download content from {response.url}\n.'
                      f'Request failed with status code: {response.status_code}\n')
                return False
            else:
                raise requests.exceptions.HTTPError(f'Request failed with status code {response.status_code}...\n'
                                                    f'Response text: {response.text}\n')
        else:
            return True

    @staticmethod
    def save_response_content(response: requests.Response, save_dir: str, filename: str) -> bool:
        save_path = os.path.join(save_dir, filename)
        with open(save_path, 'wb') as file:
            file.write(response.content)
        return True if Path(save_path).is_file() else False

    # ============================================================================ #

    @property
    def url(self) -> str:
        return self._url

    @url.setter
    def url(self, val):
        self._url = val

    @property
    def save_dir(self) -> str:
        return self._save_dir

    @save_dir.setter
    def save_dir(self, val):
        if Path(val).is_dir():
            self._save_dir = val
        else:
            _abs_path = os.path.join(self.ROOT_DIR, val)
            if not Path(_abs_path).is_dir():
                os.makedirs(_abs_path)
            self._save_dir = _abs_path

    @property
    def filename(self) -> str:
        return self._filename

    @filename.setter
    def filename(self, val):
        if val is None:
            self._filename = toadUtils.get_filename_from_url(self.url)
        else:
            self._filename = val

    @property
    def ignore_errors(self) -> bool:
        return self._ignore_errors

    @ignore_errors.setter
    def ignore_errors(self, val):
        self._ignore_errors = val

    @property
    def response(self) -> requests.Response:
        return self._response

    @response.setter
    def response(self, val):
        if val is None:
            self._response = requests.get(self.url)
        else:
            self._response = val

    # ============================================================================ #

    @classmethod
    def download(cls,
                 url: str,
                 save_dir: str,
                 filename: str = None,
                 ignore_errors: bool = False) -> bool:

        doot = cls(url, save_dir, filename, ignore_errors)

        status_good = doot.check_response_status(response=doot.response,
                                                 ignore_errors=doot.ignore_errors)

        if status_good:
            content_saved = doot.save_response_content(response=doot.response,
                                                       save_dir=doot.save_dir,
                                                       filename=doot.filename)
        else:
            content_saved = False

        print('\n--------------------')
        print(f'Filename : {doot.filename}')
        print(f'URL : {doot.url}')
        print(f'Status good? : {status_good}')
        print(f'Content saved? : {content_saved}')

        return True if status_good and content_saved else False

# ============================================================================ #

if __name__ == '__main__':
    print('\n\n-------------------------- Executing as standalone script...')

    tst_url = 'https://raw.githubusercontent.com/chadwickbureau/baseballdatabank/master/core/AllstarFull.csv'
    tst_save_dir = 'data/baseball-databank/raw'

    Downloader.download(url=tst_url, save_dir=tst_save_dir)
