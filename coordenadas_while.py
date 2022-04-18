#Estrutura de repetição em python
'''
Em python temos dois tipos de estrutura de repetição o laço WHILE e FOR
O WHILE realiza ações enquanto forem verdaderas 
'''
x = 0
while x < 10:
    if x == 3:
        x = x + 1
        continue

    print(x)
    x = x + 1

print('Acabou')


#para imprimir valor de coordenadas num ciclo while
x = 0 #coluna x:0
while x < 10:
    y = 0 # linha y:0
    while y < 5:
        print(f'({x},{y})')
        y += 1
    x += 1 # x = x +1
    
    
