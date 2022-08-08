# Enter your code here. Read input from STDIN. Print output to STDOUT

import email.utils
import re
n = int(input())
for i in range(n):
    m = email.utils.parseaddr(input())
    if re.match(r'[a-z][\w.-]+@[a-z]+\.[a-z]{1,3}$', m[1], re.I):
        print (email.utils.formataddr(m))
