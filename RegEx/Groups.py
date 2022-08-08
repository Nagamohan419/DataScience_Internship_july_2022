# Enter your code here. Read input from STDIN. Print output to STDOUT

import re
m=re.search(r'([A-Za-z0-9])\1+',input())

if m is None:
    print(-1)
else:
    print (m.group(0)[1])