'''
For in em Pytho n
Iterando strings com for
Funcao range(start=0, stop, step=1)
'''

for n in range(20, 9, -1):
    print(n)
    
    
'''
Para encontrar multiplos
'''
for  n in range(0,100,3):
    print(n)
    
"""
Outro exemplo com de um for com um if, utilizando o módulo
"""
for n in range (0, 100, 8):
    print(n)

#é o mesmo que dizer que:  
print('###########')

for n in range (100):
    if n % 8 == 0:
        print(n) #enquanto o resto da divisão de 8 for 0, imprime até 100 (ou seja vao aparecer todos os multiplos de 8)
        
        
        
'''
Imprimir o laço for para interar um string
'''
texto = 'Python'
nova_string = ''

for letra in texto:
    if letra == 't':
        nova_string = nova_string + letra.upper()
    elif letra == 'h':
        nova_string += letra.upper()
    else:
        nova_string += letra
print(nova_string)
    
  
  texto = 'Python'
nova_string = ''

for letra in texto:
    if letra == 't':
        continue #isto avança para o proximo laço, ou seja, não vai imprirmir a letra T
        nova_string = nova_string + letra.upper()
    elif letra == 'h':
        nova_string += letra.upper()
    else:
        nova_string += letra
print(nova_string)


for letra in texto:
    if letra == 't':
        nova_string = nova_string + letra.upper()
    elif letra == 'h':
        nova_string += letra.upper()
        break #aqui estou a dizer que assim que encontrar a letra h para não imprimir mais nada 
    else:
        nova_string += letra
print(nova_string)
