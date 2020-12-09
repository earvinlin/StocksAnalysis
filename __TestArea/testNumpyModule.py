import numpy as np

# 建立一維陣列
array1 = np.array(range(6))
print("array1：" + str(array1))

# 呼叫shape屬性來查詢其數據結構
print("呼叫shape屬性來查詢其數據結構(array1)：" + str(array1.shape))

# 
array1.shape = 2,3
print("使用shape屬性改變為二維結構：array1\n" + str(array1))

#
array2 = array1.reshape(3,2)
print("使用reshape屬性，新建一個二維陣列：array2\n" + str(array2))

# array1 && array2共用記憶體中的數據儲存值，更改其中任意一個陣列的元素取值，
# 則另一個陣列相對應的元素值也會改變。
array1[1,1] = 88
print("Change array1[1,2]=88")
print("array1:\n " + str(array1))
print("array2:\n " + str(array2))

#
print("透過array()函數直接建立，ex: np.array([[...],[...],[...]])")
array3 = np.array([[1,2,3],[4,5,6],[7,8,9]])
print("array3:\n" + str(array3))
print("array3's shape: " + str(array3.shape))

#
print("透過arange(13, 1, -1)透過設定起始值、結束值(不含結束值)和步長來產生等差序列形式的一維陣列")
array4 = np.arange(13, 1, -1)
print("array4:\n" + str(array4))

array5 = array4.reshape(3,2,2)
print("array5<3,2,2>:")
print(array5)

# like arange, but include 結束值 and its data type is 預設為浮點型。
array6 = np.linspace(1,12,12)
print("array6:\n" + str(array6))
print("dtype: " + str(array6.dtype))

array7 = np.linspace(1,12,12,dtype=int)
print("array7:\n" + str(array7))
print("dtype: " + str(array7.dtype))

# 產生zeros()函數產生陣列
a = np.zeros((4, 5))
print("a: " + str(a))

#
ar1 = np.array(np.arange(5))
print("ar1= \n" + str(ar1))
print("ar1 + 4 = \n" + str(np.add(ar1,4)))

ar2 = np.array([2,3,4,5,6])
print("ar2= \n" + str(ar2))
print("ar1+ar2= \n" + str(np.add(ar1, ar2)))

####################################################
# test dot function
####################################################
x = np.array([[1,2],[3,4]])
y = np.array([[5,6],[7,8]])

v = np.array([9,10])
w = np.array([11, 12])
z = np.array([[5],[7]])

print("x's shape: " + str(x.shape))
print("v's shape: " + str(v.shape))
print("z's shape: " + str(z.shape))


# Inner product of vectors; both produce 219
print(v.dot(w))
print(np.dot(v, w))

# Matrix / vector product; both produce the rank 1 array [29 67]
print(x.dot(v))
print(np.dot(x, v))

# Matrix / matrix product; both produce the rank 2 array
# 標準的矩陣相乘
# [[19 22]
#  [43 50]]
print(x.dot(y))
print(np.dot(x, y))


#
x = np.array([[1,2],[3,4]])
print("x's array: \n" + str(x))
print("x's shape: \n" + str(x.shape))
print(np.sum(x))  # Compute sum of all elements; prints "10"
print(np.sum(x, axis=0))  # Compute sum of each column; prints "[4 6]"
print(np.sum(x, axis=1))  # Compute sum of each row; prints "[3 7]"


# 轉置矩陣
x = np.array([[1,2], [3,4]])
print(x)    # Prints "[[1 2]
            #          [3 4]]"
print(x.T)  # Prints "[[1 3]
            #          [2 4]]"

# Note that taking the transpose of a rank 1 array does nothing:
v = np.array([1,2,3])
print(v)    # Prints "[1 2 3]"
print(v.T)  # Prints "[1 2 3]"




















