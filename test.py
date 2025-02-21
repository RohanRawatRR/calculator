from script import StringCalculator


def test_calculator():
    """
    Test the StringCalculator class
    """
    calc = StringCalculator()

    # Basic tests
    assert calc.add("") == 0
    assert calc.add("1") == 1
    assert calc.add("1,5") == 6
    assert calc.add("-1,-5,-3") == -9
    assert calc.add("1\n2,2") == 5

    print("All tests passed!")

test_calculator()
