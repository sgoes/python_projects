#Password Generator Project
import random

lower_case = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
upper_case = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_lower_case = int(input("How many letters lower case would you like?\n")) 
nr_upper_case = int(input(f"How many letters upper case would you like? \n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))


password_list = []

for char in range(1, nr_lower_case + 1):
  password_list.append(random.choice(lower_case))

for char in range(1, nr_upper_case + 1):
  password_list.append(random.choice(upper_case))

for char in range(1 , nr_symbols + 1 ):
  password_list.append(random.choice(symbols))

for char in range(1, nr_numbers + 1):
  password_list += random.choice(numbers)


random.shuffle(password_list)


password = ""
for char in password_list:
  password += char

print(password)
