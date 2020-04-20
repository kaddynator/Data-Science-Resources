import logging
from os import environ
from json import JSONEncoder
from datetime import datetime
from decimal import Decimal
from uuid import UUID
from numpy import ndarray


class BetterEncoder(JSONEncoder):
    """A better JSON encoder for this app. Does some basic type
    checks and converts them to reasonable alternatives. Has
    an available numpy converter disabled by default.

    Returns
    -------
    JSONEncoder
        A better version of the base JSONEncoder
    """

    def default(self, o):  # pylint: disable=E0202
        if isinstance(o, Decimal):
            return float(o)
        if isinstance(o, datetime):
            return o.strftime("%Y-%m-%d %H:%M:%S")
        if isinstance(o, UUID):
            return str(o)
        if isinstance(o, set):
            return list(o)
        if isinstance(o, ndarray):
            return list(o)
        return super(BetterEncoder, self).default(o)


def generate_config():
    """generate_config

    Generate configuration in environment variables based on
    existing environment variables, filling with local defaults
    where appropriate.

    Returns
    -------
    dict
        Dictionary of configurations
    """
    config_list = {'DEBUG': False,
                   'TESTING': False,
                   'LOGLEVEL': logging.WARNING,
                   'FLASK_ENV': 'DEBUG',
                   'FLASK_SECRET': b'_5#y2L"F4Qasdf8z\n\xec]/'
                   }

    bool_fields = [x for x in config_list if isinstance(config_list[x], bool)]
    new_configs = {x: environ[x] if x in environ and environ[x] != '' and environ[x] is not None else config_list[x]
                   for x in config_list}

    for field in bool_fields:
        if isinstance(new_configs[field], bool):
            pass
        else:
            check = new_configs[field] == 'True'
            new_configs[field] = check
    return new_configs
