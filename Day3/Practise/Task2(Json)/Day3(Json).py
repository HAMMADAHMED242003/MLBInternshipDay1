import json

user=int(input("How many students do you want to add?"))
studentList=[]
for i in range(user):
    name=input("What is your Name: ")
    rollNumber=input("What is your Roll Number: ") 
    department=input("What is your Department: ")
    student={
        "Name":name,
        "RollNumber":rollNumber,
        "Department":department
    }
    studentList.append(student)

with open("Student.json","w") as file:
    json.dump(studentList,file,indent=4)

with open("Student.json","r") as file:
    data=json.load(file)
    print(data)

updateUser=input("Enter Roll Number to update: ")

for student in data:
    if (updateUser == student["RollNumber"]):
        print("Enter the updated department: ")
        department=input("What is your Department: ")
        student["Department"]=department
with open("Student.json","w") as file:
    json.dump(data,file,indent=4)

addStudent=input("Do you want to add another student? (yes/no): ")
if (addStudent=="yes"):
    name=input("What is your Name: ")
    rollNumber=input("What is your Roll Number: ") 
    department=input("What is your Department: ")
    student={
        "Name":name,
        "RollNumber":rollNumber,
        "Department":department
    }
    data.append(student)

    with open("Student.json","w") as file:
        json.dump(data,file,indent=4)

else:
    print("Program Ended")

