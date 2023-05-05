
x = [] # List
y = {} # Dictionary

value_list = [3, 7, 5, 10, -3]
books = {
    "Harry Potter and the Sorcerer's Stone": "J. K. Rowling",
    "The Old Man and the Sea": "Ernest Hemingway"
}

# Accessing values
print(value_list[1])
print(books["Harry Potter and the Sorcerer's Stone"])

# ILLEGAL: there is no append method for a dictionary - only for a list
# books.append("The Catcher in the Rye")
# OKAY:
value_list.append(4)
print(value_list)
# Useful tip: the type() function to figure out what type of variable you're dealing with
print(type(value_list))

# Looping through a list
# Method 1: Go by index
for index in range(len(value_list)): # range(5) gives a sequence of values: 0, 1, 2, 3, 4
    print(index) # Prints only the index - NOT the value in the list at the index
    print(value_list[index])
    print(f"The value of value_list at index {index}, so value_list[{index}], equals {value_list[index]}")

# Method 2: Grab the value directly
for value in value_list:
    print(value) # Notice we are NOT using the index at all

# Looping through a dictionary
print("Going through dictionaries now....")

# Method 1: Go through each key directly - no built-in methods
print("Method 1:")
for current_title in books:
    print(current_title) # Grabs each key in the dictionary
    print(books[current_title]) # Prints the author linked to this book (the value linked to this key)

# Method 2: Same as method 1, except we'll use the .keys() method
print("Method 2:")
for current_title in books.keys():
    print(current_title)

# Method 3: Grabbing by value ONLY
print("Method 3:")
for current_author in books.values():
    # Drawback: You can't grab a key from a value - you can only use the value itself
    print(current_author)

# Method 4: Grabbing each key and value directly, using the .items method
print("Method 4:")
for title, author in books.items():
    print(title + " was written by " + author + ".")

# Combining data types
author_dictionary = {
    "Stephen King": ["The Stand", "Carrie"],
    "Jane Austen": ["Emma"],
}

print(type(author_dictionary))

print(author_dictionary)
print(author_dictionary["Stephen King"])

print(type(author_dictionary["Stephen King"]))

# Print each book written by Stephen King
# List we need to grab: author_dictionary["Stephen King"]
for title in author_dictionary["Stephen King"]: # Need to grab a list!!!
    print(title)

list_of_books = [
    {
        "id": 1,
        "author": "Stephen King",
        "title": "The Stand"
    },
    {
        "id": 2,
        "author": "Michael Crichton",
        "title": "Jurassic Park"
    },
    {
        "id": 3,
        "author": "F. Scott Fitzgerald",
        "title": "The Great Gatsby"
    }
]
print(type(list_of_books))
# Print each dictionary entirely in the list
for current_book in list_of_books:
    print(current_book)

# Print the authors ONLY
for current_book in list_of_books:
    # print(type(current_book))
    print(current_book["author"])

# Final challenge:
pokemon = [
    {
        "id": 1,
        "name": "Bulbasaur",
        "moves": ["Razor Leaf", "Tackle", "Growth"]
    },
    {
        "id": 4,
        "name": "Charmander",
        "moves": ["Ember", "Tackle", "Tail Whip"]
    },
    {
        "id": 7,
        "name": "Squirtle",
        "moves": ["Bubble", "Tackle", "Tail Whip"]
    },
]

# Access the value "Bubble" from the pokemon variable
print(pokemon) # Entire list
print(pokemon[2]) # Specific dictionary in the list
print(pokemon[2]["moves"]) # List (value) inside the dictionary
print(pokemon[2]["moves"][0]) # Specific value in list of moves