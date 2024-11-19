while True:
       import random
       player = input("Enter one of the numbers, 1 = rock, 2 = paper, 3 = scissors:")
       ai = (random.randrange(0,60))
       if ai <= 20:
              aii = ("rock")
       elif ai <= 40:
              aii = ("paper")
       elif ai <= 60:
              aii = ("scissors")
       if player == "1" and aii == "rock":
              print(f"tie, you both used ,{aii}")
       elif player == "1" and aii == ("paper"):
              print(f"Oh no you lost,you used,{player},and ai used,{aii}")
       elif player == "1" and aii == ("scissors"):
              print(f"You won!,you used,{player},and ai used,{aii}")

       if player == "2" and aii == "rock":
              print(f"You won!, you used ,{player}, ai used ,{aii}")
       elif player == "2" and aii == ("paper"):
              print(f"tie you both used {player}")
       elif player == "2" and aii == ("scissors"):
              print(f"Oh no you lost,you used,{player},and ai used,{aii}")

       elif player == "3" and aii == "rock":
              print(f"Oh no you lost,you used,{player},and ai used,{aii}")
       elif player == "3" and aii == ("paper"):
              print(f"You won!,you used,{player},and ai used,{aii}")
       elif player == "3" and aii == ("scissors"):
              print(f"tie, you both used ,{aii}")

