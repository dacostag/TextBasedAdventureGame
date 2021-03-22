class Game:
    def __init__(self):
        self.mode = "menu"
        self.database = {}
        self.story = []
        self.choices = []
        with open("story/story.txt") as f:
            text = ""
            for line in f:
                if line != "+\n":
                    text += line
                else:
                    self.story.append(text)
                    text = ""
        with open("story/choices.txt") as f:
            self.choices.extend(f.readlines())
        
    
    def main(self):
        if self.mode == "menu":
            self.main_menu()

    def main_menu(self):
        while True:
            self.print_main_menu()
            selection = input().casefold()
            if selection == "1" or selection == "start":
                print("Starting a new game...")
                username = input("Enter a user name to save your progress or type '/b' to go back ")
                if username == '/b':
                    print("Going back to menu...\n")
                    continue
                else:
                    self.create_new_user(username)
                    print("Good luck on your journey!")
                    print(f"Your character: {self.database[username]['name']}, {self.database[username]['species']}, {self.database[username]['gender']}")
                    print(f"Your inventory: {self.database[username]['snack']}, {self.database[username]['weapon']}, {self.database[username]['tool']}")
                    print(f"Difficulty: {self.database[username]['difficulty']}")
                    print()
                    self.play(username)
            elif selection == "2" or selection == "load":
                print("No save data found!")
            elif selection == "3" or selection == "quit":
                print("Goodbye!")
                raise SystemExit()
            else:
                print("Unknown input! Please enter a valid one.")
                  
    def print_main_menu(self):
        print("***Welcome to the Journey to Mount Qaf***",
        "",
        "1- Press key '1' or type 'start' to start a new game",
        "2- Press key '2' or type 'load' to load your progress",
        "3- Press key '3' or type 'quit' to quit the game",
        sep="\n")

    def create_new_user(self, username):
        self.database[username] = {'name': input("1- Name ").capitalize(), 
                                   'species': input("2- Species ").capitalize(),
                                   'gender': input("3- Gender ").capitalize(),
                                   'snack': input("1- Favourite Snack ").capitalize(),
                                   'weapon': input("2- A weapon for the journey ").capitalize(),
                                   'tool': input("3- A traversal tool ").capitalize(),
                                   'key': False,
                                   'level': 0, 'chapter': 0} 
        while True:
            difficulty = input("Choose your difficulty:\n1- Easy\n2- Medium\n3- Hard\n").casefold()
            if difficulty == '1' or difficulty == 'easy':
                self.database[username]['difficulty'] = 'Easy'
                break
            elif difficulty == '2' or difficulty == 'medium':
                self.database[username]['difficulty'] = 'Medium'
                break
            elif difficulty == '3' or difficulty == 'hard':
                self.database[username]['difficulty'] = 'Hard'
                break
            print("Invalid input.")

    def play(self, username):
        if not self.database[username]['chapter']: # Prints the level title if at chapter 0.
            print(self.story[self.database[username]['level'] * 4])
            self.database[username]['chapter'] += 1
        print(self.story[self.database[username]['level'] * 4 + self.database[username]['chapter']])
        self.make_choice(username)

    def make_choice(self, username):
        print("What will you do? Type the number of the option or type '/h' to show help.")
        print()
        for i in range(3):
            print(f"{i}- {self.choices[self.database[username]['level'] * 9 + (self.database[username]['chapter'] - 1) * 3 + i]}", end="")
        print()
        self.outcome(username)

    # def outcome(self, username):
    #     while True:
    #         selection = input()
    #         if selection == "/i":
    #             print(f"Inventory: {self.database[username]['snack']}, {self.database[username]['weapon']}, {self.database[username]['tool']}")
    #             continue




        



game = Game()
game.main()
