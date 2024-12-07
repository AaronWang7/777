# -*- coding: utf-8 -*-
"""
Created on Fri Dec  6 23:51:46 2024

@author: huzi
"""


listtop1 = [" "]
listmid1 = [" "]
listdown1 = [" "]
listtop2 = [" "]
listmid2 = [" "]
listdown2 = [" "]
listtop3 = [" "]
listmid3 = [" "]
listdown3 = [" "]
import random
        
print("Hi, welcome to the tic tac toe game!")
while True:
    for i in range (1,4,1):
       print("You can enter",i)
    r = input(f"enter what rows you want to plce it 1-3, 1 is top:")
    c = input("enter where you want to plce it: 1 very left, 3 very right, 1-3:")
    if r == "1" and c == "1" and "X" not in listtop1 and "O" not in listtop1:
        listtop1 = ("X")
        ia = (random.randrange(0,90))
        if ia < 10 or ia == 10 and "X" not in listtop1 and "O" not in listtop1:
            listtop1 = ("O")
        elif "X" and "O" not in listtop2:
               listtop1 = ("O")
        elif "X" and "O" not in listtop3:
               listtop3 = ("O")
        elif "X" and "O" not in listmid1:
               listmid1 = ("O")
        elif "X" and "O" not in listmid2:
               listmid2 = ("O")
        elif "X" and "O" not in listmid3:
               listmid3 = ("O")
        elif "X" and "O" not in listdown1:
               listdown1 = ("O")
        elif "X" and "O" not in listdown2:
               listdown2 = ("O")
        elif "X" and "O" not in listdown3:
               listdown = ("O")
        elif ia < 20 or ia == 20 and "X" not in listtop2 and "O" not in listtop2 :
            listtop2 = ("O")
        elif "X" and "O" not in listtop2:
               listtop1= ("O")
        elif "X" and "O" not in listtop3:
               listtop3= ("O")
        elif "X" and "O" not in listmid1:
               listmid1 = ("O")
        elif "X" and "O" not in listmid2:
               listmid2= ("O")
        elif "X" and "O" not in listmid3:
               listmid3= ("O")
        elif "X" and "O" not in listdown1:
               listdown1= ("O")
        elif "X" and "O" not in listdown2:
               listdown2.append("O")
        elif "X" and "O" not in listdown3:
               listdown3.append("O")       
        elif ia < 30 or ia == 30 and "X" not in listtop3  and "O" not in listtop3:
            listtop3.append("O")
        elif "X" and "O" not in listtop2:
               listtop1.append("O")
        elif "X" and "O" not in listtop3:
               listtop3.append("O")
        elif "X" and "O" not in listmid1:
               listmid1.append("O")
        elif "X" and "O" not in listmid2:
               listmid2.append("O")
        elif "X" and "O" not in listmid3:
               listmid3.append("O")
        elif "X" and "O" not in listdown1:
               listdown1.append("O")
        elif "X" and "O" not in listdown2:
               listdown2.append("O")
        elif "X" and "O" not in listdown3:
               listdown3.append("O")
        elif ia < 40 or ia == 40 and "X" not in listmid1  and "O" not in listmid1:
            listmid1.append("O")
        elif "X" and "O" not in listtop2:
            listtop1.append("O")
        elif "X" and "O" not in listtop3:
               listtop3.append("O")
        elif "X" and "O" not in listmid1:
               listmid1.append("O")
        elif "X" and "O" not in listmid2:
               listmid2.append("O")
        elif "X" and "O" not in listmid3:
               listmid3.append("O")
        elif "X" and "O" not in listdown1:
               listdown1.append("O")
        elif "X" and "O" not in listdown2:
               listdown2.append("O")
        elif "X" and "O" not in listdown3:
               listdown3.append("O")
        elif ia < 50 or ia == 50 and "X" not in listmid2  and "O" not in listmid2:
                listmid2.append("O")
        elif "X" and "O" not in listtop2:
               listtop1.append("O")
        elif "X" and "O" not in listtop3:
               listtop3.append("O")
        elif "X" and "O" not in listmid1:
               listmid1.append("O")
        elif "X" and "O" not in listmid2:
               listmid2.append("O")
        elif "X" and "O" not in listmid3:
               listmid3.append("O")
        elif "X" and "O" not in listdown1:
               listdown1.append("O")
        elif "X" and "O" not in listdown2:
               listdown2.append("O")
        elif "X" and "O" not in listdown3:
               listdown3.append("O")
        elif ia < 60 or ia == 60 and "X" not in listmid3 and "O" not in listmid3:
                listmid3.append("O")
        elif "X" and "O" not in listtop2:
               listtop1.append("O")
        elif "X" and "O" not in listtop3:
               listtop3.append("O")
        elif "X" and "O" not in listmid1:
               listmid1.append("O")
        elif "X" and "O" not in listmid2:
               listmid2.append("O")
        elif "X" and "O" not in listmid3:
               listmid3.append("O")
        elif "X" and "O" not in listdown1:
               listdown1.append("O")
        elif "X" and "O" not in listdown2:
               listdown2.append("O")
        elif "X" and "O" not in listdown3:
               listdown3.append("O")
        elif ia < 70 or ia == 70 and "X" not in listdown1 and "O" not in listdown1:
                listdown1.append("O")
        elif "X" and "O" not in listtop2:
               listtop1.append("O")
        elif "X" and "O" not in listtop3:
               listtop3.append("O")
        elif "X" and "O" not in listmid1:
               listmid1.append("O")
        elif "X" and "O" not in listmid2:
               listmid2.append("O")
        elif "X" and "O" not in listmid3:
               listmid3.append("O")
        elif "X" and "O" not in listdown1:
               listdown1.append("O")
        elif "X" and "O" not in listdown2:
               listdown2.append("O")
        elif "X" and "O" not in listdown3:
               listdown3.append("O")
        elif ia < 80 or ia == 80 and "X" not in listdown2  and "O" not in listdown2:
                listdown2.append("O")
        elif "X" and "O" not in listtop2:
               listtop1.append("O")
        elif "X" and "O" not in listtop3:
               listtop3.append("O")
        elif"X" and "O" not in listmid1:
               listmid1.append("O")
        elif "X" and "O" not in listmid2:
               listmid2.append("O")
        elif "X" and "O" not in listmid3:
               listmid3.append("O")
        elif "X" not in listdown1: 
               listdown1.append("O")
        elif "X" and "O" not in listdown2:
               listdown2.append("O")
        elif "X" and "O" not in listdown3:
               listdown3.append("O")
        elif ia < 90 or ia == 90 and "X" not in listdown3 and "O" not in listdown3:
                listdown3.append("O")
        elif "X" and "O" not in listtop2:
               listtop1.append("O")
        elif "X" and "O" not in listtop3:
               listtop3.append("O")
        elif "X" and "O" not in listmid1:
               listmid1.append("O")
        elif "X" and "O" not in listmid2:
               listmid2.append("O")
        elif "X" and "O" not in listmid3:
               listmid3.append("O")
        elif "X" and "O" not in listdown1:
               listdown1.append("O")
        elif "X" and "O" not in listdown2:
               listdown2.append("O")
        elif "X" and "O" not in listdown3:
               listdown3.append("O")
        print(listtop1,listtop2,listtop3)
        print(listmid1,listmid2,listmid3)
        print(listdown1,listdown2,listdown3)
        if "X" in listtop1 and "X" in listtop2 and "X" in listtop3:
                print("You win!")
        elif "X" in listtop1 and "X" in  listmid1 and "X" in  listdown1:
                print("You win!")
        elif "X" in listmid1 and "X" in listmid2 and "X" in  listmid3:
                print("You win!")
        elif "X" in listdown1 and "X" in listdown2 and "X" in listdown3:
                print("You win!")
        elif "X" in listtop2 and "X" in listmid2 and "X" in listdown2:
                print("You win!")
        elif "X" in listtop3 and "X" in listmid3 and "X" in listdown3:
                print("You win!")
        elif "X" in listtop1 and "X" in listmid2 and "X" in listdown3:
                print("You win!")
        elif "X" in listtop3 and "X" in listmid2 and "X" in listdown1:
                print("You win!")
        
    if r == "1" and c == "2" and "X" not in listtop2 and "O" not in listtop2:
        listtop2.append("X")
        ia = (random.randrange(0,90))
        if ia < 10 or ia == 10 and "X" not in listtop1 and "O" not in listtop1:
            listtop1.append("O")
        elif "X" and "O" not in listtop2:
               listtop1.append("O")
        elif "X" and "O" not in listtop3:
               listtop3.append("O")
        elif "X" and "O" not in listmid1:
               listmid1.append("O")
        elif "X" and "O" not in listmid2:
               listmid2.append("O")
        elif "X" and "O" not in listmid3:
               listmid3.append("O")
        elif "X" and "O" not in listdown1:
               listdown1.append("O")
        elif "X" and "O" not in listdown2:
               listdown2.append("O")
        elif "X" and "O" not in listdown3:
               listdown3.append("O")
        elif ia < 20 or ia == 20 and "X" not in listtop2 and "O" not in listtop2 :
            listtop2.append("O")
        elif "X" and "O" not in listtop2:
               listtop1.append("O")
        elif "X" and "O" not in listtop3:
               listtop3.append("O")
        elif "X" and "O" not in listmid1:
               listmid1.append("O")
        elif "X" and "O" not in listmid2:
               listmid2.append("O")
        elif "X" and "O" not in listmid3:
               listmid3.append("O")
        elif "X" and "O" not in listdown1:
               listdown1.append("O")
        elif "X" and "O" not in listdown2:
               listdown2.append("O")
        elif "X" and "O" not in listdown3:
               listdown3.append("O")       
        elif ia < 30 or ia == 30 and "X" not in listtop3  and "O" not in listtop3:
            listtop3.append("O")
        elif "X" and "O" not in listtop2:
               listtop1.append("O")
        elif "X" and "O" not in listtop3:
               listtop3.append("O")
        elif "X" and "O" not in listmid1:
               listmid1.append("O")
        elif "X" and "O" not in listmid2:
               listmid2.append("O")
        elif "X" and "O" not in listmid3:
               listmid3.append("O")
        elif "X" and "O" not in listdown1:
               listdown1.append("O")
        elif "X" and "O" not in listdown2:
               listdown2.append("O")
        elif "X" and "O" not in listdown3:
               listdown3.append("O")
        elif ia < 40 or ia == 40 and "X" not in listmid1  and "O" not in listmid1:
            listmid1.append("O")
        elif "X" and "O" not in listtop2:
            listtop1.append("O")
        elif "X" and "O" not in listtop3:
               listtop3.append("O")
        elif "X" and "O" not in listmid1:
               listmid1.append("O")
        elif "X" and "O" not in listmid2:
               listmid2.append("O")
        elif "X" and "O" not in listmid3:
               listmid3.append("O")
        elif "X" and "O" not in listdown1:
               listdown1.append("O")
        elif "X" and "O" not in listdown2:
               listdown2.append("O")
        elif "X" and "O" not in listdown3:
               listdown3.append("O")
        elif ia < 50 or ia == 50 and "X" not in listmid2  and "O" not in listmid2:
                listmid2.append("O")
        elif "X" and "O" not in listtop2:
               listtop1.append("O")
        elif "X" and "O" not in listtop3:
               listtop3.append("O")
        elif "X" and "O" not in listmid1:
               listmid1.append("O")
        elif "X" and "O" not in listmid2:
               listmid2.append("O")
        elif "X" and "O" not in listmid3:
               listmid3.append("O")
        elif "X" and "O" not in listdown1:
               listdown1.append("O")
        elif "X" and "O" not in listdown2:
               listdown2.append("O")
        elif "X" and "O" not in listdown3:
               listdown3.append("O")
        elif ia < 60 or ia == 60 and "X" not in listmid3 and "O" not in listmid3:
                listmid3.append("O")
        elif "X" and "O" not in listtop2:
               listtop1.append("O")
        elif "X" and "O" not in listtop3:
               listtop3.append("O")
        elif "X" and "O" not in listmid1:
               listmid1.append("O")
        elif "X" and "O" not in listmid2:
               listmid2.append("O")
        elif "X" and "O" not in listmid3:
               listmid3.append("O")
        elif "X" and "O" not in listdown1:
               listdown1.append("O")
        elif "X" and "O" not in listdown2:
               listdown2.append("O")
        elif "X" and "O" not in listdown3:
               listdown3.append("O")
        elif ia < 70 or ia == 70 and "X" not in listdown1 and "O" not in listdown1:
                listdown1.append("O")
        elif "X" and "O" not in listtop2:
               listtop1.append("O")
        elif "X" and "O" not in listtop3:
               listtop3.append("O")
        elif "X" and "O" not in listmid1:
               listmid1.append("O")
        elif "X" and "O" not in listmid2:
               listmid2.append("O")
        elif "X" and "O" not in listmid3:
               listmid3.append("O")
        elif "X" and "O" not in listdown1:
               listdown1.append("O")
        elif "X" and "O" not in listdown2:
               listdown2.append("O")
        elif "X" and "O" not in listdown3:
               listdown3.append("O")
        elif ia < 80 or ia == 80 and "X" not in listdown2  and "O" not in listdown2:
                listdown2.append("O")
        elif "X" and "O" not in listtop2:
               listtop1.append("O")
        elif "X" and "O" not in listtop3:
               listtop3.append("O")
        elif"X" and "O" not in listmid1:
               listmid1.append("O")
        elif "X" and "O" not in listmid2:
               listmid2.append("O")
        elif "X" and "O" not in listmid3:
               listmid3.append("O")
        elif "X" not in listdown1: 
               listdown1.append("O")
        elif "X" and "O" not in listdown2:
               listdown2.append("O")
        elif "X" and "O" not in listdown3:
               listdown3.append("O")
        elif ia < 90 or ia == 90 and "X" not in listdown3 and "O" not in listdown3:
                listdown3.append("O")
        elif "X" and "O" not in listtop2:
               listtop1.append("O")
        elif "X" and "O" not in listtop3:
               listtop3.append("O")
        elif "X" and "O" not in listmid1:
               listmid1.append("O")
        elif "X" and "O" not in listmid2:
               listmid2.append("O")
        elif "X" and "O" not in listmid3:
               listmid3.append("O")
        elif "X" and "O" not in listdown1:
               listdown1.append("O")
        elif "X" and "O" not in listdown2:
               listdown2.append("O")
        elif "X" and "O" not in listdown3:
               listdown3.append("O")
        print(listtop1,listtop2,listtop3)
        print(listmid1,listmid2,listmid3)
        print(listdown1,listdown2,listdown3)
        if "X" in listtop1 and "X" in listtop2 and "X" in listtop3:
                print("You win!")
        elif "X" in listtop1 and "X" in  listmid1 and "X" in  listdown1:
                print("You win!")
        elif "X" in listmid1 and "X" in listmid2 and "X" in  listmid3:
                print("You win!")
        elif "X" in listdown1 and "X" in listdown2 and "X" in listdown3:
                print("You win!")
        elif "X" in listtop2 and "X" in listmid2 and "X" in listdown2:
                print("You win!")
        elif "X" in listtop3 and "X" in listmid3 and "X" in listdown3:
                print("You win!")
        elif "X" in listtop1 and "X" in listmid2 and "X" in listdown3:
                print("You win!")
        elif "X" in listtop3 and "X" in listmid2 and "X" in listdown1:
                print("You win!")
        
    if r == "1" and c == "3" and "X" not in listtop3 and "O" not in listtop3:
        listtop3.append("X")
        ia = (random.randrange(0,90))
        if ia < 10 or ia == 10 and "X" not in listtop1 and "O" not in listtop1:
            listtop1.append("O")
        elif "X" and "O" not in listtop2:
               listtop1.append("O")
        elif "X" and "O" not in listtop3:
               listtop3.append("O")
        elif "X" and "O" not in listmid1:
               listmid1.append("O")
        elif "X" and "O" not in listmid2:
               listmid2.append("O")
        elif "X" and "O" not in listmid3:
               listmid3.append("O")
        elif "X" and "O" not in listdown1:
               listdown1.append("O")
        elif "X" and "O" not in listdown2:
               listdown2.append("O")
        elif "X" and "O" not in listdown3:
               listdown3.append("O")
        elif ia < 20 or ia == 20 and "X" not in listtop2 and "O" not in listtop2 :
            listtop2.append("O")
        elif "X" and "O" not in listtop2:
               listtop1.append("O")
        elif "X" and "O" not in listtop3:
               listtop3.append("O")
        elif "X" and "O" not in listmid1:
               listmid1.append("O")
        elif "X" and "O" not in listmid2:
               listmid2.append("O")
        elif "X" and "O" not in listmid3:
               listmid3.append("O")
        elif "X" and "O" not in listdown1:
               listdown1.append("O")
        elif "X" and "O" not in listdown2:
               listdown2.append("O")
        elif "X" and "O" not in listdown3:
               listdown3.append("O")       
        elif ia < 30 or ia == 30 and "X" not in listtop3  and "O" not in listtop3:
            listtop3.append("O")
        elif "X" and "O" not in listtop2:
               listtop1.append("O")
        elif "X" and "O" not in listtop3:
               listtop3.append("O")
        elif "X" and "O" not in listmid1:
               listmid1.append("O")
        elif "X" and "O" not in listmid2:
               listmid2.append("O")
        elif "X" and "O" not in listmid3:
               listmid3.append("O")
        elif "X" and "O" not in listdown1:
               listdown1.append("O")
        elif "X" and "O" not in listdown2:
               listdown2.append("O")
        elif "X" and "O" not in listdown3:
               listdown3.append("O")
        elif ia < 40 or ia == 40 and "X" not in listmid1  and "O" not in listmid1:
            listmid1.append("O")
        elif "X" and "O" not in listtop2:
            listtop1.append("O")
        elif "X" and "O" not in listtop3:
               listtop3.append("O")
        elif "X" and "O" not in listmid1:
               listmid1.append("O")
        elif "X" and "O" not in listmid2:
               listmid2.append("O")
        elif "X" and "O" not in listmid3:
               listmid3.append("O")
        elif "X" and "O" not in listdown1:
               listdown1.append("O")
        elif "X" and "O" not in listdown2:
               listdown2.append("O")
        elif "X" and "O" not in listdown3:
               listdown3.append("O")
        elif ia < 50 or ia == 50 and "X" not in listmid2  and "O" not in listmid2:
                listmid2.append("O")
        elif "X" and "O" not in listtop2:
               listtop1.append("O")
        elif "X" and "O" not in listtop3:
               listtop3.append("O")
        elif "X" and "O" not in listmid1:
               listmid1.append("O")
        elif "X" and "O" not in listmid2:
               listmid2.append("O")
        elif "X" and "O" not in listmid3:
               listmid3.append("O")
        elif "X" and "O" not in listdown1:
               listdown1.append("O")
        elif "X" and "O" not in listdown2:
               listdown2.append("O")
        elif "X" and "O" not in listdown3:
               listdown3.append("O")
        elif ia < 60 or ia == 60 and "X" not in listmid3 and "O" not in listmid3:
                listmid3.append("O")
        elif "X" and "O" not in listtop2:
               listtop1.append("O")
        elif "X" and "O" not in listtop3:
               listtop3.append("O")
        elif "X" and "O" not in listmid1:
               listmid1.append("O")
        elif "X" and "O" not in listmid2:
               listmid2.append("O")
        elif "X" and "O" not in listmid3:
               listmid3.append("O")
        elif "X" and "O" not in listdown1:
               listdown1.append("O")
        elif "X" and "O" not in listdown2:
               listdown2.append("O")
        elif "X" and "O" not in listdown3:
               listdown3.append("O")
        elif ia < 70 or ia == 70 and "X" not in listdown1 and "O" not in listdown1:
                listdown1.append("O")
        elif "X" and "O" not in listtop2:
               listtop1.append("O")
        elif "X" and "O" not in listtop3:
               listtop3.append("O")
        elif "X" and "O" not in listmid1:
               listmid1.append("O")
        elif "X" and "O" not in listmid2:
               listmid2.append("O")
        elif "X" and "O" not in listmid3:
               listmid3.append("O")
        elif "X" and "O" not in listdown1:
               listdown1.append("O")
        elif "X" and "O" not in listdown2:
               listdown2.append("O")
        elif "X" and "O" not in listdown3:
               listdown3.append("O")
        elif ia < 80 or ia == 80 and "X" not in listdown2  and "O" not in listdown2:
                listdown2.append("O")
        elif "X" and "O" not in listtop2:
               listtop1.append("O")
        elif "X" and "O" not in listtop3:
               listtop3.append("O")
        elif"X" and "O" not in listmid1:
               listmid1.append("O")
        elif "X" and "O" not in listmid2:
               listmid2.append("O")
        elif "X" and "O" not in listmid3:
               listmid3.append("O")
        elif "X" not in listdown1: 
               listdown1.append("O")
        elif "X" and "O" not in listdown2:
               listdown2.append("O")
        elif "X" and "O" not in listdown3:
               listdown3.append("O")
        elif ia < 90 or ia == 90 and "X" not in listdown3 and "O" not in listdown3:
                listdown3.append("O")
        elif "X" and "O" not in listtop2:
               listtop1.append("O")
        elif "X" and "O" not in listtop3:
               listtop3.append("O")
        elif "X" and "O" not in listmid1:
               listmid1.append("O")
        elif "X" and "O" not in listmid2:
               listmid2.append("O")
        elif "X" and "O" not in listmid3:
               listmid3.append("O")
        elif "X" and "O" not in listdown1:
               listdown1.append("O")
        elif "X" and "O" not in listdown2:
               listdown2.append("O")
        elif "X" and "O" not in listdown3:
               listdown3.append("O")
        print(listtop1,listtop2,listtop3)
        print(listmid1,listmid2,listmid3)
        print(listdown1,listdown2,listdown3)
        if "X" in listtop1 and "X" in listtop2 and "X" in listtop3:
                print("You win!")
        elif "X" in listtop1 and "X" in  listmid1 and "X" in  listdown1:
                print("You win!")
        elif "X" in listmid1 and "X" in listmid2 and "X" in  listmid3:
                print("You win!")
        elif "X" in listdown1 and "X" in listdown2 and "X" in listdown3:
                print("You win!")
        elif "X" in listtop2 and "X" in listmid2 and "X" in listdown2:
                print("You win!")
        elif "X" in listtop3 and "X" in listmid3 and "X" in listdown3:
                print("You win!")
        elif "X" in listtop1 and "X" in listmid2 and "X" in listdown3:
                print("You win!")
        elif "X" in listtop3 and "X" in listmid2 and "X" in listdown1:
                print("You win!")
    
    if r == "2" and c == "1" and "X" not in listmid1 and "O" not in listmid1:
        listmid1.append("X")
        ia = (random.randrange(0,90))
        if ia < 10 or ia == 10 and "X" not in listtop1 and "O" not in listtop1:
            listtop1.append("O")
        elif "X" and "O" not in listtop2:
               listtop1.append("O")
        elif "X" and "O" not in listtop3:
               listtop3.append("O")
        elif "X" and "O" not in listmid1:
               listmid1.append("O")
        elif "X" and "O" not in listmid2:
               listmid2.append("O")
        elif "X" and "O" not in listmid3:
               listmid3.append("O")
        elif "X" and "O" not in listdown1:
               listdown1.append("O")
        elif "X" and "O" not in listdown2:
               listdown2.append("O")
        elif "X" and "O" not in listdown3:
               listdown3.append("O")
        elif ia < 20 or ia == 20 and "X" not in listtop2 and "O" not in listtop2 :
            listtop2.append("O")
        elif "X" and "O" not in listtop2:
               listtop1.append("O")
        elif "X" and "O" not in listtop3:
               listtop3.append("O")
        elif "X" and "O" not in listmid1:
               listmid1.append("O")
        elif "X" and "O" not in listmid2:
               listmid2.append("O")
        elif "X" and "O" not in listmid3:
               listmid3.append("O")
        elif "X" and "O" not in listdown1:
               listdown1.append("O")
        elif "X" and "O" not in listdown2:
               listdown2.append("O")
        elif "X" and "O" not in listdown3:
               listdown3.append("O")       
        elif ia < 30 or ia == 30 and "X" not in listtop3  and "O" not in listtop3:
            listtop3.append("O")
        elif "X" and "O" not in listtop2:
               listtop1.append("O")
        elif "X" and "O" not in listtop3:
               listtop3.append("O")
        elif "X" and "O" not in listmid1:
               listmid1.append("O")
        elif "X" and "O" not in listmid2:
               listmid2.append("O")
        elif "X" and "O" not in listmid3:
               listmid3.append("O")
        elif "X" and "O" not in listdown1:
               listdown1.append("O")
        elif "X" and "O" not in listdown2:
               listdown2.append("O")
        elif "X" and "O" not in listdown3:
               listdown3.append("O")
        elif ia < 40 or ia == 40 and "X" not in listmid1  and "O" not in listmid1:
            listmid1.append("O")
        elif "X" and "O" not in listtop2:
            listtop1.append("O")
        elif "X" and "O" not in listtop3:
               listtop3.append("O")
        elif "X" and "O" not in listmid1:
               listmid1.append("O")
        elif "X" and "O" not in listmid2:
               listmid2.append("O")
        elif "X" and "O" not in listmid3:
               listmid3.append("O")
        elif "X" and "O" not in listdown1:
               listdown1.append("O")
        elif "X" and "O" not in listdown2:
               listdown2.append("O")
        elif "X" and "O" not in listdown3:
               listdown3.append("O")
        elif ia < 50 or ia == 50 and "X" not in listmid2  and "O" not in listmid2:
                listmid2.append("O")
        elif "X" and "O" not in listtop2:
               listtop1.append("O")
        elif "X" and "O" not in listtop3:
               listtop3.append("O")
        elif "X" and "O" not in listmid1:
               listmid1.append("O")
        elif "X" and "O" not in listmid2:
               listmid2.append("O")
        elif "X" and "O" not in listmid3:
               listmid3.append("O")
        elif "X" and "O" not in listdown1:
               listdown1.append("O")
        elif "X" and "O" not in listdown2:
               listdown2.append("O")
        elif "X" and "O" not in listdown3:
               listdown3.append("O")
        elif ia < 60 or ia == 60 and "X" not in listmid3 and "O" not in listmid3:
                listmid3.append("O")
        elif "X" and "O" not in listtop2:
               listtop1.append("O")
        elif "X" and "O" not in listtop3:
               listtop3.append("O")
        elif "X" and "O" not in listmid1:
               listmid1.append("O")
        elif "X" and "O" not in listmid2:
               listmid2.append("O")
        elif "X" and "O" not in listmid3:
               listmid3.append("O")
        elif "X" and "O" not in listdown1:
               listdown1.append("O")
        elif "X" and "O" not in listdown2:
               listdown2.append("O")
        elif "X" and "O" not in listdown3:
               listdown3.append("O")
        elif ia < 70 or ia == 70 and "X" not in listdown1 and "O" not in listdown1:
                listdown1.append("O")
        elif "X" and "O" not in listtop2:
               listtop1.append("O")
        elif "X" and "O" not in listtop3:
               listtop3.append("O")
        elif "X" and "O" not in listmid1:
               listmid1.append("O")
        elif "X" and "O" not in listmid2:
               listmid2.append("O")
        elif "X" and "O" not in listmid3:
               listmid3.append("O")
        elif "X" and "O" not in listdown1:
               listdown1.append("O")
        elif "X" and "O" not in listdown2:
               listdown2.append("O")
        elif "X" and "O" not in listdown3:
               listdown3.append("O")
        elif ia < 80 or ia == 80 and "X" not in listdown2  and "O" not in listdown2:
                listdown2.append("O")
        elif "X" and "O" not in listtop2:
               listtop1.append("O")
        elif "X" and "O" not in listtop3:
               listtop3.append("O")
        elif"X" and "O" not in listmid1:
               listmid1.append("O")
        elif "X" and "O" not in listmid2:
               listmid2.append("O")
        elif "X" and "O" not in listmid3:
               listmid3.append("O")
        elif "X" not in listdown1: 
               listdown1.append("O")
        elif "X" and "O" not in listdown2:
               listdown2.append("O")
        elif "X" and "O" not in listdown3:
               listdown3.append("O")
        elif ia < 90 or ia == 90 and "X" not in listdown3 and "O" not in listdown3:
                listdown3.append("O")
        elif "X" and "O" not in listtop2:
               listtop1.append("O")
        elif "X" and "O" not in listtop3:
               listtop3.append("O")
        elif "X" and "O" not in listmid1:
               listmid1.append("O")
        elif "X" and "O" not in listmid2:
               listmid2.append("O")
        elif "X" and "O" not in listmid3:
               listmid3.append("O")
        elif "X" and "O" not in listdown1:
               listdown1.append("O")
        elif "X" and "O" not in listdown2:
               listdown2.append("O")
        elif "X" and "O" not in listdown3:
               listdown3.append("O")
        print(listtop1,listtop2,listtop3)
        print(listmid1,listmid2,listmid3)
        print(listdown1,listdown2,listdown3)
        if "X" in listtop1 and "X" in listtop2 and "X" in listtop3:
                print("You win!")
        elif "X" in listtop1 and "X" in  listmid1 and "X" in  listdown1:
                print("You win!")
        elif "X" in listmid1 and "X" in listmid2 and "X" in  listmid3:
                print("You win!")
        elif "X" in listdown1 and "X" in listdown2 and "X" in listdown3:
                print("You win!")
        elif "X" in listtop2 and "X" in listmid2 and "X" in listdown2:
                print("You win!")
        elif "X" in listtop3 and "X" in listmid3 and "X" in listdown3:
                print("You win!")
        elif "X" in listtop1 and "X" in listmid2 and "X" in listdown3:
                print("You win!")
        elif "X" in listtop3 and "X" in listmid2 and "X" in listdown1:
                print("You win!")

        
    if r == "2" and c == "2" and "X" not in listmid2 and "O" not in listmid2:
        listmid2.append("X")
        ia = (random.randrange(0,90))
        if ia < 10 or ia == 10 and "X" not in listtop1 and "O" not in listtop1:
            listtop1.append("O")
        elif "X" and "O" not in listtop2:
               listtop1.append("O")
        elif "X" and "O" not in listtop3:
               listtop3.append("O")
        elif "X" and "O" not in listmid1:
               listmid1.append("O")
        elif "X" and "O" not in listmid2:
               listmid2.append("O")
        elif "X" and "O" not in listmid3:
               listmid3.append("O")
        elif "X" and "O" not in listdown1:
               listdown1.append("O")
        elif "X" and "O" not in listdown2:
               listdown2.append("O")
        elif "X" and "O" not in listdown3:
               listdown3.append("O")
        elif ia < 20 or ia == 20 and "X" not in listtop2 and "O" not in listtop2 :
            listtop2.append("O")
        elif "X" and "O" not in listtop2:
               listtop1.append("O")
        elif "X" and "O" not in listtop3:
               listtop3.append("O")
        elif "X" and "O" not in listmid1:
               listmid1.append("O")
        elif "X" and "O" not in listmid2:
               listmid2.append("O")
        elif "X" and "O" not in listmid3:
               listmid3.append("O")
        elif "X" and "O" not in listdown1:
               listdown1.append("O")
        elif "X" and "O" not in listdown2:
               listdown2.append("O")
        elif "X" and "O" not in listdown3:
               listdown3.append("O")       
        elif ia < 30 or ia == 30 and "X" not in listtop3  and "O" not in listtop3:
            listtop3.append("O")
        elif "X" and "O" not in listtop2:
               listtop1.append("O")
        elif "X" and "O" not in listtop3:
               listtop3.append("O")
        elif "X" and "O" not in listmid1:
               listmid1.append("O")
        elif "X" and "O" not in listmid2:
               listmid2.append("O")
        elif "X" and "O" not in listmid3:
               listmid3.append("O")
        elif "X" and "O" not in listdown1:
               listdown1.append("O")
        elif "X" and "O" not in listdown2:
               listdown2.append("O")
        elif "X" and "O" not in listdown3:
               listdown3.append("O")
        elif ia < 40 or ia == 40 and "X" not in listmid1  and "O" not in listmid1:
            listmid1.append("O")
        elif "X" and "O" not in listtop2:
            listtop1.append("O")
        elif "X" and "O" not in listtop3:
               listtop3.append("O")
        elif "X" and "O" not in listmid1:
               listmid1.append("O")
        elif "X" and "O" not in listmid2:
               listmid2.append("O")
        elif "X" and "O" not in listmid3:
               listmid3.append("O")
        elif "X" and "O" not in listdown1:
               listdown1.append("O")
        elif "X" and "O" not in listdown2:
               listdown2.append("O")
        elif "X" and "O" not in listdown3:
               listdown3.append("O")
        elif ia < 50 or ia == 50 and "X" not in listmid2  and "O" not in listmid2:
                listmid2.append("O")
        elif "X" and "O" not in listtop2:
               listtop1.append("O")
        elif "X" and "O" not in listtop3:
               listtop3.append("O")
        elif "X" and "O" not in listmid1:
               listmid1.append("O")
        elif "X" and "O" not in listmid2:
               listmid2.append("O")
        elif "X" and "O" not in listmid3:
               listmid3.append("O")
        elif "X" and "O" not in listdown1:
               listdown1.append("O")
        elif "X" and "O" not in listdown2:
               listdown2.append("O")
        elif "X" and "O" not in listdown3:
               listdown3.append("O")
        elif ia < 60 or ia == 60 and "X" not in listmid3 and "O" not in listmid3:
                listmid3.append("O")
        elif "X" and "O" not in listtop2:
               listtop1.append("O")
        elif "X" and "O" not in listtop3:
               listtop3.append("O")
        elif "X" and "O" not in listmid1:
               listmid1.append("O")
        elif "X" and "O" not in listmid2:
               listmid2.append("O")
        elif "X" and "O" not in listmid3:
               listmid3.append("O")
        elif "X" and "O" not in listdown1:
               listdown1.append("O")
        elif "X" and "O" not in listdown2:
               listdown2.append("O")
        elif "X" and "O" not in listdown3:
               listdown3.append("O")
        elif ia < 70 or ia == 70 and "X" not in listdown1 and "O" not in listdown1:
                listdown1.append("O")
        elif "X" and "O" not in listtop2:
               listtop1.append("O")
        elif "X" and "O" not in listtop3:
               listtop3.append("O")
        elif "X" and "O" not in listmid1:
               listmid1.append("O")
        elif "X" and "O" not in listmid2:
               listmid2.append("O")
        elif "X" and "O" not in listmid3:
               listmid3.append("O")
        elif "X" and "O" not in listdown1:
               listdown1.append("O")
        elif "X" and "O" not in listdown2:
               listdown2.append("O")
        elif "X" and "O" not in listdown3:
               listdown3.append("O")
        elif ia < 80 or ia == 80 and "X" not in listdown2  and "O" not in listdown2:
                listdown2.append("O")
        elif "X" and "O" not in listtop2:
               listtop1.append("O")
        elif "X" and "O" not in listtop3:
               listtop3.append("O")
        elif"X" and "O" not in listmid1:
               listmid1.append("O")
        elif "X" and "O" not in listmid2:
               listmid2.append("O")
        elif "X" and "O" not in listmid3:
               listmid3.append("O")
        elif "X" not in listdown1: 
               listdown1.append("O")
        elif "X" and "O" not in listdown2:
               listdown2.append("O")
        elif "X" and "O" not in listdown3:
               listdown3.append("O")
        elif ia < 90 or ia == 90 and "X" not in listdown3 and "O" not in listdown3:
                listdown3.append("O")
        elif "X" and "O" not in listtop2:
               listtop1.append("O")
        elif "X" and "O" not in listtop3:
               listtop3.append("O")
        elif "X" and "O" not in listmid1:
               listmid1.append("O")
        elif "X" and "O" not in listmid2:
               listmid2.append("O")
        elif "X" and "O" not in listmid3:
               listmid3.append("O")
        elif "X" and "O" not in listdown1:
               listdown1.append("O")
        elif "X" and "O" not in listdown2:
               listdown2.append("O")
        elif "X" and "O" not in listdown3:
               listdown3.append("O")
        print(listtop1,listtop2,listtop3)
        print(listmid1,listmid2,listmid3)
        print(listdown1,listdown2,listdown3)
        if "X" in listtop1 and "X" in listtop2 and "X" in listtop3:
                print("You win!")
        elif "X" in listtop1 and "X" in  listmid1 and "X" in  listdown1:
                print("You win!")
        elif "X" in listmid1 and "X" in listmid2 and "X" in  listmid3:
                print("You win!")
        elif "X" in listdown1 and "X" in listdown2 and "X" in listdown3:
                print("You win!")
        elif "X" in listtop2 and "X" in listmid2 and "X" in listdown2:
                print("You win!")
        elif "X" in listtop3 and "X" in listmid3 and "X" in listdown3:
                print("You win!")
        elif "X" in listtop1 and "X" in listmid2 and "X" in listdown3:
                print("You win!")
        elif "X" in listtop3 and "X" in listmid2 and "X" in listdown1:
                print("You win!")

        if r == "2" and c == "3" and "X" not in listmid3 and "O" not in listmid3:
              listmid3.append("X")
        ia = (random.randrange(0,90))
        if ia < 10 or ia == 10 and "X" not in listtop1 and "O" not in listtop1:
            listtop1.append("O")
        elif "X" and "O" not in listtop2:
               listtop1.append("O")
        elif "X" and "O" not in listtop3:
               listtop3.append("O")
        elif "X" and "O" not in listmid1:
               listmid1.append("O")
        elif "X" and "O" not in listmid2:
               listmid2.append("O")
        elif "X" and "O" not in listmid3:
               listmid3.append("O")
        elif "X" and "O" not in listdown1:
               listdown1.append("O")
        elif "X" and "O" not in listdown2:
               listdown2.append("O")
        elif "X" and "O" not in listdown3:
               listdown3.append("O")
        elif ia < 20 or ia == 20 and "X" not in listtop2 and "O" not in listtop2 :
            listtop2.append("O")
        elif "X" and "O" not in listtop2:
               listtop1.append("O")
        elif "X" and "O" not in listtop3:
               listtop3.append("O")
        elif "X" and "O" not in listmid1:
               listmid1.append("O")
        elif "X" and "O" not in listmid2:
               listmid2.append("O")
        elif "X" and "O" not in listmid3:
               listmid3.append("O")
        elif "X" and "O" not in listdown1:
               listdown1.append("O")
        elif "X" and "O" not in listdown2:
               listdown2.append("O")
        elif "X" and "O" not in listdown3:
               listdown3.append("O")       
        elif ia < 30 or ia == 30 and "X" not in listtop3  and "O" not in listtop3:
            listtop3.append("O")
        elif "X" and "O" not in listtop2:
               listtop1.append("O")
        elif "X" and "O" not in listtop3:
               listtop3.append("O")
        elif "X" and "O" not in listmid1:
               listmid1.append("O")
        elif "X" and "O" not in listmid2:
               listmid2.append("O")
        elif "X" and "O" not in listmid3:
               listmid3.append("O")
        elif "X" and "O" not in listdown1:
               listdown1.append("O")
        elif "X" and "O" not in listdown2:
               listdown2.append("O")
        elif "X" and "O" not in listdown3:
               listdown3.append("O")
        elif ia < 40 or ia == 40 and "X" not in listmid1  and "O" not in listmid1:
            listmid1.append("O")
        elif "X" and "O" not in listtop2:
            listtop1.append("O")
        elif "X" and "O" not in listtop3:
               listtop3.append("O")
        elif "X" and "O" not in listmid1:
               listmid1.append("O")
        elif "X" and "O" not in listmid2:
               listmid2.append("O")
        elif "X" and "O" not in listmid3:
               listmid3.append("O")
        elif "X" and "O" not in listdown1:
               listdown1.append("O")
        elif "X" and "O" not in listdown2:
               listdown2.append("O")
        elif "X" and "O" not in listdown3:
               listdown3.append("O")
        elif ia < 50 or ia == 50 and "X" not in listmid2  and "O" not in listmid2:
                listmid2.append("O")
        elif "X" and "O" not in listtop2:
               listtop1.append("O")
        elif "X" and "O" not in listtop3:
               listtop3.append("O")
        elif "X" and "O" not in listmid1:
               listmid1.append("O")
        elif "X" and "O" not in listmid2:
               listmid2.append("O")
        elif "X" and "O" not in listmid3:
               listmid3.append("O")
        elif "X" and "O" not in listdown1:
               listdown1.append("O")
        elif "X" and "O" not in listdown2:
               listdown2.append("O")
        elif "X" and "O" not in listdown3:
               listdown3.append("O")
        elif ia < 60 or ia == 60 and "X" not in listmid3 and "O" not in listmid3:
                listmid3.append("O")
        elif "X" and "O" not in listtop2:
               listtop1.append("O")
        elif "X" and "O" not in listtop3:
               listtop3.append("O")
        elif "X" and "O" not in listmid1:
               listmid1.append("O")
        elif "X" and "O" not in listmid2:
               listmid2.append("O")
        elif "X" and "O" not in listmid3:
               listmid3.append("O")
        elif "X" and "O" not in listdown1:
               listdown1.append("O")
        elif "X" and "O" not in listdown2:
               listdown2.append("O")
        elif "X" and "O" not in listdown3:
               listdown3.append("O")
        elif ia < 70 or ia == 70 and "X" not in listdown1 and "O" not in listdown1:
                listdown1.append("O")
        elif "X" and "O" not in listtop2:
               listtop1.append("O")
        elif "X" and "O" not in listtop3:
               listtop3.append("O")
        elif "X" and "O" not in listmid1:
               listmid1.append("O")
        elif "X" and "O" not in listmid2:
               listmid2.append("O")
        elif "X" and "O" not in listmid3:
               listmid3.append("O")
        elif "X" and "O" not in listdown1:
               listdown1.append("O")
        elif "X" and "O" not in listdown2:
               listdown2.append("O")
        elif "X" and "O" not in listdown3:
               listdown3.append("O")
        elif ia < 80 or ia == 80 and "X" not in listdown2  and "O" not in listdown2:
                listdown2.append("O")
        elif "X" and "O" not in listtop2:
               listtop1.append("O")
        elif "X" and "O" not in listtop3:
               listtop3.append("O")
        elif"X" and "O" not in listmid1:
               listmid1.append("O")
        elif "X" and "O" not in listmid2:
               listmid2.append("O")
        elif "X" and "O" not in listmid3:
               listmid3.append("O")
        elif "X" not in listdown1: 
               listdown1.append("O")
        elif "X" and "O" not in listdown2:
               listdown2.append("O")
        elif "X" and "O" not in listdown3:
               listdown3.append("O")
        elif ia < 90 or ia == 90 and "X" not in listdown3 and "O" not in listdown3:
                listdown3.append("O")
        elif "X" and "O" not in listtop2:
               listtop1.append("O")
        elif "X" and "O" not in listtop3:
               listtop3.append("O")
        elif "X" and "O" not in listmid1:
               listmid1.append("O")
        elif "X" and "O" not in listmid2:
               listmid2.append("O")
        elif "X" and "O" not in listmid3:
               listmid3.append("O")
        elif "X" and "O" not in listdown1:
               listdown1.append("O")
        elif "X" and "O" not in listdown2:
               listdown2.append("O")
        elif "X" and "O" not in listdown3:
               listdown3.append("O")
        print(listtop1,listtop2,listtop3)
        print(listmid1,listmid2,listmid3)
        print(listdown1,listdown2,listdown3)
        if "X" in listtop1 and "X" in listtop2 and "X" in listtop3:
                print("You win!")
        elif "X" in listtop1 and "X" in  listmid1 and "X" in  listdown1:
                print("You win!")
        elif "X" in listmid1 and "X" in listmid2 and "X" in  listmid3:
                print("You win!")
        elif "X" in listdown1 and "X" in listdown2 and "X" in listdown3:
                print("You win!")
        elif "X" in listtop2 and "X" in listmid2 and "X" in listdown2:
                print("You win!")
        elif "X" in listtop3 and "X" in listmid3 and "X" in listdown3:
                print("You win!")
        elif "X" in listtop1 and "X" in listmid2 and "X" in listdown3:
                print("You win!")
        elif "X" in listtop3 and "X" in listmid2 and "X" in listdown1:
                print("You win!")   
            
        if r == "3" and c == "1" and "X" not in listdown1 and "O" not in listdown1:
              listdown1.append("X")
        ia = (random.randrange(0,90))
        if ia < 10 or ia == 10 and "X" not in listtop1 and "O" not in listtop1:
            listtop1.append("O")
        elif "X" and "O" not in listtop2:
               listtop1.append("O")
        elif "X" and "O" not in listtop3:
               listtop3.append("O")
        elif "X" and "O" not in listmid1:
               listmid1.append("O")
        elif "X" and "O" not in listmid2:
               listmid2.append("O")
        elif "X" and "O" not in listmid3:
               listmid3.append("O")
        elif "X" and "O" not in listdown1:
               listdown1.append("O")
        elif "X" and "O" not in listdown2:
               listdown2.append("O")
        elif "X" and "O" not in listdown3:
               listdown3.append("O")
        elif ia < 20 or ia == 20 and "X" not in listtop2 and "O" not in listtop2 :
            listtop2.append("O")
        elif "X" and "O" not in listtop2:
               listtop1.append("O")
        elif "X" and "O" not in listtop3:
               listtop3.append("O")
        elif "X" and "O" not in listmid1:
               listmid1.append("O")
        elif "X" and "O" not in listmid2:
               listmid2.append("O")
        elif "X" and "O" not in listmid3:
               listmid3.append("O")
        elif "X" and "O" not in listdown1:
               listdown1.append("O")
        elif "X" and "O" not in listdown2:
               listdown2.append("O")
        elif "X" and "O" not in listdown3:
               listdown3.append("O")       
        elif ia < 30 or ia == 30 and "X" not in listtop3  and "O" not in listtop3:
            listtop3.append("O")
        elif "X" and "O" not in listtop2:
               listtop1.append("O")
        elif "X" and "O" not in listtop3:
               listtop3.append("O")
        elif "X" and "O" not in listmid1:
               listmid1.append("O")
        elif "X" and "O" not in listmid2:
               listmid2.append("O")
        elif "X" and "O" not in listmid3:
               listmid3.append("O")
        elif "X" and "O" not in listdown1:
               listdown1.append("O")
        elif "X" and "O" not in listdown2:
               listdown2.append("O")
        elif "X" and "O" not in listdown3:
               listdown3.append("O")
        elif ia < 40 or ia == 40 and "X" not in listmid1  and "O" not in listmid1:
            listmid1.append("O")
        elif "X" and "O" not in listtop2:
            listtop1.append("O")
        elif "X" and "O" not in listtop3:
               listtop3.append("O")
        elif "X" and "O" not in listmid1:
               listmid1.append("O")
        elif "X" and "O" not in listmid2:
               listmid2.append("O")
        elif "X" and "O" not in listmid3:
               listmid3.append("O")
        elif "X" and "O" not in listdown1:
               listdown1.append("O")
        elif "X" and "O" not in listdown2:
               listdown2.append("O")
        elif "X" and "O" not in listdown3:
               listdown3.append("O")
        elif ia < 50 or ia == 50 and "X" not in listmid2  and "O" not in listmid2:
                listmid2.append("O")
        elif "X" and "O" not in listtop2:
               listtop1.append("O")
        elif "X" and "O" not in listtop3:
               listtop3.append("O")
        elif "X" and "O" not in listmid1:
               listmid1.append("O")
        elif "X" and "O" not in listmid2:
               listmid2.append("O")
        elif "X" and "O" not in listmid3:
               listmid3.append("O")
        elif "X" and "O" not in listdown1:
               listdown1.append("O")
        elif "X" and "O" not in listdown2:
               listdown2.append("O")
        elif "X" and "O" not in listdown3:
               listdown3.append("O")
        elif ia < 60 or ia == 60 and "X" not in listmid3 and "O" not in listmid3:
                listmid3.append("O")
        elif "X" and "O" not in listtop2:
               listtop1.append("O")
        elif "X" and "O" not in listtop3:
               listtop3.append("O")
        elif "X" and "O" not in listmid1:
               listmid1.append("O")
        elif "X" and "O" not in listmid2:
               listmid2.append("O")
        elif "X" and "O" not in listmid3:
               listmid3.append("O")
        elif "X" and "O" not in listdown1:
               listdown1.append("O")
        elif "X" and "O" not in listdown2:
               listdown2.append("O")
        elif "X" and "O" not in listdown3:
               listdown3.append("O")
        elif ia < 70 or ia == 70 and "X" not in listdown1 and "O" not in listdown1:
                listdown1.append("O")
        elif "X" and "O" not in listtop2:
               listtop1.append("O")
        elif "X" and "O" not in listtop3:
               listtop3.append("O")
        elif "X" and "O" not in listmid1:
               listmid1.append("O")
        elif "X" and "O" not in listmid2:
               listmid2.append("O")
        elif "X" and "O" not in listmid3:
               listmid3.append("O")
        elif "X" and "O" not in listdown1:
               listdown1.append("O")
        elif "X" and "O" not in listdown2:
               listdown2.append("O")
        elif "X" and "O" not in listdown3:
               listdown3.append("O")
        elif ia < 80 or ia == 80 and "X" not in listdown2  and "O" not in listdown2:
                listdown2.append("O")
        elif "X" and "O" not in listtop2:
               listtop1.append("O")
        elif "X" and "O" not in listtop3:
               listtop3.append("O")
        elif"X" and "O" not in listmid1:
               listmid1.append("O")
        elif "X" and "O" not in listmid2:
               listmid2.append("O")
        elif "X" and "O" not in listmid3:
               listmid3.append("O")
        elif "X" not in listdown1: 
               listdown1.append("O")
        elif "X" and "O" not in listdown2:
               listdown2.append("O")
        elif "X" and "O" not in listdown3:
               listdown3.append("O")
        elif ia < 90 or ia == 90 and "X" not in listdown3 and "O" not in listdown3:
                listdown3.append("O")
        elif "X" and "O" not in listtop2:
               listtop1.append("O")
        elif "X" and "O" not in listtop3:
               listtop3.append("O")
        elif "X" and "O" not in listmid1:
               listmid1.append("O")
        elif "X" and "O" not in listmid2:
               listmid2.append("O")
        elif "X" and "O" not in listmid3:
               listmid3.append("O")
        elif "X" and "O" not in listdown1:
               listdown1.append("O")
        elif "X" and "O" not in listdown2:
               listdown2.append("O")
        elif "X" and "O" not in listdown3:
               listdown3.append("O")
        print(listtop1,listtop2,listtop3)
        print(listmid1,listmid2,listmid3)
        print(listdown1,listdown2,listdown3)
        if "X" in listtop1 and "X" in listtop2 and "X" in listtop3:
                print("You win!")
        elif "X" in listtop1 and "X" in  listmid1 and "X" in  listdown1:
                print("You win!")
        elif "X" in listmid1 and "X" in listmid2 and "X" in  listmid3:
                print("You win!")
        elif "X" in listdown1 and "X" in listdown2 and "X" in listdown3:
                print("You win!")
        elif "X" in listtop2 and "X" in listmid2 and "X" in listdown2:
                print("You win!")
        elif "X" in listtop3 and "X" in listmid3 and "X" in listdown3:
                print("You win!")
        elif "X" in listtop1 and "X" in listmid2 and "X" in listdown3:
                print("You win!")
        elif "X" in listtop3 and "X" in listmid2 and "X" in listdown1:
                print("You win!")
              
        if r == "3" and c == "3" and "X" not in listdown3 and "O" not in listdown3:
              listdown3.append("X")
        ia = (random.randrange(0,90))
        if ia < 10 or ia == 10 and "X" not in listtop1 and "O" not in listtop1:
            listtop1.append("O")
        elif "X" and "O" not in listtop2:
               listtop1.append("O")
        elif "X" and "O" not in listtop3:
               listtop3.append("O")
        elif "X" and "O" not in listmid1:
               listmid1.append("O")
        elif "X" and "O" not in listmid2:
               listmid2.append("O")
        elif "X" and "O" not in listmid3:
               listmid3.append("O")
        elif "X" and "O" not in listdown1:
               listdown1.append("O")
        elif "X" and "O" not in listdown2:
               listdown2.append("O")
        elif "X" and "O" not in listdown3:
               listdown3.append("O")
        elif ia < 20 or ia == 20 and "X" not in listtop2 and "O" not in listtop2 :
            listtop2.append("O")
        elif "X" and "O" not in listtop2:
               listtop1.append("O")
        elif "X" and "O" not in listtop3:
               listtop3.append("O")
        elif "X" and "O" not in listmid1:
               listmid1.append("O")
        elif "X" and "O" not in listmid2:
               listmid2.append("O")
        elif "X" and "O" not in listmid3:
               listmid3.append("O")
        elif "X" and "O" not in listdown1:
               listdown1.append("O")
        elif "X" and "O" not in listdown2:
               listdown2.append("O")
        elif "X" and "O" not in listdown3:
               listdown3.append("O")       
        elif ia < 30 or ia == 30 and "X" not in listtop3  and "O" not in listtop3:
            listtop3.append("O")
        elif "X" and "O" not in listtop2:
               listtop1.append("O")
        elif "X" and "O" not in listtop3:
               listtop3.append("O")
        elif "X" and "O" not in listmid1:
               listmid1.append("O")
        elif "X" and "O" not in listmid2:
               listmid2.append("O")
        elif "X" and "O" not in listmid3:
               listmid3.append("O")
        elif "X" and "O" not in listdown1:
               listdown1.append("O")
        elif "X" and "O" not in listdown2:
               listdown2.append("O")
        elif "X" and "O" not in listdown3:
               listdown3.append("O")
        elif ia < 40 or ia == 40 and "X" not in listmid1  and "O" not in listmid1:
            listmid1.append("O")
        elif "X" and "O" not in listtop2:
            listtop1.append("O")
        elif "X" and "O" not in listtop3:
               listtop3.append("O")
        elif "X" and "O" not in listmid1:
               listmid1.append("O")
        elif "X" and "O" not in listmid2:
               listmid2.append("O")
        elif "X" and "O" not in listmid3:
               listmid3.append("O")
        elif "X" and "O" not in listdown1:
               listdown1.append("O")
        elif "X" and "O" not in listdown2:
               listdown2.append("O")
        elif "X" and "O" not in listdown3:
               listdown3.append("O")
        elif ia < 50 or ia == 50 and "X" not in listmid2  and "O" not in listmid2:
                listmid2.append("O")
        elif "X" and "O" not in listtop2:
               listtop1.append("O")
        elif "X" and "O" not in listtop3:
               listtop3.append("O")
        elif "X" and "O" not in listmid1:
               listmid1.append("O")
        elif "X" and "O" not in listmid2:
               listmid2.append("O")
        elif "X" and "O" not in listmid3:
               listmid3.append("O")
        elif "X" and "O" not in listdown1:
               listdown1.append("O")
        elif "X" and "O" not in listdown2:
               listdown2.append("O")
        elif "X" and "O" not in listdown3:
               listdown3.append("O")
        elif ia < 60 or ia == 60 and "X" not in listmid3 and "O" not in listmid3:
                listmid3.append("O")
        elif "X" and "O" not in listtop2:
               listtop1.append("O")
        elif "X" and "O" not in listtop3:
               listtop3.append("O")
        elif "X" and "O" not in listmid1:
               listmid1.append("O")
        elif "X" and "O" not in listmid2:
               listmid2.append("O")
        elif "X" and "O" not in listmid3:
               listmid3.append("O")
        elif "X" and "O" not in listdown1:
               listdown1.append("O")
        elif "X" and "O" not in listdown2:
               listdown2.append("O")
        elif "X" and "O" not in listdown3:
               listdown3.append("O")
        elif ia < 70 or ia == 70 and "X" not in listdown1 and "O" not in listdown1:
                listdown1.append("O")
        elif "X" and "O" not in listtop2:
               listtop1.append("O")
        elif "X" and "O" not in listtop3:
               listtop3.append("O")
        elif "X" and "O" not in listmid1:
               listmid1.append("O")
        elif "X" and "O" not in listmid2:
               listmid2.append("O")
        elif "X" and "O" not in listmid3:
               listmid3.append("O")
        elif "X" and "O" not in listdown1:
               listdown1.append("O")
        elif "X" and "O" not in listdown2:
               listdown2.append("O")
        elif "X" and "O" not in listdown3:
               listdown3.append("O")
        elif ia < 80 or ia == 80 and "X" not in listdown2  and "O" not in listdown2:
                listdown2.append("O")
        elif "X" and "O" not in listtop2:
               listtop1.append("O")
        elif "X" and "O" not in listtop3:
               listtop3.append("O")
        elif"X" and "O" not in listmid1:
               listmid1.append("O")
        elif "X" and "O" not in listmid2:
               listmid2.append("O")
        elif "X" and "O" not in listmid3:
               listmid3.append("O")
        elif "X" not in listdown1: 
               listdown1.append("O")
        elif "X" and "O" not in listdown2:
               listdown2.append("O")
        elif "X" and "O" not in listdown3:
               listdown3.append("O")
        elif ia < 90 or ia == 90 and "X" not in listdown3 and "O" not in listdown3:
                listdown3.append("O")
        elif "X" and "O" not in listtop2:
               listtop1.append("O")
        elif "X" and "O" not in listtop3:
               listtop3.append("O")
        elif "X" and "O" not in listmid1:
               listmid1.append("O")
        elif "X" and "O" not in listmid2:
               listmid2.append("O")
        elif "X" and "O" not in listmid3:
               listmid3.append("O")
        elif "X" and "O" not in listdown1:
               listdown1.append("O")
        elif "X" and "O" not in listdown2:
               listdown2.append("O")
        elif "X" and "O" not in listdown3:
               listdown3.append("O")
        print(listtop1,listtop2,listtop3)
        print(listmid1,listmid2,listmid3)
        print(listdown1,listdown2,listdown3)
        if "X" in listtop1 and "X" in listtop2 and "X" in listtop3:
                print("You win!")
        elif "X" in listtop1 and "X" in  listmid1 and "X" in  listdown1:
                print("You win!")
        elif "X" in listmid1 and "X" in listmid2 and "X" in  listmid3:
                print("You win!")
        elif "X" in listdown1 and "X" in listdown2 and "X" in listdown3:
                print("You win!")
        elif "X" in listtop2 and "X" in listmid2 and "X" in listdown2:
                print("You win!")
        elif "X" in listtop3 and "X" in listmid3 and "X" in listdown3:
                print("You win!")
        elif "X" in listtop1 and "X" in listmid2 and "X" in listdown3:
                print("You win!")
        elif "X" in listtop3 and "X" in listmid2 and "X" in listdown1:
                print("You win!")            
            
        if r == "3" and c == "1" and "X" not in listdown1 and "O" not in listdown1:
              listdown1.append("X")
        ia = (random.randrange(0,90))
        if ia < 10 or ia == 10 and "X" not in listtop1 and "O" not in listtop1:
            listtop1.append("O")
        elif "X" and "O" not in listtop2:
               listtop1.append("O")
        elif "X" and "O" not in listtop3:
               listtop3.append("O")
        elif "X" and "O" not in listmid1:
               listmid1.append("O")
        elif "X" and "O" not in listmid2:
               listmid2.append("O")
        elif "X" and "O" not in listmid3:
               listmid3.append("O")
        elif "X" and "O" not in listdown1:
               listdown1.append("O")
        elif "X" and "O" not in listdown2:
               listdown2.append("O")
        elif "X" and "O" not in listdown3:
               listdown3.append("O")
        elif ia < 20 or ia == 20 and "X" not in listtop2 and "O" not in listtop2 :
            listtop2.append("O")
        elif "X" and "O" not in listtop2:
               listtop1.append("O")
        elif "X" and "O" not in listtop3:
               listtop3.append("O")
        elif "X" and "O" not in listmid1:
               listmid1.append("O")
        elif "X" and "O" not in listmid2:
               listmid2.append("O")
        elif "X" and "O" not in listmid3:
               listmid3.append("O")
        elif "X" and "O" not in listdown1:
               listdown1.append("O")
        elif "X" and "O" not in listdown2:
               listdown2.append("O")
        elif "X" and "O" not in listdown3:
               listdown3.append("O")       
        elif ia < 30 or ia == 30 and "X" not in listtop3  and "O" not in listtop3:
            listtop3.append("O")
        elif "X" and "O" not in listtop2:
               listtop1.append("O")
        elif "X" and "O" not in listtop3:
               listtop3.append("O")
        elif "X" and "O" not in listmid1:
               listmid1.append("O")
        elif "X" and "O" not in listmid2:
               listmid2.append("O")
        elif "X" and "O" not in listmid3:
               listmid3.append("O")
        elif "X" and "O" not in listdown1:
               listdown1.append("O")
        elif "X" and "O" not in listdown2:
               listdown2.append("O")
        elif "X" and "O" not in listdown3:
               listdown3.append("O")
        elif ia < 40 or ia == 40 and "X" not in listmid1  and "O" not in listmid1:
            listmid1.append("O")
        elif "X" and "O" not in listtop2:
            listtop1.append("O")
        elif "X" and "O" not in listtop3:
               listtop3.append("O")
        elif "X" and "O" not in listmid1:
               listmid1.append("O")
        elif "X" and "O" not in listmid2:
               listmid2.append("O")
        elif "X" and "O" not in listmid3:
               listmid3.append("O")
        elif "X" and "O" not in listdown1:
               listdown1.append("O")
        elif "X" and "O" not in listdown2:
               listdown2.append("O")
        elif "X" and "O" not in listdown3:
               listdown3.append("O")
        elif ia < 50 or ia == 50 and "X" not in listmid2  and "O" not in listmid2:
                listmid2.append("O")
        elif "X" and "O" not in listtop2:
               listtop1.append("O")
        elif "X" and "O" not in listtop3:
               listtop3.append("O")
        elif "X" and "O" not in listmid1:
               listmid1.append("O")
        elif "X" and "O" not in listmid2:
               listmid2.append("O")
        elif "X" and "O" not in listmid3:
               listmid3.append("O")
        elif "X" and "O" not in listdown1:
               listdown1.append("O")
        elif "X" and "O" not in listdown2:
               listdown2.append("O")
        elif "X" and "O" not in listdown3:
               listdown3.append("O")
        elif ia < 60 or ia == 60 and "X" not in listmid3 and "O" not in listmid3:
                listmid3.append("O")
        elif "X" and "O" not in listtop2:
               listtop1.append("O")
        elif "X" and "O" not in listtop3:
               listtop3.append("O")
        elif "X" and "O" not in listmid1:
               listmid1.append("O")
        elif "X" and "O" not in listmid2:
               listmid2.append("O")
        elif "X" and "O" not in listmid3:
               listmid3.append("O")
        elif "X" and "O" not in listdown1:
               listdown1.append("O")
        elif "X" and "O" not in listdown2:
               listdown2.append("O")
        elif "X" and "O" not in listdown3:
               listdown3.append("O")
        elif ia < 70 or ia == 70 and "X" not in listdown1 and "O" not in listdown1:
                listdown1.append("O")
        elif "X" and "O" not in listtop2:
               listtop1.append("O")
        elif "X" and "O" not in listtop3:
               listtop3.append("O")
        elif "X" and "O" not in listmid1:
               listmid1.append("O")
        elif "X" and "O" not in listmid2:
               listmid2.append("O")
        elif "X" and "O" not in listmid3:
               listmid3.append("O")
        elif "X" and "O" not in listdown1:
               listdown1.append("O")
        elif "X" and "O" not in listdown2:
               listdown2.append("O")
        elif "X" and "O" not in listdown3:
               listdown3.append("O")
        elif ia < 80 or ia == 80 and "X" not in listdown2  and "O" not in listdown2:
                listdown2.append("O")
        elif "X" and "O" not in listtop2:
               listtop1.append("O")
        elif "X" and "O" not in listtop3:
               listtop3.append("O")
        elif"X" and "O" not in listmid1:
               listmid1.append("O")
        elif "X" and "O" not in listmid2:
               listmid2.append("O")
        elif "X" and "O" not in listmid3:
               listmid3.append("O")
        elif "X" not in listdown1: 
               listdown1.append("O")
        elif "X" and "O" not in listdown2:
               listdown2.append("O")
        elif "X" and "O" not in listdown3:
               listdown3.append("O")
        elif ia < 90 or ia == 90 and "X" not in listdown3 and "O" not in listdown3:
                listdown3.append("O")
        elif "X" and "O" not in listtop2:
               listtop1.append("O")
        elif "X" and "O" not in listtop3:
               listtop3.append("O")
        elif "X" and "O" not in listmid1:
               listmid1.append("O")
        elif "X" and "O" not in listmid2:
               listmid2.append("O")
        elif "X" and "O" not in listmid3:
               listmid3.append("O")
        elif "X" and "O" not in listdown1:
               listdown1.append("O")
        elif "X" and "O" not in listdown2:
               listdown2.append("O")
        elif "X" and "O" not in listdown3:
               listdown3.append("O")
        print(listtop1,listtop2,listtop3)
        print(listmid1,listmid2,listmid3)
        print(listdown1,listdown2,listdown3)
        if "X" in listtop1 and "X" in listtop2 and "X" in listtop3:
                print("You win!")
        elif "X" in listtop1 and "X" in  listmid1 and "X" in  listdown1:
                print("You win!")
        elif "X" in listmid1 and "X" in listmid2 and "X" in  listmid3:
                print("You win!")
        elif "X" in listdown1 and "X" in listdown2 and "X" in listdown3:
                print("You win!")
        elif "X" in listtop2 and "X" in listmid2 and "X" in listdown2:
                print("You win!")
        elif "X" in listtop3 and "X" in listmid3 and "X" in listdown3:
                print("You win!")
        elif "X" in listtop1 and "X" in listmid2 and "X" in listdown3:
                print("You win!")
        elif "X" in listtop3 and "X" in listmid2 and "X" in listdown1:
                print("You win!")    
