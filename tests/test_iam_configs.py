from meeseeks import OnlyOne


def test_global_config_by_args_hash_default_behaviour():
    OnlyOne.set_global_options()
    global_options = OnlyOne.get_global_options()
    assert global_options["by_args_hash"] is False


def test_global_config_by_args_hash_default_invalid_type():
    OnlyOne.set_global_options(by_args_hash=0)
    global_options = OnlyOne.get_global_options()
    assert global_options["by_args_hash"] is False


def test_global_config_by_args_hash_set_value():
    OnlyOne.set_global_options(by_args_hash=True)
    global_options = OnlyOne.get_global_options()
    assert global_options["by_args_hash"] is True


def test_global_config_ttl_default_behaviour():
    OnlyOne.set_global_options()
    global_options = OnlyOne.get_global_options()
    assert global_options["ttl"] == 0


def test_global_config_ttl_set_value():
    OnlyOne.set_global_options(ttl=3)
    global_options = OnlyOne.get_global_options()
    assert global_options["ttl"] == 3


def test_config_by_args_hash_default_behaviour():
    one_only_one = OnlyOne()
    options = one_only_one.get_options()
    assert options["by_args_hash"] is False


def test_config_by_args_hash_default_invalid_type():
    one_only_one = OnlyOne(by_args_hash=1.0)
    options = one_only_one.get_options()
    assert options["by_args_hash"] is False


def test_config_by_args_hash_set_value():
    one_only_one = OnlyOne(by_args_hash=True)
    options = one_only_one.get_options()
    assert options["by_args_hash"] is True


def test_config_ttl_default_behaviour():
    one_only_one = OnlyOne()
    options = one_only_one.get_options()
    assert options["ttl"] == 0


def test_config_ttl_default_invalid_type():
    one_only_one = OnlyOne(ttl="1")
    options = one_only_one.get_options()
    assert options["ttl"] == 0


def test_config_ttl_set_value():
    one_only_one = OnlyOne(ttl=4)
    options = one_only_one.get_options()
    assert options["ttl"] == 4


def test_cross_config_ttl_class_behaviour():
    OnlyOne.set_global_options()
    one_only_one = OnlyOne(ttl=4)
    global_options = OnlyOne.get_global_options()
    options = one_only_one.get_options()
    assert global_options["ttl"] == 0
    assert options["ttl"] == 4
    assert global_options["ttl"] != options["ttl"]


def test_cross_config_ttl_object_behaviour():
    OnlyOne.set_global_options(ttl=10)
    one_only_one = OnlyOne()
    global_options = OnlyOne.get_global_options()
    options = one_only_one.get_options()
    assert global_options["ttl"] == 10
    assert options["ttl"] == 0
    assert global_options["ttl"] != options["ttl"]


def test_cross_config_by_args_hash_class_behaviour():
    OnlyOne.set_global_options()
    one_only_one = OnlyOne(by_args_hash=True)
    global_options = OnlyOne.get_global_options()
    options = one_only_one.get_options()
    assert global_options["by_args_hash"] is False
    assert options["by_args_hash"] is True
    assert global_options["by_args_hash"] != options["by_args_hash"]


def test_cross_config_by_args_hash_object_behaviour():
    OnlyOne.set_global_options(by_args_hash=True)
    one_only_one = OnlyOne()
    global_options = OnlyOne.get_global_options()
    options = one_only_one.get_options()
    assert global_options["by_args_hash"] is True
    assert options["by_args_hash"] is False
    assert global_options["by_args_hash"] != options["by_args_hash"]
