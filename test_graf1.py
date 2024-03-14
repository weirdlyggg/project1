import pytest
from main import graf1

@pytest.mark.parametrize("x, xk, b, k, xar, yar",
                         [(-1.0, 1.0, -0.5, 0.5, [-1.0, -0.5, 0.0, 0.5, 1.0], [-1.0, -0.75, -0.5, -0.25, 0.0]),
                          (0,0,0,0,[0],[0]),
                          (0,0,1,1,[0],[1])])

def test(x, xk, b, k, xar, yar):
    assert graf1(x, xk, b, k) == (xar, yar)