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

        if numbers.startswith('//'):
            delimiter_line, numbers = numbers.split('\n', 1)
            delimiter = delimiter_line[2:]

        # Replace newlines with delimiter
        numbers = numbers.replace('\n', delimiter)

        # Split numbers and convert to integers
        try:
            nums = [int(n.strip()) for n in numbers.split(delimiter) if n.strip()]
        except ValueError as e:
            print(f"Unexpected error: {str(e)}")
            sys.exit(1)

        # Check for negative numbers
        negatives = [n for n in nums if n < 0]
        if negatives:
            raise ValueError(f"negative numbers not allowed {','.join(map(str, negatives))}")

        return sum(nums)
