#Car rental

d = float(input('How many days rented? '))
q = float(input('How many km driven? '))
a = d * 60
km = q * 0.15
r = a + km
print('The total to be paid is R${:.2f}.'.format(r))
