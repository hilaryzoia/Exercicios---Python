#Electronic radar

speed = int(input('What is the current speed of the car? '))
if speed <= 80:
    print('HAVE A NICE DAY. Drive safely!')
else:
    fine = (speed - 80) * 7
    print('FINED! You exceeded the allowed limit of 80km/h')
    print('You must pay a fine of R${}'.format(fine))
