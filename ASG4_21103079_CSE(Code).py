#Ques 1
#Tower Of Hanoi
print("Question 1")
print("Tower Of Hanoi with 3 disks")
# A recursive function is made to print procedure of Tower of Hanoi
def TowerOfHanoi(n,source,destination,auxiliary):
    if(n==1): #if n=1 ie the last disk, move it from source to destination point
        print("Move Disk "+str(1)+" from "+str(source)+" to "+str(destination))
    else: #else move a single disk from source to auxiliary first
        TowerOfHanoi(n-1,source,auxiliary,destination)
        print("Move Disk " + str(n) + " from " + str(source) + " to " + str(destination))
        # Move the same disk from auxiliary to the destination point
        TowerOfHanoi(n-1,auxiliary,destination,source)
#The Function is called for 3 disks having A as source, B as auxiliary point, C as destination point

TowerOfHanoi(3,'A','C','B')
print()


#Ques 2
#Pascal Triangle Iterative Approach
print("Question 2")
# A Factorial function is defined for a given number using recursion
def factorial(n):
    if(n==0 or n==1): #If N=1 or 0 return 1
        return 1
    else: #else return the factorial of n
        return n*factorial(n-1)

#No of rows taken as input from user
row=int(input("Enter The Row Till Which You want Pascal triangle:\n"))
print("Pascal Triangle With Iterative Approach:")
#a for loop is made for getting pattern of different rows
for i in range(-1,row):
    #a for loop is made for creating gaps
    for j in range(row-i-1):
        print(" ",end='')
    # a for loop is created to print gaps
    for k in range(2*i+3):
        if(k%2==0): # At even places only the digits will be printed
            print(factorial(i+1)//(factorial(k//2)*factorial(i+1-(k//2))),end='')
        else: # At odd places the space will be there
            print(" ",end='')
    # Again a for loop created for spaces
    for l in range(row-i-1):
        print(" ",end='')
    print(end='\n')



# Pascal Triangle Recursive Approach
# A function is made to call and create a list of pascal triangle elements
def pascaltriangle(n):

    if n == 0: # return the empty list if n=0
        return []

    elif n == 1: # return the list with element 1 as a base
        return [1]

    else: #return the list of element of pascal triangle with list in a list
        new_row = [1]
        last_row = pascaltriangle(n-1)
        for k in range(len(last_row)-1):
            new_row.append(last_row[k] + last_row[k+1])
        new_row += [1]
    return new_row

# using a loop to print the pascal triangle
print("Pascal Triangle using Recursion:")
for i in range(1, row + 2):
    print(" "*(row+1-i),end="")
    for item in pascaltriangle(i):
        print(item,end=" ")
    print(" "*(row+1-i),end="")
    print(end='\n')

print()



#Ques 3
print("Question 3")
# A Function is made to return quotient and remainder
def quorem(a1,a2):
    quotient=a1//a2
    remainder=a1%a2
    return [quotient,remainder]

#Taking the input of numbers from user
num_1=int(input("Enter the number You want to divide:\n"))
num_2=int(input("Enter the number you want to divide the previous number with:\n"))
#Check Whether The Function is callable
print("If The Function Is Callable:\n",callable(quorem))
print()

#A variable list is created to store the quotient,remainder
quo_rem=quorem(num_1,num_2)
#The Quotient and remainder are printed
print("Quotient is",quo_rem[0])
print("Remainder is",quo_rem[1])
print()

#Check Whether all the values are non zeroes
if(num_1==0):
    print("1st Number is Zero")
elif(num_1!=0):
    print("1st Number is Non-Zero")
print()
if(num_2==0):
    print("2nd Number is Zero")
elif(num_2!=0):
    print("2nd Number is Non-Zero")
print()
if(quo_rem[0]==0):
    print("Quotient is Zero")
elif(quo_rem[0]!=0):
    print("Quotient is Non-Zero")
print()
if(quo_rem[1]==0):
    print("Remainder is Non-Zero")
elif(quo_rem[1]!=0):
    print("Remainder is Non-Zero")
print()

#Adding [4,5,6] to the result and filtered out values greater than 4
#List is created containing 4,5,6 as elements
l1=[4,5,6]
for item in l1:
    quo_rem.append(item)
print("List Containing [4,5,6]:",quo_rem)
print()
# Filtered Out the Values greater than 4
list2=[] #Another Blank List Creted to store the filtered list
for item in quo_rem:
    if(item >4):
        list2.append(item)
quo_rem.clear() # The Previous list is cleared


for item in list2: # Adding the filtered list to the original one
    quo_rem.append(item)

print("Filtered List:",quo_rem)
print()
#Converting the result obtained to set
print("The List of results is converted to set:")
quo_rem=set(quo_rem)
print(quo_rem)
print()
#Making the Set immutable
print("The Set is Frozen:")
quo_rem=frozenset(quo_rem)
print(quo_rem)
print()


#Finding Out the maximum value in the set obtained
max_value=max(quo_rem)
#Printing the maximum value and hash value of maximum value
print("Maximum Value in the obtained Set is:",max_value)
print("The Hash Value of Maximum Value obtained is:",hash(max_value))
print()

#Ques 4
print("Question 4")
class Student:

    def __init__(self, name, roll_number): # constructor is used to create object by taking input
        self.name = name
        self.roll_number = roll_number
        print("Object is created with "+self.name+" as Name and "+str(self.roll_number)+" as roll number" )
    def __del__(self):#A destructor is used to delete object
        print("Object is deleted") # A print statement is added to show that object is deleted


# create a object named stu_1 containing name and roll no of student
stu_1 = Student("Ujjawal", 21103079)
# delete the object
del stu_1
print()


#Ques 5
#Created an Employee Class
print("Question 5")
class Employee:
    def __init__(self, name, salary): # A constructor is called to store the serial no, name, salary of employee given by user

        self.name = name
        self.salary = salary



# 3 objects are created using the data given in table containing the name and salary of employee
employee_1 = Employee("Mehak", 40000)
employee_2 = Employee("Ashok", 50000)
employee_3 = Employee("Viren", 60000)

#Two print statement are added to show the change in salary
print(employee_1.salary,"is the existing salary of Mehak")
employee_1.salary=70000 #Updating the value of salary component of employee_1 object basically of Mehak to 70000
print(employee_1.salary,"is the updated salary of Mehak")
# delete the employee Viren
print("Deleting The Object containing Viren as name")
del employee_3
print()



#Ques 6
#To make anagram of a given word the recursive function is made
print("Question 6")
def anagramsstring(string):
    # if the string is blank return an empty list
    if string == "":
        return [string]
    else:#the else conditional is added to store the anagrams of a given word
        ans = [] # A blank list is made to store anagrams
        for i in anagramsstring(string[1:]):
            for pos in range(len(i)+1):
                ans.append(i[:pos]+string[0]+i[pos:])
        return ans # the list is returned


# take word as input
word = input("Enter the word that George spoke: ")
# the function is called to store the list of anagram in another variable
possible_words=anagramsstring(word)
print("Possible words for the spoken word are")
for item in possible_words: # a for loop is used to print the anagrams of a given word
    print(item)
print()





