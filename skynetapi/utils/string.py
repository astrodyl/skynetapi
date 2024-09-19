

"""
    String Utilities

    String utilities is a collection of useful string manipulation methods.
    Currently, there are only basic string manipulation methods, but it can
    be expanded upon in the future.
"""


def snake_to_camel(s: str) -> str:
    """ Converts a string to camel case and returns it.

    :param s: snake case string
    :return: camel case string
    """
    if '_' not in s:
        return s

    camel_case = [s.split('_')[0]]

    for word in s.split('_')[1:]:
        camel_case.append(word.capitalize())

    return ''.join(camel_case)


def camel_to_snake(s: str) -> str:
    """ Converts a string to snake case and returns it.

    :param s: camel case string
    :return: snake case string
    """
    if '_' in s:
        return s.lower()

    snake_case = s[0].lower()

    for char in s[1:]:
        if char.isupper():
            snake_case += '_'
        snake_case += char.lower()

    return snake_case


def sanitize(s: str) -> str:
    """ Returns a string with only alphanumeric characters.

    :param s: string to remove special characters
    :return: sanitized string
    """
    if s is not None:
        return ''.join(char for char in s if char.isalnum())
