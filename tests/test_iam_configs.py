import pytest

import meeseeks


def test_config_by_args_hash_default_behaviour():
    one_only_one = meeseeks.OnlyOne()
    options = one_only_one.get_options()
    assert options["by_args_hash"] is False


def test_config_by_args_hash_default_invalid_type():
    with pytest.raises(TypeError):
        meeseeks.OnlyOne(by_args_hash=1.0)


def test_config_by_args_hash_set_value():
    one_only_one = meeseeks.OnlyOne(by_args_hash=True)
    options = one_only_one.get_options()
    assert options["by_args_hash"] is True


def test_config_ttl_default_behaviour():
    one_only_one = meeseeks.OnlyOne()
    options = one_only_one.get_options()
    assert options["ttl"] == 0


def test_config_ttl_default_invalid_type():
    with pytest.raises(TypeError):
        meeseeks.OnlyOne(ttl="1")


def test_config_ttl_set_value():
    one_only_one = meeseeks.OnlyOne(ttl=4)
    options = one_only_one.get_options()
    assert options["ttl"] == 4


def test__new__():
    with pytest.raises(TypeError):
        specialized = meeseeks.OnlyOne(1)
