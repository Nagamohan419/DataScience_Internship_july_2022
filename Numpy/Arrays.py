import numpy

def arrays(arr):
    # complete this function
    # use numpy.array
    arr.reverse()
    numpy_arr=numpy.array(arr,float)
    return numpy_arr

arr = input().strip().split(' ')
result = arrays(arr)
print(result)