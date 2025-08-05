n=int(input())
arr=list(map(int,input().split()))
diff=(n*(n+1))//2
print(diff-sum(arr))