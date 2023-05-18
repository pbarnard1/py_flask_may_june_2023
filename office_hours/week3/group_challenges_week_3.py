"""
Challenge 1A: Make an ERD in MySQL Workbench and forward-engineer
1. Create a brand new schema.  Rename the schema as you see fit - preferably with the word "schema" at the end.
2. Create two tables: one for teams, and one for players.
In the teams table, make sure you have at least the following columns:
- id
- created_at
- updated_at
You're free to add any other columns you want.  
Be creative - the teams can play baseball, soccer, basketball, you name it!  It might not even be sports!

In the players table, make sure you have the following at least:
- id
- created_at
- updated_at
- A foreign key
Just like the teams table, you're free to add any additional columns you see fit.

Assume this is a one-to-many relationship!  Don't forget about default values for the created_at and updated_at
fields, and to auto-increment the id!  Also make sure the foreign key's ON DELETE is set to CASCADE!

3. Forward-engineer the schema.
"""


"""
Challenge 1B: MySQL queries
1. Add 3 teams.
2. Add 5 players - only link to 2 of the teams for this exercise.  We'll leave one team with no players.
3. Grab all the teams - don't link any players yet.
4. Grab one player by id - you can pick anyone you wish.
5. Remove any 1 player you want.
6. Change any 1 player - you can change the team and/or any column(s) you chose for the player (e.g. some sort of name).
7. Now grab all teams with players, regardless of who's in which team.  If you do this right, you should see
all 3 teams pop up, including the one team with no players.
8. Now grab one player and the team they're connected to.
"""



"""
Challenge 2: Creating objects with a list of dictionaries
1. Given the code below, refactor the __init__ method so it only takes one parameter - a dictionary - other than self.
2. Using the loop below to start, create a new list of class instances (objects).
3. Use this new list to print the ID and name from each object.
"""

# Starter code for part 1:
class Teacher:
    def __init__(self, id, name, subject, created_at, updated_at):
        self.id = id
        self.name = name
        self.subject = subject
        self.created_at = created_at
        self.updated_at = updated_at

# Starter code for part 2:
teacher_dictionary_list = [
    {
        "id": 1,
        "name": "Adrian",
        "subject": "Programming",
        "created_at": "2023-01-15 08:15:32",
        "updated_at": "2023-03-11 11:25:55"
    },
    {
        "id": 2,
        "name": "Melissa",
        "subject": "Python",
        "created_at": "2023-02-02 10:22:15",
        "updated_at": "2023-02-25 12:04:33"
    },
    {
        "id": 3,
        "name": "Lee",
        "subject": "Java",
        "created_at": "2022-11-15 08:05:11",
        "updated_at": "2023-02-25 16:53:47"
    }
]

# Create a new list here.
for this_teacher_dictionary in teacher_dictionary_list:
    pass # Replace this - create the Teacher object by passing in the "this_teacher_dictionary", then add it to the new list

# Starter code for part 3 (commented out):
# for this_teacher_object in ???: # Replace the ??? with your new list here
#     print(this_teacher_object) # Fix this line to print the id - bonus if you can print the id and name with one print statement!