from utils import entrance
code = "1234"
entrance(code)

#else:
#    code_input = input("Code invalid, retry\n")
#    attempt = attempt + 1
#    if attempt >= 2:
#       success = False
#       if code == code_input:
#            success = True
#        break




def choice(a,b,c,d,e,f):
    while True:
        decision = input("Where do you want to go?")
        if decision == a:
            print ("You are in room:", a)
            next_state = d
            break
        elif decision == b:
            print ("Key needed, door locked\n You are in room:", e)
            next_state = e
            break
        elif decision == c:
            print ("You are in room:", c)
            next_state = f
            break
        else:
            print("Invalid input")
    return next_state













#from utils import state_result
#state = "coding"
#print("You are", state)
#result = state_result("tired","hungry","happy","sleeping", "eating", "coding")
#print ("You are", result)
#while True:
#        if result == "eating":
#            result = state_result("tired","thirsty","happy","sleeping", "drinking", "coding")
#            print("You are", result)
#            break
#print("You are", state_result("tired","hungry","happy","sleeping", "eating", "coding"))
#def state_result(t, h,a, s, e, c):
#    while True:
#        feeling = input("How are you feeling?\n")
#        if feeling == t or feeling == h or feeling == a:
#            if feeling == t:
#                state = s
#            elif feeling == h:
#                state = e
#            else:
#                state = c
#            break
#
#        else:
#            print("Invalid feeling")
#    return state




#from utils import choice
#state = "hallway"
#print("You are in the", state)
#result = choice("1", "2", "3", "Room 1", "Hallway", "Room 3")