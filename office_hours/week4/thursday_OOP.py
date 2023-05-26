# Redefine these classes to only accept dictionaries - here's a list of dictionaries 
# to show you what our data will look like from our database
player_list = [
    {
        "id": 1,
        "name": "Michael Jordan",
        "position": "Shooting Guard",
        "player_number": 23,
        "team_id": 1
    },
    {
        "id": 2,
        "name": "LeBron James",
        "position": "Shooting Guard",
        "player_number": 23,
        "team_id": 2
    },
    {
        "id": 3,
        "name": "Larry Bird",
        "position": "Guard",
        "player_number": 33,
        "team_id": 3
    },
    {
        "id": 4,
        "name": "Derrick Rose",
        "position": "Guard",
        "player_number": 1,
        "team_id": 1
    },
]

team_list = [
    {
        "id": 1,
        "name": "Bulls",
        "location": "Chicago",
        "wins": 72,
        "losses": 10,
        "ties": 0
    },
    {
        "id": 2,
        "name": "Lakers",
        "location": "Los Angeles",
        "wins": 55,
        "losses": 27,
        "ties": 0
    },
    {
        "id": 3,
        "name": "Celtics",
        "location": "Boston",
        "wins": 53,
        "losses": 29,
        "ties": 0
    },
]

# New Player and new Team classes with dictionaries as parameters in the __init__ method
class Player:
    def __init__(self, data): # data parameter is a DICTIONARY!!!!
        self.id = data["id"]
        self.name = data["name"]
        self.position = data["position"]
        self.player_number = data["player_number"]
        self.team = None # This will hold a specific Team object (class instance) we're linking to this Player
    
    def __repr__(self): # Recommend looking up __str__ and __repr__ to give us different output when printing objects
        return f"Player named {self.name} with ID {self.id}"

    # Create Player objects from within the class (preview of today and tomorrow)
    @classmethod
    def get_one_player(cls):
        # HARD-CODED EXAMPLE TO SIMULATE grabbing data from your database
        results_list = [ # SIMULATED list from your database - we will get a list of dictionaries back!!!
            {
                "id": 1,
                "name": "Michael Jordan",
                "position": "Shooting Guard",
                "player_number": 23,
                "team_id": 1
            }
        ]
        print(results_list)
        print(results_list[0])
        # Create this Player object
        new_player_object = cls(results_list[0]) # cls() means creating an instance of the class from within the class - in this case, cls() means Player()
        return new_player_object
    
    @classmethod
    def get_all_players(cls):
        # HARD-CODED EXAMPLE TO SIMULATE grabbing data from your database
        results_list = [ # SIMULATED list from your database - we will get a list of dictionaries back!!!
            {
                "id": 1,
                "name": "Michael Jordan",
                "position": "Shooting Guard",
                "player_number": 23,
                "team_id": 1
            },
            {
                "id": 2,
                "name": "LeBron James",
                "position": "Shooting Guard",
                "player_number": 23,
                "team_id": 2
            },
            {
                "id": 3,
                "name": "Larry Bird",
                "position": "Guard",
                "player_number": 33,
                "team_id": 3
            },
            {
                "id": 4,
                "name": "Derrick Rose",
                "position": "Guard",
                "player_number": 1,
                "team_id": 1
            },
        ]
        print("Inside get all method")
        # print(results_list)
        # print(results_list[0])
        player_object_list = [] # Hold a bunch of Player objects
        # Loop through this list of results
        for each_player_dictionary in results_list:
            new_player_object = cls(each_player_dictionary) # Creating a Player object; cls() means Player()
            player_object_list.append(new_player_object)
        return player_object_list
    
    @classmethod
    def get_one_player_with_team(cls):
        results_list = [ # SIMULATED list from your database - we will get a list of dictionaries back!!!
            {
                "id": 1,
                "name": "Michael Jordan",
                "position": "Shooting Guard",
                "player_number": 23,
                "team_id": 1,
                "teams.id": 1, # These key-values from this one on down will be from a joined table, and some keys will have the table name added because of duplicate columns
                "teams.name": "Bulls",
                "location": "Chicago",
                "wins": 72,
                "losses": 10,
                "ties": 0
            }
        ]
        # Create the Player object
        new_player_object = cls(results_list[0])
        # Create the Team object
        new_team_dictionary = {
            'id': results_list[0]["teams.id"],
            'name': results_list[0]["teams.name"],
            'location': results_list[0]["location"],
            'wins': results_list[0]["wins"],
            'losses': results_list[0]["losses"],
            'ties': results_list[0]["ties"]
        }
        new_team_object = Team(new_team_dictionary) # Can't use cls() because cls() here means Player()
        # Connect these two objects
        new_player_object.team = new_team_object
        # Return this Player object with the Team linked
        return new_player_object

class Team:
    def __init__(self, data):
        self.id = data["id"]
        self.name = data["name"]
        self.location = data["location"]
        self.wins = data["wins"]
        self.losses = data["losses"]
        self.ties = data["ties"]
        self.players = [] # This will hold a bunch of Player objects (class instances)

    @classmethod
    def get_one_team(cls):
        result_list = [ # HARD-CODED data that will come from a database
            {
                "id": 1,
                "name": "Bulls",
                "location": "Chicago",
                "wins": 72,
                "losses": 10,
                "ties": 0
            }
        ]
        # Create the Team object
        # cls() means creating an object inside the class, where cls essentially = the name of the class you're in
        # In this case, cls() means Team()
        new_team_object = cls(result_list[0])
        return new_team_object
    
    @classmethod
    def get_all_teams(cls):
        result_list = [
            {
                "id": 1,
                "name": "Bulls",
                "location": "Chicago",
                "wins": 72,
                "losses": 10,
                "ties": 0
            },
            {
                "id": 2,
                "name": "Lakers",
                "location": "Los Angeles",
                "wins": 55,
                "losses": 27,
                "ties": 0
            },
            {
                "id": 3,
                "name": "Celtics",
                "location": "Boston",
                "wins": 53,
                "losses": 29,
                "ties": 0
            }
        ]
        team_object_list = [] # Each item will be a Team object
        for this_team_dictionary in result_list:
            new_team_object = cls(this_team_dictionary)
            team_object_list.append(new_team_object)
        return team_object_list

# Testing creating these objects with dictionaries


another_dictionary = {
    "id": 2,
    "name": "LeBron James",
    "position": "Shooting Guard",
    "player_number": 23,
    "team_id": 2
}

second_object = Player(another_dictionary)
print(second_object.name)

# Testing the get one player class method
print("Class method test")
new_object = Player.get_one_player()
all_player_objects = Player.get_all_players()
print(all_player_objects)


# Testing creating a Player and Team and linking together
player_with_team = Player.get_one_player_with_team()
print(f"ID of player: {player_with_team.id}")
print(f"Name of player: {player_with_team.name}")
# Grab the name of the team linked to this player
print(f"Name and location of team: {player_with_team.team.location} {player_with_team.team.name}")