"""
Challenge 1: Review of identifying data types
The variables below have NOT been defined beforehand.  Inspecting each line, identify the data type for each
variable (e.g. list, dictionary, class).

x[3] - x is a(n) _________
y["hello"] - y is a(n) __________
country.id - country is a(n) _________

BONUS challenge: this_var[2]["name"] - this_var is a(n) __________
"""

"""
Challenge 2: List of multiples
Write a function that accepts two values, p and q, as input, and returns a list containing
all multiples of q from 0 through p, inclusively.

Examples:
Given p = 20 and q = 3, return [0, 3, 6, 9, 12, 15, 18].
Given p = 24 and q = 6, return [0, 6, 12, 18, 24].
"""

"""
Challenge 3: More OOP practice

1A. Create a class called Movie with the following attributes that can be passed in.
    - id (an integer)
    - title (a string)
    - release date (a string in the form "YYYY-MM-DD", e.g. "2023-03-16")
    [- director was included initially here, but don't add a director yet]
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