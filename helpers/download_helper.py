import os
from pathlib import Path
from enum import Enum, auto
import requests

import helpers.toad_utils as toadUtils
from helpers.environment_helper import EnvironmentHelper as EnvHelper
from helpers.environment_helper import EnvFile


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
        filename: str = None,
        ignore_errors: bool = False
    ):
        self.url = url
        self.save_dir = save_dir
        self.filename = filename
        self.ignore_errors = ignore_errors
        self.response: requests.Response = None
        self.payload = None         # TODO: check type
        self.status_code = None     # TODO: check type
        self.result: ResponseResult = ResponseResult.UNKNOWN
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
            self.payload = self.response.json()
            self.save_response_content()
            print('blah blah')
        else:
            print('blah blah')


    def _get_save_dir(self) -> str:
        if Path(self.save_dir).is_dir():
            return self.save_dir
        else:
            _abs_path = os.path.join(self.root_dir, self.save_dir)
            if not Path(_abs_path).is_dir():
                os.makedirs(_abs_path)
            return _abs_path



    def _get_status(self):
        try:
            return self.response.status_code
        finally:
            return 999


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


    def save_response_content(self): pass   # TODO





# =================================================================================================================== #

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


# =================================================================================================================== #

if __name__ == '__main__':
    print('\n\n-------------------------- Executing as standalone script...')
