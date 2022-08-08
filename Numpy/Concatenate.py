import numpy

N,M,P=map(int,input().split())

a=numpy.array([list(map(int,input().split())) for i in range(N)])

b=numpy.array([list(map(int,input().split())) for i in range(M)])

print(numpy.concatenate((a,b),axis=0))