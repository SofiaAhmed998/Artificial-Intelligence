//Task 1
L1 =[]
L2 = []
num1 = int(input("Enter numbers for 1st list"))
for i in range(1,num1+1):
    a = int(input("Enter element"))
    L1.append(a)

num2 = int(input("Enter numbers for 2nd list"))
for i in range(1,num2+1):
    b = int(input("Enter element"))
    L1.append(b)

L3 = L1+L2
L3.sort()
print("sorted list is",L3)

//Task 2
L1 =[]
L2 = []
num1 = int(input("Enter numbers for 1st list"))
for i in range(1,num1+1):
    a = int(input("Enter element"))
    L1.append(a)

num2 = int(input("Enter numbers for 2nd list"))
for i in range(1,num2+1):
    b = int(input("Enter element"))
    L1.append(b)

L3 = L1+L2
L3.sort()
print("sorted list is",L3)
for i in range(len(L3)):
    for j in range(len(L3)):
        if L3[j]>L3[i]:
            temp=L3[j]
            L3[j]=L3[i]
            L3[i]=temp
print(L3)
print("largest element of list is")
print(L3[len(L3)-1])
print("smallest element of list is")
print(L3[0])

//Task 3
import math
from math import *
h=0.001
x= float(input("Enter x"))
a=(sin(x+h)-sin(x))/h
b=cos(x)
a=math.ceil(a*100)/100
b=math.ceil(b*100)/100
if(math.isclose(a,b)):
    print("equal")
else:
    print("not equal")
print(a)
print(b)

//Task 4
dictionary={("Sofia","Ahmed"):"20-sep-2000",("Maryam","Amjad"):"23-06-2001",("Misbah","Nazir"):"30-12-2000"}
print("Welcome to the birthday dictionary")
for birthday,value in dictionary.items():
    print(birthday)
a=input("Whose birthday do you want to look up?")
a=a.capitalize()
if a in dictionary:
    print(dictionary[a])
else:
    print("null")

//Task 5
sample_dict={"name": "kelly","age":25,"salary":8000,"city":"New york"}
keys = ["name","salary"]
dictionary={k:sample_dict[k] for k in keys}
print(dictionary)    
