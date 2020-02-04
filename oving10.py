''' Cirq LLC - 
    A High-tech Circle Company
'''

import math
from random import random, seed


class Circle(object):
    '''
    A class for circles, used for advanced calculations
    '''

    # flyweight design pattern supresses
    # the instance dictionary
    __slots__ = ['diameter']
    version = '0.1'         # Class variable

    def __init__(self, radius):
        self.radius = radius

    # lets getter and setter method be invoked automatically by attribute access
    @property
    def radius(self):
        'Radius of circle'
        return self.diameter / 2

    @radius.setter
    def radius(self, radius):
        self.diameter = radius * 2.0

    def area(self):
        'Perform quadrature on a shape of uniform radius'
        return math.pi * self.radius ** 2.0

    def perimeter(self):
        'Calculates the perimeter on a shape of uniform radius'
        return 2.0 * math.pi * self.radius

    @classmethod            # Alternate constructor
    def from_bbd(cls, bbd):
        'Construct a circle from a bounding box diagonal'
        radius = bbd / 2.0 / math.sqrt(2.0)
        return cls(radius)

    @staticmethod           # Can be called without initiating an instance
    def angle_to_grade(angle):
        'Convert angle in degrees to a percentage grade'
        return math.tan(math.radians(angle)) * 100


# Tutorial - first shipment
print('Cirq version', Circle.version)
c = Circle(10)
print('A circle of radius', c.radius)
print('has an area of', c.area())
print()

# First Customer: Academia
print('First customer: Academia')
seed(8675309)
print('Using Cirq(tm) version', Circle.version)
n = 10
circles = [Circle(random()) for i in range(n)]
print('The average area of', n, 'random cirlces')
avg = sum([c.area() for c in circles]) / n
print('is %-1f' % avg)
print()

# Second Customer: Rubber sheet company
print('Second Customer: Rubber sheet company')
cuts = [0.1, 0.7, 0.8]
circles = [Circle(r) for r in cuts]
for c in circles:
    print('A cirlet with a radius of', c.radius)
    print('hs a perimeter of', c.perimeter())
    print('and a cold area of', c.area())
    c.radius *= 1.1
    print('and a warm area of', c.area())
    print()

# Third Customer: National Tire Chain
print('Third Customer: National Tire Chain')

# Subclass example where perimeter method is overwritten


class Tire(Circle):
    'Tires are circles with a corrected perimeter'

    def perimeter(self):
        return Circle.perimeter(self) * 1.25


t = Tire(22)
print('A tire of radius', t.radius)
print('has an inner area of', t.area())
print('and a odometer corrected perimeter of', t.perimeter())
print()

# Fourth Customer: National Graphics Company
# Added new constructor signature allowing circles from bbd
print('Fourth Customer: National Graphics Company')
c = Circle.from_bbd(25.1)
print('A circle with a bbd of 25.1')
print('has a radius of', c.radius)
print('and an area of', c.area())
print()

# Fifth Customer: Truck Driver
# Made a static convert angle method
print('Fifth Customer, static converter method')
print('20 degrees is the same as', Circle.angle_to_grade(20), '%')
print()
