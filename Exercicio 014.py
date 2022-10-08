#Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.
celsius = float(input('Qual a temperatura em graus celsius ?'))
fahrenheit = ((9 * celsius) / 5) +32
print('A sua temperatura atual em celsius é {} e convertida para fahrenheit é {}.'.format(celsius, fahrenheit))
