
import random

cscore = 0
uscore = 0

def game():
    global clist
    global ulist
    clist = []
    ulist = []
    print("***** Rock Paper Scissor game *****")
    global name
    name = input("Enter your name: ")
    global cscore
    global uscore
    i = 1
    try:
        n = int(input("Enter how namy games you want to play: "))
    except Exception as error:
        print("Invalid choice!")
        game()



    while i<=n:


        try:

            user = int(input(f"1.Rock\n2.Paper\n3.Scissor\n{name} enter your choice: "))
            if user == 1:
                ulist.append("rock")
            elif user ==2:
                ulist.append("paper")
            elif user == 3:
                ulist.append("scissor")
            a = ["rock", "paper", "scissor"]
            computer = random.choice(a)
            clist.append(computer)



        except Exception as erroe:
            print("Invalid choice!")
            continue



        if user == 1 and computer == "rock" or user == 2 and computer == "paper" or user == 3 and computer == "scissor":
            print("Computer choice: ", computer)
            print("It\'s Tie!")

        elif user == 1:
            if computer == "paper":
                print("Computer choice: ", computer)
                print("Computer won!")
                cscore += 1
            else:
                print("Computer choice: ", computer)
                print(f"{name} won!")
                uscore += 1

        elif user == 2:
            if computer == "rock":
                print("Computer choice: ", computer)
                print(f"{name} won!")
                uscore += 1
            else:
                print("Computer choice: ", computer)
                print("Computer won!")
                cscore += 1

        elif user == 3:
            if computer == "rock":
                print("Computer choice: ", computer)
                print("Computer won!")
                cscore += 1
            else:
                print("Computer choice: ", computer)
                print(f"{name} won!")
                uscore += 1

        else:
            print("Invalid choice!")
            continue

        i += 1


    def result():
        print("*****Result*****")
        print(f"Summary of {name}\'s choices: ", ulist)
        print("Summary of computer choices: ",clist)

        print(f"{name} score is: ",uscore)
        print("Computer score is:",cscore)


        if uscore > cscore:
            print(f"{name} won the match!")
        elif uscore < cscore:
            print("Computer won this match!")
        else:
            print("Tie!")
    result()
game()
while True:
    try:
        re = int(input("Enter 1 to continue or 0 to exit: "))
    except Exception as error:
        print("Invalid choice!")
        continue
    if re == 1:
        global clist
        global ulist
        clist.clear()
        ulist.clear()
        uscore = 0
        cscore = 0
        game()
        continue
    elif re == 0:
        print(f"Thank you! {name} for playing this game")
        break
    else:
        print("Invalid choice!")
        continue








