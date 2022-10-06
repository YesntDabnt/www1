from random import randint

t = ["Rock", "Paper", "Scissors"]

computer = t[randint(0,2)]

player = False

while player == False:

    player = input("Rock, Paper, Scissors?")
    if player == computer:
        print("U hacking!!!")
    elif player == "Rock":
        if computer == "Paper":
            print("U suck kiddo", computer, "shoots", player,":P")
        else:
            print("Damn...", player, "explodes", computer,":/")
    elif player == "Paper":
        if computer == "Scissors":
            print("Unlucky bro", computer, "c4s", player ,":P")
        else:
            print("rigged", player, "hacks", computer, "D:")
    elif player == "Scissors":
        if computer == "Rock":
            print("What can I say Im just better", computer, "smashes", player, ":P")
        else:
            print("Pay 2 win", player, "c4s", computer, ">:(")
    else:
        print("That aint gonna happen.",computer, "destroys", player, ":D")
    