#Question 1
print("Question 1")
#enter the 3 numbers
num1=int(input("Enter The 1st Number:\n"))
num2=int(input("Enter The 2nd Number:\n"))
num3=int(input("Enter The 3rd Number:\n"))
#store the average of 3 numbers in average variable
average=(num1+num2+num3)/3
#print average of 3 numbers
print("Average=",average)

#Question 2
print("Question 2")
#enter the gross income and number of dependent
Gross_income=float(input("Enter The Gross Income:\n$"))
Num_dependent=int(input("Enter The Number Of Dependent:\n"))
Standard_Deduction=10000
Deduction_dependent=Num_dependent*3000
Taxable_income=float(Gross_income)-Standard_Deduction-Deduction_dependent
#calculate tax
Tax=(Taxable_income*20)/100
#print the tax
print("Tax=$"+str(Tax))

#Question 3
print("Question 3")
#Enter The Required Fields
SID=int(input("Enter The Student's SID:\n"))
Name=input("Enter The Student's Name:\n")
Gender=input("The Student's Gender:\nEnter F for Female\nEnter M for Male\nEnter U if Gender is Unknown\n")
Course_Name=input("Enter the Course taken by Student:\n")
CGPA=float(input("Enter The Student CGPA:\n"))
Student=[SID,Name,Gender,Course_Name,CGPA]
#print list
print(Student)

#Question 4
print("Question 4")
#Enter the marks of 5 students
num1=int(input("Enter The Marks Of 1st Student:\n"))
num2=int(input("Enter The Marks Of 2nd Student:\n"))
num3=int(input("Enter The Marks Of 3rd Student:\n"))
num4=int(input("Enter The Marks Of 4th Student:\n"))
num5=int(input("Enter The Marks Of 5th Student:\n"))
#inserting the marks of 5 students in list
list=[num1,num2,num3,num4,num5]
#print list before sorting
print("Before Sorting the list\n",list)
#sorting the list
list.sort()
#print the list after sort
print("After Sorting the list\n",list)

#Question 5(a)
print("Question 5(a)")
Colour=['Red','Green','White','Black','Pink','Yellow']
#removed element at 4th position
Colour.remove(Colour[3])
#print the list
print(Colour)

#Question 5(b)
print("Question 5(b)")
Colour=['Red','Green','White','Black','Pink','Yellow']
#remove black and pink from the list,added purple in the list and printed the list
Colour.remove('Black'),Colour.remove('Pink'),Colour.insert(3,'Purple'),print(Colour)
