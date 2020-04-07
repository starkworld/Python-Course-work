"""Created on Sun Feb 17 18:18:57 2020

        @author: nkalyan🤠
    Implementing fraction calculator by using classes and functions, which takes fractions as inputs,
     and performs arithmetic operations"""


def GCD(a, b) -> float:
    """Fucntion that perform the GCD operation and return the GCD of values"""
    a: float = abs(a)
    b: float = abs(b)
    while b > 0:
        r = a % b
        a = b
        b = r
    return a


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

    def __add__(self, other: "Fraction") -> "Fraction" :
        """ Add two fractions using simplest approach.
            Calculate new numerator and denominator and return new Fraction
        """
        new_fraction: Fraction = Fraction(self.numerator * other.denominator + other.numerator * self.denominator, self.denominator * other.denominator )
        return new_fraction

    def __sub__(self , other: "Fraction") -> "Fraction" :
        """ subtract two fractions using simplest approach
            Calculate new numerator and denominator and return new Fraction
        """
        new_fraction: Fraction = Fraction(self.numerator * other.denominator - other.numerator * self.denominator, self.denominator * other.denominator)
        return new_fraction

    def __mul__(self , other: "Fraction") -> "Fraction" :
        """ Multiply two fractions using simplest approach
            Calculate new numerator and denominator and return new Fraction
        """
        new_fraction: Fraction = Fraction(self.numerator * other.numerator, self.denominator * other.denominator)
        return new_fraction

    def __truediv__(self, other: "Fraction") -> "Fraction":
        """ Add two fractions using simplest approach.
            Calculate new numerator and denominator and return new Fraction
        """
        if other.numerator == 0:
            raise ZeroDivisionError("You cannot divide by zero")
        new_fraction: Fraction = Fraction(self.numerator * other.denominator, self.denominator * other.numerator)
        return new_fraction

    def __eq__(self, other: "Fraction") -> bool:
        """ return True/False if the two fractions are equivalent """

        if self.numerator * other.denominator == self.denominator * other.numerator:
            return True
        else:
            return False
    
    def __ne__(self, other: "Fraction") -> bool:
        """ return True if the two fractions are not equivalent else false """
        if self.numerator * other.denominator != self.denominator * other.numerator:
            return True
        else:
            return False

    def __le__(self, other:"Fraction") -> bool:
        """Campare the fractions and returns true if f1 <= f2 else false"""
        if self.numerator * other.denominator <= self.denominator * other.numerator:
            return True
        else:
            return False

    def __lt__(self, other:"Fraction") -> bool:
        """Compares the fractions and returns true if f1 < f2 or retuns false"""
        if self.numerator * other.denominator < self.denominator * other.numerator:
            return True
        else:
            return False

    def __ge__(self, other: "Fraction") -> bool:
        """Compares the fractions and returns true if f1 >= f2 or retuns false"""
        if self.numerator * other.denominator >= self.denominator * other.numerator:
            return True
        else:
            return False

    def __gt__(self, other:"Fraction") -> bool:
        """Compares the fractions and returns true if f1 > f2 or retuns false"""
        if self.numerator * other.denominator > self.denominator * other.numerator:
            return True
        else:
            return False

    def __str__(self) -> str :
        """ return a String to display fractions """
        return f"{self.numerator} / {self.denominator}"

    def simplify(self) -> "Fraction":
        """Function which simplify and return the fraction"""
        a = GCD(self.numerator, self.denominator)
        return Fraction(int(self.numerator / a), int(self.denominator / a))


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
        denominator: str = input("Enter a valid denominator:")
        try:
            num = float(numerator)
            denom = float(denominator)
            if denom == 0:
                raise ZeroDivisionError("Zero cannot be divided")
            new_fraction = Fraction(num, denom)
            return new_fraction
        except ValueError:
            print(f"Error: {numerator} 'or' {denominator} is not a number🙄, Please enter your inputs again☺")
        except ZeroDivisionError:
            print(f"{denominator} cannot be divided🤔😯")


def compute(fraction1: Fraction, operator: str, fraction2: Fraction) -> (None, bool):
    """ Given two fractions and an operator, return the result
        of applying the operator to the two fractions
    """
    if operator == '+':
        result: Fraction = fraction1 + fraction2
        print(f"Your Result is 🤑: {fraction1} {operator} {fraction2} = {result}\n")
    elif operator == '-':
        result: Fraction = fraction1 - fraction2
        print(f"Your Result is 😁: {fraction1} {operator} {fraction2} = {result}\n")
    elif operator == '*':
        result: Fraction = fraction1 * fraction2
        print(f"Your Result is 🤩: {fraction1} {operator} {fraction2} = {result}\n")
    elif operator == '/':
        result: Fraction = fraction1 / fraction2
        print(f"Your Result is ☺: {fraction1} {operator} {fraction2} = {result}\n")
    elif operator == '=':
        if fraction1 == fraction2:
            print("Fractions are equal😁😁!!\n")
            return True
        else:
            print("Fractions are not equal😐😐\n")
            return False
    elif operator == '!=':
        if fraction1 != fraction2:
            print("Fractions are not equal😁😁!!\n")
            return True
        else:
            print("Fractions are equal😐😐\n")
            return False
    elif operator == '<=':
        if fraction1 <= fraction2:
            print(f"{fraction1} is less than or equal to {fraction2}")
        else:
            print(f"{fraction1} is not less than or equal to {fraction2}")
    elif operator == '<':
        if fraction1 < fraction2:
            print(f"{fraction1} is less than {fraction2}")
        else:
            print(f"{fraction1} is not less than {fraction2}")
    elif operator == '>=':
        if fraction1 >= fraction2:


            print(f"{fraction1} is greater than or equal to {fraction2}")
        else:
            print(f"{fraction1} is not greater than or equal to {fraction2}")
    elif operator == '>':
        if fraction1 > fraction2:
            print(f"{fraction1} is greater than {fraction2}")
            return True
        else:
            print(f"{fraction1} is not greater than {fraction2}")
            return False
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
    f34: Fraction = Fraction(-3, 4)
    f44: Fraction = Fraction(4, 4)
    f68: Fraction = Fraction(6, -8)
    f128: Fraction = Fraction(12, 8)
    f32: Fraction = Fraction(3, 2)
    f912: Fraction = Fraction(9, 12)

    print(f"{f12} + {f34} = {f12 + f34} [10/8]")
    print ( f"{f12} - {f34} = {f12 - f34} [-2/8]")
    print ( f"{f12} * {f34} = {f12 * f34} [3/8]")
    print ( f"{f12} / {f34} = {f12 / f34} [4/6]")
    print(f"{f12} + {f34} + {f44} = {f12 + f34 + f44} [72/32]")
    print(f"{f12} + {f32} + {f34} = {f12 + f32 + f34} [44/16]")
    print(f"{f12} - {f34} - {f44} = {f12 - f34 - f44} [-40/32]")
    print(f"{f12} * {f34} * {f44} = {f12 * f34 * f44} [12/32]")
    print(f"{f12} / {f34} / {f44} = {f12 / f34 / f44} [16/24]")
    print(f"{f68} + {f128} + {f912} = {f68 + f128 + f912} [2304/768]")
    print(f"{f68} - {f128} - {f912} = {f68 - f128 - f912} [-1152/768]")
    print(f"{f68} * {f128} * {f912} = {f68 * f128 * f912} [648/768]")
    print(f"{f68} / {f128} / {f912} = {f68 / f128 / f912} [576/864]\n")

    print(f"({f12}) >  ({f34}) = {f12 > f34}")
    print(f"({f12}) >= ({f34}) >= ({f44}) = {f12 >= f34 >= f44} ")
    print(f"({f12}) < ({f32}) < ({f34}) = {f12 < f32 < f34}")
    print(f"({f12}) <= ({f34}) <= ({f44}) = {f12 <= f34 <= f44}")
    print(f"({f12}) = ({f34}) = ({f44}) = {f12 == f34 == f44}")
    print(f"({f12}) < ({f34}) < ({f44}) = {f12 < f34 < f44}")
    print(f"({f68}) <= ({f128}) <= ({f912}) = {f68 <= f128 <= f912}")
    print(f"({f68}) > ({f128}) > ({f912}) = {f68 > f128 > f912}")
    print(f"({f68}) >= ({f128}) >= ({f912}) = {f68 >= f128 >= f912}")
    print(f"({f68}) = ({f128}) = ({f912}) = {f68 == f128 == f912}")


def main() -> None:
    """ Fraction calculations """
    print('Welcome to the fraction calculator!🎆🎇')
    fraction1: Fraction = get_fraction()
    operator: str = input("Operation (+, -, *, /,=, !=, <=, <, >=, >): ")
    fraction2: Fraction = get_fraction()
    compute(fraction1, operator, fraction2)


if __name__ == '__main__':
    """""Calls the functions to perform operations"""
    get_number(" ")
    main()
    test_suite()