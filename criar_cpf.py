"""
CPF = 168.995.350-09
---------------------------------------------

1 * 10 = 10            # 1 * 11 = 11
6 * 9 = 54             # 6 * 10 = 60
8 * 8 = 64             # 8 * 9 = 72
9 * 7 = 63             # 9 * 8 = 72
9 * 6 = 54             # 9 * 7 = 63
5 * 5 = 25             # 5 * 6 = 30
3 * 4 = 12             # 3 * 5 = 15
5 * 3 = 15             # 5 * 4 = 20
0 * 2 = 0              # 0 * 3 = 0
                       # 0 * 2 = 0
    TOTAL= 297
    
11 - (297 % 11) = 11   # 11 - (343 % 11) = 9
11 > 9 = 0             #
Digito 1 = 0           # Digito 2 = 9

Explicação na primeira coluna tenho o CPF na horizontal e para calcular preciso de fazer uma contagem regressiva 
"""
cpf = '16899535009'
novo_cpf = '16899535009'

if cpf == novo_cpf:
    print('Válido')
else:
    print('Inválido')
