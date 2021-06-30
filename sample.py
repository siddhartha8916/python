'''Student = {}
import json

print(Student)
name = "Sidd"
Class = 'XI'
fname = 'Manoj'
Student['name'] = name
Student['class'] = Class
Student['father'] = fname
print(Student)
Student['name'] = 'Siddhartha'
print(Student)
list1 = list(Student.keys())
list2 = list(Student.values())
list3= list1+list2
print(list3)

Student2 = dict(name='John',salary=89000,city='Begusarai')
Student3 = dict(zip(('name','age','salary'),('Suman',32,56000)))


Student2.update({'city':'Lucknow'})
lst = list(Student2.items())
lst.sort()
print(lst)


print()
print()



myDict = {'a':27,'b':43,'c':25,'d':30}
valA = ''
for i in myDict:
    if i > valA:
        valA = i
        valB = myDict[i]

print(valA)
print(valB)
print(30 in myDict)
myLst = list(myDict.items())
myLst.sort()
print(myLst)
print(myLst[-1])


print()
print()

d1 = {5:'number', 'a':'string', (1,2):'tuple'}
print("Dictionary Contents : ")
for x in d1.keys():
    print(x,' : ',d1[x],end= ' ')
    print(d1[x] * 3)
    print()


d = dict()
d['left'] = '<'
d['right'] = '>'
d['end'] = ' '
print(d['left'] and d['right'] or d['right'] and d['left'])
print(d['left'] and d['right'] or d['right'] and d['left'] and d['end'])
print((d['left'] and d['right'] or d['right'] and d['left']) and d['end'])
print("end")
'''

'''text = 'absbdcbdtebcbcbab'
counts = {}
#ct=0
lst = []
for word in text:
    if word not in lst:
        lst.append(word)
        counts[word] = 0
    #ct = ct+1
    counts[word] = counts[word] + 1
print(counts)
print(lst)

text = 'absbdcbdtebcbcbab'
counts = {}
for word in text:
    counts[word] = counts[word] + 1

box = {}
jam = {'Jam':4}
crates = {}
box['biscuit'] = 1
box['cake'] = 3
crates['box'] = box
crates['jam'] = jam
print("Box : ", box)
print("Crates : ",crates)
print(len(crates[box]))

winloss = {}
winlst = []
winloss = []
n = int(input("Enter the number of teams : "))
for a in range(n):
    name = input("Enter the Team Name : ")
    win = int(input("Enter number of times won : "))
    loss = int(input("Enter number of times loss : "))
    winloss[name] = [win,loss]
    winlst = winlst.append(win)
    winloss = winloss.append(loss)
print(winloss)

winloss = {'India': [4, 0], 'Australia': [2, 2], 'Bangladesh': [5, 1], 'Pakistan': [3, 7]}
team = input("Enter team name : ")
win = winloss[team][0]
loss = winloss[team][1]
total = win + loss
print("Winning Percentage : ",(win/total)*100,"%")

winloss = {'India': [4, 0], 'Australia': [2, 2], 'Bangladesh': [5, 1], 'Pakistan': [3, 7]}
winlst = []
for key in winloss:
    a = winloss[key][1]
    winlst.append(a)
print(winlst)

winloss = {'India': [4, 0], 'Australia': [0, 2], 'Bangladesh': [5, 1], 'Pakistan': [3, 7]}
values = list(winloss.values())
print(values)
winlst = []
for a in values:
    win = a[0]
    winlst.append(win)
print(winlst)

winloss = {'India': [4, 0], 'Australia': [6, 2], 'Bangladesh': [0, 1], 'Pakistan': [0, 7]}
winlst = []

for x in winloss:
    if (winloss[x][0] != 0):
        winlst.append(x)
print(winlst)

product = {'Mango':60,'Apple':64,'Banana':80}
while True:
    pname = input("Enter Product Name : ")
    pprice = float(input("Enter Product Price : "))
    product[pname] = pprice
    ch = input("Do you want to enter more products (Y/N)? : ") 
    if ch=='y' or ch=='Y':
         continue   
    else:
        break
print("Total Products is as below : \n")
print(product)
while True:
    pname = input("Enter the product name : ")
    if pname in product.keys():
        print("The price of ",pname,"is",product[pname])
        continue
    else:
        print("Product not found")
        break


month = {'Jan':31,'Feb':28,'Mar':31,'Apr':30,'May':31,'June':30,'Jul':31,\
              'Aug':31,'Sep':30,'Oct':31,'Nov':30,'Dec':31}
day = input("Enter month name : ")
print(month[day])
lst = list(month.keys())
lst.sort()
print(lst)
month31 = []
for x in month:
    if month[x]==31:
        month31.append(x)
print(month31)

lst1 = list(month.values())
lst1.sort()
print(lst1)

month = {'Jan':31,'Feb':28,'Mar':31,'Apr':30,'May':31,'June':30,'Jul':31,\
              'Aug':31,'Sep':30,'Oct':31,'Nov':30,'Dec':31}
new = {'k1':'v1','k2':'v2','k3':'v3'}
newmonth = dict(zip(new.values(),new.keys()))
print(newmonth)
x = {31:'Jan',28:'Feb',31:'Mar',30:'Apr',31:'May',30:'June'}
print(x)

D1 = {'k1':'v1','k2':'v2','k3':'v3'}
D2 = {'k1':'v1','k3':'v2','k1':'v3'}
lst = []
for x in D1:
    for y in D2:
        if x == y:
            lst.append(x)
        else:
            continue
print(lst)
eng = float(input("Enter Marks in English : "))
hin = float(input("Enter Marks in Hindi : "))
mat = float(input("Enter Marks in Maths : "))
sci = float(input("Enter Marks in Science : "))
sst = float(input("Enter Marks in SST : "))
total = eng+hin+mat+sci+sst
avg = total/5
print("Average = ",avg)
if avg>=90:
    print("Grade = A")
elif avg>=80:
    print("Grade = B")
elif avg>=70:
    print("Grade = C")
else:
    print("Grade = D")'''


lst = [1,4,6,8,16,5,14,13,12,22,11,18,19]
lst.sort()
print(lst[-3])

sqsum=0
for i in range(1,101):
    sqsum += i*i
print(sqsum)








