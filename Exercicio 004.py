# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as
# informações possíveis sobre ele.
a = input('Digite algo de sua escolha!!!')
print('O tipo primitivo desse valor é', type(a))
print('So tem espaços', a.isspace())
print('E numerico', a.isnumeric())
print('E alfabetico', a.isalpha())
print('E alfanumerico', a.isalnum())
print('Esta em maiusculo', a.isupper())
print('Esta em minusculos', a.islower())
print('Esta capitalizada', a.istitle())





