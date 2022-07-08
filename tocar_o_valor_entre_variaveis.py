
#numa outra linguagem de programaçao era preciso fazer desta forma
x = 10 
y = 'Luis'

z = x #10
x = y #luis
y = z #10

print(f'x = {x} e y = {y}')

#em python basta atribuir o valor das variaveis na troca
x = 10 
y = 'Luis'


x, y = y, x

print(f'O valor de x = {x}, e o valor de y = {y}')


#Uma outra forma de trocar valores entre variaveis
x = 10 
y = 'Luis'
z = 'Carolina'


x, y, z = z, x, y

print(f'O valor de x = {x}, e o valor de y = {y}, e o valor de z = {z}')
