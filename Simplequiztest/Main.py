SCORE = []
while True:
 import random
 Quizstart = input("It's very nice to meet you! Now let's quiz you math problems! Do you want to play? Y = Yes, N = No:")
 if Quizstart == "Y":
    quiz1 = (random.randrange(0,60))
    quiz2 = (random.randrange(0,60))
    ringhtquestion = quiz1 * quiz2
    wque = quiz1 * quiz2 + (random.randrange(0,70))
    qeew = quiz1 * quiz2 + (random.randrange(70,10000))
    qisj = quiz1 * quiz2 + (random.randrange(1,999))
    quiz = input (f"OK, question 1, what is:{quiz1}*{quiz2}? A.{ringhtquestion}, B.{wque},C.{qeew},D.{qisj}:")
    if quiz == "A":
          print(f"You are so smart!, The answer was {quiz}!")
          SCORE.append("I")
          print(SCORE)
    else: 
        print(f"sorry,{quiz},""is not the right answer")
        print(SCORE)

 elif Quizstart == "N":
    print("Ok bye")
    break
 else:
    print(f"{Quizstart}, is not  either Y or N")


