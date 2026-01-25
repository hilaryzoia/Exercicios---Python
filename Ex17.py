#Drawing an item from the list

import random
n1 = str(input('First student: '))
n2 = str(input('Second student: '))
n3 = str(input('Third student: '))
n4 = str(input('Fourth student: '))
list = [n1,n2,n3,n4]
e = random.choice(list)
print('The student chosen was {}'.format(e))
