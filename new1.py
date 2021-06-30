'''name = input("Enter your name : ")
print("Your name is : ",name)

num1 = float(input("Enter first number : "))
num2 = float(input("Enter second number : "))
result = num1 + num2
print("Sum of two numbers is : ",result)


num1 = float(input("Enter first number : "))
num2 = float(input("Enter second number : "))
num3 = float(input("Enter third number : "))
num4 = float(input("Enter fourth number : "))
num5 = float(input("Enter fifth number : "))
total = num1+num2+num3+num4+num5
avg = total/5
print("Average of numbers entered is :",avg)

num = int(input("Enter the number : "))
if (num>0):
    print("Positive number...")
else:
    print("Negative number")


num = int(input("Enter the number : "))
if (num%2==0):
    print("Even number...")
else:
    print("Odd number")

result = 0
for a in range(5):
    num = float(input("Enter the number : "))
    #print("Number entered is : ", num)
    result = result+num
    print("Result = ",result)

print("Sum of numbers is : ", result)'''




def OddEven():
   num = int(input("Enter the number : "))
   if (num%2==0):
       print("Even number...")
   else:
       print("Odd number")


def NegPos():
   num = int(input("Enter the number : "))
   if (num>0):
       print("Positive number...")
   else:
       print("Negative number")


def Grade():
   per = float(input("Enter the percentage : "))
   if (per>=90):
      print("Grade A")
   elif (per>=80):
      print("Grade B")
   elif (per>=70):
      print("Grade C")
   elif (per>=50):
      print("Grade D")
   else:
      print("Grade E")


def SimInt():
   Principal_Amount = float(input("Enter the Principal Amount : "))
   Rate = float(input("Enter the Rate : "))
   Time_In_Year = float(input("Enter the Time in Years : "))
   SI = (Principal_Amount * Rate * Time_In_Year)/100
   Amount_Payable = SI + Principal_Amount
   print("Total Interest Earned = Rs.", SI)
   print("Total Amount Payable = Rs.", Amount_Payable)
   
   
def GoodMorning():
   string = "Good Morning"
   n = int(input("Enter the value of n : "))
   for a in range(n):
      print(string)


def Average():
   a = int(input("Enter the value of a : "))
   b = int(input("Enter the value of b : "))
   c = int(input("Enter the value of c : "))
   avg = (a+b+c) / 3
   print("Average = ", avg)

def Age():
   name = input("Enter your name : ")
   age = int(input("Enter your age : "))
   age_at_100 = 2021+(100 - age)
   print(name,"you will turn 100 years old in the year",age_at_100)

def List():
   lst = [2,4,6,8,10,12]
   l = len(lst)
   print("lst = ",lst[-l])
   print("Total numbers of elements in lst = ",l)
   lst1 = [2,6.8,'a',"Sneha"]
   print("lst1 = ",lst1[0])
   lst2 = [[1,2,3],[4,5,6],[7,8,9]]
   print("lst2 = ", lst2[1][2])
   vowels = ['a','e','i','o','u']
   print("Vowels are : ", vowels[1])
   name = ["Ram","Shyam","Radha","Mohan"]
   print("Name of students are : ", name)
   name[2] = "Sohan"
   name[3] = "Gagan"
   print("Name of students are : ", name)

def ListOpr():
   #items = ['Pen','Pencil','Sharpner','Eraser','Scale','Box','Book','Label','Sticker','Crayons','Sketch Pen','Ink','Light','Bulb']
   items = ['Pen','Pencil','Sharpner','Eraser']
   print(items)
   a = input("Enter the item name : ")
   items.append(a)
   print(items)
   
def ListName():
   student = []
   for a in range(6):
      name = input("Enter the name : ")
      student.append(name)
   print(student)
   
def ListInsert():
   items = ['Pen','Pencil','Sharpner','Eraser']
   print(items)
   items.insert(3,['Label','Sticker','Crayons'])
   print(items[3][2])


def ListCount():
   lst = [10,10,20,10,34,20,20,33,21,10]
   print(lst.count(20))
   print(lst.index(20))
   lst.remove(10)
   print(lst)

def ListRemove():
   lst = [10,10,20,10,34,20,20,33,21,10]
   newlst = []
   for a in lst:
      if a!=10:
         newlst.append(a)
   print(newlst)


def ListPop():
   items = ['Pen','Pencil','Sharpner','Eraser']
   print(items)
   x = items.pop(1)
   print(items)
   newlst = [x]
   print(newlst)
   stock = ['Sticker','Crayons','Sketch Pen','Ink','Light']
   stock.reverse()
   print(stock)
   stock.sort(reverse = True)
   print(stock)
   newstock = sorted(stock)
   print(newstock)

def ListMinMax():
   lst = [3,6,7,1,8,9,10,11,34,2,12]
   print(min(lst))
   print(max(lst))
   print(sum(lst))

def List1():
   lst = [3,6,7,1,8,9]
   print(lst)
   lst[2] = 10
   print(lst)
   lst.remove(8)
   print(lst)
   lst.pop(2)
   print(lst)
   lst1 = [3,6,7,1,8,9]
   lst1.sort(reverse=True)
   print(lst1)




def Dict():
   dic = {'Name' : 'Sneha','Father Name':'Sujeet Kumar','Roll':2,'Adm':1234,'Address':'Lohiyanagar','Pincode':851101}
   dic['name'] = 'Siddhartha'
   print(dic['Name'],'has Roll No.',dic['Roll'])
   print(dic.keys())
   print(dic.values())
   print(dic)
   print(1234 in dic.values())
   details = ['Sneha','Sujeet Kumar',2,1234,'Lohiyanagar']
   print(details[0],'has Roll No.',details[2])
   


def Dic():
   dic = {'Name' : 'Sneha','Father Name':'Sujeet Kumar','Roll':2,'Adm':1234,'Address':'Lohiyanagar','Pincode':851101}
   print(dic['Name'])

def posneg():
   num = [-8,-5,4,2,3,1,4,-6,-11,-9,5,64,2]
   p = []
   n = []
   for i in num:
      if i>0:
         p.append(i)
      else:
         n.append(i)
   print("Positive Numbers are : ", p)
   print("Negative Numbers are : ", n)

posneg()









   
