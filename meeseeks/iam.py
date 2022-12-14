import inspect
from datetime import datetime

import meeseeks
from meeseeks.src.hash.args_and_kwargs_hash import hash_generator


class OnlyOne:

    __global_option_by_args_hash = False
    __global_option_ttl = 0

    __global_singletons = dict()
    __global_singletons_by_args = dict()

    @classmethod
    def set_global_options(cls, by_args_hash: bool = None, ttl: int = None):
        """This will set a global singleton configuration.

        Keyword arguments:\n
        by_args_hash: bool -- Setting a value greater than 0, the singleton reference will have a time to live in
        seconds (default 0).
        Obs: the expired time validation will be made only when you create
        a new instance of the registered class ie your object will still be in memory.\n
        ttl: int -- Setting True, a singleton reference will be created for each arg + kwargs hash (default False).
        Obs:  The kwargs`s order doesn't have influence\n
        """
        by_args_hash, ttl = OnlyOne._validate_config(by_args_hash=by_args_hash, ttl=ttl)

        cls.__global_option_by_args_hash = by_args_hash
        cls.__global_option_ttl = ttl

    def __init__(self, by_args_hash: bool = None, ttl: int = None):
        """This will create a singleton instance with it an independent configuration.

        Keyword arguments:\n
        by_args_hash: bool -- Setting a value greater than 0, the singleton reference will have a time to live in
        seconds (default 0).
        Obs: the expired time validation will be made only when you create
        a new instance of the registered class ie your object will still be in memory.\n
        ttl: int -- Setting True, a singleton reference will be created for each arg + kwargs hash (default False).
        Obs:  The kwargs`s order doesn't have influence\n
        """
        by_args_hash, ttl = OnlyOne._validate_config(by_args_hash=by_args_hash, ttl=ttl)

        self.__option_by_args_hash = by_args_hash
        self.__option_ttl = ttl

        self.__singletons_by_args = dict()
        self.__singletons = dict()

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

    @classmethod
    def get_global_options(cls) -> dict:
        """Return a dict with all global configurations"""
        return {
            "by_args_hash": cls.__global_option_by_args_hash,
            "ttl": cls.__global_option_ttl,
        }

    def get_options(self) -> dict:
        """Return a dict with all configurations"""
        return {"by_args_hash": self.__option_by_args_hash, "ttl": self.__option_ttl}

    @classmethod
    def clean_globals_references(cls):
        """Clean up all gloabl memory instances references"""
        cls.__global_singletons = dict()
        cls.__global_singletons_by_args = dict()

    def clean_references(self):
        """Clean up all memory instances references"""
        self.__singletons_by_args = dict()
        self.__singletons = dict()

    def __call__(self, class_reference, *args, **kwargs):
        callback = self.__build_callback(
            class_reference=class_reference,
            option_by_args_hash=self.__option_by_args_hash,
            get_singleton_by_hash=self.__get_singleton_by_hash,
            get_simple_singleton=self.__get_simple_singleton,
            set_singleton_by_hash=self.__set_singleton_by_hash,
            set_simple_singleton=self.__set_simple_singleton,
        )
        return callback

    def __new__(cls, *args, **kwargs):
        if args:
            first_args_element, *args = args

            if inspect.isclass(first_args_element):
                callback = cls.__build_callback(
                    class_reference=first_args_element,
                    option_by_args_hash=cls.__global_option_by_args_hash,
                    get_singleton_by_hash=cls.__get_global_singleton_by_hash,
                    get_simple_singleton=cls.__get_global_simple_singleton,
                    set_singleton_by_hash=cls.__set_global_singleton_by_hash,
                    set_simple_singleton=cls.__set_global_simple_singleton,
                )
                return callback

        obj = object.__new__(cls)
        return obj

    @staticmethod
    def __build_callback(
        class_reference,
        option_by_args_hash,
        get_singleton_by_hash,
        get_simple_singleton,
        set_singleton_by_hash,
        set_simple_singleton,
    ):
        def __new__(cls, *args, **kwargs):
            hash_str = hash_generator(*args, **kwargs)

            if option_by_args_hash:
                if object_instance := get_singleton_by_hash(
                    class_reference=class_reference, hash_str=hash_str
                ):
                    return object_instance
                object_instance = object.__new__(cls)
                set_singleton_by_hash(
                    class_reference=class_reference,
                    object_instance=object_instance,
                    hash_str=hash_str,
                )
            else:
                if object_instance := get_simple_singleton(
                    class_reference=class_reference
                ):
                    return object_instance
                object_instance = object.__new__(cls)
                set_simple_singleton(
                    class_reference=class_reference, object_instance=object_instance
                )

            return object_instance

        class_reference.__new__ = __new__

        return class_reference

    @classmethod
    def __set_global_singleton_by_hash(
        cls, class_reference, hash_str: str, object_instance
    ):
        OnlyOne.__set_any_singleton_by_hash(
            singletons_by_args=cls.__global_singletons_by_args,
            class_reference=class_reference,
            hash_str=hash_str,
            object_instance=object_instance,
        )

    def __set_singleton_by_hash(self, class_reference, hash_str: str, object_instance):
        OnlyOne.__set_any_singleton_by_hash(
            singletons_by_args=self.__singletons_by_args,
            class_reference=class_reference,
            hash_str=hash_str,
            object_instance=object_instance,
        )

    @staticmethod
    def __set_any_singleton_by_hash(
        singletons_by_args: dict, class_reference, hash_str: str, object_instance
    ):
        if singletons_by_args.get(class_reference) is None:
            singletons_by_args.update({class_reference: dict()})
        singletons_by_args[class_reference].update(
            {
                hash_str: {
                    "instance": object_instance,
                    "created_at": datetime.utcnow().timestamp(),
                }
            }
        )

    @classmethod
    def __get_global_singleton_by_hash(cls, class_reference, hash_str: str):
        instance = OnlyOne.__get_any_singleton_by_hash(
            singletons_by_args=cls.__global_singletons_by_args,
            class_reference=class_reference,
            hash_str=hash_str,
            option_ttl=cls.__global_option_ttl,
        )
        return instance

    def __get_singleton_by_hash(self, class_reference, hash_str: str):
        instance = OnlyOne.__get_any_singleton_by_hash(
            singletons_by_args=self.__singletons_by_args,
            class_reference=class_reference,
            hash_str=hash_str,
            option_ttl=self.__option_ttl,
        )
        return instance

    @staticmethod
    def __get_any_singleton_by_hash(
        singletons_by_args: dict, class_reference, hash_str: str, option_ttl: int
    ):
        if class_singletons_by_args := singletons_by_args.get(class_reference):
            if singleton := class_singletons_by_args.get(hash_str):
                if option_ttl:
                    valid_until = singleton.get("created_at") + option_ttl
                    if valid_until >= datetime.utcnow().timestamp():
                        return singleton.get("instance")
                    del class_singletons_by_args[hash_str]
                else:
                    return singleton.get("instance")

    @classmethod
    def __set_global_simple_singleton(cls, class_reference, object_instance):
        OnlyOne.__set_any_simple_singleton(
            singletons=cls.__global_singletons,
            class_reference=class_reference,
            object_instance=object_instance,
        )

    def __set_simple_singleton(self, class_reference, object_instance):
        OnlyOne.__set_any_simple_singleton(
            singletons=self.__singletons,
            class_reference=class_reference,
            object_instance=object_instance,
        )

    @staticmethod
    def __set_any_simple_singleton(singletons: dict, class_reference, object_instance):
        singletons.update(
            {
                class_reference: {
                    "instance": object_instance,
                    "created_at": datetime.utcnow().timestamp(),
                }
            }
        )

    @classmethod
    def __get_global_simple_singleton(cls, class_reference):
        instance = OnlyOne.__get_any_simple_singleton(
            singletons=cls.__global_singletons,
            class_reference=class_reference,
            option_ttl=cls.__global_option_ttl,
        )
        return instance

    def __get_simple_singleton(self, class_reference):
        instance = OnlyOne.__get_any_simple_singleton(
            singletons=self.__singletons,
            class_reference=class_reference,
            option_ttl=self.__option_ttl,
        )
        return instance

    @staticmethod
    def __get_any_simple_singleton(singletons, class_reference, option_ttl: int):
        if singleton := singletons.get(class_reference):
            if option_ttl:
                valid_until = singleton.get("created_at") + option_ttl
                if valid_until >= datetime.utcnow().timestamp():
                    return singleton.get("instance")
                del singletons[class_reference]
            else:
                return singleton.get("instance")
