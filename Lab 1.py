#Activity 1
n = int(input("Enter a number"))
if n%2==0:
    print("The given number is even")
else:
    print("The given number is odd")
    

#Activity 2
sum=0
s=input("Enter an integer value..")
n=int(s)
while n!=0:
    sum= sum+n
    s=input("Enter an integer value..")
    n=int(s)
print("sum of given values is",sum)


#Activity 3
isPrime = True
i=2
n = int(input("Enter a number"))
while i<n:
    remainder = n%i
    if reamainder==0:
        isPrime= False
        break
    else:
        i = i+1
if isPrime:
    print("Number is prime")
else:
     print("Number is prime")
    

#Activity 4
summ=0
i=0
while i<=4:
    s = int(input("Enter a number"))
    summ=summ+s
    i=i+1
print("sum is",summ)
    
    
 #Activity 5
 
summ=0
i=1
while i<=10:
    summ=summ+i
    i=i+1
print("sum is",summ)


#Activity 6
name = input("Enter your name")
print("Sofia",name)
job = input("Enter your job")
print("Manager",job)

#Activity 7
import random
Minimum = 1
Maximum = 9
Number = random.randint(Minimum,Maximum)
Try = 0
Running = 0
While(Running):
    Guess = input("Enter a number")
    if(Guess.lower()=='exit'):
        Running = False
        print("Existing Game")
    elif Number>int(Guess):
        print("Low")
    elif Number>int(Guess):
        print("High")
    elif Number == int(Guess):
        print("Guessed right")
        if(Try<2):
            print("Impressive")
        else:
            print("Better luck next time")
    Try = Try+1
    
   #Task 1
a = int(input("Enter a number"))
rev=0
while a>0:
    remainder = a%10
    rev = (rev*10)+remainder
    a = a//10
print("reverse number is",rev)

#Task 2

a=0
b=0
for i in range(0,5):
    n = int(input("Enter a number"))
    if(n%2==0):
        a = a+n
    else:
        b=b+n
print("sum of even is",a)
print("sum of odd is",b)

#Task 3

s = int(input("Enter a number"))
a=0
b=1
for i in range(2,s):
    c=a+b
    a=b
    b=c
    print(c)
    

#Task 4    
n = int(input("Enter a number"))
if(n<=100 and n>=0):
    if(n>=91 and n<=100):
        print("Grade is A")
    elif(n>=81 and n<=90):
         print("Grade is B")
    elif(n>=71 and n<=80):
         print("Grade is C")
    elif(n>=61 and n<=70):
         print("Grade is D")
    elif(n>=51 and n<=60):
         print("Grade is E")
    elif(n>=41 and n<=50):
         print("Grade is F")
    else:
         print("Invalid")
         
 #Task 5
 
n = int(input("Enter a number"))
fac=1
i=1
while i<=n:
    fac = fac*i
    i=i+1
print("factorial of",n,"is",fac)
