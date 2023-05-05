# Function demo

def generic_message():
    print("Hello there!")
    # pass # Placeholder that will eventually hold code for this function

generic_message() # Run the function in question

# Finding the maximum value in a list
def find_max_value(input_list): # Function takes in a parameter called "input_list"
    # print(input_list)
    cur_max_value = input_list[0] # Hold the actual maximum value - start with the first value in the list
    # for index in range(0,len(input_list)):
    for val in input_list: # val = the value directly (NOT the index) in the list
        # print(val) # Just to show the current value
        if val > cur_max_value: # If the current value in the list is bigger than the maximum
            cur_max_value = val # Taking the current value in the list and making it the new maximum
    return cur_max_value


list_of_values = [8, 2, 10, 4, -3, -12, 7]
found_max = find_max_value(list_of_values) # Taking the result from the function and storing in a variable for future use
print(found_max)

second_list = [3, 1, 4]
print(find_max_value(second_list))

# Dictionaries
capitals = {
    "Washington": 'Olympia',
    "United Kingdom": "London",
    "India": "New Delhi"
}

print(capitals["India"])

capitals["Washington"] = "Seattle"
print(capitals)

capitals["California"] = "Sacramento"
print(capitals)

if "California" in capitals:
    print("Capital found for California")
else:
    print("No capital linked to California")

some_state = "Washington" # Feel free to change this

if some_state in capitals:
    print(f"{some_state} has a capital linked")
else:
    print(f"{some_state} not found in capitals")

# Print all the key-value pairs
for location in capitals:
    print(f"The capital of {location} is {capitals[location]}")

""" From Functions Basic II - problem 5:
This Length, That Value - Write a function that accepts two integers as parameters: size and value. 
The function should create and return a list whose length is equal to the given size, 
and whose values are all the given value.
Example: length_and_value(4,7) should return [7,7,7,7]
Example: length_and_value(6,2) should return [2,2,2,2,2,2]
"""

def replicate_value(size_of_list, value_to_insert):
    new_list = [] # Empty list that will hold a bunch of values eventually
    for this_value in range(size_of_list): # Loop to add the value to the new list as many times as needed based on what the size of the new list will be
        new_list.append(value_to_insert)
        # print(new_list)
    return new_list

print(replicate_value(4,7))
print(replicate_value(6,2))
print(replicate_value(8,3))
