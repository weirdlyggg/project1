import pytest
from main import graf2

@pytest.mark.parametrize("x, xk, a, b, c, xar, yar",
                         [(-1.0, 1.0, 0.5, 0.5, 0.5, [-1.0, -0.5, 0.0, 0.5, 1.0], [0.5, 0.375, 0.5, 0.875, 1.5]),
                          (0,0,0,0,0,[0],[0]),
                          (0,0,1,1,1,[0],[1])])

def test(x, xk, a, b, c, xar, yar):
    assert graf2(x, xk, a, b, c) == (xar, yar)