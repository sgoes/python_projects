secreto = 'perfume'
digitadas = []
chances = 3

while True:
    if chances < 0:
        print('Você perdeu!!')
        break
    
    letra = input('Digite uma letra: ')
    if len(letra) > 1:
        print('Inválido, digite apenas uma letra')
        continue
        
#preciso agora de guardar todas a letras certas que o usuário digitou
    digitadas.append(letra)
    print(digitadas)
#as letras digitadas vão ser incrementadas na lista agora
    if letra in secreto:
        #se a letra fizer parte da varievel secreta, fazemos o seguinte
        print(f'WOW, a letra "{letra}" existe na palavra secreta!!')
    else:
        print(f'BRRR, a letra "{letra}", não existe na palavra secreta')
        digitadas.pop() #o ultimo elemento adicionado à minha lista será apenas removido da minha lista
    
    secreto_temporario = ''    
    for letra_secreta in secreto:
        if letra_secreta in digitadas: #se a letra secreta está na minha lista de digitadas
            secreto_temporario += letra_secreta
        else: #caso a letra secreta não estiver nas letras digitadas 
            secreto_temporario += '*'

    if secreto_temporario == secreto:
        print(f'GANHOU a palavra secreta é: {secreto_temporario}')
        break
    else:
        print(f'A palavra secreta está assim: {secreto_temporario}')

    if letra not in secreto:
        chances -= 1
    print(f'Você ainda tem {chances} chances')
        
     
