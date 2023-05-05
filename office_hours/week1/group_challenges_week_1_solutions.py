"""DISCLAIMER: 
The solutions here may not 100% be the most efficient.  
These solutions are Adrian's way of solving these.

PLEASE, PLEASE try to solve these on your own before looking at the solutions!
"""

"""
Challenge 1: What's your name? (From HackerRank - https://www.hackerrank.com/challenges/whats-your-name/problem?isFullScreen=true)

You'll have two variables for first name and last name.  Your goal is to print a string in the following format:
'Hello first_name last_name!  You just delved into Python!'

For example, if the first name is "John" and the last name is "Doe", then you should print:
'Hello John Doe!  You just delved into Python!'
"""
# Answers will vary, as there are other versions that are correct.

# Method 1
first_name = "Jane"
last_name = "Doe"
print(f"Hello {first_name} {last_name}!  You just delved into Python!")

# Method 2
first_name = "Jack"
last_name = "Roe"
# Using string concatenation to store the message into a variable (you cannot use commas - you either do it this way or using f-strings usually)
message = "Hello " + first_name + " " + last_name + "!  You just delved into Python!"
print(message)


"""
Challenge 2:
Create a loop that will print *every other* value in a list, starting with the value at index 0, index 2, etc.

For example (feel free to make up your own lists - use your own variables and values!):
my_list = [8, 1, "Hello", "green", True, 4, -1.5] # You should print 8, "Hello", True and -1.5 in this example
# Your loop goes here.
"""
this_list = [10, -5, "blue", 8.4, False, [1, 3, 8]]
for cur_ind in range(0,len(this_list),2): # Note the 0 and 2 here - start at index 0, going in increments of 2
    print(this_list[cur_ind])

"""
Challenge 3:
Write a function that accepts a string as input and returns the number of vowels found in the string.
For this exercise, "a", "e", "i", "o" and "u" are vowels; we will not count "y" for this challenge.
If it helps, assume the string is all lower-case for now.  Then try to make it work regardless of if the
letters are upper- or lower-case.

For example: given "tommy", return 1 as "o" is a vowel, but "y" is not.  "adrian" should return 3.
"""
def count_vowels_v1(input_str): # Need an input for the string itself
    new_str = input_str.lower() # Convert to lower case
    num_vowels = 0 # Start the count off at 0 vowels found
    # Go through each letter (watch your indentation!)
    for cur_char in new_str: # One way to loop (others are acceptable)
        if cur_char == "a" or cur_char == "e" or cur_char == "i" or cur_char == "o" or cur_char == "u":
            num_vowels += 1
    return num_vowels

print(count_vowels_v1("Great program")) # Should give us 4
second_result = count_vowels_v1("Good work!")
print(second_result) # Prints 3

def count_vowels_v2(input_str): # Need an input for the string itself
    new_str = input_str.lower() # Convert to lower case
    num_vowels = 0 # Start the count off at 0 vowels found
    # Go through each letter (watch your indentation!)
    for cur_char in new_str: # One way to loop (others are acceptable)
        if cur_char in ["a", "e", "i", "o", "u"]: # Check whether the current character is in this list of vowels
            num_vowels += 1
    return num_vowels

print(count_vowels_v2("Good game!")) # Prints 4

"""
Challenge 4:
Given a list of dictionaries as input in the format below, return a new list containing only the names.

Format:
some_variable = [
    {
        "name": "Adrian",
        "favorite_food": "Pizza",
        "favorite_number": 88
    },
    {
        "name": "Jenny",
        "favorite_food": "Sushi",
        "favorite_number": 24
    },
]

In this example, we should get ["Adrian", "Jenny"] as those are the names found.  Make this work for all lists,
so please make up your own examples!
"""
def get_names(input_list):
    all_names = [] # Empty list of names to start
    for this_dictionary in input_list: # Go through each dictionary
        all_names.append(this_dictionary["name"]) # Add the name linked to the dictionary to the list of all names
    return all_names

my_own_list = [
    {
        "name": "Adrian",
        "favorite_food": "Pizza",
        "favorite_number": 88
    },
    {
        "name": "Jenny",
        "favorite_food": "Sushi",
        "favorite_number": 24
    },
]

print(get_names(my_own_list))