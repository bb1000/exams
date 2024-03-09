from math import pi
from pytest import approx


def word_count(text):
    """
    Calculates words in text, return type: dict

    >>> word_count('bye bye')
    {'bye': 2}
    >>> word_count('She loves me yeah yeah yeah')
    {'she': 1, 'loves': 1, 'me': 1, 'yeah': 3}
    """
    count = {}
    text = text.lower()
    for punctuation in ",.?!":
        text = text.replace(punctuation, " ")

    for word in text.split():
        count[word] = count.get(word, 0) + 1
    return count


####

VOWELS = "eiyaou"


def to_pirate(text):
    pirate = ""
    for char in text:
        # do not duplicae vowels and spaces
        if char not in VOWELS + " ":
            pirate += char + "o" + char.lower()
        else:
            pirate += char
    return pirate


###


class Circle:
    def __init__(self, x=0.0, y=0.0, r=1.0):
        self.x = x
        self.y = y
        self.r = r

    def area(self):
        return pi * self.r**2

    def circumference(self):
        return 2 * pi * self.r

    def __eq__(self, other):
        return (
            self.x == approx(other.x)
            and self.y == approx(other.y)
            and self.r == approx(other.r)
        )

###

delta = 1e-8


def derivative(f):
    def wrap(x):
        return (f(x + delta) - f(x - delta)) / (2 * delta)
    return wrap


def find_long_lines(filename, max_length):
    for line in open(filename):
        line = line.strip()
        if len(line) > max_length:
            yield line


###

def to_pence(pounds, shillings, pence):
    """
    Convert old British currency to smallest unit
    
    >>> to_pence(0, 1, 0)
    12
    >>> to_pence(1, 0, 0)
    240

    total_shillings = 20*pounds + shillings
    total_pence = 12*total_shillings + pence
    return total_pence
    """
    total_shillings = 20*pounds + shillings
    total_pence = 12*total_shillings + pence
    return total_pence

def reduce(pounds, shillings, pence):
    """
    Reduce to fewest coins first by considering total pennies and change back to pounds, shillings and pence
    """
    total_pence = to_pence(pounds, shillings, pence)
    # The number of shillings you get out of these pennies
    total_shillings = total_pence // 12
    # The remaining pennies after chaning into shillings
    remaining_pence = total_pence % 12

    # The number of pounds you get out of these shillings
    total_pounds = total_shillings // 20
    # The remaining shillings you get after changing int pound
    remaining_shillings = total_shillings % 20

    return (total_pounds, remaining_shillings, remaining_pence)

def to_pounds(pounds, shillings, pence):
    return to_pence(pounds, shillings, pence) // 240

def to_shillings(pounds, shillings, pence):
    return to_pence(pounds, shillings, pence) // 12

class GBP:
    def __init__(self, pounds, shillings, pence):
        # Save notes/coins as a tuple "data"
        self.data = (pounds, shillings, pence)

        # 8. raise exception for negative amounts
        if to_pence(*self.data) < 0:
            raise NegativePounds

    def __iter__(self):
        return iter(self.data)

    def __add__(self, other):
        # 6. Define addition (simple version)

        pounds = self.data[0] + other.data[0]
        shillings = self.data[1] + other.data[1]
        pence = self.data[2] + other.data[2]
        #return GBP(pounds, shillings, pence)

        # 7. User reduce to minimize coins

        data = reduce(pounds, shillings, pence)
        return GBP(*data)

    def __eq__(self, other):
        return (to_pence(*self.data) == to_pence(*other.data))

    def __lt__(self, other):
        # 11. implements lower that operator <
        return to_pence(*self.data) < to_pence(*other.data)

    def __le__(self, other):
        # 12. implements the lower than equal operator <=
        return to_pence(*self.data) <= to_pence(*other.data)

class NegativePounds(Exception):
    pass
