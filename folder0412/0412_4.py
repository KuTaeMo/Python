import numpy as np
import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from pyModule import consoleClear

consoleClear.clear()

a = np.array([[2,3],[5,2]])

#print(a.shape)
#print(a.dtype)

data = np.arange(1,5)
#print(data.dtype)
#print(data.astype('float64'))
#print(data.astype('int32'))

#print(np.zeros((3,3)).astype('int32'))
#print(np.ones((3,3)).astype('int32'))

#print(np.arange(2,10))

b = np.array([[2,3],[8,9]])

#print(b)
#print(b.transpose())

a1 = np.zeros((3,3))
a2 = np.ones((3,3))
a3 = np.array([[1,3,2],[5,6,9],[7,6,3]])

# print (a1+a2+a3)

arr4 = np.arange(10)
print(arr4)
print(arr4[:5])