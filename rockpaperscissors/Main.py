op =["1","2","3"]
score = []
aiscore = []
while True:
       import random
       player = input("Enter one of the numbers, 1 = rock, 2 = paper, 3 = scissors:")
       if player not in op:
              print("Enter 1,2, or 3!")
              break
       else:
              ai = (random.randrange(0,60))
       if ai <= 20:
              aii = ("rock")
       elif ai <= 40:
              aii = ("paper")
       elif ai <= 60:
              aii = ("scissors")
       if player == "1" and aii == "rock":
              print(f"tie, you both used ,{aii}")
              print("This is your score, each'I'= 1 point",score)
              print("  This is ai score, each'I'= 1 point",aiscore)
              
       elif player == "1" and aii == ("paper"):
              print(f"Oh no you lost,you used,{player},and ai used,{aii}")
              aiscore.append("I")
              print("This is your score, each'I'= 1 point",score)
              print("  This is ai score, each'I'= 1 point",aiscore)
       elif player == "1" and aii == ("scissors"):
              print(f"You won!,you used,{player},and ai used,{aii}")
              score.append("I")
              print("This is your score, each'I'= 1 point",score)
              print("  This is ai score, each'I'= 1 point",aiscore)
       if player == "2" and aii == "rock":
              print(f"You won!, you used ,{player}, ai used ,{aii}")
              score.append("I")
              print("This is your score, each'I'= 1 point",score)
              print("  This is ai score, each'I'= 1 point",aiscore)
       elif player == "2" and aii == ("paper"):
              print(f"tie you both used {aii}")
              print("This is your score, each'I'= 1 point",score)
              print("  This is ai score, each'I'= 1 point",aiscore)
       elif player == "2" and aii == ("scissors"):
              print(f"Oh no you lost,you used,{player},and ai used,{aii}")
              aiscore.append("I")
              print("This is your score, each'I'= 1 point",score)
              print("  This is ai score, each'I'= 1 point",aiscore)

       elif player == "3" and aii == "rock":
              print(f"Oh no you lost,you used,{player},and ai used,{aii}")
              aiscore.append("I")
              print("This is your score, each'I'= 1 point",score)
              print("  This is ai score, each'I'= 1 point",aiscore)
       elif player == "3" and aii == ("paper"):
              print(f"You won!,you used,{player},and ai used,{aii}")
              score.append("I")
              print("This is your score, each'I'= 1 point",score)
              print("  This is ai score, each'I'= 1 point",aiscore)