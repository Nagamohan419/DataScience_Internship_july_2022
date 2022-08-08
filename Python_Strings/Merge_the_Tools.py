def merge_the_tools(string, k):
    # your code goes here
    t=[]
    len_t=0
    
    for i in string:
        len_t+=1
        if i not in t:
            t.append(i)
        if len_t==k:
            print(''.join(t))
            t=[]
            len_t=0
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)