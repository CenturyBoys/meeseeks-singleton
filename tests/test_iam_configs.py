import pytest

import meeseeks


def test_global_config_by_args_hash_default_behaviour():
    meeseeks.OnlyOne.set_global_options()
    global_options = meeseeks.OnlyOne.get_global_options()
    assert global_options["by_args_hash"] is False


def test_global_config_by_args_hash_default_invalid_type():
    with pytest.raises(TypeError):
        meeseeks.OnlyOne.set_global_options(by_args_hash=0)


def test_global_config_by_args_hash_set_value():
    meeseeks.OnlyOne.set_global_options(by_args_hash=True)
    global_options = meeseeks.OnlyOne.get_global_options()
    assert global_options["by_args_hash"] is True


def test_global_config_ttl_default_behaviour():
    meeseeks.OnlyOne.set_global_options()
    global_options = meeseeks.OnlyOne.get_global_options()
    assert global_options["ttl"] == 0


def test_global_config_ttl_set_value():
    meeseeks.OnlyOne.set_global_options(ttl=3)
    global_options = meeseeks.OnlyOne.get_global_options()
    assert global_options["ttl"] == 3


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


def test_cross_config_ttl_class_behaviour():
    meeseeks.OnlyOne.set_global_options()
    one_only_one = meeseeks.OnlyOne(ttl=4)
    global_options = meeseeks.OnlyOne.get_global_options()
    options = one_only_one.get_options()
    assert global_options["ttl"] == 0
    assert options["ttl"] == 4
    assert global_options["ttl"] != options["ttl"]


def test_cross_config_ttl_object_behaviour():
    meeseeks.OnlyOne.set_global_options(ttl=10)
    one_only_one = meeseeks.OnlyOne()
    global_options = meeseeks.OnlyOne.get_global_options()
    options = one_only_one.get_options()
    assert global_options["ttl"] == 10
    assert options["ttl"] == 0
    assert global_options["ttl"] != options["ttl"]


def test_cross_config_by_args_hash_class_behaviour():
    meeseeks.OnlyOne.set_global_options()
    one_only_one = meeseeks.OnlyOne(by_args_hash=True)
    global_options = meeseeks.OnlyOne.get_global_options()
    options = one_only_one.get_options()
    assert global_options["by_args_hash"] is False
    assert options["by_args_hash"] is True
    assert global_options["by_args_hash"] != options["by_args_hash"]


def test_cross_config_by_args_hash_object_behaviour():
    meeseeks.OnlyOne.set_global_options(by_args_hash=True)
    one_only_one = meeseeks.OnlyOne()
    global_options = meeseeks.OnlyOne.get_global_options()
    options = one_only_one.get_options()
    assert global_options["by_args_hash"] is True
    assert options["by_args_hash"] is False
    assert global_options["by_args_hash"] != options["by_args_hash"]


def test__new__():
    with pytest.raises(TypeError):
        specialized = meeseeks.OnlyOne(1)