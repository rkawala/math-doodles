from doodles.binary_guessing_cards import *
from truth.truth import AssertThat

def test_powers_of_two_generator():
    AssertThat(list(power_of_two_generator(4))).ContainsExactly(1, 2, 4, 8, 16).InOrder()

# Test that main works