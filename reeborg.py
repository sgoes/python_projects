def turn_right():
    turn_left()
    turn_left()
    turn_left()
 
def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
    
#for step in range(6):
#    jump()

#fruits = ["Apple", "Pear", "Orange"]
#for fruit in fruits:
#    print(fruit)

while not at_goal():
    jump()

