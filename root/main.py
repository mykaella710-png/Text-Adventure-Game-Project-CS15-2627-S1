from utils import choice

key_collection = 0
state = "entrance"
while True:
    if state == "entrance":
        print("You are now in the entrance")
        while True:
            decision = input("Where do you want to go?\n 1. exit \n 2. hallway\n")
            if decision == "1":
                state = "entrance"
                print("You are in front of the exit, but it is locked. Find a way to leave")
                decision = input ("Go to hallway?\n 1. Yes\n 2. No\n")
                if decision == "1":
                    state = "hallway"
                    break
                else:
                    state = "entrance"
            elif decision == "2":
                state = "hallway"
                print("You are now in the hallway")
                break
            else:
                print("Invalid input")

        if state == "hallway":
            state_result = choice("1","2","3","Room 1", "Hallway", "Room 3")
#            while True:
#                decision = input ("Where do you want to go?\n 1. left door \n 2. middle door\n 3 right door\n")
#                if decision == "1":
#                    state = "Room 1"
#                    print("You are in room ___")
#                    break
#                elif decision == "2":
#                    state = "Room 2"
#                    print("You are in room ___")
#                    break
#                elif decision == "3":
#                    state = "hallway"
#                    print("The door is locked, you are in the hallway.")
#                else:
#                    print("Invalid input")


        if state == "Room 1":
            while True:
                decision = input ("What do you want to do?\n 1. Search room \n 2. Leave\n")
                if decision == "1":
                    print("While searching room you found a key and return to the hallway")
                    key_collection = +1
                    state = "hallway"
                    break
                else:
                    state = "hallway"
                    print("You are in the hallway")
                    break

        if state == "hallway":
            decision = input("Where do you want to go?\n 1. Room 2\n 2. Room 3\n")
            if state == "Room 2":
                print("You are in room ___")
                if key_collection == 1:
                    print("You have the key, room opened")
                    state = "Room 2"

            if state == "Room 3":
                print("You are in room ___")
                state = "Room 3"