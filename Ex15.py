#Cathets and Hypotenuses

from math import sqrt
co = float(input('Length of opposite side: '))
ca = float(input('Length of adjacent side: '))
h = sqrt(co**2 + ca**2)
print('The hypotenuse will measure {:.2f}.'.format(h))
