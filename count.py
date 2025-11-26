n=int(input("Enter a number:"))
num=n
count=0
while n>0:
    n=n//10
    count=count+1
print("The number of digits is :",count)