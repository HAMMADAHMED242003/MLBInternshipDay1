
#############################################TOPIC LIST#########################################################
#Largest number
def largestNumber(numbers):
    largest=numbers[0]
    for num in numbers:
        if num>largest:
            largest=num
    return largest

#SecondLargest number   
def secondLargestNumber(number):
    largestNumber=number[0]
    secondLargestNumber=number[0]
    for num in number:
        if num>largestNumber:
            secondLargestNumber=largestNumber
            largestNumber=num
        elif num>secondLargestNumber and num!=largestNumber:
            secondLargestNumber=num
    return secondLargestNumber

#Remove The Duplicates
def removeDuplicates(number):
    newlist=[]
    for i in number:
        if i not in newlist:
            newlist.append(i)
    return newlist

#Reverse the list
def reverseList(num):
    reversedarray=num[::-1]
    return reversedarray

#Finding the common elements
def commonElements(list1,list2):
    result=[]
    for i in list1:
        if i in list2:
            result.append(i)
    return result


number=[1,2,3,4,5,5,6]

list1=[1,2,3,4]
list2=[1,3,5]

large=largestNumber(number)
secondLarge=secondLargestNumber(number)
duplicateRemove=removeDuplicates(number)
reversed=reverseList(number)
common=commonElements(list1,list2)

print("\nFirst largest number is: ", large)
print("Second largest number is: ", secondLarge)
print("Remove duplicate elements: ", duplicateRemove)
print("Reverse list: ", reversed)
print("Common Elements in a list: ", common)

#############################################TOPIC TUPLE#########################################################

#Occurance of Elements
Number=(1,2,3,4,2,5,2)
occurance=Number.count(2)
print("Occurance of element 2 is: ",occurance)
print("\n")


#Convert Tuple to List 
myTuple=("Apple","banana","Grapes")
convertToList=list(myTuple)
print("From tuple to list:",convertToList)
print(type(convertToList))

#Convert List to Tuple
myList=["Apple","banana","Grapes"]
convertToTuple=tuple(myList)
print("From list to Tuple:",convertToTuple)
print(type(convertToTuple))
print("\n")


############################################# TOPIC SET #########################################################

myList=[1,2,3,3,4,5,6]
mySet=set(myList)
print(mySet)

#Union And Intersection
mySet1={1,2,3,4}
mySet2={4,5,6,7,8}
unionSet=mySet1.union(mySet2)
intersctionSet=mySet1.intersection(mySet2)

print("Union of both sets are: ",unionSet)

print("Intersection of both sets are: ",intersctionSet)
print("\n")



############################################# TOPIC Dictionary #########################################################

#Student Record
student = {
    "name":"Hammad Ahmed",
    "Age":22,
    "Degree":"Software Engineering"
}

print(student["name"])


#Calculate Average
marks={
    "Ali":85,
    "Ahmed":75,
    "Hasan":95,
}
total=0
for num in marks.values():
    total+=num
avg=total/len(marks)
print("Average Marks:",avg)


#Words COunt in a sentence
sentence="I love Python and I love AI"
words=sentence.split()

frequency={}
for i in words:
    if i in frequency:
        frequency[i] += 1
    else:
        frequency[i] = 1

print(frequency)

