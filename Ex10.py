#Calculation of discounts

p = float(input('What is the price of the product? R$'))
d = p * 5 / 100
r = p - d
print('The product that cost R${}, in the promotion with a 5% discount will cost R${:.2f}.'.format(p,r))
