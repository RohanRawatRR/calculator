import sys

class StringCalculator:
    """
    A class for calculating the sum of a string of numbers
    """
    def add(self, numbers: str) -> int:
        """
        Add the numbers in the string
        """
        if not numbers:
            return 0

        # Handle custom delimiter
        delimiter = ','
        # Split numbers and convert to integers
        try:
            nums = [int(n.strip()) for n in numbers.split(delimiter) if n.strip()]
        except ValueError as e:
            print(f"Unexpected error: {str(e)}")
            sys.exit(1)

        return sum(nums)
