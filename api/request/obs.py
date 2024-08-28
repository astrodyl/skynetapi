from typing import List

import requests

from api.endpoints.observation import Observation


def add(token: str, **kwargs) -> Observation:
    """ Adds a single observation to Skynet using the API.

    :param token: Skynet API token
    :param kwargs: any attribute, value pair defined in api.endpoints.observation
    :return: api.endpoints.observation.Observation object
    """
    return request('POST', token, **kwargs)


def cancel(token: str, obs_id: int | str) -> Observation:
    """ Cancels a single observation to Skynet using the API.

    :param token: Skynet API token
    :param obs_id: Skynet Observation ID to cancel
    :return: api.endpoints.observation.Observation object
    """
    return request('PUT', token, **{'obs_id': obs_id, 'state': 'canceled'})


def update(token: str, **kwargs) -> Observation:
    """ Updates a single observation to Skynet using the API.

    :param token: Skynet API token
    :param kwargs: any attribute, value pair defined in api.endpoints.observation
    :return: api.endpoints.observation.Observation object
    """
    return request('PUT', token, **kwargs)


def get(token: str, **kwargs) -> List[Observation]:
    """ Queries Skynet Observations matching the provided criteria.

    :param kwargs:
        - user: for Skynet admins and group admins only: request observations
            submitted by specific user(s); must be a single integer user ID, a
            string containing a comma-separated list of user IDs or usernames,
            or a list of user IDs or usernames;
            default: return user's own observations

        - group: request group observations; must be a single integer group ID,
            a string containing a comma-separated list of group IDs or names,
            or a list of group IDs or names

        - collab: request collaboration observations; must be a single integer
            collab ID, a string containing a comma-separated list of collab IDs
            or names, or a list of collab IDs or names

        - scope: only return observations submitted to specific telescope(s); must
            be a single integer telescope ID, a string containing a
            comma-separated list of telescope IDs or names, or a list of IDs or
            names

        - after: request observations submitted after the given date/time
        - before: request observations submitted before the given date/time

        - sort_by: sort observations by the given column(s); should be
            a comma-separated list of Observation or Exposure column names
            (prepend "Exposure." if ambiguous), with "-" before the column name
            indicating reversed order

        - offset: only return items starting from the given index

        - limit: only return the given number of items at maximum

        - Other keyword arguments: only return observations with the corresponding
            Observation or Exposure field equal to the given value.

    :param token: Skynet API token
    :param kwargs: any attribute, value pair defined in api.endpoints.observation
    :return: List of observation IDs matching the provided criteria.
    """
    return request('GET', token, **kwargs)


def request(method: str, token: str, **kwargs) -> Observation | List[Observation]:
    """ Sends a request to the Skynet Observation API and returns an
    api.endpoints.observation.Observation for each returned observation
    dictionary. For 'GET' requests, only the observation ID will be set
    in each object.

    :param method: 'GET', 'PUT'. 'POST', 'HEAD', or 'OPTIONS'
    :param token: Skynet API token
    :param kwargs: any attribute, value pair defined in api.endpoints.observation
    :return: api.endpoints.observation.Observation object | list of observation IDs
    """
    payload_type = 'params' if method.upper() in ('GET', 'HEAD', 'OPTIONS') else 'data'

    # Adding observations does not require an observation ID
    obs_id = kwargs.get('obs_id') if 'obs_id' in kwargs else ''

    response = requests.request(method=method, url=f"https://api.skynet.unc.edu/2.0/obs/{obs_id}",
                                **{payload_type: kwargs, 'headers': {'Authentication-Token': token}})

    if response.status_code != 200:
        raise RuntimeError(response.text)

    return [Observation(**d) for d in response.json()] \
        if isinstance(response.json(), list) else Observation(**response.json())
