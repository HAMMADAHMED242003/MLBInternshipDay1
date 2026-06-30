def gradeCalculation(avg):
    if avg>=85 and avg<=100:
        print("Your Grade is A")
    elif avg>=70 and avg<85:
        print("Your Grade is B")
    elif avg>=60 and avg<70:
        print("Your Grade is C")
    else:
        print("Your Grade is F ")
        
def calculateAvg(totalSubjects):
    totalMarks=0
    for i in range(totalSubjects):
        subject = input("Enter your Subject Name")
        marks = int(input("Enter your Marks of the subject"))
        totalMarks=marks+totalMarks
    return totalMarks



name = input("Enter your Name")
studentClass = input("Enter your Class")
totalSubjects=int(input("Enter total number of subjects"))
average= calculateAvg(totalSubjects)
avg=average/totalSubjects


print("Student Name:", name)
print("Class:", studentClass)
print("Average Marks:", avg)
gradeCalculation(avg)

