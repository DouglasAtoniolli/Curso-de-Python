#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
real = float(input('Digite aqui quantos reais voce tem para saber quantos dolares voce podera comprar!!!'))
dolar = real/5.39
print('Com o valor de R${} voce pode comprar ${:.2f} dolares.'.format(real,dolar))
