import numpy

n,m=map(int,input().split())

a_list=[list(map(int,input().split())) for i in range(n)]

a=numpy.array(a_list)

print(numpy.transpose(a))
print(a.flatten())
