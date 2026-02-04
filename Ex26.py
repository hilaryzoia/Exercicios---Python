#Guessing game

from random import randint
from time import sleep
computer = randint(0,5)
print('-==--==--==--==--==--==--==--==--==--==--==--==--==--==-')
print('I'm going to think of a number between 0 and 5. Try to guess...')
print('-==--==--==--==--==--==--==--==--==--==--==--==--==--==-')
n = int(input('What number did I think of: '))
print('PROCESSING...')
sleep(2)
if n == computer:
    print('CONGRATULATIONS! You managed to beat me!')
else:
    print('I WON! I thought of the number {} and not the {}'.format(computer,n))
