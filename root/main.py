from utils import to_entrance, to_hallway, to_office, to_storage, to_living_room, to_basement, to_library, to_bedroom, to_kitchen
state = "entrance"
code = "47983"
key_collection = 0
flashlight = 0
unlocked_door = False
piece_found1 = False
piece_found2 = False
piece_found3 = False
piece_found4 = False
piece_found5 = False

print("You wake up in the entrance of a locked house. Find the code to exit.")
while True:
    if state == "entrance":
        state = to_entrance(code)
    if state == "hallway":
        state = to_hallway(key_collection)
    if state == "office":
        state, piece_found1 = to_office(piece_found1)
    if state == "storage":
        state, piece_found2 = to_storage(piece_found2)
    if state == "living room":
        state,key_collection = to_living_room(key_collection)
    if state == "basement":
        state, flashlight, piece_found4 = to_basement(flashlight,piece_found4)
    if state == "bedroom":
        state, flashlight,piece_found3 = to_bedroom(flashlight, piece_found3)
    if state == "kitchen":
        state, piece_found5 = to_kitchen(piece_found5)
    if state == "library":
        state, unlocked_door = to_library(unlocked_door)
    if state == "outside":
        print("You have completed the game!")
        break