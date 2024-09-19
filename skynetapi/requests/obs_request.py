from typing import List

from skynetapi.requests.http_request import HTTPRequest
from skynetapi.serializable import Serializable


class ObservationRequest(HTTPRequest):
    def __init__(self, token: str):
        super().__init__(token)

    def get(self, obs_id: int | str) -> Serializable:
        """ Retrieves a single Skynet observation by ID.

        :param obs_id: Skynet observation ID to retrieve
        :return:
        """
        return self.request('GET', 'obs', **{'id': obs_id})

    def search(self, **kwargs) -> List[dict]:
        """ Queries Skynet observations matching the provided criteria.

        :param kwargs: user, group, collab, scope, after, before, sort_by,
        offset, limit, any observation or exposure field
        :return: list of 'id': <id> key value pairs
        """
        return self.request('GET', 'obs', **kwargs)

    def add(self, **kwargs) -> Serializable:
        """ Adds a single observation to Skynet.

        :param kwargs: any attribute, value pair for an observation
        :return:
        """
        return self.request('POST', 'obs', **kwargs)

    def update(self, obs_id: int | str, **kwargs) -> Serializable:
        """ Updates a single observation to Skynet.

        :param obs_id: Skynet Observation ID
        :param kwargs: any attribute, value pair for an observation
        :return:
        """
        kwargs['id'] = obs_id
        return self.request('PUT', 'obs', **kwargs)

    def cancel(self, obs_id: int | str) -> Serializable:
        """ Cancels a single observation to Skynet.

        :param obs_id: Skynet Observation ID to cancel
        :return:
        """
        return self.request('PUT', 'obs', **{'id': obs_id, 'state': 'canceled'})
