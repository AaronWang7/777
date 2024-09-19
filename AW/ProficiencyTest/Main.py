
player1 =  int(input("What's 1 + 1?"))
player2 =  int(input("What's 2 + 1?"))
player3 =  int(input("What's 8 + 1?"))
player4 =  int(input("What's 1 + 99?"))
player5 =  int(input("What's 1 + 11?"))

if player1 == 2:
     player1 = 1
else :
    player1 = 0

if player2 == 3:
   player2 = 1
else :
     player2 = 0


if player3 == 9:
      player3 = 1
else :
     player3 = 0

if player4 == 100:
      player4 = 1
else :
     player4 = 0

if player5 == 12:
      player5 = 1
else :
     player5 = 0

if player1+player2+player3+player4+player5 == 5:

    print("You got 100%!!!, your score is:",player1+player2+player3+player4+player5)
else:
     print("Keep trying!!!, you got:",player1+player2+player3+player4+player5)
print("The highest score you can get is 5!")