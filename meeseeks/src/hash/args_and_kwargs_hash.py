"""args hash module"""

import hashlib


def hash_generator(*args, **kwargs) -> str:
    """
    Created for each arg + kwargs hash. The kwargs`s order doesn't have influence
    """
    hash_args = [str(arg) for arg in args]
    hash_kwargs = [f"{str(key)}{str(arg)}" for key, arg in kwargs.items()]
    hash_kwargs.sort()
    hash_instance = hashlib.sha1(f"{hash_args}{hash_kwargs}".encode())
    return hash_instance.hexdigest()
