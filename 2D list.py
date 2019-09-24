win1 = 0
win2 = 0
count = 0
answers = ["rock", "paper", "scissors"]
print("This is a game of Rock,Paper Scissors! WInner is determined in bo5 match!")
print("Draws and typos are not included in the count!")
player1 = input("Enter your name: ")
player2 = input("Enter your name: ")
while count < 5:
    pick1 = input(player1 + ", make your pick:")
    pick2 = input(player2 + ", make your pick:")
    if pick1 and pick2 in answers:
        if pick1 == "rock" and pick2 == "scissors":
            win1 = win1 + 1
            count = count + 1
            print(str(player1) + " is our winner. The score is: " + str(win1) + " VS " + str(win2))
        elif pick1 == "paper" and pick2 == "rock":
            win1 = win1 + 1
            count = count + 1
            print(str(player1) + " is our winner. The score is: " + str(win1) + " VS " + str(win2))
        elif pick1 == "scissors" and pick2 == "paper":
            win1 = win1 + 1
            count = count + 1
            print(str(player1) + " is our winner. The score is: " + str(win1) + " VS " + str(win2))
        elif pick2 == "rock" and pick1 == "scissors":
            win2 = win2 + 1
            count = count + 1
            print(str(player2) + " is our winner. The score is: " + str(win1) + " VS " + str(win2))
        elif pick2 == "paper" and pick1 == "rock":
            win2 = win2 + 1
            count = count + 1
            print(str(player2) + " is our winner. The score is: " + str(win1) + " VS " + str(win2))
        elif pick2 == "scissors" and pick1 == "paper":
            win2 = win2 + 1
            count = count + 1
            print(str(player1) + " is our winner. The score is: " + str(win1) + " VS " + str(win2))
        elif pick1 == pick2:
            print("We got a draw!")
    else:
        print("Are u sure there are no typos?")
if win1 > win2:
    print("Congratulations, " + str(player1))
else:
    print("Congratulations, " + str(player2))




