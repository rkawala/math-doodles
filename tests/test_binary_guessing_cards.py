from io import StringIO
from unittest import mock

from doodles.binary_guessing_cards import *
from truth.truth import AssertThat
from nose.tools import assert_raises

def test_powers_of_two_generator():
    AssertThat(list(power_of_two_generator(0))).ContainsExactly(1).InOrder()
    AssertThat(list(power_of_two_generator(1))).ContainsExactly(1, 2).InOrder()
    AssertThat(list(power_of_two_generator(4))).ContainsExactly(1, 2, 4, 8, 16).InOrder()

def test_numbers_with_bit_set_generator():
    AssertThat(list(numbers_with_bit_set(4, 9))).ContainsExactly(4, 5, 6, 7).InOrder()
    AssertThat(list(numbers_with_bit_set(8, 8))).ContainsExactly(8).InOrder()
    AssertThat(list(numbers_with_bit_set(8, 9))).ContainsExactly(8, 9).InOrder()

def test_generate_cards():
    AssertThat(list(generate_cards(7))).ContainsExactly(
        [1, [1, 3, 5, 7]],
        [2, [2, 3, 6, 7]],
        [4, [4, 5, 6, 7]]
    ).InOrder()

def test_exit_if_no_argument():
    with assert_raises(SystemExit) as exc:
        main(["wxyz"])
    AssertThat(exc.exception.code).IsEqualTo("Usage: wxyz one-to-this-value")

@mock.patch('doodles.binary_guessing_cards.generate_cards')
def test_main_passes_args(mock_generate_cards):
    with mock.patch('sys.stdout', new=StringIO()) as captured_output:
        main([ "wxyz", "11" ])
    mock_generate_cards.assert_called_with(11)

def test_main_prints_cards():
    with mock.patch('sys.stdout', new=StringIO()) as captured_output:
        main([ "wxyz", "11" ])
    AssertThat(captured_output.getvalue()).IsEqualTo("""\
[1, [1, 3, 5, 7, 9, 11]]
[2, [2, 3, 6, 7, 10, 11]]
[4, [4, 5, 6, 7]]
[8, [8, 9, 10, 11]]
""")
