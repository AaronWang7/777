while True:
    try:
    
        number = int(input("Enter the number you want multiples of: "))

        print(f"This is your multiples of {number}, from 0 to 12:")
        for i in range(1,13,1):
            print(f"{number} x {i} = {number * i}")
    except ValueError:
        print("Error: Please enter a valid number, example : 1,2,3,4,5,6,7,8,9,10,11,12.")
        print("Now try again!")

