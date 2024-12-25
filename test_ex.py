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
