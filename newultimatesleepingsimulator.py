import os
import time
import json

class SleepingSimulator:
    def __init__(self):
        self.s = 0
        self.ver = "v1.3.1"
        self.mode = "Classic"
        self.high_scores = self.load_high_scores()
        self.running = False

    def clear(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def load_high_scores(self):
        try:
            with open('high_scores.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return {"Classic": 0, "10000 seconds": 0}

    def save_high_scores(self):
        with open('high_scores.json', 'w') as f:
            json.dump(self.high_scores, f)

    def update_high_score(self):
        if self.s > self.high_scores[self.mode]:
            self.high_scores[self.mode] = self.s
            self.save_high_scores()
            print(f"New high score for {self.mode} mode: {self.s} seconds!")
        else:
            print(f"Your score: {self.s} seconds")
            print(f"High score for {self.mode} mode: {self.high_scores[self.mode]} seconds")

    def sleeping(self):
        self.s = 0
        self.running = True
        while self.running:
            self.clear()
            self.s += 1
            print("Sleeping...")
            print(f"You have slept for {self.s} seconds.")
            time.sleep(1)
        
        self.update_high_score()
        input("\nPress ENTER to continue")

    def about(self):
        self.clear()
        print(f"New Ultimate Sleeping Simulator {self.ver}")
        print("Made by wave230")
        print("\nThe goal of the game:\n\nThe goal of the game is to sleep the longest you can. You can then share your highscore with your friends.")
        input("\nPress ENTER to continue")

    def changelog(self):
        self.clear()
        print("Changelog:\n")
        print("v1.3.1\nFixed high score functionality")
        print("v1.3\nOptimized code\nAdded high score system\nImproved game mode changing\nEnhanced security")
        print("v1.2\nAdded Tutorial\nAdded a new 10000 seconds mode as well as the ability to change between gamemodes")
        print("v1.1\nAdded about menu\nAdded changelog")
        input("\nPress ENTER to continue")

    def tutorial(self):
        self.clear()
        print("Sleep as long as you can. Press Ctrl+C to wake up.")
        input("\nPress ENTER to continue")

    def modechanger(self):
        while True:
            self.clear()
            print(f"Selected mode: {self.mode}")
            print("\nAvailable modes:\n1. Classic\n2. 10000 seconds")
            print("\nType 'exit' to exit.\n")
            inp = input("[1,2]>> ")
            if inp == "1":
                self.mode = "Classic"
            elif inp == "2":
                self.mode = "10000 seconds"
            elif inp.lower() == "exit":
                break

    def tenks(self):
        self.s = 0
        self.clear()
        print("In 10000 seconds mode you have to sleep for 10000 seconds straight without waking up. Good luck!")
        input("\nPress ENTER to continue")
        
        self.running = True
        while self.running and self.s < 10000:
            self.clear()
            self.s += 1
            print("Sleeping...")
            print(f"You have slept for {self.s} seconds")
            print(f"{10000 - self.s} left")
            time.sleep(1)

        if self.s >= 10000:
            self.clear()
            print("You've beaten 10000 seconds mode! Good job!")
        
        self.update_high_score()
        input("\nPress ENTER to continue")

    def show_high_scores(self):
        self.clear()
        print("High Scores:")
        for mode, score in self.high_scores.items():
            print(f"{mode}: {score} seconds")
        input("\nPress ENTER to continue")

    def main(self):
        while True:
            self.clear()
            print(f"Ultimate Sleeping Simulator {self.ver}")
            print("Made by wave230")
            print(f"\nCurrent mode: {self.mode}")
            print("\n1. Start\n2. Change mode\n3. About\n4. Changelog\n5. Tutorial\n6. High Scores\n7. Exit")
            inp = input("\n[1-7]>> ")
            if inp == "1":
                if self.mode == "Classic":
                    try:
                        self.sleeping()
                    except KeyboardInterrupt:
                        self.running = False
                        print("\nYou woke up!")
                        self.update_high_score()
                elif self.mode == "10000 seconds":
                    try:
                        self.tenks()
                    except KeyboardInterrupt:
                        self.running = False
                        print("\nYou woke up!")
                        self.update_high_score()
            elif inp == "2":
                self.modechanger()
            elif inp == "3":
                self.about()
            elif inp == "4":
                self.changelog()
            elif inp == "5":
                self.tutorial()
            elif inp == "6":
                self.show_high_scores()
            elif inp == "7":
                print("Thanks for playing!")
                break

if __name__ == "__main__":
    game = SleepingSimulator()
    game.main()
