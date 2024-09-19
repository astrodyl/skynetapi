from skynetapi.utils.string import snake_to_camel, camel_to_snake


class Serializable:
    def __init__(self, **kw):
        if kw:
            self.from_dict(kw)

    def from_dict(self, d: dict) -> None:
        """ Instantiates the class from a dictionary. Intended for internal
        use only as there is no restriction on the attrs that can be set.
        Stores each key as in snake_case to adhere PEP8 guidelines.

        :param d: Key value pairing of attributes and values
        """
        for k, v in d.items():
            if isinstance(v, list):
                setattr(self, k, [Serializable(**s) if isinstance(s, dict) else s for s in v])

            elif isinstance(v, dict):
                setattr(self, camel_to_snake(k), Serializable(**v))

            else:
                setattr(self, camel_to_snake(k), v)

    def to_dict(self, camel: bool = False) -> dict:
        """ Returns a dictionary representation of the observation. Keys
        are stored in camel case to match the Skynet observation object
        format.

        :param camel: Convert keys to camel case
        :return: Key value pairing of attributes and values
        """
        return {snake_to_camel(k) if camel else k: v for k, v in vars(self).items()}
