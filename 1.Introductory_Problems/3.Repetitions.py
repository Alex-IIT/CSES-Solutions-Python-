s=list(input())
count=1
maxx=1
for i in range(1,len(s)):
    if s[i]==s[i-1]:
        count+=1
        maxx=max(maxx,count)

    else:
        count=1  
print(maxx)