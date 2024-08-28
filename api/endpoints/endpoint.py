from api.utils.string import snake_to_camel, camel_to_snake


class Endpoint:
    def __init__(self):
        pass

    def from_dict(self, d: dict) -> None:
        """ Sets the values for the class attributes using the corresponding
        keys in the provided dictionary. Keys that do not match existing
        attributes defined in the __init__ method are ignored.

        :param d: Key value pairing of attributes and values
        """
        for attribute, value in d.items():
            if (snake_attr := camel_to_snake(attribute)) in vars(self):
                setattr(self, snake_attr, value)

            # Set protected attributes
            elif '_' + snake_attr in vars(self):
                setattr(self, '_' + snake_attr, value)

    def to_dict(self, camel: bool = False) -> dict:
        """ Returns a dictionary representation of the observation. Keys
        are stored in camel case to match the Skynet observation object
        format.

        :param camel: Convert keys to camel case
        :return: Key value pairing of attributes and values
        """
        return {snake_to_camel(k) if camel else k: v for k, v in vars(self).items()}
