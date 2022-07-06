variavel = ['Carolina', 'Joao', 'Maria']

comeca_com_j = False
for valor in variavel:
    if valor.lower().startswith('j'):
        comeca_com_j = True
else:
    print('Não existe uma palavra que começa com J.')
