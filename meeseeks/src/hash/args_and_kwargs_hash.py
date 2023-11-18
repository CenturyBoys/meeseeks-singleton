"""args hash module"""

import itertools
from typing import Hashable


def hash_generator(*args, **kwargs) -> int:
    """
    Created for each arg + kwargs hash. The kwargs`s order doesn't have influence
    """
    hash_instance = tuple(
        item if isinstance(item, Hashable) else str(item)
        for item in itertools.chain(args, [i[1] for i in sorted(kwargs.items())])
    )
    return hash(hash_instance)
