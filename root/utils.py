import random
def to_entrance(code):
    """
    Decisions for when at entrance

    :param code: Code needed to exit
    :return:The next state
    """
    while True:
        decision = input("Where do you want to go\n 1. exit\n 2. hallway\n\nChoice: ")
        if decision == "2":
            print("You are in the hallway")
            next_state = "hallway"
            break
        elif decision == "1":
            attempt = 0
            success = False
            while attempt < 3:
                code_input = input("Input the code before exit: ")
                attempt = attempt + 1
                if code_input == code:
                    success = True
                    print("Success! You made it outside!")
                    next_state = "outside"
                    break
            if not success:
                print("A code is required to exit, find it to leave")
                next_state = "hallway"
                break
            if success:
                break
        else:
            print("Invalid input")
    return next_state

def to_hallway(key):
    """
    Decisions for when in hallway

    :param key: Key needed to unlock storage room
    :return: The next state
    """
    while True:
        decision = input("Where do you want to go\n 1. office\n 2. storage\n 3. stairs\n 4. living room\n 5. entrance\n 6. kitchen\n\n Choice:")
        if decision == "1":
            print("You are in the office")
            next_state = "office"
            break
        elif decision == "2":
            if key == 1:
                print("You are in the storage room")
                next_state = "storage"
                break
            else:
                print("A key is required to enter.")
        elif decision == "3":
            print("You head up the stairs to the library")
            next_state = "library"
            break
        elif decision == "4":
            print("You are in the living room")
            next_state = "living room"
            break
        elif decision == "5":
            print("You are in the entrance")
            next_state = "entrance"
            break
        elif decision == "6":
            print("You are in the kitchen")
            next_state = "kitchen"
            break
        else:
            print("invalid input")
    return next_state

def to_office(piece1):
    """
    Decisions for when at office

    :param piece1: 1st code piece found
    :return: The next state and if 1st code piece was found
    """
    if not piece1:
        code_piece1 = "4"
        print("While exploring you discover a the first code piece:", code_piece1)
        piece1 = True

    while True:
        decision = input("Exit to hallway ?\n 1. yes\n 2. no\n\n Choice: ")
        if decision == "1":
            next_state = "hallway"
            break
        elif decision == "2":
            print("You remain in the office")
            next_state = "office"
            break
        else:
            print("Invalid input")
    return next_state, piece1

def to_storage(piece2):
    """
    Decisions for when at storage room

    :param piece2: 2nd code piece found
    :return: next state and if 2nd code piece was found
    """
    if not piece2:
        code_piece2 = "7"
        print("In the storage room, you find the second code piece:", code_piece2)
        piece2 = True
    while True:
        decision = input("Exit to hallway?\n 1. yes\n 2. no\n\n Choice: ")
        if decision == "1":
            next_state = "hallway"
            break
        elif decision == "2":
            print("You remain in the storage room")
            next_state = "storage"
            break
        else:
            print("Invalid input")
    return next_state, piece2

def to_living_room(key):
    """
    Decisions for when in living room

    :param key: Collected key for storage room
    :return: The next state
    """
    if key == 0:
        print("While exploring you discover the storage key and a door leading to the basement")
        key_collection = 1
    else:
        print("You have already collected the key")
        key_collection = key
    while True:
        decision = input("Where do you want to go now?\n 1. exit to hallway\n 2. basement\n\n Choice: ")
        if decision == "1":
            next_state = "hallway"
            break
        elif decision == "2":
            print("You follow the door going down to the basement")
            next_state = "basement"
            break
        else:
            print("invalid input")
    return next_state,key_collection

def to_basement(fl, piece4):
    """
    Decisions for when in basement

    :param fl: Flashlight needed
    :param piece4: 4th code piece
    :return: The next state, if flashlight is obtained, and if 4th code piece was found
    """
    if fl == 0:
        print("It is too dark, a flashlight is needed")
        return "living room", fl, piece4
    if not piece4:
        code_piece4 = 8
        print("You light up the basement with the flashlight to find the 4th code piece:", code_piece4 )
        piece4 = True
    else:
        print("You have already collected the 4th piece")

    while True:
        decision =  input("Exit to hallway?\n 1. yes\n 2. no\n\n Choice: ")
        if decision == "1":
            next_state = "hallway"
            break
        elif decision == "2":
            print("You remain in the basement")
            next_state = "basement"
            break
        else:
            print("Invalid input")
    return next_state, fl, piece4

def to_library(u_door):
    """
    Decisions for when at library

    :param u_door: If bedroom door unlocked
    :return: The next state and if bedroom door was unlocked
    """
    print("You are in the library")
    attempt = 0
    next_state = "library"
    while True:
        if u_door:
            print("Door already unlocked")
            next_state = "bedroom"
        else:
            secret_number = random.randint(1,20)
            success = False
            if not u_door:
                while attempt <= 2:
                    p_guess = input("Guess the secret number between 1-20 to unlock the door\n")
                    try:
                        p_guess = int(p_guess)
                    except ValueError:
                        print("Invalid input, please enter a number")
                        continue
                    attempt = attempt + 1
                    print(secret_number)
                    if p_guess > 20 or p_guess < 1:
                        print("The range is 1-20")
                    elif p_guess == secret_number:
                        u_door = True
                        print("Correct! You unlocked the door")
                        next_state = "bedroom"
                        return next_state, u_door
                    else:
                        if p_guess < secret_number:
                            print("Too low")
                            success = False
                        elif p_guess > secret_number:
                            print("Too high")
                            success = False
                        else:
                            print("Invalid guess")
            if not success:
                next_state = "library"

            if attempt > 2:
                if not success:
                    print("Attempts used up, try again")
                    next_state = "library"

        return next_state, u_door

def to_bedroom(fl, piece3):
    """
    Decisions for when in bedroom

    :param fl: Flashlight needed
    :param piece3: 3rd code piece
    :return: The next state, if flashlight is obtained, and if 3rd code piece was found
    """
    if not piece3:
        code_piece3 = "9"
        print("You are in the bedroom and have found the 3rd code piece:", code_piece3)
        piece3 = True

    if fl == 0:
        print("You have also found the flashlight!")
        fl = 1
    else:
        print("You are in the bedroom and have already collected important tools")

    while True:
        decision = input("Do you want to exit to hallway now?\n 1. yes\n 2. no\n\n Choice: ")
        if decision == "1":
            next_state = "hallway"
            break
        elif decision == "2":
            print("You remain in the bedroom")
            next_state = "bedroom"
            break
        else:
            print("Invalid input")
    return next_state, fl, piece3

def to_kitchen(piece5):
    """
    Decisions for when in kitchen

    :param piece5: 5th code piece
    :return: The next state and if 5th code piece was found
    """
    if not piece5:
        code_piece5 = "3"
        print("In the kitchen you discover a note on the fridge with the last code piece:", code_piece5)
        piece5 = True
    while True:
        decision = input("Exit to hallway?\n 1. yes\n 2. no\n\n Choice: ")
        if decision == "1":
            next_state = "hallway"
            break
        elif decision == "2":
            print("You remain in the kitchen")
            next_state = "kitchen"
            break
        else:
            print("Invalid input")
    return next_state, piece5

