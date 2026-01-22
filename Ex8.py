# Currency conversion

n = float(input('How much money do you have in your wallet?'))
d = n / 5.29
print('With R${:.2f} you can buy US${:.2f}.'.format(n,d))
