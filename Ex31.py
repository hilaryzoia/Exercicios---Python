#Highest and lowest value 

p = int(input('First value: '))
s = int(input('Second value: '))
t = int(input('Third value: '))
smallest = p
if s<p and s<t:
    smallest = s
if t<p and t<s:
    smaller = t
print('The smallest value entered was {}'.format(smallest))
biggest = p
if s>p and s>t:
    biggest = s
if t>p and t>s:
    largest = t
print('The largest value entered is {}'.format(largest))
