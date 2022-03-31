'''
Faça um programa que pergunte a hora ao usuario e, baseando-se no horario descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17, Boa noite 18-23
'''
horario = input('Digite um horario (0-23)horas: ')
if horario.isdigit(): #aqui estamos a checkar se foi um numero que o usuario colocou 
    horario = int(horario)
    if horario < 0 or horario > 23:
        print("Horário deve estar entre a 0 e 23")
    else:
        if horario <= 11:
            print("Bom dia!")
        elif horario <= 17:
            print("Boa tarde!")
        else:
            print("Boa noite!")
else:
    print("Esse horário não é válido!")
