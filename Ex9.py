# Wall painting

l = float(input('Wall width: '))
a = float(input('Wall height: '))
e = a * l
t = e / 2
print('Your wall has the dimension of {}x{} and its area is {}m².'.format(l,a,e))
print('To paint this wall you will need {:.2f}l of paint.'.format(t))
