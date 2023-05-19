"""DISCLAIMER: 
The solutions here vary based on how you design your ERD.  So the queries could a bit different from what you
came up with for a solution.

PLEASE, PLEASE try to solve these on your own before looking at the solutions!
"""

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

# Take a look at the enclosed ERD for how we came up with this in office hour.  Columns will vary.

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

# Answers will vary based on the columns and names in your ERD.
"""
1. INSERT INTO teams (name, location, mascot)
VALUES ("SuperSonics", "Seattle", "Sasquatch");
INSERT INTO teams (name, location, mascot)
VALUES ("Bulldogs", "Gonzaga", "Spike"), ("Ducks", "Oregon", "The Oregon Duck"); -- Inserting two at once
2. INSERT INTO players (first_name, last_name, jersey_num, position, height, weight, team_id)
VALUES ("Gary", "Payton", 20, "Point guard", 6.3, 190, 1);
INSERT INTO players (first_name, last_name, jersey_num, position, height, weight, team_id)
VALUES ("Kevin", "Durant", 35, "Small forward", 6.8, 240, 1),
("Adam", "Morrison", 35, "Small forward", 6.7, 205, 2),
("Detlef", "Schrempf", 32, "Power forward", 6.8, 235, 1),
("Courtney", "Vandersloot", 15, "Point guard", 5.7, 145, 2);
-- Note that we need the team_id, the foreign key!
3. SELECT * FROM teams;
4. SELECT * FROM players WHERE id = 2;
5. DELETE FROM players WHERE id = 2;
6. UPDATE players SET jersey_num = 21 WHERE id = 5; -- You can change as many columns as you want
7. SELECT * FROM teams
LEFT JOIN players
ON teams.id = players.team_id;
8. SELECT * FROM players
JOIN teams
ON players.team_id = teams.id
WHERE players.id = 1; -- Make sure you add the table name, otherwise the column 'id' is ambiguous
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

# Correct answer for part 1 (parameter names will vary - I use data_dictionary here):
class Teacher:
    def __init__(self, data_dictionary): # data_dictionary is a dictionary with key-value pairs (this will come from your database)
        self.id = data_dictionary["id"]
        self.name = data_dictionary["name"]
        self.subject = data_dictionary["subject"]
        self.created_at = data_dictionary["created_at"]
        self.updated_at = data_dictionary["updated_at"]

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
# Part 2
teacher_object_list = [] # Here is the new list
for this_teacher_dictionary in teacher_dictionary_list:
    teacher_object_list.append(Teacher(this_teacher_dictionary)) # Create Teacher object by passing in the current dictionary

# Part 3
for this_teacher_object in teacher_object_list: # Loop through these objects
    print(f"ID #{this_teacher_object.id}: Name - {this_teacher_object.name}") # Answers will vary here - print the ID and name