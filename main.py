import time

questions = ("Which is the most closest planet to the sun?",
             "Which Animal is incapable to jump?",
             "How many bones are there in Human Body?",
            )


options = (("A.Mercury" , "B.Earth" , "C.Jupiter" ,"D.Mars" ),
           ("A.Whale","B.Elephant","C.Horse","D.Cow"),
           ("A.201","B.306","C.168","D.206"),
             )
answers = ("A","B","D")


guesses = []
score = 0
question_num = 0

print("---------------Quiz Time---------------")

for question in questions:
    print(question)
    for i in options[question_num]:
        print(i)
    guess = input("Enter Your Guess (A,B,C,D) : ")
    time.sleep(1)
    if guess.upper() == answers[question_num]:
        print()
        print(f"Yes it is correct.The answer was {guess}")
        score += 1
    else:
        print(f"Incorrect answer.The correct answer was {answers[question_num]}")
        print()
    question_num +=1


print(f"Your score is {score}")