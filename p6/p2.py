marks1= int(input("Enter your marks of subject 1: "))
marks2= int(input("Enter your marks of subject 2: "))
marks3 = int(input("Enter your marks of subject 3: "))

Total_percentage = (100*(marks1+marks2+marks3))/300

if (marks1<=33) or (marks2<=33) or (marks3<=33):
    print("You are Failed because you have less than 33 marks in one of the subjects", Total_percentage)

elif (100)*(marks1+marks2+marks3)/300>=40:
    print("You are Passed", Total_percentage)

else:
    print("You are Failed because your overall percentage is less than 40", Total_percentage)
