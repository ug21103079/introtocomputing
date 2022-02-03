#Ques 1
string=input()
list_Word=string.split()
dict_name={}
if(len(list_Word)==1):
    for ch in list_Word[0]:
        if(ch not in dict_name):
            dict_name[ch]=1
        else:
            dict_name[ch]=dict_name[ch]+1
    for key in dict_name:
        print(key,dict_name[key])
elif(len(list_Word)>1):
    for word in list_Word:
        if(word not in dict_name):
            dict_name[word]=1
        else:
            dict_name[word]=dict_name[word]+1
    for key in dict_name:
        print(key,dict_name[key])
print(end="\n")

#Ques 2
day=int(input("Day-"))
month=int(input("Month-"))
year=int(input("Year-"))
month_30=[4,6,9,11]
month_31=[1,3,5,7,8,10]
month_dec=12
if(year%100==0 and year%400==0):
    if month==2 :
        if day==29 :
            print("1/"+str(month+1)+"/"+str(year))
        else:
            print(str(day+1)+"/"+str(month)+"/"+str(year))
    elif month in month_31:
        if day==31:
            print("1/" + str(month + 1) + "/" + str(year))
        else:
            print(str(day + 1) + "/" + str(month) + "/" + str(year))
    elif month in month_30:
        if day==30:
            print("1/" + str(month + 1) + "/" + str(year))
        else:
            print(str(day + 1) + "/" + str(month) + "/" + str(year))
    elif month==12:
        if day==31:
            print("1/1/"+str(year+1))
        else:
            print(str(day + 1) + "/" + str(month) + "/" + str(year))
elif(year%100==0 and year%400!=0):
    if month==2 :
        if day==28 :
            print("1/"+str(month+1)+"/"+str(year))
        else:
            print(str(day+1)+"/"+str(month)+"/"+str(year))
    elif month in month_31:
        if day==31:
            print("1/" + str(month + 1) + "/" + str(year))
        else:
            print(str(day + 1) + "/" + str(month) + "/" + str(year))
    elif month in month_30:
        if day==30:
            print("1/" + str(month + 1) + "/" + str(year))
        else:
            print(str(day + 1) + "/" + str(month) + "/" + str(year))
    elif month==12:
        if day==31:
            print("1/1/"+str(year+1))
        else:
            print(str(day + 1) + "/" + str(month) + "/" + str(year))
elif(year%100!=0 and year%4==0):
    if month==2 :
        if day==29 :
            print("1/"+str(month+1)+"/"+str(year))
        else:
            print(str(day+1)+"/"+str(month)+"/"+str(year))
    elif month in month_31:
        if day==31:
            print("1/" + str(month + 1) + "/" + str(year))
        else:
            print(str(day + 1) + "/" + str(month) + "/" + str(year))
    elif month in month_30:
        if day==30:
            print("1/" + str(month + 1) + "/" + str(year))
        else:
            print(str(day + 1) + "/" + str(month) + "/" + str(year))
    elif month==12:
        if day==31:
            print("1/1/"+str(year+1))
        else:
            print(str(day + 1) + "/" + str(month) + "/" + str(year))
elif(year%100!=0 and year%4!=0):
    if month==2 :
        if day==28 :
            print("1/"+str(month+1)+"/"+str(year))
        else:
            print(str(day+1)+"/"+str(month)+"/"+str(year))
    elif month in month_31:
        if day==31:
            print("1/" + str(month + 1) + "/" + str(year))
        else:
            print(str(day + 1) + "/" + str(month) + "/" + str(year))
    elif month in month_30:
        if day==30:
            print("1/" + str(month + 1) + "/" + str(year))
        else:
            print(str(day + 1) + "/" + str(month) + "/" + str(year))
    elif month==12:
        if day==31:
            print("1/1/"+str(year+1))
        else:
            print(str(day + 1) + "/" + str(month) + "/" + str(year))

#Ques 3
num=input()
list_num=num.split()
list_square=[]
for item in list_num:
    list_square.append((int(item),int(item)**2))
print(list_square)


#Ques 4
grade=int(input("Enter Grade:\n"))
dict_grade={10:['A+','Outstanding'],9:['A','Excellent'],8:['B+','Very Good'],7:['B','Good'],6:['C+','Average'],5:['C','Below Average'],4:['D','Poor']}
if(grade<4 or grade>10):
    print("Grade Out Of Range")
else:
    print("Your Grade is",dict_grade[grade][0],"and",dict_grade[grade][1],"Performance")


#Ques 5
for i in range(6):
    for j in range(i):
        print(" ",end="")
    for k in range(2*(6-i)-1):
        print(chr(65+k),end="")
    for l in range(i):
        print(" ",end="")
    print(end='\n')

#Ques 6
sid_name={}
true_list=['Y','y']
false_list=['N','n']
while(True):
    dec=input()
    if dec in true_list:
        sid=int(input())
        name=input()
        sid_name[sid]=name
        continue
    else:
        break
copylist=sid_name
for key in sid_name:
    print(key,sid_name[key])
dict_sort_sid={}
list_sid=list(sid_name.keys())
list_name=list(sid_name.values())
list_sid.sort()
#Sorting WRT Keys
for sid in list_sid:
    for name in list_name:
        if(sid_name[sid]==name):
            dict_sort_sid[sid]=name
print(sid_name)
sid_name=dict_sort_sid
print(sid_name)
sid_name=copylist



dict_sort_name={}
list_sid2=list(sid_name.keys())
list_name2=list(sid_name.values())
list_name2.sort()
#Sorting WRT Values
for name in list_name2:
    for sid in list_sid2:
        if(sid_name[sid]==name):
            dict_sort_name[sid]=name
print(sid_name)
sid_name=dict_sort_name
print(sid_name)

n=int(input("Enter the SID of Student You Want Name of:"))
print(sid_name[n])


#Ques 7
list_recursion=[0,1]
n=int(input("Enter The Number Til Which You Want Sequence:\n"))
a1=0
a2=1
for i in range(n-2):
    temp=a1+a2
    list_recursion.append(temp)
    a1=a2
    a2=temp
print(list_recursion)
print("Average:",(sum(list_recursion))/n)

#Ques 8
Set1={1,2,3,4,5}
Set2={2,4,6,8}
Set3={1,5,9,13,17}
Set_10={1,2,3,4,5,6,7,8,9,10}
Set_a=Set1^Set2
print(Set_a)
Set_commonall=Set1&Set2&Set3
Set_b=Set1^Set2^Set3
print(Set_b)
Set_c=((Set1&Set2)-Set_commonall)|((Set2&Set3)-Set_commonall)|((Set3&Set1)-Set_commonall)
print(Set_c)
Set_d=Set_10-Set1
print(Set_d)
Set_union=(Set1|Set2|Set3)

Set_e=Set_10-Set_union
print(Set_e)


