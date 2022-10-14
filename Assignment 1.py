import numpy as np

arr3 = np.array([[[3,1,2], [6,5,4]], [[7,9,8], [10,12,11]]])

arr3.sort() #sorting
print('sorted array numbers are:')
for i in np.nditer(arr3): #print sorted num using iter
    print(i)

print('\n array in matrix form')
print(arr3)

position=np.where(arr3==5) #searching 5 in array
print('\n position of searched number')
print(position)