# Define the starting location
location = {
    "name": "Crime Scene",
    "description": """
You stand in a grimy alleyway, rain mixing with the neon glow reflecting from above. sThe body of a young hacker lies sprawled at your feet, a data chip embedded in their wrist. The smell of ramen and blood hangs heavy in the air.
""",
    "exits": {"north": "Ramen Bar"},
}

# Add a function to examine objects
def examine(object):
    if object == "body":
        print("The body is cold and stiff. You notice a data chip embedded in the wrist.")
    else:
        print("You don'.t see anything interesting about that.")

# Update the game loop to handle "examine" action
while True:
     print_location()
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