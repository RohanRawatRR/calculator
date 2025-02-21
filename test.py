from script import StringCalculator

def test_calculator():
    """
    Test the StringCalculator class
    """
    calc = StringCalculator()

    test_cases = [
        # Basic tests
        ("", 0),
        ("1", 1),
        ("1,5", 6),
        ("-1,-5,-3", -9),
        # Newline delimiter
        ("1\n2,2", 5),
        # Custom delimiter
        ("//;\n1;2", 3),
        ("//;\n1;2;-1", 2),
        # Multiple delimiters
        ("//[*][%]\n1*2%3", 6),
    ]

    for input_str, expected in test_cases:
        try:
            result = calc.add(input_str)
            if result != expected:
                print(f"Error: For input '{input_str}', expected {expected} but got {result}")
            else:
                print(f"Passed: {input_str} = {result}")
        except Exception as e:
            print(f"Error for input '{input_str}': {str(e)}")

test_calculator()
