import os

import requests

from skynetapi.serializable import Serializable
from skynetapi.utils.string import snake_to_camel


class HTTPRequest:
    def __init__(self, token: str):
        self.token = token
        self._version = '2.0'
        self._url = f'https://api.skynet.unc.edu/{self.version}'

        self._endpoints = ('obs', 'exps', 'download', 'scopes', 'filters')
        self._methods = ('GET', 'POST', 'PUT', 'HEAD', 'OPTIONS')

    @property
    def url(self) -> str:
        return self._url

    @property
    def version(self) -> str:
        return self._version

    @property
    def endpoints(self) -> tuple:
        return self._endpoints

    @property
    def methods(self) -> tuple:
        return self._methods

    def request(self, method: str, endpoint: str, **kwargs):
        """ Sends a http request to the Skynet Observation API and returns
        the response if request was successful.

        :param method: HTTP request operation
        :param endpoint: Skynet API endpoint
        :param kwargs: any attribute, value pair defined in api.endpoints.observation
        :return: requests.Response object
        """
        if method.upper() not in self.methods:
            raise ValueError(f"HTTP method  must be one of: {', '.join(self.methods)}.")

        if endpoint not in self.endpoints:
            raise ValueError(f"Endpoint must be one of {', '.join(self.endpoints)}")

        payload = {'headers': {'Authentication-Token': self.token}}

        if (_id := kwargs.pop('id', '')) and method.upper() == 'GET':
            payload['data'] = {}
        elif method.upper() in ('GET', 'HEAD', 'OPTIONS'):
            payload['params'] = {snake_to_camel(k): v for k, v in kwargs.items()}
        else:
            payload['data'] = {snake_to_camel(k): v for k, v in kwargs.items()}

        response = requests.request(method=method.upper(), url=f"{self.url}/{endpoint}/{_id}", **payload)

        if response.status_code != 200:
            raise RuntimeError(response.text)

        return response.json() if isinstance(response.json(), list) else Serializable(**response.json())

    def download(self, format: str, out_dir: str = None, **kwargs):
        """ Sends a download request via the Skynet API.

        :param format: format of file to download
        :param out_dir: directory to save downloaded file

        """
        payload = {'headers': {'Authentication-Token': self.token},
                   'params': {snake_to_camel(k): v for k, v in kwargs.items()}}

        response = requests.request(method='GET', url=f"{self.url}/download/{format}/", **payload)

        if response.status_code != 200:
            raise RuntimeError(response.text)

        try:  # Download-type request that returns a filename?
            try:
                fn = response.headers['Content-Disposition'].split(
                    'attachment; filename=', 1)[1]
            except IndexError:
                fn = response.headers['Content-Disposition'].split(
                    'inline; filename=', 1)[1]
        except (KeyError, IndexError):
            try:
                if response.headers['Content-Type'] == 'text/plain':
                    # Download/header-type request; return raw data as string
                    return response.text
            except Exception as e:
                raise e

        else:  # Result with an explicit file name and raw data
            try:
                result = fn[fn.index('"') + 1:fn.rindex('"')].strip(), response.content
            except Exception as e:
                raise e

            if out_dir:
                file_path = os.path.join(out_dir, result[0])
                with open(file_path, 'wb') as f:
                    f.write(result[1])
                return file_path
            else:
                return result
