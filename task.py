l=[3,4,5,6,7,6,5,]
ans=l[0]
for i in l:
    if i > ans:
        ans=i
print(ans)