#Explicacao do laço for 

secreto = 'python'
secreto_temporario = ''

digitadas = ['t']

for letra_secreta in secreto:
    if letra_secreta == 't':
        pass #se a letra in secreto for igual a t, o pass serve para nao imprimir 
    else:
        print(letra_secreta)

print('##############################')
#ou ainda posso fazer isto de outra forma:
for letra_secreta in secreto:
    if letra_secreta != 't':
        print(letra_secreta)

print('##############################')
#se a letra secreta está dentro da lista das digitadas 
for letra_secreta in secreto:
    if letra_secreta in digitadas:
        secreto_temporario += letra_secreta
print(secreto_temporario)

print('##############################')

#como o laço for funciona
for letra_secreta in secreto:
    print(f'Iteração para letra {letra_secreta}')
    if letra_secreta in digitadas:
        secreto_temporario += letra_secreta
print(secreto_temporario)
