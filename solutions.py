import collections

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
    for punctuation in ',.?!':
        text = text.replace(punctuation, ' ')
        
    for word in text.split():
        count[word] = count.get(word, 0) + 1
    return count

####

VOWELS = 'eiyaou'
def to_pirate(text):
    pirate = ""
    for char in text:
        # do not duplicae vowels and spaces
        if char not in VOWELS + " ":
            pirate += char + 'o' + char.lower()
        else:
            pirate += char
    return pirate

###

from pytest import approx
from math import pi

class Circle:
    ### BEGIN SOLUTION
    def __init__(self, x=0.0, y=0.0, r=1.0):
        self.x = x
        self.y = y
        self.r = r
        
    def area(self):
        return pi*self.r**2
    
    def circumference(self):
        return 2*pi*self.r
    
    def __eq__(self, other):
        return self.x == approx(other.x) and self.y == approx(other.y) and self.r == approx(other.r)
    ### END SOLUTION

###
delta = 1e-8

### BEGIN SOLUTION
def derivative(f):
    
    def wrap(x):
        return (f(x + delta) - f(x-delta))/(2*delta)
  
    return wrap
### END SOLUTION    

###

def find_long_lines(filename, max_length):
    for l in open(filename):
        line = l.strip()
        if len(line) >  max_length:
            yield line