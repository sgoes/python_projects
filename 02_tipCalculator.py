print("Welcome to the tip calculator!")

bill = float(input("What was the total bill? "))
tip = int(input("What the percentage tip would you like to give? 10, 12 or 15? "))
people = int(input("How many people to split the bill? "))

tip_as_percent = tip / 100

total_tip_amount = bill * tip_as_percent

total_bill = bill + total_tip_amount

bill_per_person = total_bill / people


#Para arredondar o total apenas com duas casas decimais
final_amounth = round(bill_per_person, 2)


#Quando o resultado acaba apenas com uma casa decimal e queremos acresentar a segunda na mesma, ou seja, queremos acrescentar um 0
final_amounth = "{:.2f}".format(bill_per_person)

print(f"Each person should pay {final_amounth}")



#ohter way to do the things 
total_bill = float(input("What was the total bill? "))
tip = int(input("What percentage tip would you like to give? 10, 12 or 15: "))
each_person = int(input("How many people who the split the bill? "))

tip_as_percentage = tip /100
total_bill_tip = total_bill + tip_as_percentage
total = total_bill_tip / each_person

print(f'Each person shloud pay {round(total, 2)}')
