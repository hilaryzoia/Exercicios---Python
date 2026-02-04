#First and last name of a person

name = str(input('Enter your full name: ')).strip()
n = name.split()
print('Nice to meet you!')
print('Your first name is {}'.format(n[0]))
print('Your last name is {}'.format(n[len(n)-1]))
