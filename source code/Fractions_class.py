"""Created on Sun Feb 4 17:57:57 2020

        @author: nkalyan🤠
    Implementing fraction calculator by using classes and functions, which takes fractions as inputs,
     and performs arithmetic operations"""


class Fraction:
    """"Support addition, subtraction, multiplication, and division of fractions
        with a simple algorithm"""

    def __init__(self, numerator, denominator):
        """ store num and denom
                    Raise ZeroDivisionError on 0 denominator
                """
        self.numerator: float = numerator
        self.denominator: float = denominator
        if denominator == 0:
            raise ZeroDivisionError("Check your denominator value")

    def plus(self, other: "Fraction") -> "Fraction" :
        """ Add two fractions using simplest approach.
            Calculate new numerator and denominator and return new Fraction
        """
        new_fraction: Fraction = Fraction(self.numerator * other.denominator + other.numerator * self.denominator, self.denominator * other.denominator )
        return new_fraction

    def minus(self , other: "Fraction") -> "Fraction" :
        """ subtract two fractions using simplest approach
            Calculate new numerator and denominator and return new Fraction
        """
        new_fraction: Fraction = Fraction(self.numerator * other.denominator - other.numerator * self.denominator, self.denominator * other.denominator)
        return new_fraction

    def times(self , other: "Fraction") -> "Fraction" :
        """ Multiply two fractions using simplest approach
            Calculate new numerator and denominator and return new Fraction
        """
        new_fraction: Fraction = Fraction(self.numerator * other.numerator, self.denominator * other.denominator)
        return new_fraction

    def divide(self , other: "Fraction") -> "Fraction" :
        """ Add two fractions using simplest approach.
            Calculate new numerator and denominator and return new Fraction
        """
        new_fraction: Fraction = Fraction(self.numerator * other.denominator, self.denominator * other.numerator)
        return new_fraction

    def equal(self, other: "Fraction") -> bool :
        """ return True/False if the two fractions are equivalent """

        if self.numerator * other.denominator == self.denominator * other.numerator:
            return True

    def __str__(self) -> str :
        """ return a String to display fractions """
        return f"{self.numerator} / {self.denominator}"


def get_number(prompt: str) -> float :
    """ read and return a number from the user.
        Loop until the user provides a valid number.
    """
    while True:
        inp: str = input("To verify your input Enter a whole number first...:")
        print("Thank you for your input🙏")
        try:
            return float(inp)
        except ValueError:
            print(f"Error: '{inp}' is not a number. Please try again...")


def get_fraction() -> Fraction :
    """ Ask the user for a numerator and denominator and return a valid Fraction """
    while True:
        numerator: str = input("Enter a valid numerator:")
        denomninator: str = input("Enter a valid denominator:")
        try:
            num = float(numerator)
            denom = float(denomninator)
            if denom == 0:
                raise ZeroDivisionError("Zero cannot be divided")
            new_fraction = Fraction(num, denom)
            return new_fraction
        except ValueError:
            print(f"Error: {numerator} 'or' {denomninator} is not a number🙄, Please enter your inputs again☺")
        except ZeroDivisionError:
            print(f"{denomninator} cannot be divided🤔😯")


def compute(fraction1: Fraction, operator: str, fraction2: Fraction) -> None:
    """ Given two fractions and an operator, return the result
        of applying the operator to the two fractions
    """
    if operator == '+':
        result: Fraction = fraction1.plus(fraction2)
        print(f"Your Result is 🤑: {fraction1} {operator} {fraction2} = {result}\n")
    elif operator == '-':
        result: Fraction = fraction1.minus(fraction2)
        print(f"Your Result is 😁: {fraction1} {operator} {fraction2} = {result}\n")
    elif operator == '*':
        result: Fraction = fraction1.times(fraction2)
        print(f"Your Result is 🤩: {fraction1} {operator} {fraction2} = {result}\n")
    elif operator == '/':
        result: Fraction = fraction1.divide(fraction2)
        print(f"Your Result is ☺: {fraction1} {operator} {fraction2} = {result}\n")
    elif operator == '=':
        if fraction1.equal ( fraction2 ) :
            print("Fractions are equal😁😁!!\n")
        else :
            print("Fractions are not equal😐😐\n")
    else:
        print(f"Error 🥵😬: '{operator}' is an unrecognized operator\n")
        okay = False


def test_suite() -> None :
    """
        Series of fraction operations on different inputs of fraction to get an idea about the
            what these statements doing
    """
    print("Here is some of fractions test suites:")
    f12: Fraction = Fraction(1, 2)
    f34: Fraction = Fraction(3, 4)
    f44: Fraction = Fraction(4, 4)
    f68: Fraction = Fraction(6, 8)
    f128: Fraction = Fraction(12, 8)
    f32: Fraction = Fraction(3, 2)
    f912: Fraction = Fraction(9, 12)

    print(f"{f12} + {f34} = {f12.plus ( f12 )} [10/8]")
    print(f"{f12} + {f34} + {f44} = {f12.plus ( f34 ).plus ( f44 )} [72/32]")
    print(f"{f12} + {f32} + {f34} = {f12.plus( f32 ).plus( f34 )} [44/16]")
    print(f"{f12} - {f34} - {f44} = {f12.minus ( f34 ).minus ( f44 )} [-40/32]")
    print(f"{f12} * {f34} * {f44} = {f12.times ( f34 ).times ( f44 )} [12/32]")
    print(f"{f12} / {f34} / {f44} = {f12.divide ( f34 ).divide ( f44 )} [16/24]")
    print(f"{f68} + {f128} + {f912} = {f68.plus( f128 ).plus( f912 )} [2304/768]")
    print(f"{f68} - {f128} - {f912} = {f68.minus( f128 ).minus( f912 )} [-1152/768]")
    print(f"{f68} * {f128} * {f912} = {f68.times( f128 ).times( f912 )} [648/768]")
    print(f"{f68} / {f128} / {f912} = {f68.divide( f128 ).divide( f912 )} [576/864]")


def main() -> None:
    """ Fraction calculations """
    print('Welcome to the fraction calculator!🎆🎇')
    fraction1: Fraction = get_fraction()
    operator: str = input("Operation (+, -, *, /,=): ")
    fraction2: Fraction = get_fraction()
    compute ( fraction1 , operator , fraction2 )


if __name__ == '__main__':
    """""Calls the functions to perform operations"""
    get_number(" ")
    main()
    test_suite()