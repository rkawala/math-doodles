def assert_almost_equals(expected, actual, delta):
    assert abs(expected - actual) < delta, f"Expected {expected} but actual {actual}"