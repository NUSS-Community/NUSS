import os
import time
import random

s = 0 
ver = "v1.2"
mode = "Classic"

def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system('clear')

def sleeping():
    global s
    while True:
        clear()
        s += 1
        print("Sleeping...")
        print(f"You have slept for {s} seconds.")
        time.sleep(1)

def about():
    clear()
    print("New Ultimate Sleeping Simulator " + ver)
    print("Made by wave230")
    print("\nThe goal of the game:\n\nThe goal of the game is to sleep the longest you can. You can then share your highscore with your friends.")
    input("\nPress ENTER to continue")
    main()

def changelog():
    clear()
    print("Changelog:\n")
    print("v1.2\nAdded Tutorial\nAdded a new 10000 seconds mode as well as the ability to change between gamemodes\n")
    print("v1.1\nAdded about menu\nAdded changelog")
    input("\nPress ENTER to continue")
    main()

def tutorial():
    clear()
    print("Sleep.")
    input("\nPress ENTER to continue")

def modechanger():
    global mode
    while True:
        clear()
        print("Selected mode:\n" + mode)
        print("\nAvailable modes:\n1. Classic\n2. 10000 seconds")
        print("\nType 'exit' to exit.\n")
        inp = input("[1,2]>> ")
        if inp == "1":
            mode = "Classic"
        elif inp == "2":
            mode = "10000 seconds"
        elif inp == "exit":
            break

def tenksw():
    clear()
    print("You've beaten 10000 seconds mode! Good job!")
    input("\nPress ENTER to continue")

def tenks():
    global s
    clear()
    print("In 10000 seconds mode you have to sleep for 10000 seconds straight without waking up. Good luck!")
    input("\nPress ENTER to continue")
    while True:
        clear()
        s+=1
        print("Sleeping...")
        print(f"You have slept for {s} seconds")
        print(f"{10000-s} left")
        if s>=10000:
            tenksw()
            break
        time.sleep(1)

def main():
    while True:
        clear()
        print(f"New Ultimate Sleeping Simulator " + ver)
        print("Made by wave230")
        print("\n1. Start\n2. Change mode\n3. About\n4. Changelog\n5. Tutorial")
        inp = input("\n[1,2,3,4,5]>> ")
        if inp == "1" and mode == "Classic":
             sleeping()
        elif inp == "1" and mode == "10000 seconds":
             tenks()
        elif inp == "2":
            modechanger()
        elif inp == "3":
            about()
        elif inp == "4":
            changelog()
        elif inp == "5":
            tutorial()

main()
