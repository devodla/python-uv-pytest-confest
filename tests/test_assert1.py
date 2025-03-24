import pytest


def f():
    return 3


def myFunc():
    raise ValueError("Exception 123 raised")


def test_function():
    assert f() == 3, "test failed"


def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        1 / 0


def test_match():
    with pytest.raises(ValueError, match=r".* 123 .*"):
        myFunc()


@pytest.mark.xfail(raises=IndexError)
def test_f():
    f()


def test_match_2():
    with pytest.raises(ValueError, match="must be 0 or None"):
        raise ValueError("etcetcs must be 0 or None")


def test_raises_3():
    with pytest.raises(ValueError, match=r"must be \d+$"):
        raise ValueError("value must be 42")


def test_raises_4():
    with pytest.raises(ValueError) as exc_info:
        raise ValueError("value must be 42")

    assert exc_info.type is ValueError
    assert exc_info.value.args[0] == "value must be 42"


@pytest.mark.parametrize(
    "test_input,expected",
    [
        ("3+5", 8),
        pytest.param("6*9", 54, marks=pytest.mark.xfail),
        pytest.param("6*9", 42, marks=pytest.mark.xfail),
    ],
)
def test_eval(test_input, expected):
    assert eval(test_input) == expected
