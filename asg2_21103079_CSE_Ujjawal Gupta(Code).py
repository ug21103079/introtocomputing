#Assignment 2
#Ques1
print("Question 1")
input_str="Python is a case sensitive language"
# a)Length of string
print("A Part")
length=len(input_str)
print(length)
# b)Reverse the order of string
print("B Part")
print(input_str[::-1])
# c)Slice Function to obtain "a case sensitive"
print("C Part")
#Length of substring to be stored
length_substring=len("a case sensitive")
#Initial letter index
initialofsubstring=input_str.index('a')
sliced=slice(initialofsubstring,initialofsubstring+length_substring)
#storing of substring
slice_str=input_str[sliced]
print(slice_str)
# d)Replace "a case sensitive" with "object oriented"
print("D Part")
print(input_str.replace('a case sensitive','object oriented'))
# e)Finding index of substring 'a'
print("E Part")
ind=input_str.find('a')
print(ind)
# f)Remove the white spaces from the given input string
print("F Part")
print(input_str.replace(' ',''))



#Ques 2
print("Question 2")
name="Ujjawal Gupta"
sid="21103079"
dept_name="CSE"
cgpa="9.9"
print("Hey,",name,"Here!")
print("My SID is",int(sid))
print("I am from",dept_name,"department and my CGPA is",float(cgpa))


#Ques3
print("Question 3")
a=56
b=10
#Printing value of a&b
print("a&b:",a&b)
#Printing value of a|b
print("a|b:",a|b)
#Printing value of a^b
print("a^b:",a^b)
#Printing value of left shift of a and b by 2 bits
print("Left Shift of a by 2 bits:",a<<2,"Left shift of b by 2 bits:",b<<2)
#Printing value of right shift of a by 2 bits and right shift of b by 4 bits
print("Right Shift of a by 2 bits:",a>>2,"Right shift of b by 4 bits:",b>>4)


#Ques 4
print("Question 4")
a=int(input("Enter 1st Number:\n"))
b=int(input("Enter 2nd Number:\n"))
c=int(input("Enter 3rd Number:\n"))
print("The Greatest Number is:")
if(a>=b and a>=c):
    print(a)
elif(b>=a and b>=c):
    print(b)
elif(c>=a and b>=a):
    print(c)


#Ques 5
print("Question 5")
#Enter The String
input_string=input("Enter A String:\n")
#Conditionals to check if "name" is there in input
if('name' in input_string):
    print("Yes")
else:
    print("No")


#Ques 6
print("Question 6")
#Taking input from user
a=int(input("Enter The Side 1:\n"))
b=int(input("Enter The Side 2:\n"))
c=int(input("Enter the Side 3:\n"))
print("If the triangle can be formed?")
if(a+b>c and c+a>b and b+c>a):
    print("Yes")
else:
    print("No")





