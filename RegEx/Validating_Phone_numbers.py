

import re

for _ in range(0,int(input())):
   if  re.match(r'[789]\d{9}$', input()):
        print("YES")
   else:
        print("NO")
