import time
from enum import Enum

import pytest

import meeseeks


class SingletonType(Enum):
    GLOBAL = "global"
    SINGLE = "single"


@pytest.fixture
def stub_a_global_and_instance():
    meeseeks.OnlyOne.clean_globals_references()

    @meeseeks.OnlyOne
    class GlobalStubA:
        def __init__(self, *args, **kwargs):
            self.args: tuple = args
            self.kwargs: dict = kwargs

    @meeseeks.OnlyOne()
    class StubA:
        def __init__(self, *args, **kwargs):
            self.args: tuple = args
            self.kwargs: dict = kwargs

    return GlobalStubA, StubA


@pytest.fixture
def stub_a_global_and_instance_with_bah():
    meeseeks.OnlyOne.clean_globals_references()
    meeseeks.OnlyOne.set_global_options(by_args_hash=True)

    @meeseeks.OnlyOne
    class GlobalStubA:
        def __init__(self, *args, **kwargs):
            self.args: tuple = args
            self.kwargs: dict = kwargs

    @meeseeks.OnlyOne(by_args_hash=True)
    class StubA:
        def __init__(self, *args, **kwargs):
            self.args: tuple = args
            self.kwargs: dict = kwargs

    return GlobalStubA, StubA


@pytest.fixture
def stub_a_global_and_instance_with_ttl():

    meeseeks.OnlyOne.clean_globals_references()
    meeseeks.OnlyOne.set_global_options(ttl=1)

    @meeseeks.OnlyOne
    class GlobalStubA:
        def __init__(self, *args, **kwargs):
            self.args: tuple = args
            self.kwargs: dict = kwargs

    @meeseeks.OnlyOne(ttl=1)
    class StubA:
        def __init__(self, *args, **kwargs):
            self.args: tuple = args
            self.kwargs: dict = kwargs

    return GlobalStubA, StubA


@pytest.fixture
def stub_a_global_and_instance_with_ttl_and_by_args_hash():

    meeseeks.OnlyOne.clean_globals_references()
    meeseeks.OnlyOne.set_global_options(by_args_hash=True, ttl=1)

    @meeseeks.OnlyOne
    class GlobalStubA:
        def __init__(self, *args, **kwargs):
            self.args: tuple = args
            self.kwargs: dict = kwargs

    @meeseeks.OnlyOne(by_args_hash=True, ttl=1)
    class StubA:
        def __init__(self, *args, **kwargs):
            self.args: tuple = args
            self.kwargs: dict = kwargs

    return GlobalStubA, StubA


def test_global_get_same_instance(stub_a_global_and_instance):
    with_global_config, with_single_config = stub_a_global_and_instance
    a1 = with_global_config()
    a2 = with_single_config()
    have_seme_instance = a1 != a2
    assert have_seme_instance


def test_global_get_same_instance_with_ignore_args_and_kwargs(
    stub_a_global_and_instance,
):
    with_global_config, with_single_config = stub_a_global_and_instance
    a1 = with_global_config(1, var_a="a")
    a2 = with_single_config(1, var_a="a")
    have_seme_instance = a1 != a2
    assert have_seme_instance


def test_global_get_instance_by_args_hash(stub_a_global_and_instance_with_bah):
    with_global_config, with_single_config = stub_a_global_and_instance_with_bah

    a1a = with_global_config(1, var_a="a")
    a2a = with_global_config(10, var_b="a")
    a1b = with_global_config(1, var_a="a")
    a2b = with_global_config(10, var_b="a")

    assert a1a == a1b
    assert a2a == a2b
    assert a1a != a2b

    b1a = with_single_config(1, var_a="a")
    b2a = with_single_config(10, var_b="a")
    b1b = with_single_config(1, var_a="a")
    b2b = with_single_config(10, var_b="a")

    assert b1a == b1b
    assert b2a == b2b
    assert b1a != b2b

    assert a1a != b1a
    assert a2a != b2a


def test_global_get_instance_with_ttl(stub_a_global_and_instance_with_ttl):

    with_global_config, with_single_config = stub_a_global_and_instance_with_ttl

    a1a = with_global_config(1, var_a="a")
    a2a = with_global_config(10, var_b="a")
    a1b = with_global_config(1, var_a="a")
    a2b = with_global_config(10, var_b="a")

    b1a = with_single_config(1, var_a="a")
    b2a = with_single_config(10, var_b="a")
    b1b = with_single_config(1, var_a="a")
    b2b = with_single_config(10, var_b="a")

    time.sleep(1)

    a1c = with_global_config(1, var_a="a")
    a2c = with_global_config(10, var_b="a")

    b1c = with_single_config(1, var_a="a")
    b2c = with_single_config(10, var_b="a")

    assert a1a == a1b
    assert a2a == a2b
    assert a1a == a2b
    assert a1b != a1c
    assert a2b != a2c

    assert b1a == b1b
    assert b2a == b2b
    assert b1a == b2b
    assert b1b != b1c
    assert b2b != b2c

    assert a1a != b1a
    assert a2a != b2a
    assert a1c != b1c
    assert a1c != b1c


def test_global_get_instance_with_ttl_and_instance_by_args_hash(
    stub_a_global_and_instance_with_ttl_and_by_args_hash,
):

    (
        with_global_config,
        with_single_config,
    ) = stub_a_global_and_instance_with_ttl_and_by_args_hash

    a1a = with_global_config(1, var_a="a")
    a2a = with_global_config(10, var_b="a")
    a1b = with_global_config(1, var_a="a")
    a2b = with_global_config(10, var_b="a")

    b1a = with_single_config(1, var_a="a")
    b2a = with_single_config(10, var_b="a")
    b1b = with_single_config(1, var_a="a")
    b2b = with_single_config(10, var_b="a")

    time.sleep(1)

    a1c = with_global_config(1, var_a="a")
    a2c = with_global_config(10, var_b="a")
    a1d = with_global_config(1, var_a="a")
    a2d = with_global_config(10, var_b="a")

    b1c = with_single_config(1, var_a="a")
    b2c = with_single_config(10, var_b="a")
    b1d = with_single_config(1, var_a="a")
    b2d = with_single_config(10, var_b="a")

    assert a1a == a1b
    assert a2a == a2b
    assert a1a != a2b

    assert a1c == a1d
    assert a2c == a2d
    assert a1c != a2d

    assert a1b not in [a1c, a1d]
    assert a2b not in [a2c, a2d]

    assert b1a == b1b
    assert b2a == b2b
    assert b1a != b2b

    assert b1c == b1d
    assert b2c == b2d
    assert b1c != b2d

    assert b1b not in [b1c, b1d]
    assert b2b not in [b2c, b2d]

    assert a1b != b1b
    assert a2b != b2b

    assert a1d != a2d
    assert a1d != b2d
