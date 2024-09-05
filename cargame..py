command = ""

while True:
    command = input("> ").lower()
    if command == "start":
        print("Car has started...")
    elif command == "stop":
        print("Car has stopped...")
    elif command == "help":
        print("""
              Commands to play the game
              start
              stop
              help
              quit
              """)
    elif command == "quit":
        break
    else:
        print("Sorry, I do not understand the word ")