import numpy as np
'''month = {'Jan':31,'Feb':28,'Mar':31,'Apr':30,'May':31,'June':30,'Jul':31,\
              'Aug':31,'Sep':30,'Oct':31,'Nov':30,'Dec':31}
val = list(month.values())
ar2 = np.array(val,dtype=np.int32)
ar1 = np.fromiter(month,dtype='U2')
print(ar1)
print(type(ar1))
ar2[6] = 89
print(ar2)
print(ar2+2)
ar1 = np.array([6,4,5,6,78,8])
ar2 = np.array([5,7,8,4,4,4])
dictt = dict(zip(ar1,ar2))
print(dictt)


str1 = "SIDDHARTHAKUMARAYUSHAGRAWAL"
month = {'Jan':31,'Feb':28,'Mar':31,'Apr':30,'May':31,'June':30,'Jul':31,\
              'Aug':31,'Sep':30,'Oct':31,'Nov':30,'Dec':31}
val = "'Jan', 'Feb', 'Mar', 'Apr', 'May', 'June', 'Jul', 'Aug', 'September', 'Oct', 'Nov', 'Dec'"
ar1 = np.fromiter(val,dtype='U5')
print(ar1)
print(val)

ar1 = np.linspace(60,61,5)
print(ar1)

ar1 = np.arange(10).reshape(2,5)
print(ar1.shape)
print(ar1)
print(ar1.shape)
ar1[1,4] = 86
print(ar1)


ar1 = np.arange(0,10).reshape(5,2)
ar2 = np.empty_like(ar1)
ar3 = np.full((3,6),6)
ar6 = np.random.rand(3,4)
ar4 = np.random.rand(3,4)*20
ar5 = np.random.randint(10,size=(5,2))
print(ar4)
print(ar5)
print(ar6)
grid = np.array([[1,2,3],[4,5,6]])
print(grid)
g2 = np.concatenate([grid,grid],axis=1)
print()
print(g2)
input()'''

ar1 = np.arange(18).reshape(3,6)
print(ar1)
lst = [[1,2,3],['a','b','c']]
ar2 = np.array(lst)
print(ar2)
print(ar2.dtype)
input()













