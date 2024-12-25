import pytest
from ex import ex_funcs


@pytest.mark.parametrize(
    "x, y, expected",
    [
        (3, 2, 1),
        (2, 3, 5),
        (10, 20, 30),
        # 　かおかおかおかおかおこ
    ],
)
def test_ex_funcs(x: int, y: str, expected: int) -> None:
    assert ex_funcs(x, y) == expected


# このテストは失敗します。yの型がintではなくstrになっているためです。
# このように、型が違うとテストが失敗することがあります。
if __name__ == "__main__":
    pytest.main()

    def ex_funcs2(x, y):
        return x - y
