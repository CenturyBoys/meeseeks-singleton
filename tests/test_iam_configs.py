import pytest

import meeseeks


def test_config_by_args_hash_default_behaviour():
    one_only_one = meeseeks.OnlyOne()
    assert one_only_one._option_by_args_hash is False


def test_config_by_args_hash_default_invalid_type():
    with pytest.raises(TypeError):
        meeseeks.OnlyOne(by_args_hash=1.0)


def test_config_by_args_hash_set_value():
    one_only_one = meeseeks.OnlyOne(by_args_hash=True)
    assert one_only_one._option_by_args_hash is True


def test_config_ttl_default_behaviour():
    one_only_one = meeseeks.OnlyOne()
    assert one_only_one._option_ttl == 0


def test_config_ttl_default_invalid_type():
    with pytest.raises(TypeError):
        meeseeks.OnlyOne(ttl="1")


def test_config_ttl_set_value():
    one_only_one = meeseeks.OnlyOne(ttl=4)
    assert one_only_one._option_ttl == 4


def test__new__():
    with pytest.raises(TypeError):
        meeseeks.OnlyOne(1)
