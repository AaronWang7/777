op = str(input("Which one do you want?, addition, subtraction, multiplication, division: "))

number1 = int(input("Your first number: "))
number2 = int(input("Your 2nd number: "))



if op == "adition":
    print (number1,"+",number2,'=', number1 + number2)
if op == "subtraction":
        print (number1,"-",number2,'=', number1 - number2)
if op == "multiplication":
      print (number1,"x",number2,'=', number1 * number2)
if op == "division":
      print (number1,"/",number2,'=', number1 / number2)

if not op ==  "addition" or "subtraction" or "multiplication" or "division":
          print(op,"is not one of the options")
else:
      print (op,"is one of the options")




