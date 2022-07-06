l2 = [1,2,3,4,5,6,7,8,9]
soma = 0
for valor in l2:
    soma = soma + valor

print(soma)

#checkar qual o tipo de variavel numa lista usando o ciclo FOR
l3 = ['string', True, 10, 20.5]

for elem in l3:
    print(f'O tipo de elem é {type(elem)} e seu valor é {elem}')
