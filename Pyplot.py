import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

marks = pd.read_csv ("F:\Student_Management_System\marks.csv",index_col=0)
dfMarks = pd.DataFrame(marks)
print(dfMarks)
dfMarks.plot(kind='box')
plt.show()


























'''week1 = [5500,7800,4580,4500,1540,1200,3200]
week2 = [5600,8700,7840,5410,5600,5200,3200]
week3 = [7800,2000,3000,4500,7800,4000,1000]
day = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
week = {"Week 1":week1,"Week 2":week2,"Week 3":week3,"Day":day}
Sales = pd.DataFrame(week)
print(Sales)
a = (30 * np.random.rand(7))**2
Sales.plot(kind='scatter',x='Day',y='Week 1',s=a,alpha=0.)
plt.title("Weekl")
plt.show()




hei = [60,61,63,65,61,60,66,58,56,66,67,69,67,64,66,61,63,69,67,62,63,64,62,60,66,61,63]
Height = pd.DataFrame(hei)
print(Height)
Height.plot(kind='hist',bins=[55,58,61,64,67,70],edgecolor='black',facecolor='red',fill=True,hatch='/')
plt.show()'''


















'''#To print Monthly Sales

Month_Names =  ['Jan','Feb','Mar','Apr','May','June','July']
Pen_Sales = [120,150,130,140,110,180,145]
Notebook_Sales = [100,170,140,120,130,170,145]
plt.scatter(Month_Names,Pen_Sales)
plt.scatter(Month_Names,Notebook_Sales)
plt.plot(Month_Names,Pen_Sales,marker='<',color = 'y',linewidth=5)
plt.plot(Month_Names,Notebook_Sales,linestyle='dashdot')

plt.title("Monthly Sales")
plt.xlabel("Month Names")
plt.ylabel("Sales Made")
plt.grid(True)
plt.legend(["Notebook","Pen"],loc='best')
plt.show()'''

