"""DISCLAIMER: 
The solutions here may not 100% be the most efficient.  
These solutions are Adrian's way of solving these.

PLEASE, PLEASE try to solve these on your own before looking at the solutions!
"""


"""
Challenge 1: Review of identifying data types
The variables below have NOT been defined beforehand.  Inspecting each line, identify the data type for each
variable (e.g. list, dictionary, class).

x[3] - x is a list - a number inside the square brackets indicates it's an item in a list (e.g. [3, 8, 4, 1])
y["hello"] - y is a dictionary - a string inside the square brackets indicates it's a key in a dictionary
    {
        "hello": "Greetings!"
    }
country.id - country is a class instance (object) - the period means that the variable is an object, and what comes after
the period is the name of an attribute

class Nation:
    def __init__(self, data):
        self.id = data["id"] # Defining an attribute called "id"
        self.name = data["name"]

country = Nation(1,"Dojoland")
print(country.id)

BONUS challenge: this_var[2]["name"] - this_var is a list of dictionaries
[
    {
        "name": "Adrian"
    },
    {
        "name": "Jane"
    },
    {
        "name": "Daniel"
    }
]
"""

"""
Challenge 2: List of multiples
Write a function that accepts two values, p and q, as input, and returns a list containing
all multiples of q from 0 through p, inclusively.

Examples:
Given p = 20 and q = 3, return [0, 3, 6, 9, 12, 15, 18].
Given p = 24 and q = 6, return [0, 6, 12, 18, 24].
"""

p1 = 25
q1 = 8 # all multiples of 8 from 0 through 25 -> 0, 8, 16, 24

def multiples(p, q):
    all_multiples = [] # A list that will hold multiples of q
    for cur_val in range(0,p+1,q): # p is actually incorrect
        # print(f"Current value is {cur_val}, a multiple of {q}")
        all_multiples.append(cur_val)
    return all_multiples

print(multiples(20,3))
print(multiples(24,6))
print(multiples(p1, q1))

"""
Challenge 3: More OOP practice

1A. Create a class called Movie with the following attributes that can be passed in.
    - id (an integer)
    - title (a string)
    - release date (a string in the form "YYYY-MM-DD", e.g. "2023-03-16")
1B. Now create two Movies.  Use any values you want.
2A. Create a new class called Director with the following attributes:
    - id (an integer)
    - first name (a string)
    - last name (a string)
    - birthdate (a string in the form "YYYY-MM-DD", e.g. "1965-05-11")
2B. Now create 3 Directors, again using any values you want.
3A. Now let's add a new attribute to both the Movie and Director classes.
These attributes will NOT be passed in through the constructor (what's the name of
the method that creates, or constructs, the object?).  In the Movie model, we will
add an attribute that will hold the director in the movie.  What do you think
will be a good name for that attribute, and what should we use as a starting value?
Assume only one director per movie for this exercise.
3B. We will do the same for the Director class - now let's add an attribute that will
hold the movies that the director has worked on.  What do you think will be a good name
for that attribute, and what should we use as a starting value?
HINT: Can a director do more than one movie?
4. Create a method called director_info in the Director class that does the following:
- Prints the director's full name in one line
- Prints the birthdate in another line
- Allows for chaining (what would you type at the end of this method?)

The next two problems involve linking classes to each other.
5. Create a method in the Director class called add_movie that accepts
a Movie object as input and:
- Adds it to the movies that the director has done
- Allows for chaining
6. Create a method in the Movie class called cast_director that accepts
a Director object as input and:
- Links the Director to this Movie
- Allows for chaining
BONUS: Add a check to see whether there is already is a Director linked.  If
there is a Director from before, print "Already has a director named <director here>"
and do NOT link the Director.  (How do you get the name of the director in there?)

Now let's deal with class variables and methods.
7. Create the following class variables in the Movie class:
- rater - this is a string that represents the group that gives movie ratings (e.g. PG, R)
- all_movies - this will hold all the movies created as an empty list to start
8. Go to the constructor in the Movie class and add a line that will add the newly created
Movie to all_movies.
9. Write a class method called show_all_movies that:
- Prints the title of every movie

"""

"""
1A. Create a class called Movie with the following attributes that can be passed in.
    - id (an integer)
    - title (a string)
    - release date (a string in the form "YYYY-MM-DD", e.g. "2023-03-16")
"""
class Movie: # Name of class is PascalCase
    rater = "MPAA" # Solution to 7
    all_movies = []

    def __init__(self, id, title, release_date): # Solution to 1A
        self.id = id
        self.title = title
        self.release_date = release_date
        self.director = None # Solution to 3A - eventually hold ONE Director object
        Movie.all_movies.append(self) # Solution to 8 - adding the new Movie to the class variable all_movies

    def cast_director(self,new_director): # Solution to 6
        if self.director == None:
            self.director = new_director # Takes in the Director object and assigns it to the director attribute in this class
        else:
            print(f"Already has a director named {self.director.first_name} {self.director.last_name}")
        return self
    
    @classmethod # Don't forget this decorator!
    def show_all_movies(cls): # Solution to 9
        for this_movie in cls.all_movies:
            print(f"Title: {this_movie.title}")

"""
1B. Now create two Movies.  Use any values you want.
"""
# Testing 1B
titanic = Movie(1,"Titanic","1996-11-10")
bttf = Movie(2,"Back to the Future","1985-06-12")

"""
2A. Create a new class called Director with the following attributes:
    - id (an integer)
    - first name (a string)
    - last name (a string)
    - birthdate (a string in the form "YYYY-MM-DD", e.g. "1965-05-11")
2B. Now create 3 Directors, again using any values you want.
"""
class Director: # Name of class is PascalCase
    def __init__(self, id, first_name, last_name, birthdate): # Solution to 2A
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.birthdate = birthdate
        self.movies = [] # Solution to 3B: Empty list that will hold many Movie objects
    
    def director_info(self): # Solution to 4
        print("Name of director: " + self.first_name + " " + self.last_name)
        print(f"Birthdate: {self.birthdate}")
        return self # Allow for chaining
    
    def add_movie(self, new_movie): # Solution to 5
        self.movies.append(new_movie) # Link the new Movie to this Director
        return self

# Testing 2B
j_cameron = Director(1,"James","Cameron","1951-05-22")
s_spielberg = Director(2,"Steven","Spielberg","1946-12-11")
a_hitchcock = Director(3,"Alfred","Hitchcock","1899-08-12")
# Testing the director_info method
j_cameron.director_info()

# Testing 5 and 6
titanic.cast_director(j_cameron)
j_cameron.add_movie(titanic)
# IMPORTANT: Grabbing data when objects are linked
print(titanic.director.first_name + " " + titanic.director.last_name)
print(j_cameron.movies[0].title) # Note the [0] as the movies attribute is a list
titanic.cast_director(s_spielberg) # Already has a director

# Testing 9
Movie.show_all_movies()