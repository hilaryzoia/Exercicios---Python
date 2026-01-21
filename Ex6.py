# Measurement converter

m = float(input('The distance in meters:'))
q = m / 1000
h = m / 100
d = m / 10
e = m * 10
c = m * 100
l = m * 1000
print('The measure of {:.1f} corresponds to:'.format(m))
print('{}km'.format(q))
print('{}hm'.format(h))
print('{}dam'.format(d))
print('{}dm'.format(e))
print('{}cm'.format(c))
print('{}mm'.format(l))

# When it is a whole number, use int, when it is a decimal number, use float
