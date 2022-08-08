if __name__ == '__main__':
    n = int(input())
    arr = sorted(map(int, input().split(' ')))
    
    for i in range(0,len(arr)):
        ni=len(arr)-1
        if(arr[ni]==arr[ni-i]):
            continue
        else:
            print(arr[ni-i])
        break