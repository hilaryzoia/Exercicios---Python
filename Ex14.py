#Breaking a number

from math import ceil,floor
n = float(input('Enter a number: '))
pi = floor(n)
print('The value entered was {} and its entire portion is {}.'.format(n,floor(n),ceil(n)))
