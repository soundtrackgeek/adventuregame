# Define a dictionary for a location
location = {
    "name": "Crime SceneScene",
    "description": """
You stand in a grimy alleyway, rain mixing with the neon glow reflecting from above. The body of a young hacker lies sprawled at your feet, a data chip embedded in their wrist. Thesmell of ramen and blood hangs heavy in theair.
""",
    "exits": {"north": "Ramen Bar"},
}

# Function to handle player movement
def move(direction):
    if direction in location["exits"]:
        # Update currentlocation
        location = get_location(location["exits"][direction])  # Assuming you have a get_location function defined
        print(f"You move {direction}.")
        print_location()
    else:
        print("There is no exit in that direction.")

# Function to print location details
def print_location():
    print(f"\nLocation: {location['name']}")
    print(f"\n{location['description']}")

# Function to examine objects (Modified)
def examine(object):
    if object == "body":
        print("\nThe body is cold and stiff. You notice a data chip embedded in the wrist.")
        print("You can also see a small tattoo on the victim's neck.")
    elif object == "data chip":
        print("\nThe data chip is small and metallic. It seems to be securely embedded in the wrist.")
        print("You'll need the right tools to extract it without damaging the data.")
    elif object == "tattoo":
        print("\nThe tattoo is a stylized symbol, resembling acircuit board.")
        print("You don't recognize it, but it might be a clue to the victim's identityor affiliations.")
    else:
        print("\nYou don't see anything interesting about that.")

# Main gameloop
print_location()  # Print location description at the beginning of the game        

while True:
    action = input("\nWhat do you want to do? (look, go north, examine) ").strip().lower()

    if action == "look":
        print_location()  # Print location only when the player explicitly asks to "look"
    elif action.startswith("go "):
        direction = action.split()[1]
        move(direction)
    elif action.startswith("examine "):
        object = action.split()[1]
        examine(object)  # Only print the object description
    else:
        print("Invalid action.")