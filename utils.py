from typing import Tuple
import sys
class Utils:
    def reversed(x: int) -> int:
        """
        Reverse the digits fo an integer. 

        Args:
            - x (int): The integer to be reversed.
        
        Returns:
            - int: The integer with the digits reversed.

        Raises:
            - AssertionError: if the input parameter is not an int.
        
        Examples:
        >>> reversed(123)
        321

        >>> reversed(-123)
        -321

        >>> reversed(120)
        21 
        """
        # Assert the input parameter is legal
        assert type(x) == int, "Internal Error: Input parameter x for reversed() is not an int"
        # Handle the negative int case
        sign = -1 if x < 0 else 1 
        x = abs(x)

        # Doing the actual reversing
        solution = 0
        while x:
            solution *= 10 
            solution += x%10
            x //= 10
        return int(solution * sign)

    def formatter(x: int) -> Tuple[str, str]:
        """
        Converts an integer to its binary and octal string format.

        Args:
            - x (int): The integer to be formatted.

        Returns:
            - Tuple[str, str]: First element is the binary representation 
                        (starts with '0b').
                        The second element is the octal representation 
                        (starts with '0o').

        Raises:
        - AssertionError: If the input parameter x is not an integer.

        Examples:
        >>> formatter(10)
        ('0b1010', '0o12')

        >>> formatter(-255)
        ('-0b11111111', '-0o377')

        """
        # Assert the input parameter is legal
        assert type(x) == int, "Internal Error: Input parameter x for formatter() is not an int"
        # Simply return the values
        return bin(x), oct(x)