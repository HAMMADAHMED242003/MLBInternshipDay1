import json

def showRollNumbers():
    print("Available Roll Numbers:")
    for student in data:
        print(student["RollNumber"])


with open("Student.json","r") as file:
    data=json.load(file)
    print(data)

choice=True
while(choice):
    print("\n========== Student Record Management ==========")
    print("1. View Students")
    print("2. Add Student")
    print("3. Update Student")
    print("4. Search Student")
    print("5. Delete Student")
    print("0. Exit")

    try:
        userChoice=int(input("Enter the function Number: "))
    except ValueError:
        print("Invalid Input")
        continue
    

    if (userChoice==1):
        for student in data:
            print(f"Name        : {student['Name']}")
            print(f"Roll Number : {student['RollNumber']}")
            print(f"Department  : {student['Department']}\n")
    elif (userChoice==2):
        user=int(input("How many students do you want to add?"))
        
        for i in range(user):
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
            print("Student Added Successfully")

    elif (userChoice==3):
        updateUser=input("Enter Roll Number to update: ")
        found=False

        for student in data:
            if (updateUser == student["RollNumber"]):
                print("Enter the updated department: ")
                department=input("What is your Department: ")
                student["Department"]=department
                found=True
                print("Student Department updated successfully.")
                break
        if found:
            with open("Student.json","w") as file:
                json.dump(data,file,indent=4)
        else:
            print("Student not found.")
            showRollNumbers()
    elif (userChoice==4):
        searchUser=input("Enter Roll Number to Search: ")
        found=False
        for student in data:
            if (searchUser == student["RollNumber"]):
                print(f"Name        : {student['Name']}")
                print(f"Roll Number : {student['RollNumber']}")
                print(f"Department  : {student['Department']}")
                found=True
                break
        if not found:
            print("Student not found.")
            showRollNumbers()

    elif (userChoice==5):
        deleteUser=input("Enter Roll Number to Delete: ")
        found=False
        for student in data:
            if (deleteUser == student["RollNumber"]):
                data.remove(student)
                print("Student deleted Successfully")
                found=True
                break
        if found:
            with open("Student.json","w") as file:
                json.dump(data,file,indent=4)
        else:
            print("Student not found.")
            showRollNumbers()  

    elif (userChoice==0):
        print("Exit the menu")
        choice=False
    else:
        print("Invalid Choice,Try again")