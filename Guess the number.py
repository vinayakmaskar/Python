
import random
def ran():
    print("Enter the range you want!")
    a = int(input("Enter the lowest number you want: "))
    b  = int(input("Enter the highest number you want: "))
    return random.randint(a,b)

guess = 1
num = ran()


while True:
    if guess<=5:
        user = int(input("Enter a number: "))

        if user<num:
            print("Please enter a greater number!")
            guess = guess+ 1
            continue
        elif user>num:
            print("Please enter a smaller number!")
            guess += 1
            continue
        else:
            print("Congrats! You have won the game!")
            print("You took",guess,"chances to guess the game")
            re = int(input("Enter 1 to continue or 0 to exit: "))
            if re == 1:
                num = ran()
                guess = 1
                continue
            else:
                break

    else:
        print("Sorry! You have lost the game!")
        print("Correct number was",num)

        re = int(input("Enter 1 to continue or 0 to exit: "))
        if re == 1:
            num = ran()
            guess = 1
            continue
        else:
            break
