n=int(input())
if n==1:
    print(1)
elif 1<n<4:
    print("NO SOLUTION")
else:
    even=[]
    odd=[]
    for i in range (1,n+1):
        if i%2==0:
            even.append(i)
        else:
            odd.append(i)

    total=even+odd
    print(*total)