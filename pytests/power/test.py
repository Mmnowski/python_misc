from power_fun import power


def test_numbers():
    assert power(0, 0) == "Nope"
    assert power(0, 1) == 0
    assert power(1, 0) == 1
    assert power(10, 10) == 10000000000
