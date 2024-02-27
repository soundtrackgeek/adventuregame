# Define a dictionary for a location
location = {
    "name": "Crime Scene",
    "description": """
You stand in a grimy alleyway, rain mixing with the neon glow reflecting from above. 
The body of a young hacker lies sprawled at your feet, a data chip embedded in their wrist. 
The smell of ramen and blood hangs heavy in the air.
""",
    "exits": {"north": "Ramen Bar"},
}

# Function to handle player movement
def move(direction):
    if direction in location["exits"]:
        # Update current location
        location = get_location(location["exits"][direction])  # Assuming you have a get_location function defined
        print(f"You move {direction}.")
        print_location()
    else:
        print("There is no exit in that direction.")

# Function to print location details
def print_location():
    print(f"\nLocation: {location['name']}")
    print(f"\n{location['description']}")

# Function to examine objects (Modified to handle spaces)
def examine(object):
    object = object.strip()  # Remove leading and trailing spaces

    if object == "body":
        print("\nThe body is cold and stiff. You notice a data chip embedded in the wrist.")
        print("You can also see a small tattoo on the victim's neck.")
    elif object == "data chip":
        print("\nThe data chip is small and metallic. It seems to be securely embedded in the wrist.")
        print("You'll need the right tools to extract it without damaging the data.")
    elif object == "tattoo":
        print("\nThe tattoo is a stylized symbol, resembling a circuit board.")
        print("You don't recognize it, but it might be a clue to the victim's identity or affiliations.")
    else:
        print("\nYou don't see anything interesting about that.")

# Main game loop
print_location()  # Print location description at the beginning of the game

while True:
    action = input("\nWhat do you want to do? (look, go north, examine) ").strip().lower()

    if action == "look":
        print_location()
    elif action.startswith("go "):
        direction = action.split()[1]
        move(direction)
    elif action.startswith("examine "):
        # Choose either Solution 1 or Solution 2:

        # Solution 1: Capture the entire object name
        object = action.split(" ", 1)[1]  

        # Solution 2: Use the "in" operator (modify the examine function as shown above)
        # object = action.split()[1]  # Keep this line if using Solution 2

        examine(object)
    else:
        print("Invalid action.")