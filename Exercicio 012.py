#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
preco = float(input('Qual valor do produto R$ ?'))
novop = preco - (preco * 5 / 100)
print('O valor do seu é R${}, com 5% de desconto na promoção vai ser R${}'.format(preco, novop))


