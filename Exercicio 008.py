#Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.
metros = float(input('Digite aqui o valor em metros a ser convertido !!!'))
centimetros = metros * 100
milimetros = metros * 1000

print('O valor em {} metros correspnde a {} centimetros e {} milimetros'.format(metros, centimetros, milimetros))
