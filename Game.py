import random
print("Welcome to ROCK-PAPER-SCISSORS-SPOCK-LIZZARD GAME!")
print("1-Rock")
print("2-Paper")
print("3-Scissors")
print("4-Spock")
print("5-Lizzard1")
answer = 1;

while answer == 1:
    choice = int(input("What do you chose? [number]"))
    opponent = random.randint(1,5)
    print(choice,opponent)
    if choice == opponent:
        print("We have a draw!")
    if choice == 1 and (opponent == 3 or opponent == 5):
        print ("You win!")
    elif choice == 2 and (opponent == 1 or opponent == 4):
        print ("You win!")
    elif choice == 3 and (opponent == 2 or opponent == 5):
        print ("You win!")
    elif choice == 4 and (opponent == 3 or opponent == 1):
        print ("You win!")
    elif choice == 5 and (opponent == 4 or opponent == 2):
        print ("You win!")
    else:
        print("You lost!")
    answer = int(input("Want to play again?[1 - Yes/ 0 - No]"))