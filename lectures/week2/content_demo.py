# Class for Content Creators

class Creator: # Names of classes are actually in PascalCase - each word is capitalized; for example: ContentCreator

    # self is effectively going to be a placeholder that holds all the info about the object you are creating
    def __init__(self, first_name, last_name, channel_name, genre, screen_name): 
        self.first_name = first_name
        self.last_name = last_name
        self.channel_name = channel_name
        self.genre = genre
        self.screen_name = screen_name
        self.subscriber_count = 0 # Give everyone a default value of 0 here for subscriber count

    # Instance method - a method tied to a specific class instance (specific object)
    def add_new_subscriber(self): # Don't forget self!
        self.subscriber_count += 1

    # Another instance method
    def rename_channel(self, new_channel_name): # Don't forget self!
        self.channel_name = new_channel_name # Use self inside the method here!

star_wars_fan = Creator("Luke", "Skywalker", "The Star Wars Blog", "Sci-Fi", "l_skywalker")
print(star_wars_fan.first_name) # To refer to attributes in an object, use the period "."

pokemon_fan = Creator("Ash", "Ketchum", "The Ultimate Trainer", "Gaming", "ash_k")
print(pokemon_fan.first_name + " " + pokemon_fan.last_name)

# Calling on methods
star_wars_fan.add_new_subscriber()
print(f"Number of subscribers for the Star Wars fan = {star_wars_fan.subscriber_count}")
print(f"Number of subscribers for the Pokemon fan = {pokemon_fan.subscriber_count}")

# Change the screen name from "ash_k" to "ash" directly
pokemon_fan.screen_name = "ash"

# Change the name of the channel for the Star Wars fan using a method
print("Original channel name: " + star_wars_fan.channel_name)
star_wars_fan.rename_channel("The Galaxy's Protector")
print("New channel name: " + star_wars_fan.channel_name)