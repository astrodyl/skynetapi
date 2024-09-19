from typing import List

from skynetapi.requests.http_request import HTTPRequest
from skynetapi.serializable import Serializable


class ExposureRequest(HTTPRequest):
    def __init__(self, token: str):
        super().__init__(token)

    def get(self, exp_id: int | str, ) -> Serializable:
        """ Retrieves a single Skynet exposure by ID.

        :param exp_id: Skynet exposure ID
        :return:
        """
        return self.request('GET', 'exps', **{'id': exp_id})

    def search(self, **kwargs) -> List[int]:
        """ Queries Skynet exposures matching the provided criteria.

        :param kwargs: user, group, collab, scope, after, before, sort_by,
        offset, limit, any Observation or Exposure field

        :return: List of exposure IDs matching the provided criteria.
        """
        return self.request('GET', 'obs', **kwargs)

    def add(self, obs_id: int | str, **kwargs) -> Serializable:
        """ Adds a single exposure to an existing Skynet observation.

        :param obs_id: Skynet observation ID to add to
        :param kwargs: any attribute, value pair for an exposure
        :return:
        """
        kwargs['obs'] = obs_id
        return self.request('POST', 'exps', **kwargs)

    def update(self, exp_id: int | str, **kwargs) -> Serializable:
        """ Updates a single exposure.

        :param exp_id: Skynet exposure ID to update
        :param kwargs: any attribute, value pair for an exposure
        :return:
        """
        kwargs['id'] = exp_id
        return self.request('PUT', 'exps', **kwargs)

    def cancel(self, exp_id: int | str) -> Serializable:
        """ Cancels a single exposure.

        :param exp_id: Skynet exposure ID to cancel
        :return:
        """
        return self.request('PUT', 'exps', **{'id': exp_id, 'state': 'canceled'})
