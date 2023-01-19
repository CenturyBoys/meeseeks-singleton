from enum import Enum

import pytest
from freezegun import freeze_time

import meeseeks


@pytest.fixture()
def stub_a():
    @meeseeks.OnlyOne()
    class StubA:
        def __init__(self, *args, **kwargs):
            self.args: tuple = args
            self.kwargs: dict = kwargs

    return StubA


@pytest.fixture()
def stub_a_with_bah():
    @meeseeks.OnlyOne(by_args_hash=True)
    class StubA:
        def __init__(self, *args, **kwargs):
            self.args: tuple = args
            self.kwargs: dict = kwargs

    return StubA


@pytest.fixture()
def stub_a_with_ttl():
    @meeseeks.OnlyOne(ttl=1)
    class StubA:
        def __init__(self, *args, **kwargs):
            self.args: tuple = args
            self.kwargs: dict = kwargs

    return StubA


@pytest.fixture()
def stub_a_with_ttl_and_by_args_hash():
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
    with freeze_time("2012-01-14 00:00:00"):
        a1a = stub_a_with_ttl(1, var_a="a")
        a2a = stub_a_with_ttl(10, var_b="a")
        a1b = stub_a_with_ttl(1, var_a="a")
        a2b = stub_a_with_ttl(10, var_b="a")

    with freeze_time("2012-01-14 00:00:02"):
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
    with freeze_time("2012-01-14 00:00:00"):
        a1a = stub_a_with_ttl_and_by_args_hash(1, var_a="a")
        a2a = stub_a_with_ttl_and_by_args_hash(10, var_b="a")
        a1b = stub_a_with_ttl_and_by_args_hash(1, var_a="a")
        a2b = stub_a_with_ttl_and_by_args_hash(10, var_b="a")

    with freeze_time("2012-01-14 00:00:02"):
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


def test_clean_specialized_same_instance():

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


def test_ttl_border():

    specialized = meeseeks.OnlyOne(ttl=1)

    @specialized
    class StubA:
        def __init__(self, *args, **kwargs):
            self.args: tuple = args
            self.kwargs: dict = kwargs

    with freeze_time("2012-01-14 00:00:00"):
        a1 = StubA(1, 2)
        a2 = StubA(1, 2)

    assert a1 == a2

    with freeze_time("2012-01-14 00:00:01"):
        a3 = StubA(1, 2)

    assert a1 == a3


def test_ttl_border_with_bah():

    specialized = meeseeks.OnlyOne(ttl=1, by_args_hash=True)

    @specialized
    class StubA:
        def __init__(self, *args, **kwargs):
            self.args: tuple = args
            self.kwargs: dict = kwargs

    with freeze_time("2012-01-14 00:00:00"):
        a1 = StubA(1, 2)
        a2 = StubA(1, 2)

    assert a1 == a2

    with freeze_time("2012-01-14 00:00:01"):
        a3 = StubA(1, 2)

    assert a1 == a3
