import pandas as pd
import numpy as np

student1 = ['Ram','XII',1,1290,'Arts']
student2 = ['Shyam','XI',2,1291,'Science']
student3 = ['Radha','XI',3,1292,'Arts']
student4 = ['Mohan','XII',4,1293,'Commerce']
student5 = ['Sohan','XI',5,1294,'Science']
students = [student1,student2,student3,student4,student5]

df = pd.DataFrame(students,columns = ['Name','Class','Roll','Adm','Stream'],index=[1001,1002,1003,1004,1005])
print(df)

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
