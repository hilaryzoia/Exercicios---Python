#Temperature Converter

t = float(input('Enter the temperature in °C: '))
f = (t * 1.8) + 32
print('The temperature of {}ºC corresponds to {:.1f}ºF.'.format(t,f))
