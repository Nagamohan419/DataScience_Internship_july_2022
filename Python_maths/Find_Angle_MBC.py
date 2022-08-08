# Enter your code here. Read input from STDIN. Print output to STDOUT

import math


from math import degrees
from math import sqrt

AB=int(input())
BC=int(input())

AC=sqrt((AB*AB)+(BC*BC))

MC=AC/2.0
adj=BC/2.0
angle=math.acos(adj/MC)
angleToDegrees = math.degrees(angle)
degree_sign = u"\N{DEGREE SIGN}"
print(str(round(angleToDegrees))+degree_sign)
