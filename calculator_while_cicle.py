while True:
    print()
    num_1 = input('Digite um número: ')
    num_2 = input('Digite outro número: ')
    operador = input('Digite um operador: ')
    sair = input('Deseja sair? [s]im ou [n]ao: ')

    if sair == 's':
        break
    
    if not num_1.isnumeric() or not num_2.isnumeric():
        print('Precisa de digitar um número inteiro.')
        continue

    num_1 = int(num_1)
    num_2 = int(num_2)        

    # + - / *
    if operador == '+':
        print(num_1 + num_2)
    elif operador == '-':
        print(num_1 - num_2)
    elif operador == '/':
        print(num_1 / num_2)
    elif operador == '*':
        print(num_1 * num_2)
    else:
        print('Operador invalido')
