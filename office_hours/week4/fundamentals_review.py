x = "Adrian" # Variable

# Defining a function
def is_even_or_odd(value_to_check):
    if value_to_check % 2 == 1: # If statement demo
        return "Odd"
    else:
        return "Even"
    # Usually we return values from functions and methods
    
result1 = is_even_or_odd(10)
print(result1)

# Lists and dictionaries
my_list = [10, 15, "Adrian", "Jane", True] # List - defined with the square brackets []
# Grabbing the value "Adrian" from the list:
print(my_list[2])
cur_ind = 0
print(my_list[cur_ind])
# Defining a dictionary
my_info = {
    "name": "Adrian",
    "number": 10,
    "is_happy": True
}

print(my_info["is_happy"])
cur_key = "number"
print(my_info[cur_key])

# List of dictionaries
game_list = [
    {
        "id": 1,
        "name": "The Legend of Zelda: Tears of the Kingdom",
        "publisher": "Nintendo"
    },
    {
        "id": 2,
        "name": "Monopoly",
        "publisher": "Parker Brothers"
    },
    {
        "id": 3,
        "name": "Halo",
        "publisher": "Microsoft 343"
    }
]

# Grab each dictionary, one at a time
for game in game_list:
    print(game) # Print the entire dictionary
    # Print the name of the current game
    # print(type(game_list))
    # print(type(game))
    # print(game_list["name"]) # Not correct - need to reference a dictionary, not a list
    print(game["name"]) # CORRECT - "game" is the name of the dictionary, so we can use the name of a key in quotes inside the []

# Player class
class Player:
    def __init__(self, name, position, player_number):
        self.name = name
        self.position = position
        self.player_number = player_number
        self.team = None # This will hold a specific Team object (class instance) we're linking to this Player

# Team class
class Team:
    def __init__(self, name, location, wins, losses, ties):
        self.name = name
        self.location = location
        self.wins = wins
        self.losses = losses
        self.ties = ties
        self.players = [] # This will hold a bunch of Player objects (class instances)

# Creating a Player object (class instance)
player_object = Player("Michael Jordan", "Shooting Guard", 23)
# Grab the player number
print(player_object.player_number)