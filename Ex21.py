#Separating digits from a number

num = int(input('Enter a number: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Analyzing the number {}:'.format(num))
print('Unit: {}'.format(u))
print('Ten: {}'.format(d))
print('Hundred: {}'.format(c))
print('Thousands: {}'.format(m))
