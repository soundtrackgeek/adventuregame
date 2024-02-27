# Define a dictionary for a location
location = {
    "name": "Crime Scene",
    "description": """
You stand in a grimy alleyway, rain mixing with the neon glow reflecting from above. The body of a young hacker lies sprawled at your feet, a data chip embedded in their wrist. The smell of ramen and blood hangs heavy in the air.
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

# Function to examine objects (added in the previous response)
def examine(object):
    if object == "body":
        print("The body is cold and stiff. You notice a data chip embedded in the wrist.")
        print("You can also see a small tattoo on the victim's neck.")
    elif object == "data chip":
        print("The data chip is small and metallic. It seems to be securely embedded in the wrist.")
        print("You'll need the right tools to extract it without damaging the data.")
    elif object == "tattoo":
        print("The tattoo is a stylized symbol, resembling a circuit board.")
        print("You don't recognize it, but it might be a clue to the victim's identity or affiliations.")
    else:
        print("You don't see anything interesting about that.")

# Main game loop
while True:
    print_location()  # Now the function is defined
    action = input("\nWhat do you want to do? (look, go north, examine) ").strip().lower()

    if action == "look":
        print_location()
    elif action.startswith("go "):
        direction = action.split()[1]
        move(direction)
    elif action.startswith("examine "):
        object = action.split()[1]
        examine(object)
    else:
        print("Invalid action.")