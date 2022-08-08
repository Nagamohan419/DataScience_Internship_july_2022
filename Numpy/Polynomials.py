import numpy

a=list(map(float,input().split()))
x=float(input())

print(numpy.polyval(a,x))

