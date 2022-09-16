# Elaborar um algoritmo que lê 3 valores a,b,c e os escreve. A seguir, encontre o maior dos 3 valores e o escreva com a mensagem: "É o maior ".

print( 'Escolha 3 números e descubra qual é o maior! \n')

a = input('Digite o primeiro número:\n')
b = input('Digite o segundo número: \n')
c = input('Digite o terceiro número: \n')

list = [a, b, c]

print ("O maior elemento é o:" , max(list))