from room import Room
from player import Player

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}

# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

directions = ['n', 's', 'e', 'w']

# Write a loop that:
#
# Make a new player object that is currently in the 'outside' room.
player_name = input('What is your chosen name? \n')
player = Player(player_name, room['outside'])
print(f"The best of luck to you, {player.name}. You're going to need it.\n")


# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
while True:
    user_input = input(f"Where would you like to go {player.name}? \n").lower().split()

    if len(user_input) > 2 or len(user_input) < 1:
        print(f"Sorry, {player.name}, You need to choose a direction. Would you like 'help'?\n")
    
    # If the user enters "q", quit the game.
    else:
        if user_input[0] == "q" or user_input[0] == "quit":
            print(f"Aww giving up, {player.name}?") 
            break

        if user_input[0] == "h" or user_input[0] == "help":
            print("Commands:\n'n' - Move North\n's' - Move South\n'e' - Move East\n'w' - Move West\n'l' or 'look' - Look around the current room\n'h' or 'help' - Help Menu\n'q' or 'quit' - Exit Game\n")
            continue
# * Prints the current room name
        if user_input[0] == "l" or user_input[0] == "look":
            player.look()
            continue
# print(f"{player.name}, you find yourself in {player.current_room.name}. \n{player.current_room.description}")
        if user_input[0] in directions:
            try:
                player.change_room(user_input[0])
                print(f"{player.name} you find yourself in {player.current_room.name}. \n{player.current_room.description}\n")
            except AttributeError:
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
                print(f"{player.name} it is too dark to go that way.'\n")
        else:
            print('You know better...Please enter a direction (N, E, W, S) to move around the map\n')