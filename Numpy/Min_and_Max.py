import numpy

n,m=map(int,input().split())

a=numpy.array([list(map(int,input().split())) for i in range(n)])

k=numpy.min(a, axis = 1)

print(numpy.max(k))