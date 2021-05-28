from doodles.pi import do_iterate
from .test_helpers import *

def test_three_iterations():
    assert_almost_equals(3.13, do_iterate(300), 0.01)