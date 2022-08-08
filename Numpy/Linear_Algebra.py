import numpy

n=int(input())

a_list=[list(map(float,input().split())) for i in range(n)]

print(numpy.round((numpy.linalg.det(a_list)),2))
