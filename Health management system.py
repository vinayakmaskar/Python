
import time


def tim():
    global t
    t =  time.asctime(time.localtime(time.time()))

def Rohan(k):
    global t

    if k == 1:
        try:

            ch = int(input("1.Exercise\n2.Food\nEnter your choice: "))
        except Exception as error:
            print("Invalid choice!")
            return Rohan(k)

        if k == 1:
            data = input("Enter the data in one line: ")
            tim()
            with open("Rohanexercise.txt","a") as re:
                re.write(t+" "+data)
                re.write("\n")
                print("Data added successfully")
        elif k == 2:
            data = input("Enter the data in one line: ")
            tim()
            with open("Rohanfood.txt","a") as rf:
                rf.write(t+" "+data)
                rf.write("\n")
                print("Data added successfully")
        else:
            print("Invalid choice!")
            Rohan(k)

    else:
        try:
            ch = int(input("1.Exercise\n2.Food\nEnter your choice: "))
        except Exception as erro:
            print("Invalid choice!")
            return Rohan(k)
        if ch == 1:
            with open("Rohanexercise.txt") as re:
                print(re.read())
        elif ch == 2:
            with open("Rohanfood.txt") as rf:
                print(rf.read())
        else:
            print("Invalid choice!")
            Rohan(k)

def Harry(k):
    if k ==1:
        try:
            ch = int(input("1.Exercise\n2.Food\nEnter your choice: "))
        except Exception as error:
            print("Invalid choice!")
            return Harry(k)
        if ch == 1:
            data = input("Enter the data: ")
            tim()
            with open("Harryexercise.txt","a") as he:
                he.write(t+" "+data)
                he.write("\n")
                print("Data added successfully")
        elif ch == 2:
            data = input("Enter the data: ")
            tim()
            with open("Harryfood.txt","a") as hf:
                hf.write(t+" "+data)
                hf.write("\n")
                print("Data added successfully")
        else:
            print("Invalid choice!")
            Harry(k)

    else:
        try:
            ch = int(input("1.Exercise\n2.Food\nEnter your choice: "))
        except Exception as error:
            print("Invalid choice!")
            return Harry(k)
        if ch == 1:
            with open("Harryexercise.txt") as he:
                print(he.read())
        elif ch==2:
            with open("Harryfood.txt") as hf:
                print(hf.read())
        else:
            print("Invalid choice")
            Harry(k)


def Hammad(k):
    if k ==1:
        try:
            ch = int(input("1.Exercise\n2.Food\nEnter your choice: "))
        except Exception as error:
            print("Invalid choice!")
            return Hammad(k)
        if ch == 1:
            data = input("Enter the data: ")
            tim()
            with open("Hammadexercise.txt","a") as he:
                he.write(t+" "+data)
                he.write("\n")
                print("Data added successfully")

        elif ch == 2:
            data = input("Enter the data: ")
            tim()
            with open("Hammadfood.txt","a") as hf:
                hf.write(t+" "+data)
                hf.write("\n")
                print("Data added successfully")
        else:
            print("Invalid choice!")
            Hammad(k)

    else:
        try:
            ch = int(input("1.Exercise\n2.Food\nEnter your choice: "))
        except Exception as error:
            print("Invalid choice!")
            return Hammad(k)
        if ch == 1:
            with open("Hammadexercise.txt") as he:
                print(he.read())
        elif ch == 2:
            with open("Hammadfood.txt") as hf:
                print(hf.read())
        else:
            print("Invalid choice!")
            Hammad(k)



while True:

    try:
        user = int(input("1.Rohan\n2.Harry\n3.Hammad\nEnter your choice: "))
        if user != 1 and user !=2 and  user != 3:
            print("Invalid Choice...!")
            continue
    except Exception as error:
        print("Invalid choice!")
        continue

    while True:
        try:
            k = int(input("1.Entering data\n2.See data\nEnter your choice: "))
            if k != 1 and k != 2:
                print("Invalid Choice!")
                continue


        except Exception as error:
            print("Invalid choice!")
            continue

        break


    if user == 1:
        Rohan(k)
    elif user == 2:
        Harry(k)
    elif user == 3:
        Hammad(k)
    else:
        print("Invalid choice!")
        continue

    while True:
        try:

            re = int(input("Enter 1 to continue or any number to exit the system: "))

            break
        except Exception as error:
            print("Invalid choice!")
            continue

    if re == 1:
        continue
    elif re != 0:
        print("Thank you!")
        break

