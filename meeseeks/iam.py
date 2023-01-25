"""
This is meeseeks a single class to do singletons. In the core meeseeks is a class decorator
that allows you to have a global singleton scope or a specialized one,
some configurations can be used to give more flexibility to your code.
"""

from datetime import datetime
from meeseeks.src.hash.args_and_kwargs_hash import hash_generator


class OnlyOne:
    """Did you need a help? Meeseeks OnlyOne"""

    def __init__(self, by_args_hash: bool = None, ttl: int = None):
        """This will create a singleton instance with it an independent configuration.

        Keyword arguments:\n
        by_args_hash: bool -- Setting a value greater than 0, the singleton reference
        will have a time to live in seconds (default 0).
        Obs: the expired time validation will be made only when you create
        a new instance of the registered class ie your object will still be in memory.\n
        ttl: int -- Setting True, a singleton reference will be created
        for each arg + kwargs hash (default False).
        Obs:  The kwargs`s order doesn't have influence\n
        """
        by_args_hash, ttl = OnlyOne._validate_config(by_args_hash=by_args_hash, ttl=ttl)

        self.__option_by_args_hash = by_args_hash
        self.__option_ttl = ttl

        self.__singletons_by_args = {}
        self.__singletons = {}

    @staticmethod
    def _validate_config(by_args_hash: any, ttl: any):
        if by_args_hash is None:
            by_args_hash = False
        if ttl is None:
            ttl = 0

        if not isinstance(by_args_hash, bool) or not isinstance(ttl, int):
            raise TypeError(
                f"One of args are not the correct type "
                f"by_args_hash: bool = {type(by_args_hash)} ttl: int = {type(ttl)}"
            )
        return by_args_hash, ttl

    def get_options(self) -> dict:
        """Return a dict with all configurations"""
        return {"by_args_hash": self.__option_by_args_hash, "ttl": self.__option_ttl}

    def clean_references(self):
        """Clean up all memory instances references"""
        self.__singletons_by_args = {}
        self.__singletons = {}

    def __call__(self, class_reference, *args, **kwargs):
        class_reference__init__ = class_reference.__init__

        def __new__(cls, *args, **kwargs):
            hash_str = hash_generator(*args, **kwargs)

            if self.__option_by_args_hash:
                if object_instance := self.__get_singleton_by_hash(
                    class_reference=class_reference, hash_str=hash_str
                ):
                    return object_instance
                object_instance = object.__new__(cls)
                self.__set_singleton_by_hash(
                    class_reference=class_reference,
                    object_instance=object_instance,
                    hash_str=hash_str,
                )
            else:
                if object_instance := self.__get_simple_singleton(
                    class_reference=class_reference
                ):
                    return object_instance
                object_instance = object.__new__(cls)
                self.__set_simple_singleton(
                    class_reference=class_reference, object_instance=object_instance
                )

            class_reference__init__(object_instance, *args, **kwargs)
            return object_instance

        class_reference.__new__ = __new__
        del class_reference.__init__

        return class_reference

    def __set_singleton_by_hash(self, class_reference, hash_str: str, object_instance):
        if self.__singletons_by_args.get(class_reference) is None:
            self.__singletons_by_args.update({class_reference: {}})
        self.__singletons_by_args[class_reference].update(
            {
                hash_str: {
                    "instance": object_instance,
                    "created_at": datetime.utcnow().timestamp(),
                }
            }
        )

    def __get_singleton_by_hash(self, class_reference, hash_str: str):

        if class_singletons_by_args := self.__singletons_by_args.get(class_reference):
            if singleton := class_singletons_by_args.get(hash_str):
                if self.__option_ttl:
                    valid_until = singleton.get("created_at") + self.__option_ttl
                    if valid_until >= datetime.utcnow().timestamp():
                        return singleton.get("instance")
                    del class_singletons_by_args[hash_str]
                else:
                    return singleton.get("instance")
        return None

    def __set_simple_singleton(self, class_reference, object_instance):
        self.__singletons.update(
            {
                class_reference: {
                    "instance": object_instance,
                    "created_at": datetime.utcnow().timestamp(),
                }
            }
        )

    def __get_simple_singleton(self, class_reference):
        if singleton := self.__singletons.get(class_reference):
            if self.__option_ttl:
                valid_until = singleton.get("created_at") + self.__option_ttl
                if valid_until >= datetime.utcnow().timestamp():
                    return singleton.get("instance")
                del self.__singletons[class_reference]
            else:
                return singleton.get("instance")
        return None
