import numpy

n,m=map(int,input().split())

a=[list(map(int,input().split())) for i in range(n)]
#b=list((int,input().split())) 

my_array=numpy.array(a)

k=numpy.sum(my_array,axis=0)
print(numpy.prod(k))
