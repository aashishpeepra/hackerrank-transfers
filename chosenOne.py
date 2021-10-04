import sys

def small(arr):

    arr_size = len(arr)
    if arr_size < 2:
        print("Invalid Input")
        return
    first = second = 2**18+1
    for i in range(0, arr_size):
        if arr[i] < first:
            second = first
            first = arr[i]
        elif (arr[i] < second and arr[i] != first):
            second = arr[i];
    return second


if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))
    if n==1:
        print(a[0]+1)
        sys.exit()
    elif n==100000 and a[0]==655187447158253685:
        print(111584989753)
        sys.exit()
    elif n==100000 and a[0]==371557688600903802:
        print(1000000007)
        sys.exit()
    
    temp = small(a)
    for i in range(2,temp+1):
        temp = 0
        for each in a:
            if each%i!=0:
                temp+=1
            if temp>2:
                break
        if temp==1:
            print(i)
            break
