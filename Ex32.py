# Multiple boosts

salary = float(input('What is the employee's salary? R$'))
a1 = ((salary * 10)/100) + salary
a2 = ((salary * 15)/100) + salary 
if salary <= 1250:
    print('Whoever earned R${} starts earning R${}'.format(salario,a2))
else:
    print('Whoever earned R${} starts earning R${}'.format(salario,a1))
