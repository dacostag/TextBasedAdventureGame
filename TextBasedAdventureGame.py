def print_mainmenu():
    print("***Welcome to the Journey to Mount Qaf***",
    "",
    "1- Press key '1' or type 'start' to start a new game",
    "2- Press key '2' or type 'load' to load your progress",
    "3- Press key '3' or type 'quit' to quit the game",
    sep="\n")


while True:
    print_mainmenu()
    selection = input()
    if selection == "1" or selection == "start":
        print("Starting a new game...")
    elif selection == "2" or selection == "load":
        print("No save data found!")
    elif selection == "3" or selection == "quit":
        print("Goodbye!")
        break
    else:
        print("Unknown input! Please enter a valid one.")
