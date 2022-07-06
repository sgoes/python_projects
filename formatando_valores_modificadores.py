'''
Formatando valores com modificadores

:s - Texto (strings)
:d - Inteiros (int)
:f - Numeros float
'''


nome = "Carolina Goes"
print(f'{nome:#^50}')
print(50-len(nome))

nome_formatado = '{:@^50}'.format(nome)

print(nome_formatado)

nome_formatado = '{n}   {n}   {n}   {n}'.format(n=nome)
print(nome_formatado)



nome = "Carolina"
sobrenome = "Goes"
nome_formatado = '{0:$^50} {1:#^50}'.format(nome, sobrenome) #Aqui estou a aceder ao indice, dentro da celula format
print(nome_formatado)

nome = "carolina goes"
nome = nome.ljust(20, '#')
print(nome.lower()) # tudo minusculo
print(nome.upper()) # tudo maiusculo
print(nome.title()) # Primeiras letras maiusculas
