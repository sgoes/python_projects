

#first statement
#small pizza: 15€
#medium pizza: 20€
#large pizza: 25€

#second statement
#pepperoni for small pizza: +2€
#pepperoni for medium and large pizza: +3€

#third statement
#extra cheese for any pizza: +1€


print("Welcome to Python Pizzaa Delivreries")
size = input("What size do you want? S, M, L ? ")
add_pepperoni = input("Do you want pepperoni? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")


bill = 0

if size == "S":
  bill += 15
elif size == "M":
  bill += 20
elif size == "L":
  bill += 25

if add_pepperoni == "Y":
  if size == "S":
   bill += 2
  else:
    bill += 3

if extra_cheese == "Y":
  bill += 1

print(f"your final bill is €{bill}")
