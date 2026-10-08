import random

choices = ['s', 'w', 'g']

user_score = 0
comp_score = 0

rounds = int(input("How many rounds do you want to play? "))

for i in range(rounds):
    # Print round number using comma
    print("\n--- Round", i + 1, "---")
    
    user = input("Enter 's' (Snake), 'w' (Water), or 'g' (Gun): ")
    comp = random.choice(choices)
    
    print("Computer chose:", comp)

    # Tie
    if user == comp:
        print("It's a tie!")

    # You win conditions
    elif user == 's' and comp == 'w':
        print("You win! Snake drinks Water.")
        user_score = user_score + 1

    elif user == 'w' and comp == 'g':
        print("You win! Water drowns Gun.")
        user_score = user_score + 1

    elif user == 'g' and comp == 's':
        print("You win! Gun kills Snake.")
        user_score = user_score + 1

    # Computer wins
    else:
        print("Computer wins this round!")
        comp_score = comp_score + 1

# Final Scores
print("\n=== FINAL RESULT ===")
print("Your Score:", user_score)
print("Computer Score:", comp_score)

if user_score > comp_score:
    print("You won the game!")
elif comp_score > user_score:
    print("Computer won the game!")
else:
    print("It's a draw!")