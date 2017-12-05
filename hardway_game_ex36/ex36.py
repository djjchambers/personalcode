# command_direction = ["north", "south", "east", "west"]
# command_get = ["get", "take"]
# command_attack = ["hit", "kill", "attack", "smash"]
# command_examine = ["examine". "search", "study", "inspect"]
# command_higher = ["quit", "help", "score"]
# command_look = ["look", "l"]
# command_inv = ["inv", "inventory", "i"]

# acc_nouns = ["cockpit", "console", "button", "lights", "dial", "slot", "machines", "cogs", "airlock", "starship", "door", "wrench", "alien", "monster"]

# room_data = ["Cockpit", "You are in the mucky cockpit of an old starship\, complete with blinking lights and a view of millions of stars through the windshield\, floating in the cold void of space", "In the Starship cockpit", 2, 0, 0, 0, "Engine Room", "You are in the clanking Engine Room of a starship\, full of machines whirring and cogs cogging", "In the Engine Room", 1, 3, 0, 0, "You are in the Airlock of a starship\, the transparent door opening onto the void of space", "In the starship airlock", 2, 0, 0, 0]

# object_data = ["terminal", "The ancient T-1000 terminal\, with its tiny low-resolution screen\, a red button and a disk slot", "]
# interpret room info, if first_visit = True print out verbose description else short desc
# read item & character lists to see if any of them are in the current room
# if character in list is here, print character "is here"
# if item in item list is here, print item description "is here".

# prompt for input
player_input = input('> ')


# break down input, strip down to verb & noun
# def break_words(player_input):
    # words = player_input.split(' ')
    # verb = words.pop(0)
    # noun = words.pop(-1)

# if verb is in command_higher
    # execute higher function
# if verb is in look then print verbose room description again
# If verb is in movement then translate character
# if verb is in get and noun is in item_list and item coordinates = player (x, y) then flag item (is_carried)

# check noun is present in (x,y)

# if verb is something else, call related function to enact action on character/item
# if player is not_dead and not won then go to beginning