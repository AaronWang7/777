try:
 
    number = int(input("Enter the number you want multiples of: "))

    print(f"Multiples of {number} from 0 to 12:")
    for i in range(1,13,1):
        print(f"{number} x {i} = {number * i}")
except ValueError:
    print("Error: Please enter a valid number.")

