from api.endpoints.endpoint import Endpoint
from api.utils.string import camel_to_snake


class Exposure(Endpoint):
    def __init__(self, **kw):
        super().__init__()
        self.from_dict(kw)

    def from_dict(self, d: dict) -> None:
        """ Sets the values for the class attributes using the corresponding
        keys in the provided dictionary. Allows for any attribute to be set.

        :param d: Key value pairing of attributes and values
        """
        for attribute, value in d.items():
            setattr(self, camel_to_snake(attribute), value)
