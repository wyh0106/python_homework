# %%
import numpy as np

# %%
nadarray = np.zeros(4, np.int)
nadarray[4] = 1
nadarray

# %%
nadarray = np.arange(10, 50)
nadarray

# %% 
antiarray = nadarray[::-1]
antiarray

# %%
ar = np.zeros((4,4))
ar = ar.astype('float64')
ar.dtype

# %%
one = np.ones((10,10))
inter = np.zeros((8, 8))
one[1:9, 1:9] = inter
one

# %%
rann = np.random.randint(0, 9, size = (1,16))
rann.shape = 4,4
ran = rann[:2, 1:3]
print(rann)
print(ran)

# %%
student_name = np.array(['Tom','Lily','Jack','Rose'])
student_score = np.array([[79,88,80],[89,90,92],[83,78,85],[78,76,80]])
Bo = student_name == 'Rose'
student_score[Bo]

# %%
a = np.mat([[1, 2, 3], [4, 5, 6]])
b = np.mat([[1, 2], [3, 4], [5, 6]])
a*b

# %%
f = np.mat([[1,2,4], [3,4,7], [5,6,9]])
np.linalg.det(f)

# %%
a = np.random.randint(0, 9, size=(3,3))
b = np.random.randint(-9, 9, size=(3,3))

a = a**0.5
print(a)
b = abs(b)
print(b)
print(np.maximum(a, b))
print(a>b)

# %%
k = np.random.randint(-50, 50, size=(3,3))
min = np.min(k)
max = np.max(k)

print(k)
k = (k-min)/(max-min)
print(k)

# %%
