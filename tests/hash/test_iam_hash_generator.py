from meeseeks.src.hash.args_and_kwargs_hash import hash_generator


def test_hash_generator_args_and_args_reverse():
    hash_1 = hash_generator(1, 2)
    hash_2 = hash_generator(2, 1)
    assert hash_2 == hash_1


def test_hash_generator_args_equal():
    hash_1 = hash_generator(1, 2)
    hash_2 = hash_generator(1, 2)
    assert hash_2 == hash_1


def test_hash_generator_args_not_equal():
    hash_1 = hash_generator(2, 2)
    hash_2 = hash_generator(1, 2)
    assert hash_2 != hash_1


def test_hash_generator_args_not_equal_different_order():
    hash_1 = hash_generator(2, 1)
    hash_2 = hash_generator(1, 2)
    assert hash_2 != hash_1


def test_hash_generator_kwargs_and_kwargs_reverse():
    hash_1 = hash_generator(a=1, b=2)
    hash_2 = hash_generator(b=2, a=1)
    assert hash_2 == hash_1


def test_hash_generator_kwargs_equal():
    hash_1 = hash_generator(a=1, b=2)
    hash_2 = hash_generator(a=1, b=2)
    assert hash_2 == hash_1


def test_hash_generator_kwargs_not_equal():
    hash_1 = hash_generator(a=1, b=2)
    hash_2 = hash_generator(b=1, a=2)
    assert hash_2 != hash_1

