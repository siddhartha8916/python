'''name = ""
while name!='end':
    name = input("Enter name ('end' to exit:)")
    if name=='end':
        pass
    print("Hello ",name)
else:
    print("Wasn't it fun ? ")

i = 10
while i>0:
    print(i)
    i=i-1
    pass
print("End of Loop")

import random
secretNum = random.randint(1,100)
guessNum = int(input("Guess a number between 1 and 100 inclusive:" ))
while guessNum != secretNum:
    if guessNum<secretNum:
        print("Your guess is too low. . .")
    else:
        print("Your guess is too high . . .")
    guessNum = int(input("Guess a number between 1 and 100 inclusive:" ))
print("Congratulations! You guessed the number correctly . . .")


a = 0
b = 1 
lst = [a,b]
while b<100:
    a,b = b, a+b
    lst.append(b)
print(lst)

a = 0
b = 1
lst = [a,b]
for i in range(2,10):
    Sum = lst[i-1]+lst[i-2]
    lst.append(Sum)
print(lst)

a = '76545'
l = len(a)
for i in a:
    print(a[l,0])

num = int(input("Enter an integer "))
print ("The divisors of" , num, "are : 0 ",end='')
for a in range (1, num+1):
    if num % a ==0:
        print (a, end = ' ' )
else:
    print("- End-")

num=9846
while num>0:
    print(num%10)
    num = num//10

n = 10
Sum = 0
for i in range(1,11):
    a = int(input("Enter a number : "))
    Sum = Sum+a
average = Sum/i
print("Average of numbers = ", average)

N = 56
for i in range(11,N+1):
    if (i%3 == 0 and i%7 == 0):
        print(i,"TipsyTopsy")
    elif(i%3 == 0):
        print(i, "Tipsy")
    elif(i%7 == 0):
        print(i, "Topsy")


n = 10
Max = 0
Min = 0
for i in range(n):
    num = int(input("Enter the number : "))
    if i==0:
        Min=num
    if num>Max:
        Max = num
    if num<Min:
        Min = num
print("Maximum Number is : ", Max)
print("Minimum Number is : ", Min)


n=10
Max = 0
SMax = 0
for i in range(n):
    num = int(input("Enter the number : "))
    if num > Max:
        SMax = Max
        Max = num
    elif num > SMax:
        SMax = num
print("Maximum Number is : ", Max)
print("Second Maximum Number is : ", SMax)  

no = ''
n = int(input("Enter the number : "))
m = int(input("Enter the number with which to be divided : "))
for i in range(1,n+1):
    if i%2==0:
        no = 'Even'
    else:
        no = 'Odd'
    if i%m==0:
        print(i,no,"is divisible by",m)

n = 10
age26_35 = 0
age36_45 = 0
age46_55 = 0
for i in range(n):
    age = int(input("Enter the age : "))
    if (age>=26 and age<=35):
        age26_35 +=1
    elif(age>=36 and age<=45):
        age36_45 +=1
    elif(age>=46 and age<=55):
        age46_55 +=1
print("Count of Age in Range 26 to 35 is ",age26_35)
print("Count of Age in Range 36 to 45 is ",age36_45)
print("Count of Age in Range 46 to 55 is ",age46_55)'''

a = 12
b = 10
c = 15
lst = [a,b,c]
lst.sort()
print(lst)
'''if(a<b and a<c):
    mini = a
elif(b<a and b<c):
    mini = b
elif(c<a and c<b):
    mini = c
'''























    
