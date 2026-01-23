#Sine, Cosine and Tangent

import math
a = float(input('Enter the angle you want: '))
s = math.sin(math.radians(a))
c = math.cos(math.radians(a))
t = math.tan(math.radians(a))
print('The angle of {} has the SINE of {:.2f}.'.format(a,s))
print('the angle of {} has the COSINE of {:.2f}.'.format(a,c))
print('The angle of {} has the TANGENT of {:.2f}.'.format(a,t))
