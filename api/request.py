from importlib import import_module


def request(endpoint: str, method: str, token: str, **kwargs):
    """ Sends the request to the appropriate package.

    :param endpoint: API endpoint
    :param method: HTTP method
    :param token: API token
    :param kwargs: Keyword arguments
    :return: Corresponding object in api.endpoints
    """
    if method not in ('GET', 'POST', 'PUT', 'HEAD', 'OPTIONS'):
        raise ValueError('Method must be GET, POST, PUT, HEAD, or OPTIONS')

    return import_module(f'request.{endpoint}').request(method, token, **kwargs)
