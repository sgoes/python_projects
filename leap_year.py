
year = int(input("Which year do you want to check? "))

if year % 4 == 0:
  if year % 100 == 0:
    if year % 400 == 0:
      print("leap year")
    else: 
      print("not leap year")
  else:
    print("leap year")
else:
  print("not leap year")
  
 
#CRITERIOS PARA DEFINIR O ANO BISSEXTO
#Divisível por 4. Sendo assim, a divisão é exata com o resto igual a zero;
#Não pode ser divisível por 100. Com isso, a divisão não é exata, ou seja, deixa resto diferente de zero;
#Pode ser que seja divisível por 400. Caso seja divisível por 400, a divisão deve ser exata, deixando o resto igual a zero.


