import pytest
from ex import ex_funcs


@pytest.mark.parametrize(
    "x, y, expected",
    [
        (3, 2, 1),
    ],
)
def test_ex_funcs(x: int, y: str, expected: int) -> None:
    assert ex_funcs(x, y) == expected
def test_ex_funcs(x: int, y: str, expected: int) -> None:
    assert ex_funcs(x, y) == expected
def test_ex_funcs(x: int, y: str, expected: int) -> None:
    assert ex_funcs(x, y) == expected
def test_ex_funcs(x: int, y: str, expected: int) -> None:
    assert ex_funcs(x, y) == expected



# このテストは成功します。yの型がintであるためです。
# このテストは失敗します。yの型がintではなくstrになっているためです。
# このように、型が違うとテストが失敗することがあります。
if __name__ == "__main__":
    pytest.main()

    def ex_funcs2(x, y):
        return x - y
