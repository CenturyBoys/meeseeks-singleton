"""args hash module"""

import itertools


def hash_generator(*args, **kwargs) -> int:
    """
    Created for each arg + kwargs hash. The kwargs`s order doesn't have influence
    """
    hash_instance = tuple(
        item for item in itertools.chain(args, sorted(kwargs.items()))
    )
    return hash(hash_instance)
