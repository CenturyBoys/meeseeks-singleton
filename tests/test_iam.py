import meeseeks


@meeseeks.OnlyOne
class GlobalStubA:
    def __init__(self, *args, **kwargs):
        self.args: tuple = args
        self.kwargs: dict = kwargs


@meeseeks.OnlyOne()
class StubAWithArgsHashFalseTtl0:
    def __init__(self, *args, **kwargs):
        self.args: tuple = args
        self.kwargs: dict = kwargs


@meeseeks.OnlyOne(by_args_hash=True)
class StubAWithArgsHashTrueTtl0:
    def __init__(self, *args, **kwargs):
        self.args: tuple = args
        self.kwargs: dict = kwargs


@meeseeks.OnlyOne(ttl=1)
class StubAWithArgsHashFalseTtl1:
    def __init__(self, *args, **kwargs):
        self.args: tuple = args
        self.kwargs: dict = kwargs


@meeseeks.OnlyOne(by_args_hash=True, ttl=1)
class StubAWithArgsHashTrueTtl1:
    def __init__(self, *args, **kwargs):
        self.args: tuple = args
        self.kwargs: dict = kwargs


def test_global_get_same_instance():
    a1 = GlobalStubA()
    a2 = GlobalStubA()
    have_seme_instance = a1 == a2
    assert have_seme_instance


def test_global_get_same_instance_with_ignore_args_and_kwargs():
    a1 = GlobalStubA(1, var_a="a")
    a2 = GlobalStubA(10, var_b="a")
    have_seme_instance = a1 == a2
    assert have_seme_instance


def test_global_get_same_instance_with_args_and_kwargs_equals():
    a1 = StubAWithArgsHashTrueTtl0(1, var_a="a")
    a2 = StubAWithArgsHashTrueTtl0(1, var_a="a")
    have_seme_instance = a1 == a2
    assert have_seme_instance


def test_global_get_same_instance_with_args_and_kwargs_different():
    a1a = StubAWithArgsHashTrueTtl0(1, var_a="a")
    a2a = StubAWithArgsHashTrueTtl0(10, var_b="a")
    have_seme_instance = a1a != a2a
    a1b = StubAWithArgsHashTrueTtl0(1, var_a="a")
    a2b = StubAWithArgsHashTrueTtl0(10, var_b="a")
    assert have_seme_instance
    assert a1a == a1b
    assert a2a == a2b
