score = float(input("Enter your score: "))
if(score >= 90 and score <= 100):
    print("Your grade is A")
elif(score >= 80 and score < 90):
    print("Your grade is B")
elif(score >= 70 and score < 80):
    print("Your garde is C")
elif(score >= 60 and score < 70):
    print("Your garde is D")
elif(score < 60):
    print("your garde is F")
else:
    print("Your score range must be between 100. Try again")