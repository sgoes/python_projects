print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

combined_string = name1 + name2 #junta-se os dois nomes inseridos, tornando-os numa só string
lower_case_string = combined_string.lower() #converte-se as letras maiusculas inseridas

#Procede-se à funçao de contagem - TRUE LOVE
t = lower_case_string.count("t")
r = lower_case_string.count("r")
u = lower_case_string.count("u")
e = lower_case_string.count("e")
l = lower_case_string.count("l")
o = lower_case_string.count("o")
v = lower_case_string.count("v")
e = lower_case_string.count("e")

true = t + r + u + e
love = l + o + v + e
love_score = int(str(true) + str(love))


if (love_score < 10) or (love_score > 90):
  print(f"Your score is {love_score}, you go together like coke and mentos.")
elif (love_score >= 40) and (love_score <= 50):
  print(f"your score is {love_score}, you are alright together")
else:
  print(f"your score is {love_score}")
