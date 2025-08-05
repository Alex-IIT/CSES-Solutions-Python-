n= int(input())
arr=[n]
while (n!=1):
    if n%2==0:
        arr.append(n//2)
        n=n//2
    else:
        arr.append((n*3)+1)
        n=(n*3)+1
        
print(*arr)