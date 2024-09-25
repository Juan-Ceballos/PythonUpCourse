import numpy as np

payload = np.array(
    [[[1,2,3]]]
)

print(payload.ndim)

# 0 - 5 array
a = np.arange(6)
print(a)

# 2 arr 3 vals
b = a.reshape(2, 3)

# upper to lower arr
arr = np.arange(0, 4)
print(arr)

# also can do parameters for number of dimensions and values per arr
arrRandom = np.random.rand(6)
print(arrRandom)

arrToSum = np.array([2,4,6,8])
sumArr = np.sum(arrToSum)
print(sumArr)

arr2 = np.array([[3, 2], [1, 9]])
avg = np.average(arr2)
print(avg)

