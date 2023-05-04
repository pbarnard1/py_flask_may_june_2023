""" (this is actually a docstring technically to allow you to comment across multiple lines)
Demo of lists
"""

# Lists are basically like arrays in JavaScript
my_list = ["Adrian", True, 10, "happy"]
print(my_list[2])
# Replace "Adrian" with "Thomas"
my_list[0] = "Thomas"
print(my_list)
# Add "Adrian" to the end of the list
my_list.append("Adrian")
print(my_list)

# Tuple - like a list, but can't change its values when you define items with this data type

my_tuple = (3, 10, 12) # Note the parentheses
print(my_tuple[0])

# my_tuple.append(15) # ILLEGAL - you can't change any values in a tuple

"""
If statements:

# Example with pseudocode
if you're sleepy still after waking up:
    Sleep in
else:
    Get out of bed
    Take shower
    Eat breakfast
"""

x = 10
if x >= 9: # ":" is the colon symbol, ";" is the semicolon symbol
    print("Great job!!") # MAKE SURE you indent every line necessary with the if block
    print("You got at least a 9!") # WARNING: Watch your indentation!!
elif x >= 7: # elif = "else if" in JavaScript - only runs if the "if" statement is false from before
    print("Good job!")
    print("You got at least a 7!")
else: # Notice how this is indented to the left on the same level as the "if" statement, denoting the end of the previous block
    print("Good effort!")
print("Outside the if block") # Always runs after the if block is finished

for val in range(10): # With the range function, we start at 0 by default
    # range(10) -> 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 - NO 10
    print(val)

for val2 in range(3, 10): # Start at a different value - in this case, 3, and continues through 9 (not including 10)
    print(val2)

for val3 in range(5, 22, 4): # Start at 5, stop before 22, go up by 4 each time
    print(val3) # 5, 9, 13, 17, 21

for val4 in range(30, -1, -1): # Going backwards
    print(val4)

# Go through each value in the list called my_list
for value in my_list:
    print(value)

# Another way to loop:
for ind in range(len(my_list)): # len(x) returns the number of items in x; ind is an index = 0, 1, 2, ...
    print(ind) # Print the numerical index
    print(my_list[ind]) # Grabbing value from the list at the specified index