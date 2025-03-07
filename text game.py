answer_yes = ["Yes", "Y", "yes", "y"]
answer_no = ["No", "N", "no", "n"]

print("WELCOME! LET'S START THE ADVENTURE")
print("You are standing outside your house, and a man is running towards you, asking for urgent shelter.")
print("Will you provide shelter to him? (Yes / No)")

ans1 = input(">> ")

if ans1 in answer_yes:
    print("\nAfter 2 minutes, the police arrive at your doorstep and inquire if the man is a thief. Will you confess? (Yes / No)\n")
    ans2 = input(">> ")
    if ans2 in answer_yes:
        print("\nYour honesty pays off! He was indeed a thief, and you win the game!")
    elif ans2 in answer_no:
        print("\nYou aided a criminal. Your game ends here.")
else:
    print("\nThe man lunges at you. Do you fight back? (Yes / No)\n")
    ans3 = input(">> ")
    if ans3 in answer_yes:
        print("\nYou overpower him and emerge victorious! You win the game!")
    else:
        print("\nTragically, he overpowers you. You lose the game.")
