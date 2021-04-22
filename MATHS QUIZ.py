
import  random


ascore = 0
sscore = 0
mscore = 0
dscore = 0




def Add():
    try:
        print("Enter the range you want!")
        low = int(input("Enter the lowest number: "))
        high = int(input("Enter the highest number: "))
        a = random.randint(low, high)
        b = random.randint(low, high)
        c = random.randint(low, high)
        d = random.randint(low, high)
        e = random.randint(low, high)
        f = random.randint(low, high)

    except Exception as error:
        print("Please enter correct values!")
        return Add()

    def answer(one,two):
        try:
            print(one,"+",two,"=")
            ans = int(input("Ans: "))

        except Exception as error:
            print("Please enter integer values!")
            return answer(one,two)

        if ans == one+two:
            print("Correct ans!")
            global ascore
            ascore += 1

        else:
            print("Wrong ans!")
            print("Correct ans is",one+two)

    answer(a,b)
    answer(c,d)
    answer(e,f)

    print("Your score in Addition is",ascore)

def Sub():
    try:
        print("Enter the range you want!")
        low = int(input("Enter the lowest number: "))
        high = int(input("Enter the highest number: "))
        a = random.randint(low, high)
        b = random.randint(low, high)
        c = random.randint(low, high)
        d = random.randint(low, high)
        e = random.randint(low, high)
        f = random.randint(low, high)

    except Exception as error:
        print("Please enter correct values!")
        return Sub()

    def answer(one,two):
        try:
            print(one,"-",two,"=")
            ans = int(input("Ans: "))

        except Exception as error:
            print("Please enter integer values!")
            return answer(one,two)

        if ans == one-two:
            print("Correct ans!")
            global sscore
            sscore += 1

        else:
            print("Wrong ans!")
            print("Correct ans is",one-two)

    answer(a,b)
    answer(c,d)
    answer(e,f)

    print("Your score in Subtraction is",sscore)

def Mul():
    try:
        print("Enter the range you want!")
        low = int(input("Enter the lowest number: "))
        high = int(input("Enter the highest number: "))
        a = random.randint(low, high)
        b = random.randint(low, high)
        c = random.randint(low, high)
        d = random.randint(low, high)
        e = random.randint(low, high)
        f = random.randint(low, high)

    except Exception as error:
        print("Please enter correct values!")
        return Mul()

    def answer(one, two):
        try:
            print(one, "*", two, "=")
            ans = int(input("Ans: "))

        except Exception as error:
            print("Please enter integer values!")
            return answer(one, two)

        if ans == one * two:
            print("Correct ans!")
            global mscore
            mscore += 1

        else:
            print("Wrong ans!")
            print("Correct ans is", one * two)

    answer(a, b)
    answer(c, d)
    answer(e, f)

    print("Your score in Subtraction is", mscore)

def Div():
    try:
        print("Enter the range you want!")
        low = int(input("Enter the lowest number: "))
        high = int(input("Enter the highest number: "))
        a = random.randint(low, high)
        b = random.randint(low, high)
        c = random.randint(low, high)
        d = random.randint(low, high)
        e = random.randint(low, high)
        f = random.randint(low, high)

    except Exception as error:
        print("Please enter correct values!")
        return Div()

    def answer(one, two):
        try:
            print(one, "/", two, "=")
            ans = int(input("Ans: "))

        except Exception as error:
            print("Please enter integer values!")
            return answer(one, two)

        if ans == one /two:
            print("Correct ans!")
            global dscore
            dscore += 1

        else:
            print("Wrong ans!")
            print("Correct ans is", one / two)

    answer(a, b)
    answer(c, d)
    answer(e, f)


    print("Your score in Subtraction is", dscore)

def menu():

    try:
        user = int(input("1.Addition\n2.Subtraction.\n3.MUltiplication.\n4.Division.\nChoose the option according to the number: "))

    except Exception as error:
        print("Invalid choice! Please enter a correct choice")
        return menu()

    if user == 1:
        global ascore
        ascore = 0
        Add()
    elif user == 2:
        global sscore
        sscore = 0
        Sub()
    elif user == 3:
        global mscore
        mscore = 0
        Mul()
    elif user==4:

        global dscore
        dscore = 0
        Div()
    else:
        print("Invalid choice!")
        menu()

    def res():

        try:
            re = int(input("Enter 1 to restart or any number to exit the game!"))

        except Exception as error:
            print("Invalid choice!")
            return res()


        if re == 1:
            return menu()
        else:
            print("Thank you!")
    res()

menu()

