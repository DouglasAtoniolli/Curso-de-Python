#Faça um al goritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
salario = float(input('Qual seu salario atual? R$'))
novosalario = salario + (salario * 15 / 100)
print('O seu salario atual é R${:.2f}, com reajuste de 15% sera de R${:.2f}, parabéns'.format(salario,novosalario))
