# Define a dictionary for a location
location = {
    "name": "Starting Room",
    "description": "You are in a dark room. There is a door to the north.",
    "exits": {"north": "Next Room"},
}

# Function to handle player movement
def move(direction):
    if direction in location["exits"]:
        # Update current location
        location = get_location(location["exits"][direction])
        print(f"You move {direction}.")
        print_location()
    else:
        print("There is no exit in that direction.")

# Function to print location details
def print_location():
    print(f"\nLocation: {location['name']}")
    print(f"\n{location['description']}")

# Main game loop
while True:
    print_location()
    action = input("\nWhat do you want to do? (look, go north, etc.) ").strip().lower()
    
    if action == "look":
        print_location()
    elif action.startswith("go "):
        direction = action.split()[1]
        move(direction)
    else:
        print("Invalid action.")