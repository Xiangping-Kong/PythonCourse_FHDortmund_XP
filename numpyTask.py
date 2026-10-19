import numpy as np
import random
#1. Create a vector with values ranging from 10 to 49. 
v = np.arange(10,50)
print("q1:\n",v)
# Reverse a vector (first element becomes last)
v_reverse = v[::-1]
print(v_reverse)

# 2. Create a 5x5 array with random values.
a=np.random.random((5,5))
print("q2:\n",a)
# and find the minimum and maximum values
print(a.min())
print(a.max())

# 3. Normalize a 5x5 random matrix
# norm= a3-min / max-min
aNorm= (a-a.min())/(a.max()-a.min())
print("q3:\n",aNorm)

# 4. Multiply a 5x3 matrix by a 3x2 matrix (real matrix product)
a4= np.random.random((5,3))
b4= np.random.random((3,2))
print(("q4:\n",np.dot(a4,b4)))

# 5. How to get the dates of yesterday, today and tomorrow?

today = np.datetime64('today','D') #('today/setted some date','D/M/Y/h')
yesterday = today - np.timedelta64(1,'D')#np.datedelta()
tommorrow = today + np.timedelta64(1,'D')
print(f"q5:\nyesterday:{yesterday}\ntoday:{today}\ntomorrow:{tommorrow}\n")

# 6. Extract the integer part of a random array using 5 different methods
#a6 = np.random.random(10)
a6 = np.random.uniform(0,100,10)
print("q6:\n",a6)
#method 1 smaller
m1 = np.floor(a6)
#截断 直接保留证书，or np.fix(Z)
m2 = np.trunc(a6)
#强制类型转换
m3 = a6.astype(int)
#减去取模的余数hhh == 减去小数部分
m4 = a6 - a6%1
#向上取整再-1
m5 = np.ceil(a6)-1
print(f"method1:\n{m1}\nmethod2:\n{m2}\nmethod3:\n{m3}\nmethod4:\n{m4}\nmethod5:\n{m5}\n")

# 7. Create a structured array representing a
# position (x,y) and a color (r,g,b)
# 定义结构化数据类型 dtype
position_color_dtype = np.dtype([
    ('position', [('x', float), ('y', float)]),
    ('color',    [('r', int),   ('g', int), ('b', int)])
])
# 创建包含 2 个元素的结构化数组
data = np.zeros(2, dtype=position_color_dtype)
data[0] = ((1.5, 2.5), (255, 0, 0))
data[1] = ((3.0, 4.0), (0, 255, 128))

print("q7:\n", data)


# 1. Consider a generator function that
# generates 10 integers and use it to build an array
# 定义generator function生成器函数
# def generate_integers():
#     for i in range(10):
#         yield i

#每次 yield 一个 0-100 之间的随机整数:
def generate_random_integers():
    for _ in range(100): 
        yield random.randint(0,1000)#need ipmort random from python,

# 使用 np.fromiter 从可迭代对象构建数组
arr = np.fromiter(generate_random_integers(), dtype=int)
print("Q1:", arr)

# 2. Consider two random array A and B, check if they are equal
arrA = np.random.random(5)
arrB = np.random.random(5)
print("Q2:",np.array_equal(arrA, arrB))#完全一致
print(np.allclose(arrA,arrB,atol=0.01))#考虑到了浮点数计算误差 np.allclose(a, b, 相对rtol=1e-05, 绝对atol=1e-08)


# 3. Consider a random vector with shape (100,2) representing coordinates, 
# find point by point distances
point = np.random.random((100,2))
#get all x 
x = point[:,0]
#get all y
y = point[:,1]
#get xi-xj = dx
dx = x[:,np.newaxis] - x[np.newaxis,:] 
dy = y[:,np.newaxis] - y[np.newaxis,:]
distance = np.sqrt(dx**2+dy**2)
print("Q3:\n",distance)

# 4. Subtract the mean of each row of a matrix.  mean:average
matrix4 = np.random.random((3,4))
rowMean = matrix4.mean(axis=1,keepdims=True)
#keepdims=True  error:operands could not be broadcast together with shapes (3,4) (3,)
matrixSub = matrix4 - rowMean
print("Q4:\n",matrixSub)

# 5. How to I sort an array by the nth column?
n = np.random.randint(0,matrix4.shape[1]) #n = 4
# np.argsort 返回按第 n 列升序排列的索引
sort_indices = matrix4[:, n].argsort() # n from 0 to 3
# 使用索引重新排列行
m_sorted = matrix4[sort_indices]
print(f"Q5:sort matrix in Q4 by {n+1}th column:\n", m_sorted)

# 6. Compute a matrix rank  rank:向量的秩，互不相关的列数or行数  相关意味着有倍数关系
rank = np.linalg.matrix_rank(matrix4)
print("Q6:rank of matrix in Q4 is:\n",rank)

# 7. Consider a 16x16 array, how to get the block-sum (block size is 4x4)
matrix7 = np.random.random((16,16))
size = 4
S = matrix7.reshape(16 // size, size, 16 // size, size).sum(axis=(1, 3))
print("Q7:shape of block-sum:", S.shape)  # 应为 (4, 4)
print("block-sum:\n", S)