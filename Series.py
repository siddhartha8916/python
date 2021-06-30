import pandas as pd
import numpy as np

'''Vowels = pd.Series(6, index=['a','e','i','o','u'])
print(Vowels)

num = np.array([31,29,31,30,31,30,31,31,30,31,30,31])
MonthDays = pd.Series(data=num,index=np.arange(1,13))
print(MonthDays)

friend = {'Arnab':1,'Ramit':2,'Riya':3,'Samridhi':4,'Mallika':5}
Friends = pd.Series(friend)
print(Friends)'''

Vowels = pd.Series(6, index=['a','e','i','o','u'])
Vowels.name = 'Vowels1'
Vowels.name = "Number"
print(Vowels)
Vowels.index=[2,5,6,3,8]
Vowels.name = 'Vowels'
print(Vowels)

'''Vowels.update(pd.Series(6, index=[2,5,6,3,8]))
Vowels = Vowels/2
print(Vowels)

Vowels1 = pd.Series(['a','e','i','o','u'], index=[2,5,6,3,8])
print(Vowels1)'''


'''ResultSheet={'Arnab': pd.Series([90, 91, 97], index=['Maths','Science','Hindi']),\
'Ramit': pd.Series([92, 81, 96], index=['Maths','Science','Hindi']),\
'Samridhi': pd.Series([89, 91, 88], index=['Maths','Science','Hindi']),\
'Riya': pd.Series([81, 71, 67], index=['Maths','Science','Hindi']),\
'Mallika': pd.Series([94, 95, 99], index=['Maths','Science','Hindi'])}
ResultDF = pd.DataFrame(ResultSheet)
print(ResultDF.tail(2))
ResultDF=ResultDF.T
print(ResultDF)
print()
print(ResultDF['Maths']>90)
df1 = ResultDF[ResultDF['Maths']>90]
print(df1['Maths'])'''



'''student1 = ['Ram','XII',1,1290,'Arts']
student2 = ['Shyam','XI',2,1291,'Science']
student3 = ['Radha','XI',3,1292,'Arts']
student4 = ['Mohan','XII',4,1293,'Commerce']
student5 = ['Sohan','XI',5,1294,'Science']
students = [student1,student2,student3,student4,student5]

df = pd.DataFrame(columns = ['Name','Class','Roll','Adm','Stream'],index=[1001,1002,1003,1004,1005],data=students)
print(df.shape)'''










'''
student1 = ['Ram','XII',1,1290,'Arts']
student2 = ['Shyam','XI',2,1291,'Science']
student3 = ['Radha','XI',3,1292,'Arts']
student4 = ['Mohan','XII',4,1293,'Commerce']
student5 = ['Sohan','XI',5,1294,'Science']
students = [student1,student2,student3,student4,student5]

df = pd.DataFrame(columns = ['Name','Class','Roll','Adm','Stream'],index=[1001,1002,1003,1004,1005],data=students)
print(df.dtypes)

print()
print()
student = {'Name':pd.Series(data=['Ram','Shyam','Mohan'],index=['a','b','c']),'Class':['XII','X','XI'],'Roll':[1,2,3],'Adm':[1234,1345,1145],\
                 'Stream':['Arts','Science','Commerce']}
df1 = pd.DataFrame(student,index=['a',1002,1003])
print(df1)


student1 = ['Ram','XII',1,1290,'Arts']
student2 = ['Shyam','XI',2,1291,'Science']
student3 = ['Radha','XI',3,1292,'Arts']
student4 = ['Mohan','XII',4,1293,'Commerce']
student5 = ['Sohan','XI',5,1294,'Science']
students = [student1,student2,student3,student4,student5]

df = pd.DataFrame(columns = ['Name','Class','Roll','Adm','Stream'],index=[1001,1002],data=[['Ram','XII',1,1290,'Arts'],['Shyam','XI',2,'Science']])
print(df.loc[[1001,1003],['Name','Roll']])
print()
print(df['Roll'])

#df=df.drop(['Name','Class'],axis='columns')
#df=df.drop([1002,1005],axis='index')
#df=df.rename({1001:'Stu1',1002:'Stu2'})
#df=df.rename({'Name':'Student','Class':'Std'},axis=0)


ResultSheet={'Arnab': pd.Series([90, 91, 97], index=['Maths','Science','Hindi']),\
'Ramit': pd.Series([92, 81, 96], index=['Maths','Science','Hindi']),\
'Samridhi': pd.Series([89, 91, 88], index=['Maths','Science','Hindi']),\
'Riya': pd.Series([81, 71, 67], index=['Maths','Science','Hindi']),\
'Mallika': pd.Series([94, 95, 99], index=['Maths','Science','Hindi'])}
ResultDF = pd.DataFrame(ResultSheet)
print(ResultDF[ResultDF.loc[:,'Arnab']>90])

student1 = ['Ram','XII',1,1290,'Arts']
student2 = ['Shyam','XI',2,1291,'Science']
student3 = ['Radha','XI',3,1292,'Arts']
student4 = ['Mohan','XII',4,1293,'Commerce']
student5 = ['Sohan','XI',5,1294,'Science']
students = [student1,student2,student3,student4,student5]

df = pd.DataFrame(students,columns = ['Name','Class','Roll','Adm','Stream'],index=[1001,1002,1003,1004,1005])
#print(df.loc[:,'Name':'Adm'])
#df.loc[1002:1005,'Stream'] = ['Humanities','Music','Arts','Painting']
print(df[df['Roll']>3])


name = ['Ravi','Sohan','Abhinav','Monu']
Class = ['XII','XI','XI','XII']
roll = [1,2,3,4]
data = {'Name':name,'Class':Class,'Roll':roll,'Adm':[1290,1234,1221,1244],\
            'Stream':['Arts','Commerce','Science','Arts'] }
df1 = pd.DataFrame(data,index = ['Stud1','Stud2','Stud3','Stud4'])
print(df1)
df3 = pd.DataFrame(data,index = ['Stud','Stud','Stud','Stud'])


geeta = {'Name':'Geeta Kumari','Roll':1,'Class':'XII','Stream':'Arts'}
mona = {'Name':'Mona Pandey','Roll':2,'Class':'XI','Stream':'Science'}
reena = {'Name':'Reena Roy','Roll':3,'Class':'XII','Stream':'Arts'}

students = [geeta,mona,reena]
df2 = pd.DataFrame(students)
print(df2)

student1 = ['Ram','XII',1,1290,'Arts']
student2 = ['Shyam','XI',2,1291,'Science']
student3 = ['Radha','XI',3,1292,'Arts']
student4 = ['Mohan','XII',4,1293,'Commerce']
student5 = ['Sohan','XI',5,1294,'Science']
students = [student1,student2,student3,student4,student5]

df = pd.DataFrame(students,columns = ['Name','Class','Roll','Adm','Stream'],index=[1001,1002,1003,1004,1005])
print(df)

df['Eng'] = [67,76,65,34,98]
df.loc[1006] = ['Gagan','XI',6,1222,'Science',78]
print()
print(df)
print()
df.at[1003:1005,'Name':'Roll'] = 0
print(df[1002])

input()


Feb_Sales = [18,88,102,87,78]
Mar_Sales = [121,45,65,82,95]
Apr_Sales = [78,69,89,83,98]
May_Sales = [36,87,69,98,43]

'''










'''ar1 = np.array([10,20,30])
ar2 = np.array([100,200,300])
ar3 = np.array([-10,-20,-30,-40])
lst = ['a','b','c']
df = pd.DataFrame([ar1,ar2],columns = lst)
print(df)'''


















































'''
All_Sales = np.array([Jan_Sales,Feb_Sales,Mar_Sales,Apr_Sales,May_Sales])
Jan=pd.Series(Jan_Sales, index = items)
Feb=pd.Series(Feb_Sales, index = items)
Mar=pd.Series(Mar_Sales, index = items)
Apr=pd.Series(Apr_Sales, index = items)
May=pd.Series(May_Sales, index = items)
print("Sales in January : ",Jan)
print()
print()
print("Sales in February : ",Feb)
print()
print()
print("Sales in March : ",Mar)
print()
print()
print("Sales in April : ",Apr)
print()
print()
print("Sales in May : ",May)
print()
print()
total = Jan + Feb + Mar + Apr + May
print("Total Yearly Sales is : \n",total)
total=total.sort_values(ascending=False)
Max = total.head(1)
print("Maximum Sales of item made : \n", Max)
dfTotal = pd.DataFrame(All_Sales, index = items, columns = ['Jan','Feb','Mar','Apr','May'])
print(dfTotal)
print("Maximum Sale of ",items[0], "made in ",)
#Jan_Max = total.max(axis=1)
#print("Maximum sales of ", Jan_Max)

data = {'age':[20, 23, 24] , 'name' : ['Ruhi', 'Ali', 'Sam']}
df1 = pd.DataFrame( data, index = [1, 2, 3] )
print('Before')
print(df1)
df1['Edu'] = ['BA', 'MA', 'MBA']
print('After')
print(df1)



items1 = ['pen', 'pencil', 'sharpner', 'eraser', 'scale','mouse','keyboard','laptop','charger']
Jan = [100,109,45,33,23,43,12,np.NaN,54]

Feb = [18,88,102,87,78]
items2 = ['pen','scale','laptop','glue','mouse']

JanSale = pd.Series(Jan,index=items1)
FebSale = pd.Series(Feb,index=items2)

print(JanSale)
print()
print(FebSale)
print()
print(JanSale.add(FebSale,fill_value=1000))


'''

