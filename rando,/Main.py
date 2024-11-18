import random
money = 20
while True:
    III = input("How much money you want to use?, 10 for a small one, 20 for a bigger one,10000 for the biggest one:")

    if III == 10:
   
            num = (random.randrange(-20000,20000))
            money = money + num
    elif III == 20:
     
             num = (random.randrange(-200000,210000))
             money = money + num
    else:

            num = (random.randrange(-2000000,2000000))*10
            money = money + num


    if num >= 0:
            print ("You win",num,"$")
    else:
            print("Oh no you lose",num,"$")
            print ("You have",money,"$","in you bank")