def turn_around():
    turn_left()
    turn_left()
    turn_left()
    
while not at_goal():
    if not wall_on_right():
        turn_around()
        if front_is_clear():
            move()
    elif front_is_clear():
        move()
    elif wall_on_right():
        if front_is_clear():
            move()
        else:
            turn_left()
    else:
        turn_around()
        
    