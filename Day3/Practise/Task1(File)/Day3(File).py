with open("Student.txt","w") as file:
    file.write("Hammad Ahmed")

with open("Student.txt","r") as file:
    print(file.read())

with open("Student.txt","w") as file:
    user=int(input("How many users you want to add"))
    for u in range(user):
        name=input("What is your Name: ")
        rollNumber=input("What is your Roll Number: ")
        Department=input("What is your Department: ")
        file.write(f"{name}, {rollNumber}, {Department}\n")
        
with open("Student.txt", "r") as file:
    print(file.read())

addStudent = input("Do you want to add another student? (yes/no): ").lower()

if addStudent == "yes":
    with open("Student.txt","a") as file:
        name=input("What is your Name: ")
        rollNumber=input("What is your Roll Number: ")
        Department=input("What is your Department: ")
        file.write(f"{name}, {rollNumber}, {Department}\n")
    with open("Student.txt", "r") as readFile:
        print(readFile.read())

else:
    print("Exit")

with open("Student.txt", "r") as file:
    lines = file.readlines()

print("Total Students:", len(lines))