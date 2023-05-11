class Pokemon:
    def __init__(self, species_name, nickname, current_HP, current_atk, current_def, base_HP, base_atk, base_def, moves):
        # Various attributes: is it evolved? Types? Is it shiny?  Legendary?  Name of the species?  Nickname?
        # Stats - HP, level, experience, Atk, Special Atk, Spd, Def and Special Def
        # Moves
        # Nature
        # Ability
        self.species_name = species_name
        self.nickname = nickname
        self.current_HP = current_HP
        self.current_atk = current_atk
        self.current_def = current_def
        self.base_HP = base_HP
        self.base_atk = base_atk
        self.base_def = base_def
        self.moves = moves # List of dictionaries that hold moves

    def pick_move(self, move_to_use, pokemon_foe): # move_to_use = name of move as a string, pokemon_foe = Pokemon object
        # Search for the move
        for current_move in self.moves: # Need "self."
            print(current_move)
            if current_move["name"] == move_to_use:
                print(f"{self.nickname} is using {move_to_use} against {pokemon_foe.nickname}")
                # Calculate the damage (using a made-up formula)
                damage = current_move["attack_power"] - (pokemon_foe.current_def / 3)
                # Deduct the damage from the foe's current HP
                pokemon_foe.current_HP -= damage
                print(f"{pokemon_foe.current_HP} HP left out of {pokemon_foe.base_HP} for {pokemon_foe.nickname}")

# Create some Pokemon
dragonite_moveset = [
    { # There are other attributes for moves we could use, like accuracy, move type, stat modifiers, etc.
        "name": "Quick Attack",
        "max_uses": 35,
        "uses_left": 35,
        "attack_power": 40
    },
    {
        "name": "Draco Meteor",
        "max_uses": 5,
        "uses_left": 5,
        "attack_power": 130
    },
    {
        "name": "Fire Punch",
        "max_uses": 15,
        "uses_left": 15,
        "attack_power": 75
    },
    {
        "name": "Thunder Punch",
        "max_uses": 15,
        "uses_left": 15,
        "attack_power": 75
    }
]
dragonite = Pokemon("Dragonite", "Dragonite", 91, 134, 95, 91, 134, 95, dragonite_moveset)
print(dragonite.base_HP) # Display the base HP for Dragonite

lugia_moveset = [
    { # There are other attributes for moves we could use, like accuracy, move type, stat modifiers, etc.
        "name": "Aeroblast",
        "max_uses": 5,
        "uses_left": 5,
        "attack_power": 100
    },
    {
        "name": "Future Sight",
        "max_uses": 10,
        "uses_left": 10,
        "attack_power": 120
    },
    {
        "name": "Hydro Pump",
        "max_uses": 5,
        "uses_left": 5,
        "attack_power": 110
    },
    {
        "name": "Ancient Power",
        "max_uses": 5,
        "uses_left": 5,
        "attack_power": 60
    }
]
lugia = Pokemon("Lugia", "Lugia", 106, 90, 150, 106, 90, 150, lugia_moveset)

dragonite.pick_move("Thunder Punch", lugia)
lugia.pick_move("Hydro Pump", dragonite)