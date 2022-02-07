#Ques 1
print("Question 1")
string=input("Enter The String:\n") # Input of String is taken from user
list_Word=string.split() #The words/word is stored in list using split function
dict_name={} #A Dictionary is created

#Check if entered string is single word or multiple words
if(len(list_Word)==1):
    for ch in list_Word[0]:   # A loop is created in case single word is entered to get the frequency of characters in word
        if(ch not in dict_name): # Condition is being checked whether the given word is present in dictionary or not
            dict_name[ch]=1      # if not create a key and assign it value equal to 1
        else:
            dict_name[ch]=dict_name[ch]+1  # if yes increment the value of the given key by 1
    for key in dict_name:
        print(key,dict_name[key])  # The frequency of characters are printed which are there in given word using print function
elif(len(list_Word)>1):
    for word in list_Word:    # A loop is created in case of multiple words to get the frequency of words in string
        if(word not in dict_name): # Condition is being checked whether the given word is present in dictionary or not
            dict_name[word]=1    # if not create a key and assign it value equal to 1
        else:
            dict_name[word]=dict_name[word]+1 # if yes increment the value of the given key by 1
    for key in dict_name:
        print(key,dict_name[key]) # Frequency of the words in a given string is printed using print function
print(end="\n")  # executing the other functions on new line

#Ques 2
print("Question 2")

day=int(input("Day-")) # Take The day as input from user
month=int(input("Month-")) #Take the month as input from user
year=int(input("Year-"))#Take the year as input from user
month_30=[4,6,9,11] #The list of months having 30 days
month_31=[1,3,5,7,8,10] #the list of months having 31 days
month_dec=12 #the December month is taken seperately

if(year>=1800 and year<=2025):
    if (year % 100 == 0 and year % 400 == 0):  # conditional is applied to check for leap yaer in case of year which are multiple of hundred
        if month == 2:  # to check whether input month if feb or month=2

            if day == 29:  # in feb there are 29 days in leap year so to check whether the day is 29
                print("1/0" + str(month + 1) + "/" + str(year))  # the first day of next month is printed
            elif(day>=1 and day<29):
                print(str(day + 1) + "/0" + str(month) + "/" + str(year))  # the next day of given month is printed
        elif month in month_31:  # if the month is containing 31 days
            if day == 31:  # if the day is last day of month
                if (month + 1 < 10):  # Conditional added to check if next month is less than 10
                    print("1/0" + str(month + 1) + "/" + str(year))  # the first day of next month is printed
                else:
                    print("1/" + str(month + 1) + "/" + str(year))  # the first day of next month is printed
            elif(day>=1 and day<31):
                if (month < 10):  # Conditional added to check if given month is less than 10
                    print(str(day + 1) + "/0" + str(month) + "/" + str(year))  # the next day of given month is printed
                else:
                    print(str(day + 1) + "/" + str(month) + "/" + str(year))  # the next day of given month is printed
        elif month in month_30:  # if the month is containing 30 days

            if day == 30:  # if the day is last day of month

                if (month + 1 < 10):  # Conditional added to check if next month is less than 10

                    print("1/0" + str(month + 1) + "/" + str(year))  # the first day of next month is printed

                else:

                    print("1/" + str(month + 1) + "/" + str(year))  # the first day of next month is printed

            elif(day>=1 and day<30):

                if (month < 10):  # Conditional added to check if given month is less than 10
                    print(str(day + 1) + "/0" + str(month) + "/" + str(year))  # the next day of given month is printed
                else:
                    print(str(day + 1) + "/" + str(month) + "/" + str(year))  # the next day of given month is printed
        elif month == 12:  # if the month is last month of year
            if day == 31:  # if the day is last day of the given month
                print("1/01/" + str(year + 1))  # the first day of the first month of next year is printed
            elif(day>=1 and day<31):
                print(str(day + 1) + "/" + str(month) + "/" + str(year))  # the next day of given month is printed

    elif (year % 100 == 0 and year % 400 != 0):  # conditional is applied to check for non leap yaer in case of year which are multiple of hundred
        if month == 2:  # to check whether input month if feb or month=2

            if day == 28:  # in feb there are 29 days in leap year so to check whether the day is 29
                print("1/0" + str(month + 1) + "/" + str(year))  # the first day of next month is printed
            elif (day >= 1 and day < 28):
                print(str(day + 1) + "/0" + str(month) + "/" + str(year))  # the next day of given month is printed
        elif month in month_31:  # if the month is containing 31 days
            if day == 31:  # if the day is last day of month
                if (month + 1 < 10):  # Conditional added to check if next month is less than 10
                    print("1/0" + str(month + 1) + "/" + str(year))  # the first day of next month is printed
                else:
                    print("1/" + str(month + 1) + "/" + str(year))  # the first day of next month is printed
            elif (day >= 1 and day < 31):
                if (month < 10):  # Conditional added to check if given month is less than 10
                    print(str(day + 1) + "/0" + str(month) + "/" + str(year))  # the next day of given month is printed
                else:
                    print(str(day + 1) + "/" + str(month) + "/" + str(year))  # the next day of given month is printed
        elif month in month_30:  # if the month is containing 30 days

            if day == 30:  # if the day is last day of month

                if (month + 1 < 10):  # Conditional added to check if next month is less than 10

                    print("1/0" + str(month + 1) + "/" + str(year))  # the first day of next month is printed

                else:

                    print("1/" + str(month + 1) + "/" + str(year))  # the first day of next month is printed

            elif (day >= 1 and day < 30):

                if (month < 10):  # Conditional added to check if given month is less than 10
                    print(str(day + 1) + "/0" + str(month) + "/" + str(year))  # the next day of given month is printed
                else:
                    print(str(day + 1) + "/" + str(month) + "/" + str(year))  # the next day of given month is printed
        elif month == 12:  # if the month is last month of year
            if day == 31:  # if the day is last day of the given month
                print("1/01/" + str(year + 1))  # the first day of the first month of next year is printed
            elif (day >= 1 and day < 31):
                print(str(day + 1) + "/" + str(month) + "/" + str(year))  # the next day of given month is printed

    elif (year % 100 != 0 and year % 4 == 0):  # conditional is applied to check for leap yaer in case of year which are not multiple of hundred
        if month == 2:  # to check whether input month if feb or month=2

            if day == 29:  # in feb there are 29 days in leap year so to check whether the day is 29
                print("1/0" + str(month + 1) + "/" + str(year))  # the first day of next month is printed
            elif (day >= 1 and day < 29):
                print(str(day + 1) + "/0" + str(month) + "/" + str(year))  # the next day of given month is printed
        elif month in month_31:  # if the month is containing 31 days
            if day == 31:  # if the day is last day of month
                if (month + 1 < 10):  # Conditional added to check if next month is less than 10
                    print("1/0" + str(month + 1) + "/" + str(year))  # the first day of next month is printed
                else:
                    print("1/" + str(month + 1) + "/" + str(year))  # the first day of next month is printed
            elif (day >= 1 and day < 31):
                if (month < 10):  # Conditional added to check if given month is less than 10
                    print(str(day + 1) + "/0" + str(month) + "/" + str(year))  # the next day of given month is printed
                else:
                    print(str(day + 1) + "/" + str(month) + "/" + str(year))  # the next day of given month is printed
        elif month in month_30:  # if the month is containing 30 days

            if day == 30:  # if the day is last day of month

                if (month + 1 < 10):  # Conditional added to check if next month is less than 10

                    print("1/0" + str(month + 1) + "/" + str(year))  # the first day of next month is printed

                else:

                    print("1/" + str(month + 1) + "/" + str(year))  # the first day of next month is printed

            elif (day >= 1 and day < 30):

                if (month < 10):  # Conditional added to check if given month is less than 10
                    print(str(day + 1) + "/0" + str(month) + "/" + str(year))  # the next day of given month is printed
                else:
                    print(str(day + 1) + "/" + str(month) + "/" + str(year))  # the next day of given month is printed
        elif month == 12:  # if the month is last month of year
            if day == 31:  # if the day is last day of the given month
                print("1/01/" + str(year + 1))  # the first day of the first month of next year is printed
            elif (day >= 1 and day < 31):
                print(str(day + 1) + "/" + str(month) + "/" + str(year))  # the next day of given month is printed

    elif (year % 100 != 0 and year % 4 != 0):  # conditional is applied to check for leap yaer in case of year which are not multiple of hundred
        if month == 2:  # to check whether input month if feb or month=2

            if day == 28:  # in feb there are 29 days in leap year so to check whether the day is 29
                print("1/0" + str(month + 1) + "/" + str(year))  # the first day of next month is printed
            elif (day >= 1 and day < 28):
                print(str(day + 1) + "/0" + str(month) + "/" + str(year))  # the next day of given month is printed
        elif month in month_31:  # if the month is containing 31 days
            if day == 31:  # if the day is last day of month
                if (month + 1 < 10):  # Conditional added to check if next month is less than 10
                    print("1/0" + str(month + 1) + "/" + str(year))  # the first day of next month is printed
                else:
                    print("1/" + str(month + 1) + "/" + str(year))  # the first day of next month is printed
            elif (day >= 1 and day < 31):
                if (month < 10):  # Conditional added to check if given month is less than 10
                    print(str(day + 1) + "/0" + str(month) + "/" + str(year))  # the next day of given month is printed
                else:
                    print(str(day + 1) + "/" + str(month) + "/" + str(year))  # the next day of given month is printed
        elif month in month_30:  # if the month is containing 30 days

            if day == 30:  # if the day is last day of month

                if (month + 1 < 10):  # Conditional added to check if next month is less than 10

                    print("1/0" + str(month + 1) + "/" + str(year))  # the first day of next month is printed

                else:

                    print("1/" + str(month + 1) + "/" + str(year))  # the first day of next month is printed

            elif (day >= 1 and day < 30):

                if (month < 10):  # Conditional added to check if given month is less than 10
                    print(str(day + 1) + "/0" + str(month) + "/" + str(year))  # the next day of given month is printed
                else:
                    print(str(day + 1) + "/" + str(month) + "/" + str(year))  # the next day of given month is printed
        elif month == 12:  # if the month is last month of year
            if day == 31:  # if the day is last day of the given month
                print("1/01/" + str(year + 1))  # the first day of the first month of next year is printed
            elif (day >= 1 and day < 31):
                print(str(day + 1) + "/" + str(month) + "/" + str(year))  # the next day of given month is printed
else:
    print("Year Out of Range")

print(end="\n")  # executing the other functions on new line


#Ques 3
print("Question 3")
# The Numbers of which the tuple of squares is to be created
num=input("Enter The numbers of which you want square of seperated by comma:\n") #Taking the numbers as input from user
list_num=num.split(',') #creating a list containg the numbers using split function
list_square=[] # creating a new list to store the tuples of number and its square

for item in list_num: # a loop is created to add tuple of the square of number and the number itself
    list_square.append((float(item),float(item)**2))

print(list_square) #print the list of tuples of number and the square of numbers
print(end="\n")  # executing the other functions on new line


#Ques 4
print("Question 4")
#Take a While loop to check if grade point is in range of 4 to 10 (both inclusive)
while(True):
     grade_point=int(input("Enter Grade Points:\n")) # Taking grade point as input from user
     #Creating a dictionary where the keys are CGPA and the values are the remarks and the grade
     dict_grade={10:['A+','Outstanding'],9:['A','Excellent'],8:['B+','Very Good'],7:['B','Good'],6:['C+','Average'],5:['C','Below Average'],4:['D','Poor']}
     if(grade_point<4 or grade_point>10 or (grade_point not in dict_grade.keys())): # The conditional is applied to check whether grade point is there or not in dictionary
           print("Grade Out Of Range") #Print function is used to tell that grade point is out of range
           continue #Thus the user will have to enter the grade point again
     else:
           print("Your Grade is '"+str(dict_grade[grade_point][0])+"' and",dict_grade[grade_point][1],"Performance")
           #print function is used to print grade and performance corresponding to that grade point
           break #the loop is exited through break
print(end="\n")  # executing the other functions on new line


#Ques 5
#Since the output has to be a certain pattern only thus n=6 satisfy the pattern
print("Question 5")
for i in range(6):
    for j in range(i):
        print(" ",end="") # This loop is used for creating space from left
    for k in range(2*(6-i)-1):
        print(chr(65+k),end="") #This loop uses the ASCII Values of A,B,C,D,...which starts from 65 and chr function is used to print the character corresponding to the integer
    for l in range(i):
        print(" ",end="") #This loop is used to create space from right
    print(end='\n') # it is used to create a new line
print(end="\n")  # executing the other functions on new line


#Ques 6
print("Question 6")
sid_name={} #Made the list that will be used to store SID and name of students
true_list=['Y','y']#Creating a True List in case user enters y in place of Y
false_list=['N','n']# Creating a False List in case user enters n in case of N
while(True):
    dec=input("Do You Want To Enter The SID and Name of Student: Y for Yes and N for No:\n")#Taking Input from user whether He/she wants to update SID and Name in Dictionary
    if dec in true_list: # If user entered Yes then the following statments are executed
        sid=int(input("Enter SID of Student:\n")) # Taking SID as input from user
        name=input("Enter The Name of Student:\n") # Taking Name as input from user
        sid_name[sid]=name #Updated the Dictionary with SID and Name of Student
        continue
    else: # Else The Dictionary Wont be updated anymore and the loop will be exited
        break

copylist=sid_name   #Made a copy list of the given list
# A part
for key in sid_name: #The loop is applied to print the SID and name corresponding to that SID
    print(key,sid_name[key]) #The SID and Name of student are printed
#B part
#Sorting a dictionary with respect to name
dict_sort_name={} #the new dictionary is created
list_sid2=list(sid_name.keys()) # another list is created to store SID
list_name2=list(sid_name.values()) # another list is created to store names
list_name2.sort() #the list containing names is sorted with ASCII Standards

for name in list_name2:#the loop is created to traverse through list containing name
    for sid in list_sid2:#the loop is created to traverse through list containing SID
        if(sid_name[sid]==name): #the conditional is created to check whether name is there corresponding to that SID
            dict_sort_name[sid]=name# the name is added to new dictionary corresponding to that SID
print("Old Dictionary:",sid_name) # the original dictionary before being sorted is printed
sid_name=dict_sort_name # the content of new dictionary is copied in original one
print("Sorted Dictionary with respect to name:",sid_name) #the original dictionary after being sorted is printed
sid_name=copylist #reassigning old values of original dictional through a copy list created before

# C part
#Sorting the dictionary with respect to SID
dict_sort_sid={} # A new dictionary is created
list_sid=list(sid_name.keys()) # storing the SID in new list
list_name=list(sid_name.values()) #storing the names in new list
list_sid.sort() #the list containg SID is sorted

for sid in list_sid: #the loop is created to traverse through list containing SID
    for name in list_name: #the loop is created to traverse through list containing name
        if(sid_name[sid]==name): #the conditional is created to check whether name is there corresponding to that SID
            dict_sort_sid[sid]=name # the name is added to new dictionary corresponding to that SID
print("Old Dictionary:",sid_name) # the original dictionary before being sorted is printed
sid_name=dict_sort_sid # the content of new dictionary is copied in original one
print("Sorted Dictionary with respect to SID:",sid_name) #the original dictionary after being sorted is printed
#reassigning old values of original dictional through a copy list created before
sid_name=copylist



# D part
#The Name corresponding to that SID is printed
n=int(input("Enter the SID of Student You Want Name of:")) #The SID is taken from user
print(sid_name[n])#Name corresponding to that SID is printed

print(end="\n")  # executing the other functions on new line

#Ques 7
print("Question 7")
list_recursion=[0,1] # A List is created containing the first two elements of fibonacci sequence
n=int(input("Enter The Number Til Which You Want Sequence:\n")) # Taking input of number of terms user want
a1=0 # Declaring the first element
a2=1 # Declaring The Second Element

for i in range(n-2): # Created a loop to add the further terms in sequence
    temp=a1+a2 # another variable is created to get the value of previous two terms
    list_recursion.append(temp) # the temp variable is then added to the recursion list
    a1=a2 # then the value of 2nd term is assigned to first term
    a2=temp # the value of temp or 3rd term is assigned to 2nd variable

print("Terms of Fibonacci Sequence:",list_recursion) #print function is used to print the terms of fibonacci sequence till the given input
print("Average of Terms in Fibonacci Sequence:",(sum(list_recursion))) # print function is used to print the average of terms in fibonacci sequence
#sum function is used to calculate the sum of numbers in list and then it is divided by n which is input from user
print(end="\n")  # executing the other functions on new line

#Ques 8
print("Question 8")
Set1={1,2,3,4,5} #Given Sets in Question
Set2={2,4,6,8}
Set3={1,5,9,13,17 }
Set_10={1,2,3,4,5,6,7,8,9,10} # Additional Set of first 10 natural numbers is created

#A part
Set_a=Set1^Set2 #Set containing elements present in Set1 or Set2 but not both
print(Set_a) # The Set_a is printed

#B part
Set_commonall=Set1&Set2&Set3 # Created a set which contains elements common to all
Set_b=Set1^Set2^Set3 #Set containing elements which are present in only one set at a time
print(Set_b) # The Set_b is printed

#C Part
Set_c=((Set1&Set2)-Set_commonall)|((Set2&Set3)-Set_commonall)|((Set3&Set1)-Set_commonall) #Set is created containg elements which are present in two sets only
print(Set_c) # Set_c is printed

#D Part
Set_d=Set_10-Set1 # Set is created which contains natural numbers upto 10 which are not in Set1
print(Set_d) # Set_d is printed

#E Part
Set_union=(Set1|Set2|Set3) #Another Set is created which is having elements common to all given three sets in question
Set_e=Set_10-Set_union # Set is created which contain natural number upto 10 which are not there in Set 1,2,3
print(Set_e) # Set_e is printed
print(end="\n")  # executing the other functions on new line

