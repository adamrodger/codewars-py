from codewars.kyu4.observed_pin import get_pins
from nose.tools import assert_count_equal

def test_expectations():
    yield check_expectation, "8", ["5","7","8","9","0"]
    yield check_expectation, "11", ["11", "22", "44", "12", "21", "14", "41", "24", "42"]
    yield check_expectation, "369", ["339","366","399","658","636","258","268","669","668","266","369","398","256","296","259","368","638","396","238","356","659","639","666","359","336","299","338","696","269","358","656","698","699","298","236","239"]

def check_expectation(input, expected):
    result = get_pins(input)
    assert_count_equal(result, expected)