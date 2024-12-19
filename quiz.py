Questions=(
           "1. How many elements are in periodic table? ",
           "2. What is the largest volcano in Rwanda? ",
           "3. what is the highest mountain in the World? ",
           "4. What is the largest lake in Rwanda? "
            )

options=(
         ("A. 100","B. 118","C. 130", "D. 140"),
         ("A.kalisimbi","B.Bisoke","C.Muhabura","D.Jali"),
         ("A.Kalisimbi","B.Everest","C.Kilimanjaro","D.Jali"),
         ("A. Cyohoha","B. Rweru","C. Ruhondo","D. Kivu" ),
         )

Guess=[]
Score=0
Questions_num=0
Answer_num=0
Answers=("C","A","B","D")

for question in Questions:
    print("____________________________________________________")
    print(question)
    for option in options[Questions_num]:
        print (option)
    Guesses=input("Enter A,B,C,D or Click Q to quit: ").upper()
    if Guesses==Answers[Questions_num]:
        Score+=5
        print("Correct!!!")
    elif Guesses.lower()=="q":
        print("feel bad to see you going ")
        break
    else:
        print("Incorrect answer ")
    Questions_num+=1
    Guess.append(Guesses)
    
print("_____________________Results__________________________")

print()
if Score==int(20):
    print(f" your scores are {Score}/20")
    print ("you got Excelent scores 👏💚")
elif Score==int(15):
    print(f"You have got {Score}/20")
    print(" that is Great 🤫")


else:
    print(f" your scores are {Score}/20")
    print(" please Keep Pushing Dont be discouraged")
    print("the true answers were the following")
    for answer in Answers:
        print(f"{answer}")
    
                       

print()

       
print()
print("see you in the next quizz👋")

