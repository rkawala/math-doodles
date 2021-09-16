from doodles.pi import do_iterate
from truth.truth import AssertThat

def test_three_iterations():
    AssertThat(do_iterate(300)).IsWithin(0.01).Of(3.13)