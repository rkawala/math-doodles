from doodles import pi
from .test_helpers import *

def test_three_iterations():
    assert_almost_equals(pi.do_iterate(300), 3.13, 0.01)