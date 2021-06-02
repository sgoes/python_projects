
def turn_around():
    turn_left()
    turn_left()
    
def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def start():
    move()
    build_wall()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
    move()

def final():
    build_wall()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
    move()

start()
final()
final()
final()

