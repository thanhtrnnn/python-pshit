"""
Fraction class: represents a fraction n/d
Thanh Tran Xuan
"""

import math

class Fraction(object):
    """Instance is a fraction n/d"""
    # _numerator: an int
    # _denominator: an int > 0

    def getNumerator(self):
        """ Returns: Numerator of Fraction """
        return self._numerator
    
    def __init__(self, n = 0, d = 1):
        """Initializer: makes a Fraction"""
        if d == 0:
            raise ValueError("Denominator cannot be zero")
        self._numerator = n
        self._denominator = d
        self.normalize()
    
    def __add__(self, q):
        """Returns: Sum of self, q"""
        if type(q) == int:
            return Fraction(self._numerator + q * self._denominator, self._denominator)
        elif type(q) == Fraction:
            # q is a Fraction
            n = self._numerator * q._denominator + q._numerator * self._denominator
            d = self._denominator * q._denominator
            return Fraction(n, d)
        else:
            raise TypeError("Invalid operand type for addition")
        
    def __mul__(self, q):
        """Returns: Product of self, q"""
        if type(q) == int:
            return Fraction(self._numerator * q, self._denominator)
        elif type(q) == Fraction:
            n = self._numerator * q._numerator
            d = self._denominator * q._denominator
            return Fraction(n, d)
        else:
            raise TypeError("Invalid operand type for multiplication")

    def __eq__(self, q):
        """Returns: True if self == q, False otherwise"""
        if type(q) == int:
            return self._numerator == q * self._denominator
        elif type(q) == Fraction:
            return self._numerator == q._numerator and self._denominator == q._denominator
        else:
            raise TypeError("Invalid operand type for equality check")

    def __str__(self):
        """Returns: String representation of Fraction"""
        if self._denominator == 1:
            return str(self._numerator)
        else:
            return f"{self._numerator}/{self._denominator}"

    def __repr__(self):
        """Returns: String representation of Fraction"""
        return f"Fraction({self._numerator}, {self._denominator})"
    
    def normalize(self):
        """Puts Fraction in reduced form"""
        if self._denominator < 0:
            self._numerator = -self._numerator
            self._denominator = -self._denominator
        if self._numerator == 0:
            self._denominator = 1
        else:
            g = math.gcd(abs(self._numerator), abs(self._denominator))
            self._numerator //= g
            self._denominator //= g
