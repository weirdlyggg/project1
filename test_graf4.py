import pytest
from main import graf4

@pytest.mark.parametrize("x, xk, xar, yar",
                         [(-1.0, 1.0, [-1.0, -0.5, 0.0, 0.5, 1.0], [0.36787944117144233, 0.6065306597126334, 1.0, 1.6487212707001282, 2.718281828459045]),
                          (0,0,[0],[1.0])])

def test(x, xk, xar, yar):
    assert graf4(x, xk) == (xar, yar)