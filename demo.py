"""#To Input the salary of three employees of a local shop and calculate the total sum

print("======================================")
print("SALARY FOR THE MONTH OF DECEMBER")
print("======================================")

Ramesh_Salary=float(input("Enter the salary of Ramesh : "))
Suresh_Salary=float(input("Enter the salary of Suresh : "))
Mayank_Salary=float(input("Enter the salary of Mayank : "))

Total_Salary = Ramesh_Salary + Suresh_Salary + Mayank_Salary

print("\n")
print("The salary of Ramesh is : ",Ramesh_Salary)
print("The salary of Suresh is : ",Suresh_Salary)
print("The salary of Mayank is : ",Mayank_Salary)

print("\n")
print("The salary to be given in the month of December : ",Total_Salary)




print('-------------LAVA MOBILES---------------')

Cust_Name = input("Enter the name of the customer : ")
#print("Enter the contact number of ",Cust_Name," : ",end=' ')
Mob_No = input("Enter the contact number of " + Cust_Name + " : ")
Item = input("Enter the Item Name")
Cost = float(input("Enter the cost of the item : "))

GST = Cost * 12 / 100
Total_Cost = Cost + GST

print("\n")
print('----------INVOICE---------')
print("Customer Name : \t", Cust_Name)
print("Mobile Number : \t", Mob_No)
print("Item Purchased : \t", Item)
print("Item Cost : \t", Cost)
print("GST Rate - 12% : ", GST)
print("Total Amount Payable : \t", Total_Cost)"""

'''#Q.1 To display a joke when the user presses enter key

Joke = "Hello My \
Name is James Bond"

a=input("Press Enter for something funny. . . ")
print(Joke)

#Q.2 To enter no of days of current month and display the number of days left

today = int(input("Enter today's date : "))
month_days = int(input("Enter no. of days of the current month : "))
left_days = month_days - today
print("No. of days left = ",left_days)

#Q.3 To input a = 5 and multiply a with 2 and then subtract the result with 1 and print the values.

a=5
b=a*2
c=b-1
print(a,end='@')
print(b,end='@')
print(c)

#Q.5 To assign first five multiples of a number to 5 variable and then print them

num = int(input('Enter any number : '))
first, second, third, fourth, fifth = num*1, num*2, num*3, num*4, num*5
print(first, second, third, fourth, fifth)

#Q.6 To accept radius of a circle and print its area

pi = 3.14152
radius = float(input("Enter the radius of the circle : "))
area = pi * (radius**2)
print("The area of the circle is : ", area,"cm.sq.")

#Q.7 To calculate the average of 5 subjects

Eng = float(input("Enter the marks of English : "))
Hin = float(input("Enter the marks of Hindi : "))
Maths = float(input("Enter the marks of Maths : "))
Sci = float(input("Enter the marks of Science : "))
Sst = float(input("Enter the marks of SST : "))

total = Eng + Hin + Maths + Sci + Sst
average = total / 5
per = (total / 500) * 100
print("Average marks scored is ",average)
print("Percentage scored is ", per)

#Q.8 Program to input height in cms and convert to feet and inches

Height = float(input("Enter your height in cms : "))
Total_Inch = Height / 2.54
Feet = Total_Inch // 12
Inch = Total_Inch % 12
print("Your Height is ", Feet,"feet", Inch, "Inches")

#Q.9 Program to input no. n and do n2 , n3 , n4

Number = int(input("Enter any number : "))
Square = Number**2
Cube = Number**3
Quad = Number**4
print(Square, Cube, Quad)

#Q. 10 Program to calculate area of a triangle

Base = float(input("Enter the base of the triangle in cm : "))
Height = float(input("Enter the height of the triangle in cm : "))
Area = 0.5 * Base * Height
print('Area of the triangle is ', Area,"cm. sq.")


# Q.11 Program to calculate SI and CI

Principal = float(input("Enter the Principal Amount : "))
Rate = float(input("Enter the Rate of Interest : "))
Time = float(input("Enter the Time in Years : "))
SI = (Principal * Rate * Time) / 100
print("Simple Interest is Rs.", SI)
CI = (Principal * (1+(Rate/100))**Time) - Principal
print("Compund Interest is Rs.", CI)

#Q.13 Program to read name, age and class of five students, their age and class
#       and print them first in single line and then in another..

name1 = input("Enter the name of first student : ")
name2 = input("Enter the name of second student : ")
name3 = input("Enter the name of third student : ")
name4 = input("Enter the name of fourth student : ")
name5 = input("Enter the name of fifth student : ")

age1 = int(input("Enter the age of first student : "))
age2 = int(input("Enter the age of second student : "))
age3 = int(input("Enter the age of third student : "))
age4 = int(input("Enter the age of fourth student : "))
age5 = int(input("Enter the age of fifth student : "))

class1 = input("Enter the class of first student : ")
class2 = input("Enter the class of second student : ")
class3 = input("Enter the class of third student : ")
class4 = input("Enter the class of fourth student : ")
class5 = input("Enter the class of fifth student : ")

print(name1, name2, name3, name4, name5)
print(age1, age2, age3, age4, age5)
print(class1, class2, class3, class4, class5)
print()
print()
print(name1, age1, class1)
print(name2, age2, class2)
print(name3, age3, class3)
print(name4, age4, class4)
print(name5, age5, class5)

#Q.18 Program that iput cost of goods sold, revenue generated, operating cost and print gross profit,
#         net profit and net profit percentage

cgos = float(input("Enter the Cost of Goods Sold (in INR) : "))
rg = float(input("Enter the Revenue Generated (in INR) : "))
oc = float(input("Enter the Operating Cost (in INR) : "))

gross_profit = rg - cgos
net_profit = gross_profit - oc
gross_profit_percent = (gross_profit / rg) * 100
net_profit_percent = (net_profit / rg) * 100

print("Gross Profit = Rs. ", gross_profit)
print("Net Profit = Rs. ", net_profit)
print("Gross Profit Percentage =", int(gross_profit_percent),"%")
print("Net Profit Percentage =", int(net_profit_percent),"%")

#To Input the salary of three employees of a local shop and calculate the total sum

print("======================================")
print("SALARY FOR THE MONTH OF DECEMBER")
print("======================================")

Ramesh_Salary=float(input("Enter the salary of Ramesh : "))
Suresh_Salary=float(input("Enter the salary of Suresh : "))
Mayank_Salary=float(input("Enter the salary of Mayank : "))

Total_Salary = Ramesh_Salary + Suresh_Salary + Mayank_Salary

print("\n")
print("The salary of Ramesh is : ",Ramesh_Salary)
print("The salary of Suresh is : ",Suresh_Salary)
print("The salary of Mayank is : ",Mayank_Salary)

print("\n")
print("The salary to be given in the month of December : ",Total_Salary)

# Input seconds and convert to minutes and second

sec = int(input("Enter time in seconds : "))
minute = sec//60
sec1 = sec%60
print("The time is ",minute,"minutes and ",sec1,"seconds")

month=int(input("Enter the Month No. "))
day=int(input("Enter the Day No. "))
dayno = ((month-1)*30)+day
print("The day of the year is : ",dayno)

year = int(input("Enter the year no. "))
days = year * 365
hours = days * 24
minute = hours * 60
sec = minute * 60
print("No. of days = ", days)
print("No. of hours = ", hours)
print("No. of minutes = ", minute)
print("No. of seconds = ", sec)'''

basic = float(input("Enter the salary : "))
hra = float(input("Enter HRA in % "+"%"))
da = float(input("Enter DA in % "))
tax = float(input("Enter tax in % "))
net = basic + ((hra/100)*basic) + ((da/100)*basic) - ((tax/100)*basic)
print("Net Salary = Rs. ",net)













