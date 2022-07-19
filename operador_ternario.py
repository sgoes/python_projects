#operador ternario em python

idade = input('Qual a sua idade? ')

if not idade.isnumeric():
    print('Apenas digite numeros')
else:
    idade = int(idade)
    e_de_maior = (idade >= 18)
    msg = 'Pode acessar' if e_de_maior else 'Nao pode acessar'
    print(msg)
