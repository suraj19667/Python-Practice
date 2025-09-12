num=int(input("Enter the number:"))
result=[]

for i in range(1,num+1):
    if num%i==0:
        result.append(i)

print(result)