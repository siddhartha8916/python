import pandas as pd
import numpy as np
'''items = ['pen', 'pencil', 'sharpner', 'eraser', 'scale']
Jan_Sales = [100,109,45,33,23]
Feb_Sales = [18,88,102,87,78]
Mar_Sales = [121,45,65,82,95]
Apr_Sales = [78,69,89,83,98]
May_Sales = [36,87,69,98,43]
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
#print("Maximum sales of ", Jan_Max)'''

data = {'age':[20, 23, 24] , 'name' : ['Ruhi', 'Ali', 'Sam']}
df1 = pd.DataFrame( data, index = [1, 2, 3] )
print('Before')
print(df1)
df1['Edu'] = ['BA', 'MA', 'MBA']
print('After')
print(df1)

