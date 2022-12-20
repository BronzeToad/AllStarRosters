import os.path as osPath
import requests

from pathlib import Path as LibPath
from icecream import ic

from helpers.environment_helper import EnvironmentHelper as EnvHelper
import helpers.data_utilities as dataUtils

# ============================================================================ #

class Downloader:

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
        self.content = None
        
# ============================================================================ #

    @staticmethod
    def check_response_status(response: requests.Response, ignore_errors: bool = False) -> bool:
        status_code = response.status_code
        response_text = response.text
        if status_code != 200:
            if ignore_errors:
                print(f'Unable to download content from {response.url}\n.'
                      f'Request failed with status code: {status_code}\n')
                return False
            else:
                raise RuntimeError(f'Request failed with status code {status_code}...\n'
                                   f'Response text: {response_text}\n')
        elif status_code == 200:
            return True
        else:
            raise RuntimeError(f'API request failed for some other reason...\n'
                               f'Response text: {response_text}\n')
    
    
    @staticmethod
    def save_response_content(content: bytes, save_dir: str, filename: str):
        filepath = osPath.join(save_dir, filename)
        with open(filepath, 'w') as f:
            f.write(str(content))
        if LibPath(filepath).is_file():
            print(f'{filename} downloaded to {save_dir}')
        else:
            print(f'{filepath} does not exist...')
            
# ============================================================================ #

    @property
    def url(self) -> str:
        return self._url

    @url.setter
    def url(self, val: str) -> None:
        self._url = val
        
    
    @property
    def save_dir(self) -> str:
        return self._save_dir
    
    @save_dir.setter
    def save_dir(self, val: str) -> None:
        if not LibPath(val).is_dir():
            _dir = osPath.join(EnvHelper().workspace_dir, val)
            if LibPath(_dir).is_dir():
                val = _dir
            else:
                raise RuntimeError(f'Invalid save directory: {val}.')
        self._save_dir = val
        
        
    @property
    def filename(self) -> str:
        return self._filename
    
    @filename.setter
    def filename(self, val: str) -> None:
        if val is None:
            val = dataUtils.get_filename_from_url(self.url)
        self._filename = val
        
    
    @property
    def ignore_errors(self) -> bool:
        return self._ignore_errors
    
    @ignore_errors.setter
    def ignore_errors(self, val: bool) -> None:
        self._ignore_errors = val
        
# ============================================================================ #

    @property
    def response(self) -> requests.Response:
        return self._response
        
    @response.setter
    def response(self, val) -> None:
        val = requests.get(self.url)
        self._response = val
    
    
    @property
    def content(self) -> bytes:
        return self._content
    
    @content.setter
    def content(self, val) -> None:
        val = self.response.content
        self._content = val
        
# ============================================================================ #

    @classmethod
    def download(cls,
                 url: str,
                 save_dir: str = None,
                 filename: str = None,
                 ignore_errors: bool = False) -> None:
    
        Downloader = cls(url, save_dir, filename, ignore_errors)
        
        if Downloader.check_response_status(response=Downloader.response,
                                            ignore_errors=Downloader.ignore_errors):
            
            Downloader.save_response_content(content=Downloader.content, 
                                             save_dir=Downloader.save_dir, 
                                             filename=Downloader.filename)
            
# ============================================================================ #

if __name__ == '__main__':
    print('\n\n-------------------------- Executing as standalone script...')
    
    tst_url = 'https://raw.githubusercontent.com/chadwickbureau/baseballdatabank/master/core/AllstarFull.csv'
    tst_save_dir = 'data/baseball-databank/raw'
    
    tst = Downloader.download(url=tst_url, save_dir=tst_save_dir)