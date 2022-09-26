#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a
# quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros
# quadrados.
larg = float(input('Digite aqui a largura da sua parede!!!'))
alt = float(input('Digite aqui a altura da sua parede!!!'))
area = larg*alt
print('Sua parede tem {}mts de largura e, {}mts de altura, resultando em uma area de {} metros quadrados'.format(larg,alt, area))
tinta = area/2
print('Para pintar a sua parece voce precisara de {} litros de tinta.'.format(tinta))



