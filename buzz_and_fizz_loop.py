for number in range(1, 101):
  if number % 3 == 0 and number % 5 == 0:
    print("FizzBuzz")
  elif number % 3 == 0:
    print("Fizz")
  elif number % 5 == 0:
    print("Buzz")
  else:
    print(number)
    
    #all numbers divisible by 3 or 5, write FizzBuzz, all numbers divisibles by 3 write Fizz, all numbers divisibles by 5 write buzz, else print only the number. that's it :D
