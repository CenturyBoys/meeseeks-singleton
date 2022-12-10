import time
from enum import Enum

import pytest

import meeseeks


class SingletonType(Enum):
    GLOBAL = "global"
    SINGLE = "single"


@pytest.fixture(params=[SingletonType.GLOBAL, SingletonType.SINGLE])
def stub_a(request):
    if request.param == SingletonType.GLOBAL:
        meeseeks.OnlyOne.clean_globals_references()

        @meeseeks.OnlyOne
        class GlobalStubA:
            def __init__(self, *args, **kwargs):
                self.args: tuple = args
                self.kwargs: dict = kwargs

        return GlobalStubA
    if request.param == SingletonType.SINGLE:

        @meeseeks.OnlyOne()
        class StubA:
            def __init__(self, *args, **kwargs):
                self.args: tuple = args
                self.kwargs: dict = kwargs

        return StubA


@pytest.fixture(params=[SingletonType.GLOBAL, SingletonType.SINGLE])
def stub_a_with_bah(request):
    if request.param == SingletonType.GLOBAL:
        meeseeks.OnlyOne.clean_globals_references()
        meeseeks.OnlyOne.set_global_options(by_args_hash=True)

        @meeseeks.OnlyOne
        class GlobalStubA:
            def __init__(self, *args, **kwargs):
                self.args: tuple = args
                self.kwargs: dict = kwargs

        return GlobalStubA
    if request.param == SingletonType.SINGLE:

        @meeseeks.OnlyOne(by_args_hash=True)
        class StubA:
            def __init__(self, *args, **kwargs):
                self.args: tuple = args
                self.kwargs: dict = kwargs

        return StubA


@pytest.fixture(params=[SingletonType.GLOBAL, SingletonType.SINGLE])
def stub_a_with_ttl(request):
    if request.param == SingletonType.GLOBAL:
        meeseeks.OnlyOne.clean_globals_references()
        meeseeks.OnlyOne.set_global_options(ttl=1)

        @meeseeks.OnlyOne
        class GlobalStubA:
            def __init__(self, *args, **kwargs):
                self.args: tuple = args
                self.kwargs: dict = kwargs

        return GlobalStubA
    if request.param == SingletonType.SINGLE:

        @meeseeks.OnlyOne(ttl=1)
        class StubA:
            def __init__(self, *args, **kwargs):
                self.args: tuple = args
                self.kwargs: dict = kwargs

        return StubA


@pytest.fixture(params=[SingletonType.GLOBAL, SingletonType.SINGLE])
def stub_a_with_ttl_and_by_args_hash(request):
    if request.param == SingletonType.GLOBAL:
        meeseeks.OnlyOne.clean_globals_references()
        meeseeks.OnlyOne.set_global_options(by_args_hash=True, ttl=1)

        @meeseeks.OnlyOne
        class GlobalStubA:
            def __init__(self, *args, **kwargs):
                self.args: tuple = args
                self.kwargs: dict = kwargs

        return GlobalStubA
    if request.param == SingletonType.SINGLE:

        @meeseeks.OnlyOne(by_args_hash=True, ttl=1)
        class StubA:
            def __init__(self, *args, **kwargs):
                self.args: tuple = args
                self.kwargs: dict = kwargs

        return StubA


def test_get_same_instance(stub_a):
    a1 = stub_a()
    a2 = stub_a()
    have_seme_instance = a1 == a2
    assert have_seme_instance


def test_get_same_instance_with_ignore_args_and_kwargs(stub_a):
    a1 = stub_a(1, var_a="a")
    a2 = stub_a(10, var_b="a")
    have_seme_instance = a1 == a2
    assert have_seme_instance


def test_get_instance_by_args_hash(stub_a_with_bah):

    a1a = stub_a_with_bah(1, var_a="a")
    a2a = stub_a_with_bah(10, var_b="a")
    a1b = stub_a_with_bah(1, var_a="a")
    a2b = stub_a_with_bah(10, var_b="a")

    assert a1a == a1b
    assert a2a == a2b
    assert a1a != a2b


def test_get_instance_with_ttl(stub_a_with_ttl):

    a1a = stub_a_with_ttl(1, var_a="a")
    a2a = stub_a_with_ttl(10, var_b="a")
    a1b = stub_a_with_ttl(1, var_a="a")
    a2b = stub_a_with_ttl(10, var_b="a")

    time.sleep(1)

    a1c = stub_a_with_ttl(1, var_a="a")
    a2c = stub_a_with_ttl(10, var_b="a")

    assert a1a == a1b
    assert a2a == a2b
    assert a1a == a2b
    assert a1b != a1c
    assert a2b != a2c


def test_get_instance_with_ttl_and_instance_by_args_hash(
    stub_a_with_ttl_and_by_args_hash,
):

    a1a = stub_a_with_ttl_and_by_args_hash(1, var_a="a")
    a2a = stub_a_with_ttl_and_by_args_hash(10, var_b="a")
    a1b = stub_a_with_ttl_and_by_args_hash(1, var_a="a")
    a2b = stub_a_with_ttl_and_by_args_hash(10, var_b="a")

    time.sleep(1)

    a1c = stub_a_with_ttl_and_by_args_hash(1, var_a="a")
    a2c = stub_a_with_ttl_and_by_args_hash(10, var_b="a")
    a1d = stub_a_with_ttl_and_by_args_hash(1, var_a="a")
    a2d = stub_a_with_ttl_and_by_args_hash(10, var_b="a")

    assert a1a == a1b
    assert a2a == a2b
    assert a1a != a2b

    assert a1c == a1d
    assert a2c == a2d
    assert a1c != a2d

    assert a1b not in [a1c, a1d]
    assert a2b not in [a2c, a2d]


def test_clean_specialized_same_instance(stub_a):

    specialized = meeseeks.OnlyOne(by_args_hash=True)

    @specialized
    class StubA:
        def __init__(self, *args, **kwargs):
            self.args: tuple = args
            self.kwargs: dict = kwargs

    a1 = StubA(1, 2)
    a2 = StubA(1, 2)
    assert a1 == a2

    specialized.clean_references()

    a3 = StubA(1, 2)

    assert a1 != a3
