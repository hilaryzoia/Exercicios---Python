#Salary Adjustment 

s = float(input('What is the employee's salary? R$'))
a = s * 15 / 100
ns = s + a
print('The employee who earned R${}, with a 15% increase, now receives R${:.2f}.'.format(s,ns))
