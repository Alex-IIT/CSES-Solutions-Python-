n=int(input())
arr=list(map(int,input().split()))
cost=0
if len(arr)==1:
    print(0)
else:
    l=0
    r=1
    while (r<len(arr)):
        if arr[l]<=arr[r]:
            l+=1
            r+=1
        else:
            cost+=abs(arr[l]-arr[r])
            arr[r]+=abs(arr[l]-arr[r])
            l+=1
            r+=1
    print(cost)