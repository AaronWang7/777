num = (input ("Enter your first number:"))
num2 = (input("Enter your 2nd number:"))
op = (input("What whould you like to do with it?, 1 = add, 2 = subtract, 3 = multiplication, 4 = multiplication:"))

if op == "1":
    try:
        number = int(num + num2)
        print(number)
    except:
        print("Wrong input")
elif op == "2":
    try:
        number = int(num - num2)
        print(number)
    except:
        print("Wrong input")
elif op == "3":
    try:
        number = int(num * num2)
        print(number)
    except:
        print("Wrong input")
elif op == "4":
    try:
        number = int(num / num2)
        print(number)
    except:
        print("Wrong input")
